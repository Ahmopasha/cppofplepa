---
cilt: "I — Temel"
kisim: "23 — STL"
baslik: "23.7 Algoritmalar"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 23.7 Algoritmalar

`<algorithm>` başlığındaki işlevler, iteratör çiftiyle belirtilen bir aralık üzerinde
çalışır.

```cpp
std::sort(v.begin(), v.end());
std::reverse(v.begin(), v.end());

auto it = std::find(v.begin(), v.end(), 42);
auto n  = std::count(v.begin(), v.end(), 42);

bool hepsi = std::all_of(v.begin(), v.end(), [](int x) { return x > 0; });
```

Çoğu algoritma, karşılaştırma veya koşul için bir **çağrılabilir** nesne alabilir; bu,
lambda ifadelerinin en sık kullanıldığı yerdir (bkz. Kısım 24).

```cpp
std::sort(v.begin(), v.end(), [](int a, int b) { return a > b; });
```

Sık kullanılan gruplar: arama (`find`, `find_if`, `search`), sayma (`count`, `count_if`),
dönüştürme (`transform`, `copy`, `replace`), sıralama (`sort`, `stable_sort`,
`partial_sort`), sıralı aralıkta arama (`binary_search`, `lower_bound`, `upper_bound`),
sayısal işlemler (`accumulate`, `iota` — `<numeric>` başlığında).

**Algoritmalar eleman silmez.** `std::remove`, silinmeyecek elemanları aralığın başına
doğru kaydırır ve yeni mantıksal sonu, yani korunan son elemandan sonraki konumu gösteren
iteratörü döndürür. Kabın boyutu değişmez; mantıksal sondan itibaren elemanların değerine
güvenilmez (gerekçesi: Cilt II, Kısım 2.5). Gerçek silmeyi kabın `erase` işlevi yapar:

```cpp
v.erase(std::remove(v.begin(), v.end(), 42), v.end());
```

Buna *remove-erase* deyimi denir. C++20 bunu tek çağrıya indirdi:

```cpp
std::erase(v, 42);     // C++20
```

`begin()` ve `end()` yazma zorunluluğunu tamamen ortadan kaldıran ranges kütüphanesi:
**Cilt II, Kısım 8.**
