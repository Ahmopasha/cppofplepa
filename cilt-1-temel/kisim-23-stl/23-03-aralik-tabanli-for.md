---
cilt: "I — Temel"
kisim: "23 — STL"
baslik: "23.3 Aralık tabanlı `for`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 23.3 Aralık tabanlı `for`

Dolaşmanın kısa yazımıdır ve arka planda `begin()` / `end()` kullanır.

```cpp
for (const auto& eleman : v)
    std::cout << eleman;
```

Üç yazım arasındaki seçim şöyledir:

```cpp
for (auto  x : v)      // kopya alır — küçük türler için uygun
for (auto& x : v)      // değiştirmek için
for (const auto& x : v)  // okumak için, kopyasız
```

> **Değiştirmek istiyorsanız `auto&&` kullanın.** Bazı kapların iteratörleri gerçek bir
> elemana değil, geçici bir **vekil nesneye** *(proxy)* erişir; `std::vector<bool>` bunun
> en bilinen örneğidir. Vekil nesne geçici olduğu için `auto&` ona bağlanamaz ve kod
> derlenmez. `auto&&` her iki durumda da çalışır.

```cpp
for (auto&& x : v)     // her kapla çalışır
    x = 0;
```

`auto&&`'ın neden böyle davrandığı: **Cilt II, Kısım 1.2.**
