#!/usr/bin/env python3
"""C++ Başvuru Kitabı — derleme betiği.

Alt başlık dosyalarından iki cildi, birleşik kitap kaynağını, Leanpub içindekiler
listesini ve bakım durumu tablosunu kurar. İstenirse PDF'i de üretir.

Yalnızca Python 3.8+ standart kütüphanesi kullanılır. PDF için pandoc, xelatex ve
DejaVu yazı tipleri gerekir.

Kullanım (depo kökünden):
    python3 araclar/derle.py               geçiş paragraflarıyla derle
    python3 araclar/derle.py --gecissiz    geçiş paragrafları olmadan derle
    python3 araclar/derle.py --pdf         ayrıca PDF üret
    python3 araclar/derle.py --kati        uyarı varsa da başarısız say (otomatik denetim için)
    python3 araclar/derle.py --kod         ayrıca kod örneklerini derle (araclar/kod_denetimi.py;
                                           şimdilik yalnızca rapor, çıkış kodunu etkilemez)

Çıktılar cikti/ klasörüne yazılır.
"""
import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CILTLER = [
    # kod, klasör, birleşik kitaptaki bölüm adı, alt başlık, Leanpub etiketi, çıktı dosyası
    ("I", "cilt-1-temel", "Cilt I — Temel",
     "Yeni mezun bir C++ geliştiricisinin ilk yılında bilmesi gerekenler",
     "CİLT I — TEMEL", "CILT_I.md"),
    ("II", "cilt-2-ileri", "Cilt II — İleri",
     "Kıdemli bir C++ geliştiricisinin bilmesi gerekenler",
     "CİLT II — İLERİ", "CILT_II.md"),
]

KITAP_BASLIGI = "C++"
KITAP_ALT_BASLIGI = "İki Ciltlik Başvuru Kitabı"
PDF_DOSYASI = "CPP_Kitabi.pdf"

DOSYA_ADI = re.compile(r"^(\d+)-(\d+)(?:-(\d+))?-[^/\\]+\.md$")
KISIM_KLASORU = re.compile(r"^kisim-(\d+)-")
GECIS_DOSYASI = re.compile(r"^kisim-(\d+)-(\d+)\.md$")
# Kod denetiminin işaretleri (araclar/kod_denetimi.py); kitabın metnine girmez.
KOD_ISARETI = re.compile(r"^<!--\s*kod(?:-baglam)?\b.*?-->[ \t]*\n", re.S | re.M)

uyarilar = []
hatalar = []


def uyar(mesaj):
    uyarilar.append(mesaj)


def hata(mesaj):
    hatalar.append(mesaj)


# ---------------------------------------------------------------------------
# Dosya okuma
# ---------------------------------------------------------------------------

def goreli(yol):
    return os.path.relpath(yol, KOK).replace(os.sep, "/")


def oku(yol):
    """Dosyayı okur; üst bilgiyi (front matter) ve gövdeyi ayrı döndürür."""
    with open(yol, encoding="utf-8") as f:
        metin = f.read().replace("\r\n", "\n").lstrip("\ufeff")
    meta = {}
    if metin.startswith("---\n"):
        son = metin.find("\n---\n", 4)
        if son < 0:
            hata(f"{goreli(yol)}: üst bilgi kapanmamış ('---' satırı eksik)")
            return meta, metin.strip()
        for satir in metin[4:son].split("\n"):
            if not satir.strip() or satir.lstrip().startswith("#"):
                continue
            anahtar, _, deger = satir.partition(":")
            deger = deger.strip()
            try:
                meta[anahtar.strip()] = json.loads(deger)
            except ValueError:
                meta[anahtar.strip()] = deger.strip('"')
        metin = metin[son + 5:]
    metin = KOD_ISARETI.sub("", metin)
    return meta, metin.strip("\n").rstrip()


def kod_disi_satirlar(metin):
    """(satır no, satır) çiftlerini kod blokları hariç döndürür."""
    kodda = False
    for no, satir in enumerate(metin.split("\n"), 1):
        if satir.startswith("```"):
            kodda = not kodda
            continue
        if not kodda:
            yield no, satir


# ---------------------------------------------------------------------------
# Cildin yüklenmesi
# ---------------------------------------------------------------------------

