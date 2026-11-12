---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.3 Kopyalayan kurucu işlev ne zaman çağrılır"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 13.3 Kopyalayan kurucu işlev ne zaman çağrılır

Kopyalayan kurucu işlev, yeni bir nesneye aynı türden bir L-Value'dan ilk değer verilirken
çağrılır. Tipik üç yer:

```cpp
void func(Myclass m);            // 1. değerle geçirilen parametre: func(a) çağrısında
Myclass glob;
Myclass bar() { return glob; }   // 2. yerel olmayan bir nesneyi değerle döndürmek

Myclass a;
Myclass b = a;                   // 3. aynı türden nesneden ilk değer alma
Myclass c{a};                    // aynı şey
```

Bu örnekte üçüncü maddedeki iki yazım da kopyalayan kurucu işlevi çağırır; aralarında
davranış farkı yoktur. İlk değer veren ifade (argüman ya da döndürülen ifade de) aynı
türden bir PR-Value ise ne kopyalayan ne de taşıyan kurucu işlev çağrılır; nesne doğrudan
o ifadeden ilk değer alır (Kısım 12.17); işlev gövdesinde tanımlanmış, dönüş türüyle aynı
türden yerel (`static` olmayan) bir nesne döndürülürken de kopyalama elenebilir (kopyalama
eliminasyonu, Cilt II, Kısım 3.1) ya da yerine taşıma denenir; değerle alınmış bir
parametre döndürülürken eleme olmaz ama yine önce taşıma denenir (Kısım 13.12).
