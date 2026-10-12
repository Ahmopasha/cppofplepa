---
cilt: "I — Temel"
kisim: "6 — Sabitler"
baslik: "6.6 `constexpr` işlevler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
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

**Neden her işlev `constexpr` olamaz?** Derleyici, `constexpr` olmayan bir işlevin
gövdesine derleme zamanında bakmaz; yalnızca bildirimini görür. `constexpr` yazdığınızda
gövdeye bakmak zorunda kalır ve gövdenin derleme zamanında yürütülebilir olması gerekir.
Bu da neler yazabileceğinize sınır getirir: çalışma zamanına ait işler (dinamik bellek
ayırma, giriş-çıkış, `static` yerel nesneler) gövdede yer alamaz.

Bu sınırların C++11'den C++20'ye kadar nasıl gevşediği ve `consteval` ile `constinit`
anahtar sözcükleri: **Cilt II, Kısım 18.**