def birim(yol, tur, anahtar=None):
    meta, govde = oku(yol)
    return {"yol": yol, "tur": tur, "anahtar": anahtar, "meta": meta, "govde": govde}


def kisim_yukle(klasor, kisim_no):
    dosyalar = []
    for ad in os.listdir(klasor):
        tam = os.path.join(klasor, ad)
        if not ad.endswith(".md") or os.path.isdir(tam):
            continue
        m = DOSYA_ADI.match(ad)
        if not m:
            uyar(f"{goreli(tam)}: adlandırma kalıbına uymuyor, derlemeye alınmadı")
            continue
        a, b = int(m.group(1)), int(m.group(2))
        c = int(m.group(3)) if m.group(3) is not None else -1
        if a != kisim_no:
            hata(f"{goreli(tam)}: dosya numarası ({a}) klasörün kısım numarasıyla ({kisim_no}) uyuşmuyor")
        dosyalar.append(((a, b, c), tam))
    dosyalar.sort()

    kisim = {"no": kisim_no, "klasor": klasor, "baslik": None, "giris": "",
             "bolumler": [], "kapanis": None}
    bolumler = {}
    for (a, b, c), yol in dosyalar:
        if b == 0 and c == -1:
            u = birim(yol, "kisim_basligi")
            ilk, _, kalan = u["govde"].partition("\n")
            if not re.match(rf"^# Kısım {kisim_no} — .+$", ilk):
                hata(f"{goreli(yol)}: ilk satır '# Kısım {kisim_no} — ...' olmalı")
            kisim["baslik"] = u
            kisim["baslik_satiri"] = ilk
            kisim["giris"] = kalan.strip("\n")
        elif b == 99 and c == -1:
            kisim["kapanis"] = birim(yol, "kisim_kapanisi")
        elif c == -1:
            u = birim(yol, "bolum", f"{a}.{b}")
            if not u["govde"].startswith(f"## {a}.{b} "):
                hata(f"{goreli(yol)}: ilk satır '## {a}.{b} ...' olmalı")
            if (a, b) in bolumler:
                hata(f"{goreli(yol)}: {a}.{b} için birden fazla dosya var")
            bolumler[(a, b)] = {"ust": u, "cocuklar": [], "kapanis": None}
        else:
            bl = bolumler.setdefault((a, b), {"ust": None, "cocuklar": [], "kapanis": None})
            if c == 0:
                u = birim(yol, "bolum", f"{a}.{b}")
                if not u["govde"].startswith(f"## {a}.{b} "):
                    hata(f"{goreli(yol)}: ilk satır '## {a}.{b} ...' olmalı")
                if bl["ust"] is not None:
                    hata(f"{goreli(yol)}: {a}.{b} için birden fazla dosya var")
                bl["ust"] = u
            elif c == 99:
                bl["kapanis"] = birim(yol, "bolum_kapanisi")
            else:
                u = birim(yol, "alt_bolum", f"{a}.{b}.{c}")
                if not u["govde"].startswith(f"### {a}.{b}.{c} "):
                    hata(f"{goreli(yol)}: ilk satır '### {a}.{b}.{c} ...' olmalı")
                bl["cocuklar"].append(u)
    for (a, b), bl in sorted(bolumler.items()):
        if bl["ust"] is None:
            hata(f"{goreli(klasor)}: {a}.{b} alt başlıklarının üst dosyası ({a:02d}-{b:02d}-00-...) yok")
            continue
        kisim["bolumler"].append(bl)
    if kisim["baslik"] is None:
        hata(f"{goreli(klasor)}: kısım başlığı dosyası ({kisim_no:02d}-00-kisim-basligi.md) yok")
    return kisim


def cilt_yukle(kod, klasor_adi):
    klasor = os.path.join(KOK, klasor_adi)
    on_metin = birim(os.path.join(klasor, "00-on-metin.md"), "on_metin")
    kisimlar = []
    for ad in sorted(os.listdir(klasor), key=lambda x: (KISIM_KLASORU.match(x) is None, x)):
        tam = os.path.join(klasor, ad)
        m = KISIM_KLASORU.match(ad)
        if os.path.isdir(tam) and m:
            kisimlar.append(kisim_yukle(tam, int(m.group(1))))
    kisimlar.sort(key=lambda k: k["no"])
    numaralar = [k["no"] for k in kisimlar]
    if len(set(numaralar)) != len(numaralar):
        hata(f"{klasor_adi}: aynı numaralı birden fazla kısım klasörü var")
    return {"kod": kod, "klasor": klasor_adi, "on_metin": on_metin, "kisimlar": kisimlar}


