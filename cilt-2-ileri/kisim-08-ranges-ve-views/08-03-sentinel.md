---
cilt: "II — İleri"
kisim: "8 — Ranges ve Views"
baslik: "8.3 Sentinel"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 8.3 Sentinel

Eski STL'de `begin()` ve `end()` **aynı türden** olmak zorundaydı. Ranges bu kısıtı
kaldırdı: bitişi belirten nesne farklı türden olabilir ve ona **sentinel** denir.

```cpp
template<typename Iter, typename Son>
requires std::input_iterator<Iter> && std::sentinel_for<Son, Iter>
void algoritma(Iter ilk, Son son);
```

Kazancı şudur. Sonlandırıcı karakterle biten bir C yazısında, bitiş konumu önceden
bilinmez; eski STL ile çalışmak için önce uzunluğu hesaplamak gerekirdi. Sentinel ile
bitiş koşulu bir **karşılaştırma** hâline gelir: "iteratörün gösterdiği karakter boş
karakter mi?"

`std::unreachable_sentinel`, hiçbir zaman eşit olmayan özel bir sentineldir. Sonsuz
aralıklar bununla kurulur; bitiş denetimi tamamen elenir ve derleyici döngüyü daha iyi
optimize eder.
