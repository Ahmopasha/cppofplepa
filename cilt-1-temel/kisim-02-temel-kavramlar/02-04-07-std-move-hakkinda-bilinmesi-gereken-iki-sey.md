---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.4.7 `std::move` hakkında bilinmesi gereken iki şey"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

### 2.4.7 `std::move` hakkında bilinmesi gereken iki şey

**Birincisi: `std::move` taşıma yapmaz.** Yalnızca ifadeyi X-Value olarak işaretler.
Taşımayı yapan, o işaretlenmiş ifadeyi alan taşıyan kurucu işlev veya taşıyan atama
işlevidir. İngilizce'de bunu şöyle söylerler: *"move does not move."*

**İkincisi: kaynağı devralınmış nesneyi kendi değeriyle kullanmayın.**

```cpp
std::string str(10000, 'A');
auto s = std::move(str);

str.size();   // 0 döner — kaynağı devralındı
```

Standart kütüphane sınıfları için verilen garanti şudur: kaynağı devralınmış nesne
**geçerlidir ama değeri belirsizdir.** Yani nesneyi yok saymanız gerekmez; ona yeni
bir değer atayıp kullanmaya devam edebilirsiniz. Yapmamanız gereken, mevcut değerine
güvenerek okumaktır.

```cpp
auto s = std::move(str);
str = "yeni değer";   // bu geçerlidir
std::cout << str;     // artık okunabilir
```

Üçüncü parti kütüphaneler bu garantiyi vermek zorunda değildir; belgelerine bakın.
