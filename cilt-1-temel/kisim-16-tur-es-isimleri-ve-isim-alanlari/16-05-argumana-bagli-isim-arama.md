---
cilt: "I — Temel"
kisim: "16 — Tür Eş İsimleri ve İsim Alanları"
baslik: "16.5 Argümana bağlı isim arama"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 16.5 Argümana bağlı isim arama

Aşağıdaki kod niçin derlenir?

```cpp
std::string s1, s2;
auto s3 = s1 + s2;              // operator+ nerede?

std::vector<int> v;
sort(v.begin(), v.end());       // std:: yazmadık
```

`operator+` ve `sort`, `std` isim alanının içindedir ama nitelenmeden çağrılmışlardır.
Çalışmalarının sebebi **argümana bağlı isim arama** *(argument dependent lookup, ADL)*
mekanizmasıdır.

Kural şudur: nitelenmemiş bir işlev çağrısında, isim yalnızca normal kapsamlarda değil,
**argümanların türlerinin ait olduğu isim alanlarında da** aranır.

`v.begin()` bir `std::vector<int>::iterator` döndürdüğü için, `sort` ismi `std` isim
alanında da aranır ve bulunur.

ADL'in varlık sebebi, operatör yüklemelerinin nitelenerek çağrılamamasıdır. `a + b`
yazarken `std::operator+(a, b)` yazmak zorunda kalsaydınız operatör yüklemesi işe
yaramazdı.

İki ek nokta. Sınıf içinde `friend` olarak bildirilen işlevlerin isimleri de ADL yoluyla
bulunur; bu, operatör işlevlerini sınıf içinde tanımlamanın yaygın bir gerekçesidir
(bkz. Kısım 12.16 ve 14). Ve ADL, işlev yüklemesinin aday listesini genişletir; Kısım
9.3'teki birinci aşamanın bir parçasıdır.

ADL'in ayrıntıları ve şablonlarla etkileşimi: **Cilt II, Kısım 4.**
