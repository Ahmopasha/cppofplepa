"""Kitap araçlarının başarı sinyali için regresyon testleri.

Çalıştırma (depo kökünden): python3 -m unittest discover -s araclar/testler

1. derle.py --kod, kod denetimi çalışamazsa (derleyici yok) başarısız döner; --kati'yi aktarır.
2. Çalıştırılan örneğin çıkış kodu beklentiyle karşılaştırılır (varsayılan 0; cikis-N, cikis-sinyal).
3. Derleyici farkı: çalışma zamanı bulgusu muaf tutulmaz; derleme farkı yalnızca bloğun özetine
   ve derleyici sürümüne bağlı gerekçeli kayıtla geçer. Kayıt, aynı sonuçtaki çalışma zamanı
   bulgusunu kapatmaz.
"""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ARACLAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KOK = os.path.dirname(ARACLAR)
sys.path.insert(0, ARACLAR)

import kod_denetimi as kd  # noqa: E402

DERLEYICI = shutil.which("clang++") or shutil.which("g++")


def blok(satirlar, isaretler=(), yol="cilt-2-ileri/ornek.md", satir=10):
    return {"yol": yol, "satir": satir, "dil": "cpp", "std": "c++23", "isaretler": set(isaretler),
            "satirlar": list(satirlar), "baglam": ""}


class TestDerleCikisKodu(unittest.TestCase):
    def test_missing_compiler_fails_build(self):
        bos = tempfile.mkdtemp(prefix="bos-path-")
        cikti = tempfile.mkdtemp(prefix="derle-cikti-")
        try:
            r = subprocess.run([sys.executable, os.path.join(ARACLAR, "derle.py"), "--kod", "--cikti", cikti],
                               cwd=KOK, capture_output=True, text=True, env=dict(os.environ, PATH=bos))
            self.assertNotEqual(r.returncode, 0, r.stdout[-500:])
            self.assertIn("derleyici bulunamadı", r.stdout)
            self.assertIn("kod denetimi basarisiz", r.stdout)
        finally:
            shutil.rmtree(bos, ignore_errors=True)
            shutil.rmtree(cikti, ignore_errors=True)

    def test_kati_is_passed_to_code_check(self):
        with open(os.path.join(ARACLAR, "derle.py"), encoding="utf-8") as f:
            self.assertIn('*(["--kati"] if arg.kati else [])', f.read())


class TestBeklenenCikis(unittest.TestCase):
    def test_markers(self):
        self.assertEqual(kd.beklenen_cikis(set()), 0)
        self.assertEqual(kd.beklenen_cikis({"cikis-3"}), 3)
        self.assertEqual(kd.beklenen_cikis({"cikis-sinyal"}), "sinyal")
        self.assertTrue(kd.cikis_uygun(0, 0))
        self.assertFalse(kd.cikis_uygun(1, 0))
        self.assertTrue(kd.cikis_uygun(-6, "sinyal"))
        self.assertFalse(kd.cikis_uygun(0, "sinyal"))

    @unittest.skipUnless(DERLEYICI, "C++ derleyicisi yok")
    def test_nonzero_exit_is_a_problem_unless_expected(self):
        gecici = tempfile.mkdtemp(prefix="kod-test-")
        try:
            der = kd.Derleyici(DERLEYICI, gecici)
            der.onsoz_hazirla("c++23")
            for isaret, sorunlu in (((), True), (("cikis-1",), False)):
                b = blok(["int main()", "{", "    return 1;", "}"], isaret)
                [(_, s)] = kd.dosyayi_denetle(der, [b])
                self.assertEqual(s["calisma"]["kod"], 1)
                self.assertEqual(kd.sorunlu_mu(s), sorunlu, isaret)
                if sorunlu:
                    self.assertEqual(s["calisma"]["durum"], "beklenmeyen-cikis")
        finally:
            shutil.rmtree(gecici, ignore_errors=True)


