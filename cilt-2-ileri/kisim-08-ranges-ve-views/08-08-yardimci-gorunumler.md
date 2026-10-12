---
cilt: "II — İleri"
kisim: "8 — Ranges ve Views"
baslik: "8.8 Yardımcı görünümler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 8.8 Yardımcı görünümler

**`views::all`**, bir aralığı görünüme çevirir. Boru hattının başında örtülü olarak
uygulanır.

**`views::counted`**, bir iteratör ve sayı alıp aralık üretir; C'den gelen
`(gösterici, uzunluk)` ikilisini ranges dünyasına taşır.

**`std::ranges::subrange`**, bir aralığın içindeki başka bir aralıktır. İteratör çiftini
tek nesnede paketler; eski STL arayüzlerinden ranges'e köprü kurar.

**`views::common`**, `begin()` ve `end()` türleri farklı olan bir aralığı, ikisi aynı
olan bir aralığa çevirir. Sentinel kullanan bir görünümü eski STL algoritmalarına
geçirmek için gerekir:

```cpp
auto g = v | std::views::take(3);
std::sort(g.begin(), g.end());                    // türler uyuşmayabilir
auto c = g | std::views::common;
std::sort(c.begin(), c.end());                    // artık uyuşur
```