def gecisleri_yukle(cilt):
    """gecisler/<cilt klasörü>/kisim-AA-BB.md -> {BB: birim}"""
    sonuc = {}
    klasor = os.path.join(KOK, "gecisler", cilt["klasor"])
    if not os.path.isdir(klasor):
        return sonuc
    mevcut = {k["no"]: i for i, k in enumerate(cilt["kisimlar"])}
    for ad in sorted(os.listdir(klasor)):
        m = GECIS_DOSYASI.match(ad)
        if not m:
            continue
        onceki, sonraki = int(m.group(1)), int(m.group(2))
        yol = os.path.join(klasor, ad)
        if sonraki not in mevcut:
            uyar(f"{goreli(yol)}: Kısım {sonraki} yok, geçiş kullanılmadı")
            continue
        i = mevcut[sonraki]
        if i == 0 or cilt["kisimlar"][i - 1]["no"] != onceki:
            uyar(f"{goreli(yol)}: Kısım {sonraki}'den önce gelen kısım {onceki} değil; dosya adını kontrol edin")
        sonuc[sonraki] = birim(yol, "gecis")
    return sonuc


def cilt_gecisleri_yukle():
    klasor = os.path.join(KOK, "gecisler", "ciltler-arasi")
    sonuc = {}
    for anahtar, ad in (("kapanis", "cilt-1-kapanis.md"), ("acilis", "cilt-2-acilis.md")):
        yol = os.path.join(klasor, ad)
        if os.path.exists(yol):
            sonuc[anahtar] = birim(yol, "cilt_gecisi")
    if "kapanis" in sonuc and not sonuc["kapanis"]["govde"].startswith("# "):
        hata(f"{goreli(sonuc['kapanis']['yol'])}: ilk satır '# ...' biçiminde bir başlık olmalı")
    return sonuc


# ---------------------------------------------------------------------------
# Metnin kurulması
# ---------------------------------------------------------------------------

def bolum_metni(bl):
    parcalar = [bl["ust"]["govde"]]
    parcalar += [c["govde"] for c in bl["cocuklar"]]
    if bl["kapanis"]:
        parcalar += ["---", bl["kapanis"]["govde"]]
    return "\n\n".join(p for p in parcalar if p)


def kisim_metni(kisim, gecis):
    parcalar = [kisim["baslik_satiri"]]
    if gecis:
        parcalar.append(gecis["govde"])
    if kisim["giris"]:
        parcalar.append(kisim["giris"])
    parcalar += [bolum_metni(bl) for bl in kisim["bolumler"]]
    if kisim["kapanis"]:
        parcalar += ["---", kisim["kapanis"]["govde"]]
    return "\n\n".join(parcalar)


def icindekiler(ust_birimler):
    """ust_birimler: [(başlık satırı '# ...', [alt başlık metinleri])]"""
    girdiler = []
    for baslik, altlar in ust_birimler:
        satir = f"**{baslik[2:]}**"
        if altlar:
            satir += "  \n  " + " · ".join(altlar)
        girdiler.append(satir)
    return "## İçindekiler\n\n" + "\n\n".join(girdiler)


def alt_basliklar(kisim):
    return [bl["ust"]["govde"].split("\n", 1)[0][3:] for bl in kisim["bolumler"]]


def cilt_metni(cilt, gecisli, kisim_gecisleri, cilt_gecisleri):
    ust = []
    govdeler = []
    for k in cilt["kisimlar"]:
        gecis = kisim_gecisleri.get(k["no"]) if gecisli else None
        govdeler.append(kisim_metni(k, gecis))
        ust.append((k["baslik_satiri"], alt_basliklar(k)))
    if gecisli and cilt["kod"] == "I" and "kapanis" in cilt_gecisleri:
        kapanis = cilt_gecisleri["kapanis"]["govde"]
        govdeler.append(kapanis)
        ust.append((kapanis.split("\n", 1)[0], []))
    on = cilt["on_metin"]["govde"]
    if gecisli and cilt["kod"] == "II" and "acilis" in cilt_gecisleri:
        on += "\n\n" + cilt_gecisleri["acilis"]["govde"]
    metin = (on + "\n\n---\n\n" + icindekiler(ust) + "\n\n\n---\n\n\n"
             + "\n\n---\n\n\n".join(govdeler) + "\n\n---\n")
    return metin, govdeler


