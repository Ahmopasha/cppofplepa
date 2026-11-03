---
cilt: "I — Temel"
kisim: "1 — C ve C++ İçindeki C"
baslik: "1.7 Operatörlerin değer kategorileri"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 1.7 Operatörlerin değer kategorileri

Kısım 2.4.4'te ayrıntılandırılır. `++x`, `--x`, atama, virgül ve koşul operatörü C'de
R-Value üretirken C++'ta L-Value üretebilir. Bu, C'de geçersiz olan bazı yazımları C++'ta
geçerli kılar:

<!-- kod: c -->
```cpp
int x = 0;
++x = 5;           // C'de sentaks hatası, C++'ta geçerli
```
