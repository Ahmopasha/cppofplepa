---
cilt: "II — İleri"
kisim: "8 — Ranges ve Views"
baslik: "8.1 STL'in ikinci sürümü"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 8.1 STL'in ikinci sürümü

Cilt I Kısım 23.7'de bütün algoritmaların iteratör çiftiyle çağrıldığını görmüştük:

```cpp
std::sort(v.begin(), v.end());
```

Bu yazımın üç sorunu vardır.

**Tekrar.** Neredeyse her çağrıda `v.begin(), v.end()` yazılır. Kabın tamamı üzerinde
çalışmak istisna değil, kuraldır.

**Güvenlik.** İki ayrı kaptan iteratör geçirmek sentaks hatası değildir; tanımsız
davranıştır.

```cpp
std::sort(v1.begin(), v2.end());     // derlenir, çöker
```

**Birleştirilememe.** İki algoritmayı ardışık uygulamak için ara kap gerekir; her adımda
kopyalama ve bellek ayırma olur.

C++20'nin **ranges** kütüphanesi üçünü birden çözer. Standart kütüphanenin eski
algoritmaları yerinde durur; ranges sürümleri `std::ranges` isim alanında paralel olarak
bulunur.

```cpp
#include <ranges>
#include <algorithm>

std::ranges::sort(v);        // kabın kendisi yeterli
```
