---
cilt: "II — İleri"
kisim: "18 — Derleme Zamanı Hesaplamanın Evrimi"
baslik: "18.3 `consteval`"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
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

Bu tür işlevlere **ivedi işlev** *(immediate function)* denir. Değerlendirilmeyen
işlenenler (ör. `sizeof` ve `decltype` işlenenleri) dışında, böyle bir işlevin **ivedi
işlev bağlamı** *(immediate function context)* dışındaki çağrısı derleme zamanında bir
sabite dönüşmek zorundadır; aksi hâlde sentaks hatası olur. Örneğin bir ivedi işlevin
gövdesi bu bağlamdadır; oradaki çağrı sabit ifade olmak zorunda değildir: parametresi `x`
olan `consteval` bir işlevin gövdesinde `kare(x)` geçerlidir. Ayrıca örneğin `constexpr`
bir şablondan örneklenen işlevde ya da bir lambdanın çağrı işlecinde, sabit ifade olmayan
böyle bir çağrı sentaks hatası değildir; çağrıyı içeren işlev ivedi işleve dönüşür
(C++20'ye de uygulanan bir kusur raporu).

Kullanım alanı, çalışma zamanında çalışmasını **istemediğiniz** hesaplamalardır.
Örneğin bir yapılandırma değerinin derleme zamanında doğrulanması: `constexpr`
yazsaydınız, birileri onu çalışma zamanında çağırabilir ve maliyeti fark etmezdiniz.
