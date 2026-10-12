---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.10 Eş isim ve değişken şablonları"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 4.10 Eş isim ve değişken şablonları

**Eş isim şablonu** *(alias template)*, tür eş ismini şablonlaştırır. `typedef` bunu
yapamaz; Cilt I Kısım 16.1'de `using`'in üstünlüğü olarak belirtilmişti.

```cpp
template<typename T>
using Sozluk = std::map<std::string, T>;

Sozluk<int> yas;
```

**Değişken şablonu** *(variable template)*, değişkeni şablonlaştırır.

```cpp
template<typename T>
constexpr T pi = T(3.1415926535897932385);

pi<float>;
pi<double>;
```

`type_traits` kütüphanesindeki `_v` ekli isimler bu mekanizmayla tanımlanmıştır:
`std::is_integral_v<T>`, `std::is_integral<T>::value`'nun kısaltmasıdır.
