---
cilt: "II — İleri"
kisim: "14 — Deyimler ve Kalıplar"
baslik: "14.7 Karma işlevini özelleştirme"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 14.7 Karma işlevini özelleştirme

Kendi türünüzü `std::unordered_map` anahtarı yapmak için `std::hash` şablonunun o tür
için özelleştirilmesi gerekir (bkz. Cilt I Kısım 23.4).

```cpp
struct Nokta { int x, y; };

template<>
struct std::hash<Nokta> {
    std::size_t operator()(const Nokta& n) const noexcept
    {
        return std::hash<int>{}(n.x) ^ (std::hash<int>{}(n.y) << 1);
    }
};
```

Bu, standart kütüphane şablonlarının tam özelleştirilmesine izin verilen az sayıdaki
durumdan biridir; kendi türünüz için yapmanız şarttır.

İkinci gereklilik `operator==`'dır; sırasız kaplar çarpışma durumunda eşitliğe bakar.
Kısım 16.4'teki `= default` yazımı bunu tek satırda sağlar.
