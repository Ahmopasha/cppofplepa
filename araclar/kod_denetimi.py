#!/usr/bin/env python3
"""C++ Başvuru Kitabı — kod örneği denetimi.

Kitaptaki her ```cpp bloğunu ayrı bir dosyaya çıkarır ve derler. Cilt I'deki bloklar
-std=c++20, Cilt II'dekiler -std=c++23 ile, -pedantic-errors bayrağıyla derlenir;
standart kütüphanenin başlıkları her bloğun önüne eklenir. ```c blokları C17 olarak
derlenir.

YERLEŞİM. Blokların çoğu tam program değil, parçadır. Blok, en dıştaki bildirim ve
deyimlerine ("parça") ayrılır ve şu yerleşimler sırayla denenir; ilk derlenen kaydedilir:

    birim     bütün blok ad alanı düzeyinde
    karma     ilk parçalar ad alanı düzeyinde, kalanı bir işlev gövdesinde
    govde     bütün blok bir işlev gövdesinde

Blok tek başına derlenmezse sırayla şunlar eklenerek yeniden denenir:

    +önceki   aynı dosyada bir önceki derlenen blok (örnek bir öncekinin devamıysa)
    +ifade    noktalı virgülsüz ifade listeleri ("x + 5   // R-Value") deyime çevrilir
    +genel    araclar/kod_baglami.hpp'deki yer tutucu adlar (Myclass, v, s ...);
              yalnızca derleyicinin bulamadığı adlar eklenir

HATA SATIRLARI. Yorumunda (satır sonundaki // yorumu ya da hemen üstündeki /* ... */
bloğu) "sentaks hatası", "çift anlamlılık hatası", "derlenmez" geçen ya da "hata —",
"hata →" ile başlayan satırlar (yorum C++'ın satırı geçerli saydığını
söylemiyorsa) bilerek hata verir sayılır. Bu satırlar çıkarılınca kalan blok
derlenmeli, her biri tek başına geri konunca derleyici tam o satırda hata vermelidir.
Satır, derlenen yerleşimlerin en dıştakinde ve en içtekinde ayrı ayrı sınanır.

C VE C++. "kod: c" işaretli blok C17 olarak da derlenir. Yorumunda yalnızca "C++'ta"
geçen satırlar C sınamasına alınmaz; "C'de sentaks hatası" diyen satırların C'de hata
verdiği doğrulanır.

ÇALIŞTIRMA. main() içeren ve tek başına derlenen bloklar -fsanitize=address,undefined
(iş parçacığı kullananlar -fsanitize=thread) ile derlenip çalıştırılır. Yorumunda
"tanımsız" geçmeyen bir örnekte sanitizer uyarısı sorun sayılır.

İŞARETLER. Bloğun hemen önüne konan HTML yorumu davranışı değiştirir. Bu yorumlar
kitabın derlenmiş metnine girmez (`derle.py` bunları atar):

    <!-- kod: atla -->        blok derlenmez (sözde kod, tek başına anlamsız parça)
    <!-- kod: c -->           blok C olarak da derlenir
    <!-- kod-baglam
    struct Myclass { };
    -->                       yorumdaki kod bloğun önüne eklenir; "@kod@" satırı varsa
                              blok o satırın yerine konur (ör. bir sınıfın içine)

Kullanım (depo kökünden):
    python3 araclar/kod_denetimi.py                  Clang ile; rapor cikti/kod_denetimi.md
    python3 araclar/kod_denetimi.py --derleyici g++-14 --derleyici clang++-18
    python3 araclar/kod_denetimi.py --calistirma     sanitizer ile çalıştırmayı atla
    python3 araclar/kod_denetimi.py --kati           sorun varsa hata koduyla çık
    python3 araclar/kod_denetimi.py --goster DOSYA:SATIR
                                                     tek bloğun denemelerini ayrıntılı göster

Yalnızca Python 3.8+ standart kütüphanesi kullanılır.
"""
import argparse
import concurrent.futures
import os
import re
import shutil
import subprocess
import sys
import tempfile

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CILT_STANDARDI = {"cilt-1-temel": "c++20", "cilt-2-ileri": "c++23"}
C_STANDARDI = "c17"
CALISMA_SURESI = 20     # saniye

# Önsöz: standart kütüphanenin başlıkları. Derleyicide bulunmayan başlık atlanır.
BASLIKLAR = """
algorithm any array atomic barrier bit bitset cassert cctype cerrno cfloat charconv chrono
cinttypes climits cmath compare complex concepts condition_variable coroutine cstddef cstdint
cstdio cstdlib cstring ctime cwchar deque exception execution expected filesystem flat_map
flat_set format forward_list fstream functional future generator initializer_list iomanip ios
iosfwd iostream istream iterator latch limits list locale map mdspan memory memory_resource
mutex new numbers numeric optional ostream print queue random ranges ratio regex scoped_allocator
semaphore set shared_mutex source_location span spanstream sstream stack stacktrace
stdexcept stop_token streambuf string string_view syncstream system_error thread tuple
type_traits typeindex typeinfo unordered_map unordered_set utility valarray variant vector
version
""".split()
C_BASLIKLARI = ["stdio.h", "stdlib.h", "string.h", "stdbool.h"]

# Standart kütüphanenin derleyiciye göre eksik kalan parçaları. Bu mesajlarla derlenmeyen
# blok kitabın değil derleyicinin sorunudur; ayrı listelenir ve sorun sayılmaz.
BILINEN_EKSIKLER = [
    (r"'generator' file not found|generator: No such file",
     "std::generator (C++23) bu standart kütüphanede yok"),
    (r"no member named '(par|par_unseq|seq|unseq)' in namespace 'std::execution'",
     "paralel algoritmalar (C++17) bu standart kütüphanede varsayılan olarak kapalı"),
]

