---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.8 SFINAE"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 4.8 SFINAE

Şablon argüman yerleştirmesi sırasında geçersiz bir tür oluşursa, bu bir sentaks hatası
değildir; o aday yalnızca **listeden düşer.** İlkenin adı buradan gelir:
*substitution failure is not an error*.

```cpp
template<typename T>
typename T::deger_turu func(T t);      // T'nin deger_turu yoksa aday düşer

void func(int);                        // bu aday kalır

func(42);                              // ikincisi seçilir, hata verilmez
```

Kural yalnızca **doğrudan bağlamda** *(immediate context)* geçerlidir; yani imzada.
İşlevin gövdesinde oluşan hata gerçek bir hatadır.

SFINAE'yi bilinçli olarak kullanmanın standart aracı `std::enable_if`'tir:

```cpp
template<typename T,
         typename = std::enable_if_t<std::is_integral_v<T>>>
void func(T t);        // yalnızca tamsayı türleri için
```

Bu yazım C++20 öncesinin çözümüdür ve okunması zordur. C++20'nin kavramları aynı işi
çok daha açık biçimde yapar: **Kısım 7.**
