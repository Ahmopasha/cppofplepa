---
cilt: "II — İleri"
kisim: "18 — Derleme Zamanı Hesaplamanın Evrimi"
baslik: "18.2 `constexpr` sınıflar ve kurucu işlevler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 18.2 `constexpr` sınıflar ve kurucu işlevler

Bir sınıf türünden nesnenin derleme zamanında oluşabilmesi için kurucu işlevinin
`constexpr` olması gerekir.

```cpp
class Nokta {
    int x, y;
public:
    constexpr Nokta(int a, int b) : x{a}, y{b} { }
    constexpr int getX() const { return x; }
};

constexpr Nokta n{3, 5};
static_assert(n.getX() == 3);
```

`constexpr` sınıf diye ayrı bir kavram yoktur; sınıfın üye işlevlerinin `constexpr`
olması yeterlidir. C++20'den itibaren sonlandırıcı işlev de `constexpr` olabilir; bu,
derleme zamanında bellek ayıran türlerin çalışabilmesinin ön koşuludur.

Bir `constexpr` nesne aynı zamanda `const`'tur; değiştirilemez.