# Derleyicinin bir adı bulamadığını söyleyen mesajlar (Clang ve GCC).
EKSIK_AD = [
    re.compile(r"(?:undeclared identifier|unknown type name|no template named|no member named|"
               r"unknown class name) '(\w+)'"),
    re.compile(r"'(\w+)' (?:was not declared in this scope|does not name a type|"
               r"has not been declared|is not a template)"),
]
SINIF_ADI_YOK = re.compile(r"expected class[ -]name")
# Yerleşimden doğan hatalar: ad alanı düzeyinde deyim, gövdede tanım gibi.
YERLESIM_HATASI = re.compile(
    r"^expected |type specifier is required|not allowed here|no type named|"
    r"does not have automatic storage|non-local lambda|cannot have '.*' qualifier|"
    r"must be a non-?static member|templates? can only be declared|redefinition of|"
    r"function-style cast|declaration of anonymous|local variable cannot be declared|"
    r"a function-definition is not allowed|conflicting declaration|"
    r"expected constructor, destructor, or type conversion|expected primary-expression|"
    r"template declaration cannot appear|cannot be declared 'constinit'")

BLOK = re.compile(r"^```(\S*)[ \t]*$")
YORUM = re.compile(r"<!--\s*(kod(?:-baglam)?)\b(.*?)-->", re.S)
ISARET = "/*@hata-satiri@*/"
GOVDE_ADI = "kod_parcasi_"
ORTAM = dict(os.environ, LC_ALL="C", LANG="C")    # GCC'nin düz tırnak kullanması için


# ---------------------------------------------------------------------------
# Satır çözümleme
# ---------------------------------------------------------------------------

def yorum_baslangici(satir):
    """Satırdaki // yorumunun başladığı konum (dize ve karakter sabitlerinin içi sayılmaz)."""
    i, tirnak = 0, None
    while i < len(satir):
        c = satir[i]
        if tirnak:
            if c == "\\":
                i += 1
            elif c == tirnak:
                tirnak = None
        elif c in "\"'":
            # 1'000 gibi basamak ayırıcıları karakter sabiti sayılmaz
            if not (c == "'" and 0 < i < len(satir) - 1
                    and satir[i - 1].isalnum() and satir[i + 1].isalnum()):
                tirnak = c
        elif satir.startswith("//", i):
            return i
        i += 1
    return len(satir)


def yorum(satir):
    return satir[yorum_baslangici(satir) + 2:].strip()


def kod_kismi(satir):
    """Yorumu ve dize/karakter sabitlerini atılmış satır (parantez saymak için)."""
    satir = satir[:yorum_baslangici(satir)]
    satir = re.sub(r'"(\\.|[^"\\])*"' + r"|'(\\.|[^'\\])*'", '""', satir)
    return re.sub(r"/\*.*?\*/", " ", satir)


def satirlari_cozumle(satirlar):
    """Her satır için (kod kısmı, yorum metni) listelerini döndürür.

    Kendi satırlarında açılıp kapanan /* ... */ bloklarını izler (kitabın biçimi: uzun
    açıklama kodun hemen üstünde bir blok yorumdur). Blok yorumun metni, hemen altındaki
    kod satırının yorumuna eklenir; böylece "sentaks hatası" gibi işaretler o satıra ait
    sayılır.
    """
    kodlar, yorumlar = [], []
    blokta, bekleyen = False, []
    for s in satirlar:
        duz = s.strip()
        if blokta or (duz.startswith("/*") and "*/" not in duz):
            if "*/" in duz:
                blokta = False
            else:
                blokta = True
            bekleyen.append(duz.lstrip("/*").rstrip("*/").strip())
            kodlar.append("")
            yorumlar.append("")
            continue
        kod = kod_kismi(s)
        yor = yorum(s) if yorum_baslangici(s) < len(s) else ""
        if kod.strip() and bekleyen:
            yor = " ".join(bekleyen + [yor]).strip()
        if kod.strip() or not duz:
            bekleyen = []
        kodlar.append(kod)
        yorumlar.append(yor)
    return kodlar, yorumlar


def hata_satiri_mi(yorum_metni):
    """Satırın yorumu, satırın C++'ta bilerek derleme hatası verdiğini söylüyor mu?"""
    kucuk = yorum_metni.lower()
    if not kucuk or re.search(r"c\+\+'ta (geçerli|derlenir)", kucuk):
        return False
    if re.search(r"sentaks hatası|çift anlamlılık hatası|böyle bir yazım yok", kucuk):
        return True
    if re.match(r"derlenmez\b", kucuk):
        return True
    return re.match(r"hata\s*(—|→|$)", kucuk) is not None or re.search(r":\s*hata$", kucuk) is not None


def yalniz_cpp_mi(yorum_metni):
    """Yorumu yalnızca C++'tan söz eden satır (C sınamasına alınmaz)."""
    kucuk = yorum_metni.lower()
    return "c++'ta" in kucuk and "c'de" not in kucuk


def c_hata_satiri_mi(yorum_metni):
    return re.search(r"c'de (sentaks hatası|geçersiz|derlenmez)", yorum_metni.lower()) is not None


def tanimsiz_mi(blok):
    return any("tanımsız" in y.lower() for y in satirlari_cozumle(blok["satirlar"])[1])


def onsoz():
    satirlar = ["// otomatik önsöz: standart başlıklar"]
    for b in BASLIKLAR:
        satirlar += [f"#if __has_include(<{b}>)", f"#include <{b}>", "#endif"]
    return "\n".join(satirlar) + "\n"


# ---------------------------------------------------------------------------
# Blokların toplanması
# ---------------------------------------------------------------------------