class TestDerleyiciFarki(unittest.TestCase):
    def sonuclar(self, sorunlu_s, b=None):
        b = b or blok(["int x;"])
        return b, {"g++-14": [(b, sorunlu_s)], "clang++-18": [(b, {"durum": "gecti"})]}

    ANAHTAR = {"g++-14": "g++ 14", "clang++-18": "clang++ 18"}

    def test_runtime_finding_is_never_exempted(self):
        s = {"durum": "gecti", "calisma": {"beklenti": "tanımlı", "durum": "uyari", "uyari": "runtime error"}}
        _, ss = self.sonuclar(s)
        kd.derleyici_farklarini_isle(ss, self.ANAHTAR, istisnalar=[])
        self.assertEqual(s["durum"], "gecti")
        self.assertTrue(kd.sorunlu_mu(s), "baska derleyicinin temiz sonucu sanitizer bulgusunu kapatmamali")

    def test_compile_difference_needs_registered_exception(self):
        s = {"durum": "derlenmedi", "kip": "birim", "hatalar": [(1, "hata")]}
        b, ss = self.sonuclar(s)
        kd.derleyici_farklarini_isle(ss, self.ANAHTAR, istisnalar=[])
        self.assertEqual(s["durum"], "derleyici-farki")
        self.assertTrue(kd.sorunlu_mu(s), "kayitsiz fark kati kapidan gecmemeli")
        self.assertIn(s["fark_anahtar"]["ozet"], kd.sorun_ozeti(s))

    def test_matching_exception_passes_and_stale_one_does_not(self):
        b = blok(["int x;"])
        kayit = {"yol": b["yol"], "ozet": kd.blok_ozeti(b), "derleyici": "g++ 14", "gerekce": "GCC sapiyor."}
        s = {"durum": "derlenmedi", "kip": "birim", "hatalar": [(1, "hata")]}
        _, ss = self.sonuclar(s, b)
        kd.derleyici_farklarini_isle(ss, self.ANAHTAR, istisnalar=[kayit])
        self.assertFalse(kd.sorunlu_mu(s))
        self.assertEqual(s["istisna"], "GCC sapiyor.")
        for degisen in (dict(kayit, ozet="eski"), dict(kayit, derleyici="g++ 15")):
            s = {"durum": "derlenmedi", "kip": "birim", "hatalar": [(1, "hata")]}
            _, ss = self.sonuclar(s, b)
            kd.derleyici_farklarini_isle(ss, self.ANAHTAR, istisnalar=[degisen])
            self.assertTrue(kd.sorunlu_mu(s), f"kod ya da surum degisince kayit gecersiz: {degisen}")


    def test_exception_does_not_cover_runtime_finding_in_same_result(self):
        b = blok(["int x;"])
        kayit = {"yol": b["yol"], "ozet": kd.blok_ozeti(b), "derleyici": "g++ 14", "gerekce": "GCC sapiyor."}
        for calisma in ({"durum": "uyari", "uyari": "runtime error: load of null pointer"},
                        {"durum": "zaman-asimi"},
                        {"durum": "beklenmeyen-cikis", "ayrinti": ["çıkış kodu 1, beklenen 0"]}):
            s = {"durum": "hata-satiri-sorunu", "bozmayanlar": [("x", "derlendi")],
                 "calisma": dict(calisma, beklenti="tanımlı")}
            _, ss = self.sonuclar(s, b)
            kd.derleyici_farklarini_isle(ss, self.ANAHTAR, istisnalar=[kayit])
            self.assertEqual(s["durum"], "derleyici-farki")
            self.assertEqual(s["istisna"], "GCC sapiyor.")
            self.assertTrue(kd.sorunlu_mu(s), f"istisna calisma zamani bulgusunu kapatmamali: {calisma}")
            self.assertTrue(kd.sorun_ozeti(s).startswith("çalıştırma:"), kd.sorun_ozeti(s))
            rapor = kd.rapor({"g++-14": [(b, s)], "clang++-18": [(b, {"durum": "gecti"})]}, 1)
            self.assertIn("### Sorunlu bloklar", rapor)


class TestCIKapsami(unittest.TestCase):
    def test_tarama_changes_trigger_code_check(self):
        with open(os.path.join(KOK, ".github", "workflows", "kod-denetimi.yml"), encoding="utf-8") as f:
            metin = f.read()
        for olay in ("push:", "pull_request:"):
            satir = metin.split(olay, 1)[1].split("paths:", 1)[1].split("\n", 1)[0]
            self.assertIn('"tarama/**"', satir, olay)
            self.assertIn('".github/workflows/kod-denetimi.yml"', satir, olay)


if __name__ == "__main__":
    unittest.main()
