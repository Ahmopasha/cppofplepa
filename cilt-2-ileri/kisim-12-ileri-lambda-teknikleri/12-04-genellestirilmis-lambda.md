---
cilt: "II — İleri"
kisim: "12 — İleri Lambda Teknikleri"
baslik: "12.4 Genelleştirilmiş lambda"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 12.4 Genelleştirilmiş lambda

C++14, parametre türü olarak `auto` yazmayı mümkün kıldı.

```cpp
auto topla = [](auto a, auto b) { return a + b; };

topla(1, 2);
topla(1.5, 2.5);
topla(std::string{"a"}, std::string{"b"});
```

Bu, `operator()` işlevini bir **şablon** hâline getirir; kapanış türü tek, çağrı
operatörü şablondur.

En sık kullanıldığı yer `std::visit` ziyaretçileridir (bkz. Kısım 11.5):

<!-- kod-baglam
std::variant<int, double> v;
-->
```cpp
std::visit([](const auto& d) { std::cout << d; }, v);
```

Mükemmel gönderim yapmak isterseniz `auto&&` ve `std::forward<decltype(x)>(x)`
yazımı kullanılır (bkz. Kısım 1.2.7):

```cpp
auto ilet = [](auto&&... args) { hedef(std::forward<decltype(args)>(args)...); };
```

C++20, şablon parametre listesini açıkça yazmayı da mümkün kıldı:

```cpp
auto f = []<typename T>(const std::vector<T>& v) { return v.size(); };
```

Bu yazım, `auto` ile ulaşılamayan tür bilgisine erişim sağlar.