def bloklari_topla():
    bloklar = []
    for cilt, std in CILT_STANDARDI.items():
        for kok, _, dosyalar in sorted(os.walk(os.path.join(KOK, cilt))):
            for ad in sorted(dosyalar):
                if ad.endswith(".md"):
                    bloklar += dosyadaki_bloklar(os.path.join(kok, ad), std)
    # Aşama 2 taramalarının test kodları (tarama/<tarih>/cilt-N-...md): dosya adının
    # başındaki cilt, standardı belirler.
    for kok, _, dosyalar in sorted(os.walk(os.path.join(KOK, "tarama"))):
        for ad in sorted(dosyalar):
            m = re.match(r"cilt-([12])-", ad)
            if m and ad.endswith(".md"):
                std = CILT_STANDARDI["cilt-1-temel" if m.group(1) == "1" else "cilt-2-ileri"]
                bloklar += dosyadaki_bloklar(os.path.join(kok, ad), std)
    return bloklar


def dosyadaki_bloklar(yol, std):
    with open(yol, encoding="utf-8") as f:
        satirlar = f.read().replace("\r\n", "\n").split("\n")
    sonuc, i, sira = [], 0, 0
    while i < len(satirlar):
        m = BLOK.match(satirlar[i])
        if not m:
            i += 1
            continue
        j = i + 1
        while j < len(satirlar) and not satirlar[j].startswith("```"):
            j += 1
        if m.group(1) in ("cpp", "c"):
            sira += 1
            isaretler, baglam = blok_isaretleri("\n".join(satirlar[max(0, i - 60):i]))
            sonuc.append({"yol": os.path.relpath(yol, KOK).replace(os.sep, "/"),
                          "satir": i + 1, "sira": sira, "dil": m.group(1),
                          "std": std if m.group(1) == "cpp" else C_STANDARDI,
                          "satirlar": satirlar[i + 1:j],
                          "isaretler": isaretler, "baglam": baglam})
        i = j + 1
    return sonuc


def blok_isaretleri(onceki):
    """Bloğun hemen önündeki kod yorumlarını okur (aralarında boş satır olabilir)."""
    isaretler, baglam = set(), []
    kalan = onceki.rstrip()
    while kalan.endswith("-->"):
        bas = kalan.rfind("<!--")
        m = YORUM.fullmatch(kalan[bas:]) if bas >= 0 else None
        if not m:
            break
        if m.group(1) == "kod-baglam":
            baglam.insert(0, m.group(2).strip("\n"))
        else:
            isaretler |= set(re.findall(r"[\w-]+", m.group(2)))
        kalan = kalan[:bas].rstrip()
    return isaretler, "\n".join(baglam)


# ---------------------------------------------------------------------------
# Parçalara ayırma ve yerleşimler
# ---------------------------------------------------------------------------

def parcalara_ayir(satirlar):
    """Satır numaralarını en dıştaki bildirim/deyimlere göre gruplar: [[i, i+1, ...], ...]."""
    kodlar = satirlari_cozumle(satirlar)[0]
    parcalar, simdiki, derinlik = [], [], 0
    for i, k in enumerate(kodlar):
        k = k.strip()
        simdiki.append(i)
        if derinlik == 0 and k.startswith("#"):
            parcalar.append(simdiki)
            simdiki = []
            continue
        derinlik += sum(k.count(a) for a in "({[") - sum(k.count(a) for a in ")}]")
        if derinlik <= 0 and k and k[-1] in ";}":
            derinlik = 0
            parcalar.append(simdiki)
            simdiki = []
    if simdiki:
        parcalar.append(simdiki)
    # "else" ve "catch" ile başlayan parça, öncekinin devamıdır.
    birlesik = []
    for p in parcalar:
        ilk = next((kodlar[i].strip() for i in p if kodlar[i].strip()), "")
        if birlesik and re.match(r"(else|catch)\b", ilk):
            birlesik[-1] = birlesik[-1] + p
        else:
            birlesik.append(p)
    return birlesik


def yerlesimler(blok):
    """(ad, ad alanı düzeyindeki satırlar, gövdedeki satırlar) üçlüleri üretir;
    en dıştakinden (birim) en içtekine (govde) doğru."""
    parcalar = parcalara_ayir(blok["satirlar"])
    n = len(parcalar)
    for k in range(n, -1, -1):
        ad = "birim" if k == n else "govde" if k == 0 else f"karma:{k}"
        yield ad, [i for p in parcalar[:k] for i in p], [i for p in parcalar[k:] for i in p]


def kaynak(blok, disari, iceri, haric=(), isaretli=None, genel=("", "")):
    """Yerleşime göre derlenecek kaynak metni kurar. genel: (türler, değişkenler)."""
    def satir(i):
        s = blok["satirlar"][i]
        return s + " " + ISARET if i == isaretli else s
    turler, degiskenler = genel
    kod = "\n".join(satir(i) for i in disari if i not in haric)
    if iceri:
        govde = "\n".join(satir(i) for i in iceri if i not in haric)
        imza = "(void)" if blok["std"] == C_STANDARDI else "()"
        kod += f"\nvoid {GOVDE_ADI}{imza}\n{{\n" + (degiskenler + "\n" if degiskenler else "") + govde + "\n}"
    elif degiskenler:
        turler += "\n" + degiskenler
    baglam = blok["baglam"]
    if re.search(r"^@kod@$", baglam, re.M):
        kod = re.sub(r"^@kod@$", lambda _: kod, baglam, count=1, flags=re.M)
    elif baglam:
        kod = baglam + "\n" + kod
    return (turler + "\n" if turler else "") + kod + "\n"


