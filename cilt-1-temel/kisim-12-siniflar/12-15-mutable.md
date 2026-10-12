---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.15 `mutable`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 12.15 `mutable`

`const` üye işlevlerin bile değiştirebileceği bir veri elemanı tanımlamak için kullanılır.

```cpp
class Myclass {
    mutable int erisim_sayisi{};
    int x;
public:
    int get() const
    {
        ++erisim_sayisi;      // const üye işlevde değiştirilebiliyor
        return x;
    }
};
```

Meşru kullanımı, nesnenin **problem alanındaki değerine dahil olmayan** öğelerdir:
önbellek, erişim sayacı, kilit. Veri elemanının kendisi için kullanmak, `const`luğun
anlamını boşa çıkarır.
