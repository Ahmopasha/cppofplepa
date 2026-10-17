---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.1 Şablon parametrelerinin dört grubu"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 4.1 Şablon parametrelerinin dört grubu

Cilt I'de ikisi tanıtılmıştı. Tamamı şöyledir:

**Tür parametreleri.**

<!-- kod: atla -->
```cpp
template<typename T>
```

**Tür olmayan parametreler.** Derleme zamanında bilinen bir değer taşırlar. Tamsayı
türleri, `enum` türleri, gösterici ve referanslar kullanılabilir; C++20'den itibaren
kayan noktalı türler ve sade sınıf türleri de eklendi.

```cpp
template<typename T, std::size_t N>
class Dizi { T veri[N]; };
```

**Şablon şablon parametreleri.** Parametrenin kendisi bir şablondur.

```cpp
template<typename T, template<typename, typename> class Kap>
class Sarmalayici {
    Kap<T, std::allocator<T>> veri;
};

Sarmalayici<int, std::vector> s;
```

Kullanım alanı dardır; kap türünün kendisini parametre yapmak istediğinizde gerekir.
Çoğu durumda `typename Kap` yazıp `Kap<T>` beklemek daha esnektir.

**Parametre paketleri.** 4.5'in konusu.
