---
cilt: "I — Temel"
kisim: "22 — Şablonlara Giriş"
baslik: "22.3 Şablon parametresi türleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 22.3 Şablon parametresi türleri

Şablon parametreleri dört gruba ayrılır. Cilt I'de ikisiyle karşılaşırsınız.

**Tür parametreleri** — şimdiye kadarki bütün örnekler.

<!-- kod: atla -->
```cpp
template<typename T>
```

**Tür olmayan parametreler** — derleme zamanında bilinen bir değer.

```cpp
template<typename T, std::size_t N>
class Dizi {
    T veri[N];
};

Dizi<int, 10> d;
```

`std::array` bu şekilde tanımlanmıştır; boyut tür bilgisinin parçasıdır.

Kalan iki grup (şablon şablon parametreleri ve şablon parametre paketleri):
**Cilt II, Kısım 4.**
