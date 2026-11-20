---
cilt: "I — Temel"
kisim: "23 — STL"
baslik: "23.2 İteratörler"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
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

| Kategori | Yapabildikleri | Örnek |
|---|---|---|
| **Girdi** *(input)* / **Çıktı** *(output)* | Tek yönde bir kez okuma (girdi) ya da yazma (çıktı) | akım iteratörleri (bkz. Cilt II, Kısım 4.12) |
| **İleri** *(forward)* | Tek yönde defalarca dolaşma | `std::forward_list` |
| **Çift yönlü** *(bidirectional)* | `--` ile geri gidebilme | `std::list`, `std::map`, `std::set` |
| **Rastgele erişimli** *(random access)* | `it + 5`, `it[3]`, sıra karşılaştırması (`it1 < it2`) | `std::deque` |
| **Bitişik** *(contiguous)* | Rastgele erişim; elemanlar bellekte art arda durur | `std::vector` (`bool` dışında; bkz. Kısım 23.3), `std::array`, `std::string` |

Bitişik iteratör aynı zamanda rastgele erişimli bir iteratördür. Bitişik iteratör tanımı
C++17'de geldi; C++20'den itibaren ayrı bir kategori olarak sayılır.

`std::sort` rastgele erişimli iteratör ister; bu yüzden `std::list` ile kullanılamaz,
`std::list` kendi `sort` üye işlevini sunar.

İteratör kategorilerinin şablon kodunda nasıl sorgulandığı (`iterator_traits`):
**Cilt II, Kısım 4.11.**
