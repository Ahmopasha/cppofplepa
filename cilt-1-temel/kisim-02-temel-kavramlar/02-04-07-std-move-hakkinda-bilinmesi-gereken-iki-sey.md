---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.4.7 `std::move` hakkında bilinmesi gereken iki şey"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

### 2.4.7 `std::move` hakkında bilinmesi gereken iki şey

**Birincisi: `std::move` taşıma yapmaz.** Yalnızca bir nesne ifadesini X-Value olarak
işaretler. Taşımayı yapan, o işaretlenmiş ifadeyi alan **taşıyan kurucu işlev**
*(move constructor)* veya **taşıyan atama işlevi** *(move assignment operator)* olur
(Kısım 13.7). İngilizcede bunu şöyle söylerler: *"move does not move."*

**İkincisi: kaynağı devralınmış nesneyi *(moved-from object)* kendi değeriyle
kullanmayın.**

```cpp
std::string str(10000, 'A');
auto s = std::move(str);

str.size();   // belirtilmemiş: 0 olması garanti değildir
```

Aksi belirtilmedikçe standart kütüphane türleri için verilen garanti şudur: kaynağı
devralınmış nesne **geçerli ama belirtilmemiş** *(valid but unspecified)* bir durumdadır
(Kısım 2.5; ayrıntısı Cilt II, Kısım 2.5). Yani nesneyi yok saymanız gerekmez; ona yeni
bir değer atayıp kullanmaya devam edebilirsiniz. Yapmamanız gereken, mevcut değerine
güvenmektir.

```cpp
auto s = std::move(str);
str = "yeni değer";   // bu geçerlidir
std::cout << str;     // artık okunabilir
```

Üçüncü parti kütüphaneler bu garantiyi vermek zorunda değildir; belgelerine bakın.
