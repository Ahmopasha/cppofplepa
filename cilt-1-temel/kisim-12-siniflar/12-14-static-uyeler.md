---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.14 `static` üyeler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
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

Sınıf tanımı içinde ilk değer veremezsiniz; istisnası `const` ve tamsayı türünden
olanlardır. C++17'den itibaren `inline` yazarak sınıf içinde tanımlayabilirsiniz.

**`static` üye işlevler** gizli `this` parametresi almaz. Sonuçları:

- `const` üye işlev yapılamazlar (`const`luk `this`'in özelliğidir)
- Gövdelerinde `static` olmayan veri elemanlarına erişemezler
- Gövdelerinde `static` olmayan üye işlev çağıramazlar
- `static` veri elemanlarına ve `private` bölüme erişebilirler, çünkü sınıf kapsamındadırlar

Nesne üzerinden de çağrılabilirler, ama doğru yazım `Myclass::yardimci()` biçimidir.

Aynı parametre yapısına sahip `static` ve `static` olmayan iki üye işlev bir arada
bildirilemez.
