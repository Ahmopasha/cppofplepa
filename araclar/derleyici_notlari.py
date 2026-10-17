#!/usr/bin/env python3
"""C++ Başvuru Kitabı — Derleyici Notu testleri.

Kitaptaki her "Derleyici Notu" kutusu, belirli bir derleyicinin bugünkü davranışını
anlatır. testler/derleyici_notlari/ altındaki her .cpp dosyası bir kutunun iddiasını
sınar. Dosyanın başındaki yorum satırları testi tanımlar:

    // tur: derleme | cikti
    // kipler: c++11 c++14 c++17 c++20 c++23
    // beklenti: clang=hata gcc=derlenir msvc=X-Value

"derleme" testinde sonuç "hata" ya da "derlenir"dir; "cikti" testinde program çalıştırılır
ve sonuç, standart çıktının kendisidir. Beklentisi yazılmamış derleyici ailesi için sonuç
yalnızca kaydedilir. Bir beklenti tutmazsa betik hata koduyla çıkar: o gün, kutunun
gözden geçirileceği gündür.

Kullanım (depo kökünden):
    python3 araclar/derleyici_notlari.py --derleyici g++-14
    python3 araclar/derleyici_notlari.py --derleyici clang++
    python araclar/derleyici_notlari.py --derleyici cl          (MSVC geliştirici ortamında)

Yalnızca Python 3.8+ standart kütüphanesi kullanılır.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_KLASORU = os.path.join(KOK, "testler", "derleyici_notlari")
MSVC_KIPLERI = {"c++14": "/std:c++14", "c++17": "/std:c++17", "c++20": "/std:c++20",
                "c++23": "/std:c++latest"}


def aile(komut):
    ad = os.path.basename(komut).lower()
    if ad in ("cl", "cl.exe"):
        return "msvc"
    r = subprocess.run([komut, "--version"], capture_output=True, text=True)
    surum = r.stdout + r.stderr
    if "clang" in surum.lower():
        return "clang"
    if "Free Software Foundation" in surum or "g++" in ad or "gcc" in ad:
        return "gcc"
    return ad


def surum_satiri(komut, ail):
    if ail == "msvc":
        r = subprocess.run([komut], capture_output=True, text=True)
        return (r.stderr.strip().splitlines() or ["cl"])[0]
    r = subprocess.run([komut, "--version"], capture_output=True, text=True)
    return (r.stdout.strip().splitlines() or [komut])[0]


def test_oku(yol):
    tanim = {"tur": "derleme", "kipler": ["c++20"], "beklenti": {}}
    with open(yol, encoding="utf-8") as f:
        for satir in f:
            m = re.match(r"^//\s*(tur|kipler|beklenti):\s*(.*)$", satir.strip())
            if not m:
                continue
            anahtar, deger = m.group(1), m.group(2).strip()
            if anahtar == "tur":
                tanim["tur"] = deger
            elif anahtar == "kipler":
                tanim["kipler"] = deger.split()
            else:
                tanim["beklenti"] = dict(x.split("=", 1) for x in deger.split())
    return tanim


def calistir(komut, ail, yol, kip, tur, gecici):
    """Sonucu döndürür: 'hata' / 'derlenir' ya da programın çıktısı; kip desteklenmiyorsa None."""
    exe = os.path.join(gecici, "test" + (".exe" if ail == "msvc" else ""))
    if ail == "msvc":
        if kip not in MSVC_KIPLERI:
            return None
        bayraklar = ["/nologo", "/EHsc", MSVC_KIPLERI[kip], yol]
        bayraklar += ["/Zs"] if tur == "derleme" else [f"/Fe:{exe}", f"/Fo:{gecici}{os.sep}"]
    else:
        bayraklar = [f"-std={kip}", "-pedantic-errors", yol]
        bayraklar += ["-fsyntax-only"] if tur == "derleme" else ["-o", exe]
    r = subprocess.run([komut] + bayraklar, capture_output=True, text=True, cwd=gecici)
    if tur == "derleme":
        return "derlenir" if r.returncode == 0 else "hata"
    if r.returncode != 0:
        return "derlenemedi: " + (r.stdout + r.stderr).strip().splitlines()[0]
    p = subprocess.run([exe], capture_output=True, text=True, timeout=30)
    return p.stdout.strip()


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Derleyici Notu kutularının iddialarını sınar")
    ap.add_argument("--derleyici", required=True, help="clang++, g++-14, cl ...")
    arg = ap.parse_args()
    komut = shutil.which(arg.derleyici)
    if not komut:
        print(f"HATA: derleyici bulunamadı: {arg.derleyici}")
        sys.exit(2)
    ail = aile(komut)
    print(f"Derleyici: {surum_satiri(komut, ail)} (aile: {ail})\n")

    tutmayan = 0
    for ad in sorted(os.listdir(TEST_KLASORU)):
        if not ad.endswith(".cpp"):
            continue
        yol = os.path.join(TEST_KLASORU, ad)
        tanim = test_oku(yol)
        beklenti = tanim["beklenti"].get(ail)
        for kip in tanim["kipler"]:
            with tempfile.TemporaryDirectory() as gecici:
                sonuc = calistir(komut, ail, yol, kip, tanim["tur"], gecici)
            if sonuc is None:
                continue
            if beklenti is None:
                durum = "kayıt"
            elif sonuc == beklenti:
                durum = "tamam"
            else:
                durum = f"TUTMADI (beklenen: {beklenti})"
                tutmayan += 1
            print(f"{ad:38} {kip:6} {sonuc:12} {durum}")
    if tutmayan:
        print(f"\n{tutmayan} beklenti tutmadı. İlgili Derleyici Notu kutusunu gözden geçirin.")
        sys.exit(1)
    print("\nBütün beklentiler tuttu.")


if __name__ == "__main__":
    main()
