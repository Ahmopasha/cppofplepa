---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.11 Kendi iteratörünüzü yazmak"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 4.11 Kendi iteratörünüzü yazmak

Cilt I Kısım 23.2'de iteratör kategorileri tanıtılmıştı. Algoritmaların bu kategoriyi
sorgulayabilmesi için, her iteratörün beş tür bilgisi sunması gerekir.

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
sınıf değildir; içine `value_type` yazamazsınız. `iterator_traits`, göstericiler için
kısmi özelleştirilmiştir ve bu bilgileri onlar adına sunar.

<!-- kod: atla -->
```cpp
template<typename T>
struct iterator_traits<T*> {           // temsili
    using iterator_category = std::random_access_iterator_tag;
    using value_type        = T;
    // ...
};
```

Bu, 4.4'teki kısmi özelleştirmenin standart kütüphanedeki en öğretici uygulamasıdır.