def kunye_bilgisi(on_metin):
    kunye = re.search(r"^\*\*(.+)\*\*$", on_metin, re.M)
    derleyen = re.search(r"^Derleyen: (.+?) · Sürüm (.+?) · (.+)$", on_metin, re.M)
    if not (kunye and derleyen):
        hata("cilt-1-temel/00-on-metin.md: künye satırı ya da 'Derleyen: ... · Sürüm ... · ...' satırı bulunamadı")
        return {"kunye": "", "derleyen": "", "surum": "", "tarih": ""}
    return {"kunye": kunye.group(1), "derleyen": derleyen.group(1),
            "surum": derleyen.group(2), "tarih": derleyen.group(3)}


def basliklari_indir(metin):
    """# -> ##, ## -> ###, ### -> #### (kod blokları hariç)."""
    satirlar = metin.split("\n")
    kodda = False
    for i, satir in enumerate(satirlar):
        if satir.startswith("```"):
            kodda = not kodda
        elif not kodda and re.match(r"^#{1,3} ", satir):
            satirlar[i] = "#" + satir
    return "\n".join(satirlar)


def birlesik_kitap(ciltler, govdeler, cilt_gecisleri, gecisli, bilgi):
    meta = f"""---
title: "{KITAP_BASLIGI}"
subtitle: "{KITAP_ALT_BASLIGI}"
author:
  - "Derleyen: {bilgi['derleyen']}"
  - "{bilgi['kunye']}"
date: "Sürüm {bilgi['surum']} — {bilgi['tarih']}"
lang: tr
documentclass: book
classoption: [11pt, oneside]
geometry: [a4paper, margin=2.4cm, bottom=2.8cm]
mainfont: "DejaVu Serif"
sansfont: "DejaVu Sans"
monofont: "DejaVu Sans Mono"
monofontoptions: "Scale=0.86"
colorlinks: true
linkcolor: black
toccolor: black
toc: true
toc-depth: 2
numbersections: false
---

"""
    parcalar = []
    for (kod, _, ad, alt, _, _), cilt in zip(CILTLER, ciltler):
        kapak = cilt["on_metin"]["govde"] + "\n\n---\n\n"
        kapak = re.sub(r"^#{1,3} .*$", "", kapak, flags=re.M)
        kapak = re.sub(r"^\*\*.*\*\*$", "", kapak, flags=re.M)
        kapak = re.sub(r"^Derleyen:.*$", "", kapak, flags=re.M)
        kapak = re.sub(r"\n-{3,}\n", "\n", kapak).strip()
        if gecisli and kod == "II" and "acilis" in cilt_gecisleri:
            kapak += "\n\n" + cilt_gecisleri["acilis"]["govde"]
        govde = "\n" + "\n\n---\n\n\n".join(govdeler[kod]) + "\n\n---\n"
        parcalar.append(f"# {ad}\n\n*{alt}*\n\n{kapak}\n\n{basliklari_indir(govde)}")
    return meta + "\n\n\\newpage\n\n".join(parcalar)


def satir_ici_html(metin):
    parcalar = re.split(r"(`[^`]*`)", metin)
    sonuc = []
    for p in parcalar:
        if p.startswith("`") and p.endswith("`") and len(p) >= 2:
            sonuc.append("<code>" + html.escape(p[1:-1], quote=False) + "</code>")
        else:
            sonuc.append(html.escape(p, quote=False))
    return "".join(sonuc)


