---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.1 Şablon parametrelerinin üç biçimi"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++23)"
---

## 4.1 Şablon parametrelerinin üç biçimi

Cilt I Kısım 22.3 üç biçimi tanıtmış, ilk ikisini kullanmıştı.

**Tür parametreleri.**

<!-- kod: atla -->
```cpp
template<typename T>
```

**Tür olmayan parametreler.** Türleri bir **yapısal tür** *(structural type)* olmalıdır:
tamsayı, `enum`, kayan noktalı tür, gösterici, üye göstericisi ve `std::nullptr_t` gibi
skaler türler; sol taraf referansları; bütün taban sınıfları ve statik olmayan veri
elemanları `public` olan ve `mutable` olmayan, bunların türleri de yapısal tür ya da
yapısal türlerin (çok boyutlu olabilen) dizisi olan literal (Kısım 18.1) sınıf türleri.
C++17'den itibaren tür yerine `auto` gibi bir yer tutucu da yazılabilir. Kayan noktalı ve
sınıf türleri C++20 ile eklendi.

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

Üç biçimin her biri `...` ile bildirilirse bir parametre paketi olur; konusu Kısım 4.5.
