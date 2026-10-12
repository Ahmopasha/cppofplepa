---
cilt: "I — Temel"
kisim: "8 — Referanslar"
baslik: "8.9 Üçüncü referans türü"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 8.9 Üçüncü referans türü

Şimdiye kadar iki referans türü gördünüz: `T&` ve `T&&`. `T&&` biçimini Kısım 13'te,
taşıma semantiğiyle birlikte kullanacaksınız.

Bilmeniz gereken üçüncü bir tür daha vardır ve **yazılışı `T&&` ile birebir aynıdır.**
Şablon bağlamında yazıldığında bu biçim R-Value referansı değil, her şeye bağlanabilen
bir referans anlamına gelir:

```cpp
void f(Myclass&& x);        // R-Value referans

template<typename T>
void g(T&& x);              // aynı yazılış, farklı anlam
```

Şablon yazmaya başlayana kadar bu ayrım sizi ilgilendirmez. Ayrımın ne olduğu ve neden
böyle tasarlandığı: **Cilt II, Kısım 1.2.**