def leanpub_icindekiler(ciltler, cilt_gecisleri, gecisli):
    satirlar = ["<ul class='toc no-parts'>"]
    for (kod, _, _, _, etiket, _), cilt in zip(CILTLER, ciltler):
        satirlar.append(f"  <li><strong>{etiket}</strong></li>")
        for k in cilt["kisimlar"]:
            satirlar.append(f"  <li>{satir_ici_html(k['baslik_satiri'][2:])}")
            satirlar.append("    <ul>")
            for alt in alt_basliklar(k):
                satirlar.append(f"      <li>{satir_ici_html(alt)}</li>")
            satirlar.append("    </ul>")
            satirlar.append("  </li>")
        if gecisli and kod == "I" and "kapanis" in cilt_gecisleri:
            baslik = cilt_gecisleri["kapanis"]["govde"].split("\n", 1)[0][2:]
            satirlar.append(f"  <li>{satir_ici_html(baslik)}</li>")
    satirlar.append("</ul>")
    return "\n".join(satirlar) + "\n"


# ---------------------------------------------------------------------------
# Denetimler
# ---------------------------------------------------------------------------

ATIF = re.compile(r"(?:Cilt (II|I),? )?Kısım (\d+(?:\.\d+)*)((?:(?:, | ve )\d+(?:\.\d+)*)*)")


def gecerli_numaralar(cilt):
    s = set()
    for k in cilt["kisimlar"]:
        s.add(str(k["no"]))
        for bl in k["bolumler"]:
            s.add(bl["ust"]["anahtar"])
            for c in bl["cocuklar"]:
                s.add(c["anahtar"])
    return s


def tum_birimler(cilt):
    yield cilt["on_metin"]
    for k in cilt["kisimlar"]:
        if k["baslik"]:
            yield k["baslik"]
        for bl in k["bolumler"]:
            yield bl["ust"]
            yield from bl["cocuklar"]
            if bl["kapanis"]:
                yield bl["kapanis"]
        if k["kapanis"]:
            yield k["kapanis"]


def atif_parcalari(govde, varsayilan_cilt):
    """Metni (parça, cilt) çiftlerine böler.

    Düz metin tek parça olarak birleştirilir, çünkü satır sonları bir atfı bölebilir
    ("Cilt I" bir satırda, "Kısım 23.2" sonrakinde). Tablo hücreleri ise ayrı ayrı ele
    alınır: sütun başlığında "Cilt I" ya da "Cilt II" geçiyorsa, o sütundaki atıflar
    o cilde göre çözülür.
    """
    def hucreler(satir):
        return [h.strip() for h in satir.strip().strip("|").split("|")]

    satirlar = [s for _, s in kod_disi_satirlar(govde)]
    duz, parcalar, i = [], [], 0
    while i < len(satirlar):
        if not satirlar[i].lstrip().startswith("|"):
            duz.append(satirlar[i])
            i += 1
            continue
        blok = []
        while i < len(satirlar) and satirlar[i].lstrip().startswith("|"):
            blok.append(satirlar[i])
            i += 1
        baglam = []
        for h in hucreler(blok[0]):
            baglam.append("II" if "Cilt II" in h else "I" if "Cilt I" in h else varsayilan_cilt)
        for satir in blok:
            for j, h in enumerate(hucreler(satir)):
                parcalar.append((h, baglam[j] if j < len(baglam) else varsayilan_cilt))
    parcalar.append((re.sub(r"\s+", " ", " ".join(duz)), varsayilan_cilt))
    return parcalar


def atiflari_denetle(birimler_ve_cilt, numaralar):
    sayi = 0
    for u, varsayilan in birimler_ve_cilt:
        for satir, kod in atif_parcalari(u["govde"], varsayilan):
            for m in ATIF.finditer(satir):
                hedef_cilt = m.group(1) or kod
                adaylar = [m.group(2)] + re.findall(r"\d+(?:\.\d+)*", m.group(3) or "")
                for n in adaylar:
                    sayi += 1
                    if n not in numaralar[hedef_cilt]:
                        uyar(f"{goreli(u['yol'])}: '{m.group(0)}' atfı — Cilt {hedef_cilt} içinde "
                             f"{n} numaralı başlık yok")
    return sayi


KUTU = re.compile(r"^> \*\*(Standart Notu — [^*]+|Derleyici Notu[^*]*)\*\*", re.M)


