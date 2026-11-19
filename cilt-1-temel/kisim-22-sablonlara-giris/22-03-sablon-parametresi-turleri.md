---
cilt: "I — Temel"
kisim: "22 — Şablonlara Giriş"
baslik: "22.3 Şablon parametresi türleri"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 22.3 Şablon parametresi türleri

Şablon parametreleri üç biçimde bildirilir: **tür parametreleri** *(type parameters)*,
**tür olmayan parametreler** *(non-type template parameters)* ve
**şablon şablon parametreleri** *(template template parameters)*. Her biri `...` ile
bildirilirse bir **parametre paketi** *(parameter pack)* olur ve sıfır ya da daha fazla
argüman alır (Cilt II, Kısım 4.5). Cilt I'de ilk ikisiyle karşılaşırsınız.

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

`std::array` (Kısım 23) da bu parametre biçimiyle bildirilir; boyut tür bilgisinin
parçasıdır.

Şablon şablon parametreleri ve parametre paketleri: **Cilt II, Kısım 4.**
