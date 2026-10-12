---
cilt: "II — İleri"
kisim: "18 — Derleme Zamanı Hesaplamanın Evrimi"
baslik: "18.3 `consteval`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 18.3 `consteval`

`constexpr` bir imkân bildirir; `consteval` bir **zorunluluk** bildirir. Böyle bir işlev
yalnızca derleme zamanında çağrılabilir.

```cpp
consteval int kare(int x) { return x * x; }

constexpr int a = kare(5);     // geçerli

int oku();
int b = kare(oku());           // sentaks hatası — argüman sabit ifade değil
```

Bu tür işlevlere **ivedi işlev** *(immediate function)* denir. Her çağrısı, derleme
zamanında bir sabite dönüşmek zorundadır; aksi hâlde kod derlenmez.

Kullanım alanı, çalışma zamanında çalışmasını **istemediğiniz** hesaplamalardır.
Örneğin bir yapılandırma değerinin derleme zamanında doğrulanması: `constexpr`
yazsaydınız, birileri onu çalışma zamanında çağırabilir ve maliyeti fark etmezdiniz.
