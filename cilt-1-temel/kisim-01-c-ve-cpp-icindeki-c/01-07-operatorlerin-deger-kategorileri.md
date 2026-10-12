---
cilt: "I — Temel"
kisim: "1 — C ve C++ İçindeki C"
baslik: "1.7 Operatörlerin değer kategorileri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 1.7 Operatörlerin değer kategorileri

Kısım 2.4.4'te verilmişti. `++x`, `--x` ve virgül operatörü C'de R-Value üretirken C++'ta
L-Value üretebilir. Bu, C'de geçersiz olan bazı yazımları C++'ta geçerli kılar:

```cpp
int x = 0;
++x = 5;           // C'de sentaks hatası, C++'ta geçerli
```
