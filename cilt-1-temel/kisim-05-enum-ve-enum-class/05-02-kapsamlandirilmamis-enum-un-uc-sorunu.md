---
cilt: "I — Temel"
kisim: "5 — `enum` ve `enum class`"
baslik: "5.2 Kapsamlandırılmamış `enum`'un üç sorunu"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 5.2 Kapsamlandırılmamış `enum`'un üç sorunu

**Birinci sorun: numaralandırma sabitlerinin ayrı bir kapsamı yoktur.** Sabitler, `enum`
türünün bildirildiği kapsama sızar.

```cpp
enum Renk  { Kirmizi, Yesil, Mavi };
enum Meyve { Elma, Armut, Kirmizi };   // sentaks hatası: Kirmizi zaten var
```

**İkinci sorun: tamsayı türlerine örtülü dönüşüm vardır.** Ters yön sentaks hatasıdır,
ama bu yön serbesttir ve anlamsız karşılaştırmalara izin verir.

```cpp
enum Renk  { Kirmizi, Yesil, Mavi };
enum Meyve { Elma, Armut };

if (Kirmizi == Elma) { }     // derlenir — ikisi de 0
int x = Yesil;               // derlenir
```

**Üçüncü sorun: temel tür üzerinde denetiminiz yoktur.** `enum` türünün hangi tamsayı
türüyle temsil edileceğine derleyici karar verir; bu da `sizeof` değerini ve ileri
bildirim yapabilme imkânını belirsizleştirir.

C dilinde temel tür `int` olmak zorundadır. C++'ta ise derleyici seçer.