def ifade_satirlari(satirlar):
    """Noktalı virgülsüz ifade listelerini ("x  // L-Value") deyime çevirir; değişmezse None."""
    yeni, degisti, derinlik = [], False, 0
    for s, k in zip(satirlar, satirlari_cozumle(satirlar)[0]):
        k = k.rstrip()
        devam = k[-1:] in tuple(";{}(,:>=|&+-") and not k.endswith(("++", "--"))
        if derinlik == 0 and k.strip() and not k.strip().startswith("#") and not devam:
            y = yorum_baslangici(s)
            s = s[:y].rstrip() + ";" + s[len(s[:y].rstrip()):]
            degisti = True
        derinlik += sum(k.count(a) for a in "({[") - sum(k.count(a) for a in ")}]")
        derinlik = max(derinlik, 0)
        yeni.append(s)
    return yeni if degisti else None


# ---------------------------------------------------------------------------
# Genel bağlam (araclar/kod_baglami.hpp)
# ---------------------------------------------------------------------------

def genel_baglami_yukle():
    """{ad: (değişken mi, bağımlılıklar, tanım)}"""
    yol = os.path.join(KOK, "araclar", "kod_baglami.hpp")
    sozluk, ad = {}, None
    if not os.path.exists(yol):
        return sozluk
    with open(yol, encoding="utf-8") as f:
        for satir in f.read().split("\n"):
            m = re.match(r"^//(@@?) (\w+)(?:\s*:\s*(.*))?$", satir)
            if m:
                ad = m.group(2)
                sozluk[ad] = [m.group(1) == "@@", (m.group(3) or "").split(), []]
            elif ad and not satir.startswith("//"):
                sozluk[ad][2].append(satir)
    return {a: (d, b, "\n".join(t).strip()) for a, (d, b, t) in sozluk.items()}


GENEL = genel_baglami_yukle()


def eksik_adlar(hatalar):
    return {m.group(1) for _, mesaj in hatalar for r in EKSIK_AD for m in [r.search(mesaj)] if m}


def yalniz_anlamsal(hatalar):
    """Hataların hiçbiri ad bulunamaması ya da yerleşim kaynaklı değilse True."""
    return all(not any(r.search(m) for r in EKSIK_AD) and not YERLESIM_HATASI.search(m)
               and not SINIF_ADI_YOK.search(m) for _, m in hatalar)


def genel_metin(adlar):
    """Adları bağımlılıklarıyla birlikte, sözlükteki sırayla (türler, değişkenler) olarak verir."""
    gerekli, yigin = set(), list(adlar)
    while yigin:
        a = yigin.pop()
        if a in GENEL and a not in gerekli:
            gerekli.add(a)
            yigin += GENEL[a][1]
    turler = [GENEL[a][2] for a in GENEL if a in gerekli and not GENEL[a][0]]
    degiskenler = [GENEL[a][2] for a in GENEL if a in gerekli and GENEL[a][0]]
    return "\n".join(turler), "\n".join(degiskenler)


# ---------------------------------------------------------------------------
# Derleme
# ---------------------------------------------------------------------------

def c_derleyicisi(komut):
    ad = os.path.basename(komut)
    return os.path.join(os.path.dirname(komut), ad.replace("clang++", "clang").replace("g++", "gcc"))


