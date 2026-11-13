---
cilt: "I — Temel"
kisim: "16 — Tür Eş İsimleri ve İsim Alanları"
baslik: "16.5 Argümana bağlı isim arama"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 16.5 Argümana bağlı isim arama

Aşağıdaki kod niçin derlenir?

```cpp
std::string s1, s2;
auto s3 = s1 + s2;              // operator+ nerede?
getline(std::cin, s1);          // std:: yazmadık
```

`std::operator+` ve `std::getline`, `std` isim alanının içindedir ama nitelenmeden
kullanılmışlardır. Çalışmalarının sebebi **argümana bağlı isim arama**
*(argument-dependent name lookup, ADL)* mekanizmasıdır.

Kural şudur: nitelenmemiş bir işlev çağrısında ve operatör ifadelerinde, isim yalnızca
normal kapsamlarda değil, **argümanların türlerinin ait olduğu isim alanlarında da**
aranır.

`std::cin`'in türü `std::istream` olduğu için `getline` ismi `std` isim alanında da aranır
ve bulunur. Argüman yerleşik bir türdense ya da yerleşik türden bir göstericiyse, ADL'in
bakacağı bir isim alanı yoktur. Bu yüzden `std::vector<int> v;` için
`sort(v.begin(), v.end())` yazımının derlenmesi garanti değildir (`v.begin()` ve
`v.end()`, öğelerin konumunu gösteren, göstericiye benzer nesneler, yani iteratör
döndürür; `std::sort` bu aralığı sıralar; bkz. Kısım 23.2 ve 23.7): `std::vector`'ün
iteratör türü gerçeklemeye bağlıdır ve `int*` olabilir. `std::sort` yazın.

ADL olmasaydı, başka bir isim alanında bildirilmiş bir operatör işlevini `a + b` biçiminde
kullanmak için önce bir `using` bildirimi ya da direktifi gerekirdi; yoksa her seferinde
`std::operator+(a, b)` gibi bir işlev çağrısı yazardınız, çünkü operatör ifadesine isim
alanı yazılamaz. ADL, operatörlerin nitelenmeden yazılabilmesini sağlar (bkz. Kısım 14.4).

İki ek nokta. Sınıf içinde `friend` olarak bildirilen işlevlerin isimleri de,
argümanlardan biri o sınıf türündeyse, ADL yoluyla bulunur; operatör işlevlerini sınıf
içinde `friend` olarak tanımlamak bu sayede mümkündür (bkz. Kısım 12.16 ve 14.4). Ve ADL,
işlev yüklemesinin aday listesini genişletir; Kısım 9.3'teki birinci aşamanın bir
parçasıdır.

ADL'i şablonlarla birlikte kullanan bir deyim: **Cilt II, Kısım 14.4.**