def kutulari_denetle(birimler):
    """Üst bilgideki 'kutular' alanını metindeki kutularla karşılaştırır.

    Bakım tablosu her zaman metinden hesaplanır; alan yalnızca GitHub'da dosyaya
    bakan kişi içindir. Uyuşmazlık bir uyarıyla bildirilir.
    """
    for u in birimler:
        u["kutular"] = [k.strip() for k in KUTU.findall(u["govde"])]
        yazili = u["meta"].get("kutular") or []
        if isinstance(yazili, str):
            yazili = [yazili]
        if sorted(yazili) != sorted(u["kutular"]):
            uyar(f"{goreli(u['yol'])}: üst bilgideki 'kutular' alanı metinle uyuşmuyor; "
                 f"metinde: {u['kutular'] or 'yok'}")


def bakim_durumu(birimler):
    satirlar = ["# Bakım durumu", "",
                "Bu dosya `araclar/derle.py` tarafından üretilir; elle düzenlemeyin.", ""]
    sayac = {}
    for u in birimler:
        k = u["meta"].get("son_kontrol", "(yok)")
        sayac[k] = sayac.get(k, 0) + 1
    satirlar.append("| Son kontrol | Dosya sayısı |")
    satirlar.append("|---|---|")
    for k in sorted(sayac):
        satirlar.append(f"| {k} | {sayac[k]} |")
    satirlar += ["", "## Kutu içeren dosyalar", "",
                 "Standart değiştiğinde ya da derleyiciler güncellendiğinde önce bunlara bakın.", "",
                 "| Dosya | Başlık | Kutular | Son kontrol |", "|---|---|---|---|"]
    for u in birimler:
        kutular = u.get("kutular")
        if kutular:
            satirlar.append(f"| `{goreli(u['yol'])}` | {u['meta'].get('baslik', '')} | "
                            f"{'; '.join(kutular)} | {u['meta'].get('son_kontrol', '')} |")
    satirlar += ["", "## Bütün dosyalar (en eski kontrol en üstte)", "",
                 "| Dosya | Başlık | Kaynak | Son kontrol |", "|---|---|---|---|"]
    for u in sorted(birimler, key=lambda x: (x["meta"].get("son_kontrol", ""), x["yol"])):
        satirlar.append(f"| `{goreli(u['yol'])}` | {u['meta'].get('baslik', '')} | "
                        f"{u['meta'].get('kaynak', '')} | {u['meta'].get('son_kontrol', '')} |")
    return "\n".join(satirlar) + "\n"


# ---------------------------------------------------------------------------
# PDF
# ---------------------------------------------------------------------------

def pdf_uret(cikti):
    if not shutil.which("pandoc"):
        hata("PDF için pandoc bulunamadı")
        return
    komut = ["pandoc", "kitap_birlesik.md", "-o", PDF_DOSYASI, "--pdf-engine=xelatex",
             "--include-in-header=" + os.path.join(KOK, "araclar", "pdf", "baslik.tex"),
             "--top-level-division=part", "--highlight-style=tango", "-V", "linestretch=1.08"]
    # Bazı TeX kurulumlarında lmodern paketi yoktur; o durumda varsayılan şablon,
    # lmodern satırı çıkarılarak kullanılır (yazı tipleri zaten fontspec ile seçiliyor).
    lmodern_var = False
    if shutil.which("kpsewhich"):
        lmodern_var = subprocess.run(["kpsewhich", "lmodern.sty"], capture_output=True,
                                     text=True).stdout.strip() != ""
    if not lmodern_var:
        sablon = subprocess.run(["pandoc", "--print-default-template=latex"],
                                capture_output=True, text=True, encoding="utf-8").stdout
        sablon = sablon.replace("\\usepackage{lmodern}\n", "").replace("\\usepackage{lmodern}", "")
        with open(os.path.join(cikti, "sablon.tex"), "w", encoding="utf-8") as f:
            f.write(sablon)
        komut.append("--template=sablon.tex")
    print("PDF üretiliyor (birkaç dakika sürebilir)...")
    sonuc = subprocess.run(komut, cwd=cikti, capture_output=True, text=True, encoding="utf-8")
    if sonuc.returncode != 0:
        hata("pandoc hata verdi:\n" + sonuc.stderr[-3000:])


