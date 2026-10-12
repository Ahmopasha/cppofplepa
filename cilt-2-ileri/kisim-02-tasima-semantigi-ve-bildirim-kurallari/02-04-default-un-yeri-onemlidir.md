---
cilt: "II — İleri"
kisim: "2 — Taşıma Semantiği ve Bildirim Kuralları"
baslik: "2.4 `= default`'un yeri önemlidir"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 2.4 `= default`'un yeri önemlidir

`= default`'u sınıf tanımı içinde, işlevin **ilk bildiriminde** yazarsanız işlev
*user declared, defaulted* olur ve triviallik korunur. Sınıf dışında yazarsanız işlev
*user provided* sayılır ve trivialliğini kaybeder.

```cpp
class A { public: A() = default; };        // trivial kalır

class B { public: B(); };
B::B() = default;                           // trivial DEĞİL
```

Fark, `std::is_trivially_copyable` gibi özellik sorgularına ve dolayısıyla kütüphanelerin
seçtiği kod yollarına yansır. Görünürde aynı olan iki yazımın farklı sonuç vermesi,
şablon kodu yazarken karşınıza çıkar.
