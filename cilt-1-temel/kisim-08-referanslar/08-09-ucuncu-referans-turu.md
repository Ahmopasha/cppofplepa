---
cilt: "I — Temel"
kisim: "8 — Referanslar"
baslik: "8.9 Şablonlarda `T&&`"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 8.9 Şablonlarda `T&&`

Şimdiye kadar iki referans türü gördünüz: `T&` ve `T&&`. `T&&` biçimini Kısım 13'te,
taşıma semantiğiyle birlikte kullanacaksınız.

Dilde başka bir referans türü yoktur, ama `T&&` yazılışının işlev şablonlarında
(şablonlar: Kısım 22) özel bir kullanımı vardır. Bildirimde yazılan `T&&` biçim olarak
R-Value referanstır; ancak `T` çağrıdan çıkarılıyorsa, yani `T` çağrıda açıkça yazılmayıp
argümanın türünden belirleniyorsa, L-Value argümanla yapılan çağrıda parametre L-Value
referans olur:

```cpp
void f(Myclass&& x);        // R-Value referans; yalnızca R-Value'ya bağlanır

template<typename T>
void g(T&& x);              // T çağrıdan çıkarılırsa L-Value da alır
```

Bu kullanıma **forwarding reference** denir. Şablon yazmaya başlayana kadar bu ayrım sizi
ilgilendirmez. Kuralın ayrıntısı ve neden böyle tasarlandığı: **Cilt II, Kısım 1.2.**
