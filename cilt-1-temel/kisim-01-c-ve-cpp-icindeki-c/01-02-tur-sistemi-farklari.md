---
cilt: "I — Temel"
kisim: "1 — C ve C++ İçindeki C"
baslik: "1.2 Tür sistemi farkları"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 1.2 Tür sistemi farkları

**C++'ta `bool` yerleşik bir türdür.** C'de `bool`, `<stdbool.h>` ile gelen ve `_Bool`
türüne genişleyen bir makrodur.

**C'den gelen karşılaştırma ve mantık operatörlerinin yerleşik biçimleri (bkz. Kısım 14) `bool` döndürür.**
C'de `int` döndürürler.

<!-- kod: c -->
```cpp
sizeof(1 == 1);     // C'de sizeof(int), C++'ta sizeof(bool)
```

**`'A'` gibi temel karakter kümesinden *(basic character set)* tek bir karakter içeren, ön
eksiz karakter sabitlerinin türü `char`'dır.** C'de `int`'tir. Temel karakter kümesi
`a`–`z`, `A`–`Z` harflerini, rakamları ve bazı noktalama işaretlerini içerir; Türkçe
harfler bu kümede değildir.

<!-- kod: c -->
```cpp
sizeof('A');        // C'de sizeof(int), C++'ta 1
```

**Yazı sabitlerinin türü `const char[N]`'dir.** C'de `char[N]`'dir (bkz. Kısım 6.2).
