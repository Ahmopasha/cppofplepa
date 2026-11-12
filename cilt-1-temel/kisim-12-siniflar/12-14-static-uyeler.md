---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.14 `static` üyeler"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 12.14 `static` üyeler

**`static` veri elemanları** sınıfın tamamına aittir, nesnelere değil. Bütün nesneler
aynı değişkeni paylaşır.

```cpp
class Myclass {
public:
    static int sayac;       // bildirim
};

int Myclass::sayac = 0;     // tanım — kaynak dosyada
```

Sınıf tanımı içinde ilk değer veremezsiniz; istisnası `const` tamsayı ya da numaralandırma
türünden olanlar (ilk değer sabit bir ifade olmalıdır) ile `constexpr` `static` veri
elemanlarıdır. C++17'den itibaren `inline` yazarak sınıf içinde tanımlayabilir ve ilk
değer verebilirsiniz; `constexpr` `static` veri elemanları da örtülü olarak `inline`'dır
(Kısım 11.4).

**`static` üye işlevlerin** `this` göstericisi yoktur (Kısım 12.6). Sonuçları:

- `const` üye işlev yapılamazlar (`const`luk `this`'in özelliğidir)
- Bir nesne belirtmeden `static` olmayan veri elemanlarına erişemezler
- Bir nesne belirtmeden `static` olmayan üye işlev çağıramazlar
- `static` veri elemanlarına ve `private` bölüme erişebilirler, çünkü sınıfın üyesidirler

Nesne üzerinden de çağrılabilirler, ama doğru yazım `Myclass::yardimci()` biçimidir.

Aynı parametre yapısına sahip `static` ve `static` olmayan iki üye işlev bir arada
bildirilemez.
