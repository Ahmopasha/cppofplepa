---
cilt: "I — Temel"
kisim: "19 — Çalışma Zamanı Tür Bilgisi"
baslik: "19.4 Ne zaman kullanmamalı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 19.4 Ne zaman kullanmamalı

RTTI kullanma ihtiyacı, çoğu zaman tasarımın sanal işlevlerle çözülmesi gereken bir yerde
çözülmediğinin işaretidir.

<!-- kod-baglam
struct Kare : Sekil { };
void daire_ciz(Sekil*);
void kare_ciz(Sekil*);
Sekil* s = nullptr;
-->
```cpp
// Kaçınılması gereken
if (typeid(*s) == typeid(Daire))       daire_ciz(s);
else if (typeid(*s) == typeid(Kare))   kare_ciz(s);
```

Bu koda her yeni şekil türü eklendiğinde dokunmanız gerekir. Sanal bir `ciz()` işlevi
aynı işi yapar ve yeni türler eklendiğinde değişmez (bkz. Kısım 17.6).

RTTI'nin meşru kullanımı, hiyerarşinin dışından gelen ve genişletilemeyen durumlardır:
serileştirme, hata ayıklama araçları, eski kodla köprü kurma.

Maliyeti de vardır: `dynamic_cast` çalışma zamanında hiyerarşide arama yapar ve sanal
çağrıdan pahalıdır.
