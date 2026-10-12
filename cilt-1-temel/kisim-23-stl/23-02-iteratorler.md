---
cilt: "I — Temel"
kisim: "23 — STL"
baslik: "23.2 İteratörler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 23.2 İteratörler

İteratör, bir kaptaki konumu temsil eden nesnedir. Göstericiye benzer davranır: `*` ile
eleman okunur, `++` ile ilerlenir.

Her kap iki temel iteratör verir:

```cpp
std::vector<int> v{1, 2, 3};

auto ilk  = v.begin();     // ilk elemanı gösterir
auto son  = v.end();       // SON ELEMANDAN SONRAKİ konumu gösterir
```

`end()` geçerli bir elemanı göstermez; bitiş işaretidir. `*v.end()` yazmak tanımsız
davranıştır.

```cpp
for (auto it = v.begin(); it != v.end(); ++it)
    std::cout << *it;
```

İteratörler yeteneklerine göre kategorilere ayrılır ve algoritmalar hangi kategoriyi
gerektirdiğini belirtir.

| Kategori | Yapabildikleri | Örnek kap |
|---|---|---|
| Girdi / Çıktı | Tek yönde bir kez dolaşma | akım iteratörleri |
| İleri | Tek yönde defalarca dolaşma | `forward_list` |
| Çift yönlü | `--` ile geri gidebilme | `list`, `map`, `set` |
| Rastgele erişimli | `it + 5`, `it[3]`, karşılaştırma | `vector`, `deque`, `array` |

`std::sort` rastgele erişimli iteratör ister; bu yüzden `std::list` ile kullanılamaz,
`list` kendi `sort` üye işlevini sunar.

İteratör kategorilerinin şablon kodunda nasıl sorgulandığı (`iterator_traits`):
**Cilt II, Kısım 4.**