class Derleyici:
    def __init__(self, komut, gecici):
        self.komut = komut
        self.c_komut = c_derleyicisi(komut)
        self.gecici = gecici
        self.onsoz_yolu = {}
        self.onsoz_bayraklari = {}

    def ad(self):
        return os.path.basename(self.komut)

    def onsoz_hazirla(self, std):
        """Önsözü bir kez ön derlenmiş başlığa çevirir; olmazsa düz dahil eder."""
        yol = os.path.join(self.gecici, f"onsoz-{std}.hpp")
        with open(yol, "w", encoding="utf-8") as f:
            f.write(onsoz())
        self.onsoz_yolu[std] = yol
        self.onsoz_bayraklari[std] = ["-include", yol]
        if "clang" in self.ad():
            pch = yol + ".pch"
            r = subprocess.run([self.komut, f"-std={std}", "-x", "c++-header", yol, "-o", pch],
                               capture_output=True, text=True, env=ORTAM)
            if r.returncode == 0:
                self.onsoz_bayraklari[std] = ["-include-pch", pch]
        else:
            # GCC, -include ile verilen başlığın yanındaki .gch dosyasını kendiliğinden kullanır.
            subprocess.run([self.komut, f"-std={std}", "-pedantic-errors", "-x", "c++-header",
                            yol, "-o", yol + ".gch"], capture_output=True, text=True, env=ORTAM)

    def _calistir(self, komut, yol):
        r = subprocess.run(komut, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", env=ORTAM)
        hatalar = []
        for s in r.stderr.splitlines():
            m = re.match(r"^(.*?):(\d+):\d+: (?:fatal )?error: (.*)$", s)
            if m and os.path.basename(m.group(1)) == os.path.basename(yol):
                hatalar.append((int(m.group(2)), m.group(3).strip()))
            elif m:
                hatalar.append((0, m.group(3).strip()))
        if r.returncode != 0 and not hatalar:
            hatalar.append((0, r.stderr.strip()[:200]))
        return r.returncode == 0, hatalar

    def derle(self, kod, std, ad):
        """(başarılı mı, [(satır, mesaj), ...]) döndürür."""
        if std == C_STANDARDI:
            return self.derle_c(kod, ad)
        yol = os.path.join(self.gecici, ad + ".cpp")
        with open(yol, "w", encoding="utf-8") as f:
            f.write(kod)
        return self._calistir([self.komut, f"-std={std}", "-pedantic-errors", "-fsyntax-only",
                               "-fmax-errors=20" if "g++" in self.ad() else "-ferror-limit=20",
                               *self.onsoz_bayraklari[std], yol], yol)

    def derle_c(self, kod, ad):
        yol = os.path.join(self.gecici, ad + ".c")
        with open(yol, "w", encoding="utf-8") as f:
            f.write(kod)
        basliklar = [x for b in C_BASLIKLARI for x in ("-include", b)]
        # Prototipsiz işlev bildirimi C17'de geçerli ama eskimiş; Clang bunu -pedantic-errors
        # altında hataya çevirir. Kitabın C örnekleri tam da bu yazımı gösterir.
        return self._calistir([self.c_komut, f"-std={C_STANDARDI}", "-pedantic-errors",
                               "-Wno-strict-prototypes", "-Wno-deprecated-non-prototype",
                               "-fsyntax-only", *basliklar, yol], yol)

    def calistir(self, kod, std, ad, is_parcacigi):
        """Programı sanitizer ile derleyip çalıştırır."""
        yol = os.path.join(self.gecici, ad + "_prog.cpp")
        exe = os.path.join(self.gecici, ad + "_prog")
        with open(yol, "w", encoding="utf-8") as f:
            f.write(kod)
        sanitizer = "thread" if is_parcacigi else "address,undefined"
        # Ön derlenmiş başlık sanitizer bayraklarıyla uyuşmaz; yanında .pch/.gch olmayan kopya.
        onsoz_kopya = self.onsoz_yolu[std].replace(".hpp", "-calistir.hpp")
        if not os.path.exists(onsoz_kopya):
            shutil.copyfile(self.onsoz_yolu[std], onsoz_kopya)
        r = subprocess.run([self.komut, f"-std={std}", "-g", "-O1", f"-fsanitize={sanitizer}",
                            "-fno-sanitize-recover=all", "-fno-omit-frame-pointer",
                            "-include", onsoz_kopya, yol, "-o", exe,
                            *(["-pthread"] if is_parcacigi else [])],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", env=ORTAM)
        if r.returncode != 0 and re.search(r"Undefined symbols|undefined reference", r.stderr):
            # Örnek bildirdiği işlevleri tanımlamıyor; derlenir ama program olarak bağlanamaz.
            return {"durum": "baglanamadi", "sanitizer": sanitizer}
        if r.returncode != 0:
            hata = next((x for x in r.stderr.splitlines() if "error" in x), r.stderr.strip()[:200])
            return {"durum": "derlenemedi", "ayrinti": [hata]}
        try:
            p = subprocess.run([exe], capture_output=True, text=True, encoding="utf-8",
                               errors="replace", timeout=CALISMA_SURESI, stdin=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            return {"durum": "zaman-asimi", "sanitizer": sanitizer}
        uyari = next((s.strip() for s in p.stderr.splitlines()
                      if re.search(r"runtime error|ERROR: AddressSanitizer|WARNING: ThreadSanitizer|"
                                   r"ERROR: LeakSanitizer|SUMMARY: \w+Sanitizer", s)), "")
        return {"durum": "uyari" if uyari else "temiz", "uyari": uyari, "sanitizer": sanitizer,
                "kod": p.returncode, "cikti": p.stdout}


# ---------------------------------------------------------------------------
# Denetim
# ---------------------------------------------------------------------------

def blok_adi(blok):
    return re.sub(r"\W", "_", f"{blok['yol']}_{blok['satir']}")


def birlesik(blok, onceki):
    """Önceki blokların satırlarını bloğun önüne ekleyen sanal blok."""
    return dict(blok, satirlar=onceki + blok["satirlar"])


def hata_satirlarini_sina(der, blok, hata_satirlari, gecenler, ad, kayit):
    """Bilerek hata veren her satırı derlenen yerleşimlerin en dıştakinde ve en içtekinde sınar.

    Ad alanı düzeyinde her deyim, gövdede de her şablon bildirimi kendiliğinden hata verir;
    iki yerleşimde birden o satırda hata çıkması, hatanın yerleşimden doğmadığını gösterir.
    (doğrulananlar, bozmayanlar) döndürür.
    """
    dogrulanan, bozmayan = [], []
    sinanacak = [gecenler[0]] + ([gecenler[-1]] if len(gecenler) > 1 else [])
    for i in hata_satirlari:
        mesajlar, bozmadi = [], None
        for yer, sanal, haric, dis, ic, genel in sinanacak:
            j = i + len(sanal["satirlar"]) - len(blok["satirlar"])
            kod = kaynak(sanal, dis, ic, haric - {j}, isaretli=j, genel=genel)
            hedef = next(n for n, s in enumerate(kod.split("\n"), 1) if ISARET in s)
            ok, hatalar = der.derle(kod, blok["std"], f"{ad}_h{i}")
            if kayit is not None:
                kayit.append((f"hata satırı {i + 1} ({yer})", kod, hatalar))
            o_satirda = [m for n, m in hatalar if n == hedef]
            if o_satirda:
                mesajlar.append(o_satirda[0])
            else:
                bozmadi = (yer, hatalar[0][1] if hatalar else "derlendi")
        satir = blok["satirlar"][i].strip()
        if bozmadi:
            bozmayan.append((satir, f"{bozmadi[0]}: {bozmadi[1]}"))
        else:
            # Gösterilecek mesaj: yerleşimden doğmayan ilk mesaj (yoksa en dıştaki).
            anlamli = [m for m in mesajlar if not YERLESIM_HATASI.search(m)]
            dogrulanan.append((satir, (anlamli or mesajlar)[0]))
    return dogrulanan, bozmayan


def c_denetle(der, blok, kayit=None):
    """Bloğu C olarak denetler. 'gecti' ya da sorunun açıklamasını döndürür."""
    ad = blok_adi(blok) + "_c"
    yorumlar = satirlari_cozumle(blok["satirlar"])[1]
    alinan = [s for s, y in zip(blok["satirlar"], yorumlar) if not yalniz_cpp_mi(y)]
    sanal = dict(blok, satirlar=alinan, baglam="", std=C_STANDARDI)
    hata_satirlari = [i for i, y in enumerate(satirlari_cozumle(alinan)[1]) if c_hata_satiri_mi(y)]
    haric = set(hata_satirlari)
    gecenler, ilk_hata = [], None
    for yer, dis, ic in yerlesimler(sanal):
        kod = kaynak(sanal, dis, ic, haric)
        ok, hatalar = der.derle_c(kod, ad)
        if kayit is not None:
            kayit.append((f"C: {yer}", kod, hatalar))
        if ok:
            gecenler.append((yer, sanal, haric, dis, ic, ("", "")))
        elif ilk_hata is None:
            ilk_hata = hatalar[0][1] if hatalar else "?"
    if not gecenler:
        return f"C'de derlenmedi: {ilk_hata}", []
    dogrulanan, bozmayan = hata_satirlarini_sina(der, sanal, hata_satirlari, gecenler, ad, kayit)
    if bozmayan:
        return "C'de hata vermesi gereken satır derlendi: " + "; ".join(f"`{x}`" for x, _ in bozmayan), dogrulanan
    return "gecti", dogrulanan


def blogu_denetle(der, blok, oncekiler, kayit=None):
    """Bloğu denetler. oncekiler: aynı dosyada önce gelen, derlenmiş blokların temiz satırları.
    Sonuç sözlüğünde 'durum':
    gecti | atlandi | derlenmedi | hata-satiri-sorunu | derleyici-eksigi
    """
    if "atla" in blok["isaretler"]:
        return {"durum": "atlandi"}
    if blok["dil"] == "c":
        c, dogrulanan = c_denetle(der, blok, kayit)
        return {"durum": "gecti" if c == "gecti" else "derlenmedi", "kip": "C", "c": c,
                "hatalar": [(0, c)], "dogrulanan": [(x, "C: " + m) for x, m in dogrulanan]}
    ad = blok_adi(blok)
    yerel_hatalar = [i for i, y in enumerate(satirlari_cozumle(blok["satirlar"])[1]) if hata_satiri_mi(y)]
    temiz = [s for i, s in enumerate(blok["satirlar"]) if i not in yerel_hatalar]

    adaylar = [("", [])]
    if oncekiler:
        adaylar.append(("+önceki", oncekiler[-1]))
        if len(oncekiler) > 1:
            adaylar.append(("+öncekiler", [s for x in oncekiler for s in x]))
    ifade = ifade_satirlari(blok["satirlar"])
    surumler = [("", blok)] + ([("+ifade", dict(blok, satirlar=ifade))] if ifade else [])

    def dene(genel_adlar):
        en_iyi, gecenler, tum = None, [], []
        genel = genel_metin(genel_adlar)
        etiket_g = "+genel" if genel_adlar else ""
        for etiket_s, surum in surumler:
            for onek_adi, onek in adaylar:
                sanal = birlesik(surum, onek)
                haric = {i + len(onek) for i in yerel_hatalar}
                for yer, dis, ic in yerlesimler(sanal):
                    kod = kaynak(sanal, dis, ic, haric, genel=genel)
                    ok, hatalar = der.derle(kod, blok["std"], ad)
                    etiket = yer + onek_adi + etiket_s + etiket_g
                    if kayit is not None:
                        kayit.append((etiket, kod, hatalar))
                    if ok:
                        gecenler.append((etiket, sanal, haric, dis, ic, genel))
                        if not yerel_hatalar:
                            break
                    else:
                        tum += hatalar
                        if en_iyi is None or len(hatalar) < len(en_iyi[1]):
                            en_iyi = (etiket, hatalar)
                if gecenler:
                    return en_iyi, gecenler, tum
        return en_iyi, gecenler, tum

    en_iyi, gecenler, tum = dene(set())
    # Kendi bağlamıyla derlenmeyen blokta bulunamayan bir ad varsa genel bağlam denenir.
    # En iyi deneme yalnızca başka türden hata veriyorsa (ad bulunmuş ama kullanımı
    # geçersiz) genel bağlam o hatayı örtebileceği için denenmez.
    sinif_adi_yok = any(SINIF_ADI_YOK.search(m) for _, m in tum)
    if not gecenler and GENEL and not yalniz_anlamsal(en_iyi[1]) and (eksik_adlar(tum) or sinif_adi_yok):
        adlar = set()
        metin = blok["baglam"] + "\n" + "\n".join(blok["satirlar"])
        for _ in range(3):
            yeni = (eksik_adlar(tum) & set(GENEL)) - adlar
            if sinif_adi_yok:
                yeni |= {a for a in GENEL if re.search(rf"\b{a}\b", metin)} - adlar
            # Blokta ya da bağlamında bildirilen ad için genel değişken eklenmez.
            yeni = {a for a in yeni if not (GENEL[a][0] and re.search(
                rf"[\w>\]&*]\s+[*&]*{a}\s*[=;{{(\[,):]", metin))}
            if not yeni:
                break
            adlar |= yeni
            en_iyi_g, gecenler, tum_g = dene(adlar)
            tum += tum_g
            if gecenler:
                break
            if len(en_iyi_g[1]) < len(en_iyi[1]):
                en_iyi = en_iyi_g
    if not gecenler:
        for kalip, aciklama in BILINEN_EKSIKLER:
            if any(re.search(kalip, m) for _, m in tum + en_iyi[1]):
                return {"durum": "derleyici-eksigi", "aciklama": aciklama}
        return {"durum": "derlenmedi", "kip": en_iyi[0], "hatalar": en_iyi[1],
                "hata_satiri": len(yerel_hatalar)}

    dogrulanan, bozmayan = hata_satirlarini_sina(der, blok, yerel_hatalar, gecenler, ad, kayit)
    yer, sanal, haric, dis, ic, genel = gecenler[0]
    sonuc = {"durum": "hata-satiri-sorunu" if bozmayan else "gecti", "kip": yer,
             "hata_satiri": len(yerel_hatalar), "temiz": temiz,
             "dogrulanan": dogrulanan, "bozmayanlar": bozmayan}
    if not ic and re.search(r"\bint\s+main\s*\(", "\n".join(temiz)):
        sonuc["program"] = kaynak(sanal, dis, ic, haric, genel=genel)
    if "c" in blok["isaretler"]:
        sonuc["c"], c_dogrulanan = c_denetle(der, blok, kayit)
        sonuc["dogrulanan"] += [(x, "C: " + m) for x, m in c_dogrulanan]
    return sonuc


def dosyayi_denetle(der, bloklar, calistir=True):
    """Bir dosyanın blokları sırayla denetlenir; geçenler sonrakilere bağlam olabilir."""
    oncekiler, sonuclar = [], []
    for b in bloklar:
        s = blogu_denetle(der, b, oncekiler)
        if calistir and s.get("program"):
            is_parcacigi = re.search(r"std::(j?thread|async)\b", s["program"]) is not None
            s["calisma"] = der.calistir(s["program"], b["std"], blok_adi(b), is_parcacigi)
            s["calisma"]["beklenti"] = "tanımsız" if tanimsiz_mi(b) else "tanımlı"
        sonuclar.append((b, s))
        if s.get("temiz"):
            oncekiler.append(s["temiz"])
    return sonuclar


def sorunlu_mu(s):
    if s["durum"] in ("derlenmedi", "hata-satiri-sorunu"):
        return True
    if s.get("c", "gecti") != "gecti":
        return True
    c = s.get("calisma")
    return bool(c) and c["beklenti"] == "tanımlı" and c["durum"] in ("uyari", "zaman-asimi", "derlenemedi")


# ---------------------------------------------------------------------------
# Rapor
# ---------------------------------------------------------------------------

def hucre(metin):
    return metin.replace("|", "\\|").replace("\n", " ")


def rapor(derleyici_sonuclari, toplam):
    satirlar = ["# Kod denetimi raporu", "",
                "Bu dosya `araclar/kod_denetimi.py` tarafından üretilir; elle düzenlemeyin.", ""]
    for ad, sonuclar in derleyici_sonuclari.items():
        sayac, kipsay = {}, {}
        for _, s in sonuclar:
            sayac[s["durum"]] = sayac.get(s["durum"], 0) + 1
            if s["durum"] not in ("derlenmedi", "atlandi", "derleyici-eksigi") and s.get("kip"):
                k = re.sub(r":\d+", "", s["kip"])
                kipsay[k] = kipsay.get(k, 0) + 1
        satirlar += [f"## {ad}", "",
                     f"Toplam {toplam} blok: " + ", ".join(f"{k} {v}" for k, v in sorted(sayac.items())) + ".",
                     "Derlenenlerin yerleşimi: " + ", ".join(f"{k} {v}" for k, v in sorted(kipsay.items())) + ".",
                     ""]
        sorunlu = [(b, s) for b, s in sonuclar if sorunlu_mu(s)]
        if sorunlu:
            satirlar += ["### Sorunlu bloklar", "",
                         "| Dosya | Satır | Durum | Ayrıntı |", "|---|---|---|---|"]
            for b, s in sorunlu:
                if s["durum"] == "derlenmedi":
                    n, m = s["hatalar"][0]
                    durum, ayr = "derlenmedi", f"({s['kip']}, {len(s['hatalar'])} hata) {m}"
                elif s["durum"] == "hata-satiri-sorunu":
                    durum = "hata satırı derlendi"
                    ayr = "; ".join(f"`{x}` → {m}" for x, m in s["bozmayanlar"])
                elif s.get("c", "gecti") != "gecti":
                    durum, ayr = "C", s["c"]
                else:
                    c = s["calisma"]
                    durum = "çalıştırma"
                    ayr = {"uyari": c.get("uyari", ""), "zaman-asimi": f"{CALISMA_SURESI} sn'de bitmedi",
                           "derlenemedi": "sanitizer ile derlenemedi: " + " ".join(c.get("ayrinti", []))}[c["durum"]]
                satirlar.append(f"| `{b['yol']}` | {b['satir']} | {durum} | {hucre(ayr)} |")
            satirlar.append("")
        eksik = [(b, s) for b, s in sonuclar if s["durum"] == "derleyici-eksigi"]
        if eksik:
            satirlar += ["### Derleyicinin eksikleri", "",
                         "Bu bloklar standart C++'tır; bu derleyicinin kütüphanesi ilgili parçayı sunmuyor.", "",
                         "| Dosya | Satır | Açıklama |", "|---|---|---|"]
            satirlar += [f"| `{b['yol']}` | {b['satir']} | {s['aciklama']} |" for b, s in eksik]
            satirlar.append("")
        calisan = [(b, s["calisma"]) for b, s in sonuclar if s.get("calisma")]
        if calisan:
            satirlar += ["### Çalıştırılan örnekler", "",
                         "Beklenti, örneğin yorumlarında \"tanımsız\" geçip geçmediğine göre belirlenir. "
                         "Tanımsız davranışın her türünü sanitizer yakalamaz (ör. ilk değer verilmemiş "
                         "değişkeni okumak); \"temiz\" sonucu tanımlı davranışın kanıtı değildir.", "",
                         "| Dosya | Satır | Beklenti | Sanitizer | Sonuç | Çıktı |", "|---|---|---|---|---|---|"]
            for b, c in calisan:
                sonuc = c.get("uyari") or c["durum"]
                cikti = " ⏎ ".join(c.get("cikti", "").strip().splitlines())[:120]
                satirlar.append(f"| `{b['yol']}` | {b['satir']} | {c['beklenti']} | {c.get('sanitizer', '')} "
                                f"| {hucre(sonuc)} | {hucre(cikti)} |")
            satirlar.append("")
        dogrulanan = [(b, x, m) for b, s in sonuclar for x, m in s.get("dogrulanan", [])]
        if dogrulanan:
            satirlar += ["### Doğrulanan hata satırları", "",
                         "Kitabın hata verdiğini söylediği satırlar ve derleyicinin o satır için ilk mesajı.",
                         "Mesajın kitaptaki açıklamayla örtüştüğü gözle denetlenmelidir.", "",
                         "| Dosya | Satır | Kod | Derleyici |", "|---|---|---|---|"]
            for b, x, m in dogrulanan:
                satirlar.append(f"| `{b['yol']}` | {b['satir']} | `{hucre(x)}` | {hucre(m)} |")
            satirlar.append("")
    return "\n".join(satirlar) + "\n"


def goster(der, bloklar, hedef):
    yol, _, satir = hedef.rpartition(":")
    secilen = [b for b in bloklar if b["yol"].endswith(yol) and str(b["satir"]) == satir]
    if not secilen:
        print(f"Blok bulunamadı: {hedef}")
        return
    b = secilen[0]
    oncekiler = []
    for x in bloklar:
        if x is b:
            break
        if x["yol"] == b["yol"]:
            s = blogu_denetle(der, x, oncekiler)
            if s.get("temiz"):
                oncekiler.append(s["temiz"])
    kayit = []
    s = blogu_denetle(der, b, oncekiler, kayit)
    for yer, kod, hatalar in kayit:
        print(f"===== {yer}")
        print(kod)
        for n, m in hatalar[:5]:
            print(f"  ! {n}: {m}")
    print("===== sonuç:", {k: v for k, v in s.items() if k not in ("temiz", "program")})


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Kitaptaki C++ kod bloklarını derler")
    ap.add_argument("--derleyici", action="append",
                    help="kullanılacak C++ derleyicisi (birden çok verilebilir; varsayılan clang++)")
    ap.add_argument("--kati", action="store_true", help="sorunlu blok varsa hata koduyla çık")
    ap.add_argument("--calistirma", action="store_true", help="örnekleri sanitizer ile çalıştırma")
    ap.add_argument("--cikti", default=os.path.join(KOK, "cikti"))
    ap.add_argument("--paralel", type=int, default=os.cpu_count() or 4, help="eşzamanlı iş sayısı")
    ap.add_argument("--goster", metavar="DOSYA:SATIR", help="tek bloğun denemelerini göster")
    arg = ap.parse_args()

    komutlar = arg.derleyici or ["clang++"]
    for k in komutlar:
        if not shutil.which(k):
            print(f"HATA: derleyici bulunamadı: {k}")
            sys.exit(2)
    bloklar = bloklari_topla()
    dosyalara = {}
    for b in bloklar:
        dosyalara.setdefault(b["yol"], []).append(b)

    sonuclar = {}
    with tempfile.TemporaryDirectory(prefix="kod-denetimi-") as gecici:
        for k in komutlar:
            der = Derleyici(shutil.which(k), os.path.join(gecici, os.path.basename(k)))
            os.makedirs(der.gecici)
            for std in sorted(set(CILT_STANDARDI.values())):
                der.onsoz_hazirla(std)
            if arg.goster:
                goster(der, bloklar, arg.goster)
                return
            with concurrent.futures.ThreadPoolExecutor(arg.paralel) as havuz:
                isler = [havuz.submit(dosyayi_denetle, der, bl, not arg.calistirma)
                         for bl in dosyalara.values()]
                sonuclar[k] = [x for i in isler for x in i.result()]

    os.makedirs(arg.cikti, exist_ok=True)
    with open(os.path.join(arg.cikti, "kod_denetimi.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(rapor(sonuclar, len(bloklar)))
    sorun = 0
    for ad, ss in sonuclar.items():
        say = {}
        for _, s in ss:
            say[s["durum"]] = say.get(s["durum"], 0) + 1
        n = sum(1 for _, s in ss if sorunlu_mu(s))
        sorun += n
        print(f"{ad}: {len(ss)} blok — " + ", ".join(f"{k} {v}" for k, v in sorted(say.items()))
              + f"; sorunlu {n}")
    print("Rapor: " + os.path.relpath(os.path.join(arg.cikti, "kod_denetimi.md"), KOK))
    if os.environ.get("GITHUB_ACTIONS") == "true":
        # İş günlükleri ve özet yalnızca oturum açınca görünür; annotation'lar herkese açıktır.
        for ad, ss in sonuclar.items():
            for b, s in ss:
                if sorunlu_mu(s):
                    ileti = f"{os.path.basename(ad)}: {sorun_ozeti(s)}".replace("%", "%25").replace("\n", " ")
                    print(f"::error file={b['yol']},line={b['satir']}::{ileti[:900]}")
    sys.exit(1 if arg.kati and sorun else 0)


def sorun_ozeti(s):
    """Sorunlu bir bloğun tek satırlık açıklaması."""
    if s["durum"] == "derlenmedi":
        return f"derlenmedi ({s['kip']}): {s['hatalar'][0][1]}"
    if s["durum"] == "hata-satiri-sorunu":
        return "hata satırı derlendi: " + "; ".join(f"{x} → {m}" for x, m in s["bozmayanlar"])
    if s.get("c", "gecti") != "gecti":
        return s["c"]
    c = s.get("calisma") or {}
    return f"çalıştırma: {c.get('uyari') or c.get('durum')} {' '.join(c.get('ayrinti', []))}".strip()


if __name__ == "__main__":
    main()
