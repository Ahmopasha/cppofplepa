---
cilt: "I — Temel"
kisim: "22 — Şablonlara Giriş"
baslik: "22.4 Sınıf şablonları"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 22.4 Sınıf şablonları

Sınıflar da şablonlaştırılabilir. Standart kütüphanenin kapları böyle tanımlanmıştır.

```cpp
template<typename T>
class Kutu {
    T icerik;
public:
    Kutu(const T& i) : icerik{i} { }
    const T& al() const { return icerik; }
};

Kutu<int> k1{42};
Kutu<std::string> k2{"merhaba"};
```

C++17'den itibaren, kurucu işlev argümanlarından çıkarım yapılabilir:

```cpp
Kutu k3{42};      // Kutu<int> — C++17
```

Bu mekanizmanın adı CTAD'dir ve sınırları vardır: **Cilt II, Kısım 4.**
