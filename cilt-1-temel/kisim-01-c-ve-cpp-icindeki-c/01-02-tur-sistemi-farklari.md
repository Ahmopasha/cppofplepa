---
cilt: "I — Temel"
kisim: "1 — C ve C++ İçindeki C"
baslik: "1.2 Tür sistemi farkları"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 1.2 Tür sistemi farkları

**`bool` gerçek bir türdür.** C'de `bool`, `stdbool.h` ile gelen bir makrodur ve `int`
üzerine kuruludur. C++'ta yerleşik bir türdür.

**Karşılaştırma ve mantık operatörleri `bool` döndürür.** C'de `int` döndürürler.

```cpp
sizeof(1 == 1);     // C'de 4, C++'ta 1
```

**Karakter sabitlerinin türü `char`'dır.** C'de `int`'tir.

```cpp
sizeof('A');        // C'de 4, C++'ta 1
```

**Yazı sabitlerinin türü `const char[N]`'dir.** C'de `char[N]`'dir (bkz. Kısım 6.2).
