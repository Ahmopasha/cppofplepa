---
cilt: "II — İleri"
kisim: "8 — Ranges ve Views"
baslik: "8.8 Yardımcı görünümler"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++23)"
---

## 8.8 Yardımcı görünümler

**`views::all`**, bir aralığı görünüme çevirir. Boru hattının başında örtülü olarak
uygulanır.

**`views::counted`**, bir iteratör ve sayı alıp aralık üretir; C'den gelen
`(gösterici, uzunluk)` ikilisini ranges dünyasına taşır.

**`std::ranges::subrange`**, bir aralığın içindeki başka bir aralıktır. Bir iteratörü ve
bir sentineli tek nesnede paketler; eski STL arayüzlerinden ranges'e köprü kurar.

**`views::common`**, `begin()` ve `end()` türleri farklı olan bir aralığı, ikisi aynı
olan bir aralığa çevirir. Sentinel kullanan bir görünümü eski STL algoritmalarına
geçirmek için gerekir:

```cpp
auto g = std::views::iota(0) | std::views::take(3);
int t1 = std::accumulate(g.begin(), g.end(), 0);  // sentaks hatası — türler farklı
auto c = g | std::views::common;
int t2 = std::accumulate(c.begin(), c.end(), 0);  // artık uyuşur
```
