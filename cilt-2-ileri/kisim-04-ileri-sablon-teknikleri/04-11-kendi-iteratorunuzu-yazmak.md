---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.11 Kendi iteratörünüzü yazmak"
kaynak: "ders notları"
kutular: ["Standart Notu — C++20"]
son_kontrol: "2026-11 (C++23)"
---

## 4.11 Kendi iteratörünüzü yazmak

Algoritmalar iteratörün kategorisini (Cilt I Kısım 23.2) ve öteki tür bilgilerini
sorgular; bunları sunmanın en açık yolu üye tür bildirimleridir:

```cpp
class Iteratorum {
public:
    using iterator_category = std::forward_iterator_tag;
    using value_type        = int;
    using difference_type   = std::ptrdiff_t;
    using pointer           = int*;
    using reference         = int&;
};
```

Algoritmalar bu bilgilere doğrudan değil, `std::iterator_traits` üzerinden erişir:

```cpp
template<typename Iter>
void algoritma(Iter ilk, Iter son)
{
    using kategori = typename std::iterator_traits<Iter>::iterator_category;
    using deger    = typename std::iterator_traits<Iter>::value_type;
}
```

Aradaki katmanın sebebi, **çıplak göstericilerin de iteratör sayılmasıdır.** `int*` bir
sınıf değildir; içine `value_type` yazamazsınız. `std::iterator_traits`, göstericiler için
kısmi özelleştirilmiştir ve bu bilgileri onlar adına sunar.

<!-- kod: atla -->
```cpp
template<typename T>
struct iterator_traits<T*> {           // temsili
    using iterator_category = std::random_access_iterator_tag;
    using value_type        = std::remove_cv_t<T>;
    // ...
};
```

Bu, Kısım 4.4'teki kısmi özelleştirmenin standart kütüphanedeki en öğretici uygulamasıdır.

> **Standart Notu — C++20**
> **C++20 öncesi:** C++17'de beş üye türden biri bile eksikse
> `std::iterator_traits<I>`'nin hiç üyesi olmazdı.
> **C++20 ile:** Öteki dört üye tür varsa `pointer` yazılmayabilir; `void` sayılır. Biri
> eksikse ve sınıf giriş iteratörü koşullarını sağlıyorsa eksik türler (kategori dahil)
> işlemlerden hesaplanır; ama `value_type` üye olarak verilir, `difference_type` ise üye
> yoksa `-` işleminden çıkarılır. Bu koşulu sağlamayan ama kopyalanabilir olup `*i`,
> `I&` döndüren `++i` ve `*i++` işlemlerini sunan sınıfta kategori
> `std::output_iterator_tag`, `value_type` `void` olur; bunlar da sağlanmıyorsa üye
> olmaz.