# ---------------------------------------------------------------------------

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="C++ Başvuru Kitabı derleyicisi")
    ap.add_argument("--gecissiz", action="store_true",
                    help="geçiş paragrafları olmadan derle")
    ap.add_argument("--pdf", action="store_true", help="ayrıca PDF üret")
    ap.add_argument("--kati", action="store_true",
                    help="uyarı varsa da hata koduyla çık (otomatik denetim için)")
    ap.add_argument("--kod", action="store_true",
                    help="ayrıca kod örneklerini derle (yalnızca rapor; bkz. araclar/kod_denetimi.py)")
    ap.add_argument("--cikti", default=os.path.join(KOK, "cikti"),
                    help="çıktı klasörü (varsayılan: cikti/)")
    arg = ap.parse_args()
    gecisli = not arg.gecissiz

    ciltler = [cilt_yukle(kod, klasor) for kod, klasor, *_ in CILTLER]
    cilt_gecisleri = cilt_gecisleri_yukle()
    kisim_gecisleri = {c["kod"]: gecisleri_yukle(c) for c in ciltler}

    # bilgi satırları iki ciltte aynı olmalı
    bilgiler = [kunye_bilgisi(c["on_metin"]["govde"]) for c in ciltler]
    if bilgiler[0] != bilgiler[1]:
        uyar("İki cildin ön metnindeki künye / sürüm satırları farklı; PDF Cilt I'dekini kullanır")
    if gecisli:
        for c in ciltler:
            for k in c["kisimlar"][1:]:
                if k["no"] not in kisim_gecisleri[c["kod"]]:
                    uyar(f"Cilt {c['kod']}, Kısım {k['no']}: geçiş paragrafı yok "
                         f"(gecisler/{c['klasor']}/kisim-AA-{k['no']:02d}.md)")

    if hatalar:
        for h in hatalar:
            print("HATA:", h)
        sys.exit(1)

    os.makedirs(arg.cikti, exist_ok=True)
    govdeler = {}
    for (kod, _, _, _, _, dosya), cilt in zip(CILTLER, ciltler):
        metin, govdeler[kod] = cilt_metni(cilt, gecisli, kisim_gecisleri[kod], cilt_gecisleri)
        with open(os.path.join(arg.cikti, dosya), "w", encoding="utf-8", newline="\n") as f:
            f.write(metin)

    with open(os.path.join(arg.cikti, "kitap_birlesik.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(birlesik_kitap(ciltler, govdeler, cilt_gecisleri, gecisli, bilgiler[0]))
    with open(os.path.join(arg.cikti, "leanpub_icindekiler.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(leanpub_icindekiler(ciltler, cilt_gecisleri, gecisli))

    # denetimler ve bakım durumu
    numaralar = {c["kod"]: gecerli_numaralar(c) for c in ciltler}
    denetlenecek = [(u, c["kod"]) for c in ciltler for u in tum_birimler(c)]
    if gecisli:
        denetlenecek += [(u, c["kod"]) for c in ciltler for u in kisim_gecisleri[c["kod"]].values()]
        denetlenecek += [(u, "II" if a == "acilis" else "I") for a, u in cilt_gecisleri.items()]
    atif_sayisi = atiflari_denetle(denetlenecek, numaralar)
    kutulari_denetle([u for u, _ in denetlenecek])
    with open(os.path.join(arg.cikti, "bakim_durumu.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(bakim_durumu([u for u, _ in denetlenecek]))

    if arg.pdf:
        pdf_uret(arg.cikti)

    dosya_sayisi = sum(1 for _ in denetlenecek)
    print(f"Derlendi ({'geçişli' if gecisli else 'geçişsiz'}): {dosya_sayisi} dosya, "
          f"{sum(len(c['kisimlar']) for c in ciltler)} kısım, {atif_sayisi} kısım atfı denetlendi.")
    print(f"Çıktılar: {goreli(arg.cikti) if arg.cikti.startswith(KOK) else arg.cikti}/")
    for u in uyarilar:
        print("UYARI:", u)
    for h in hatalar:
        print("HATA:", h)
    if arg.kod:
        sys.stdout.flush()
        subprocess.run([sys.executable, os.path.join(KOK, "araclar", "kod_denetimi.py"),
                        "--cikti", arg.cikti])
    sys.exit(1 if hatalar or (arg.kati and uyarilar) else 0)


if __name__ == "__main__":
    main()
