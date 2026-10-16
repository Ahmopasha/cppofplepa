---
cilt: "I — Temel"
kisim: "6 — Sabitler"
baslik: "6.6 `constexpr` işlevler"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 6.6 `constexpr` işlevler

Bir işlev `constexpr` olarak nitelenirse, **argümanları derleme zamanında biliniyorsa
sonucu da derleme zamanında hesaplanabilir** demektir.

```cpp
constexpr int kare(int x) { return x * x; }

constexpr int a = kare(5);     // derleme zamanında hesaplanır
int n = oku();
int b = kare(n);               // çalışma zamanında çalışır
```

Aynı işlev her iki şekilde de kullanılabilir. `constexpr`, "her zaman derleme zamanında
çalış" demek değil, "gerekirse çalışabil" demektir.

`constexpr` işlevler örtülü olarak `inline`'dır (bkz. Kısım 11.3).

**Derleme zamanında neler yapılamaz?** Derleyici, `constexpr` olmayan bir işlevin
gövdesini derleme zamanında çalıştırmaz. `constexpr` bir işlev derleme zamanında
çağrıldığında ise gövdesini derleyici yürütür; bu yüzden o çağrıda yürütülen kodun
yapabilecekleri sınırlıdır. Giriş-çıkış gibi çalışma zamanına ait işler yapılamaz.
C++20'den itibaren dinamik bellek de ayrılabilir, ama aynı hesaplama bitmeden geri
verilmelidir.

Bu sınırların C++11'den C++23'e kadar nasıl gevşediği ve `consteval` ile `constinit`
anahtar sözcükleri: **Cilt II, Kısım 18.**
