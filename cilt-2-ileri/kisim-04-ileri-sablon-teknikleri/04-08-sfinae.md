---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.8 SFINAE"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++23)"
---

## 4.8 SFINAE

Şablon argümanları yerleştirilirken geçersiz bir tür ya da ifade oluşursa sentaks hatası
olmaz; aday yalnızca **listeden düşer.** İlkenin adı buradan gelir: *substitution failure
is not an error*.

```cpp
template<typename T>
typename T::deger_turu func(T t);      // T'nin deger_turu yoksa aday düşer

void func(int);                        // bu aday kalır

func(42);                              // ikincisi seçilir, hata verilmez
```

Kural yalnızca **doğrudan bağlamda** *(immediate context)* geçerlidir. Yerleştirmenin
yapıldığı başlıca yerler işlevin `noexcept` belirteci dışındaki türü (geri dönüş ve
parametre türleri) ve şablon parametresi bildirimleridir; aşağıdaki `std::enable_if_t` bir
şablon parametresi bildirimindedir. Yerleştirmenin tetiklediği bir sınıf şablonu
örneklemesinin içi ve işlevin gövdesi doğrudan bağlamda değildir; buralarda oluşan hata
sentaks hatasıdır.

SFINAE'yi bilinçli olarak kullanmanın standart aracı `std::enable_if`'tir:

```cpp
template<typename T,
         typename = std::enable_if_t<std::is_integral_v<T>>>
void func(T t);        // yalnızca tamsayı türleri için
```

Bu yazım C++20 öncesinin çözümüdür ve okunması zordur. C++20'nin kavramları aynı işi
çok daha açık biçimde yapar: **Kısım 7.**
