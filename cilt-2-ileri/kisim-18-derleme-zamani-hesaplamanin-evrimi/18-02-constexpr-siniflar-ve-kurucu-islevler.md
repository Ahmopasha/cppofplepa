---
cilt: "II — İleri"
kisim: "18 — Derleme Zamanı Hesaplamanın Evrimi"
baslik: "18.2 `constexpr` sınıflar ve kurucu işlevler"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 18.2 `constexpr` sınıflar ve kurucu işlevler

Bir sınıf türünden nesnenin derleme zamanında oluşabilmesi için, onu oluşturan kurucu
işlevin gövdesi kullanıcı tarafından yazılmışsa bu işlev `constexpr` olmalıdır. Bileşik
türler (Cilt I, Kısım 3.10) ve örtülü tanımlanan kurucu işlevler bu şartı kendiliğinden
karşılayabilir.

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

`constexpr` sınıf diye ayrı bir kavram yoktur; ilgili kavram **literal tür**dür.
`constexpr` bir nesnenin türü literal tür olmalıdır. Bunun için başka şartların yanı sıra
sınıfın statik olmayan veri elemanları (`union` elemanları hariç) ve taban sınıfları da
`volatile` olmayan literal türden, sonlandırıcı işlevi de `constexpr` olmalıdır. Bu
sonlandırıcı şartı C++20'den itibaren geçerlidir; öncesinde sonlandırıcının trivial olması
gerekirdi. Artık sonlandırıcı işlev de `constexpr` olabilir; bu, derleme zamanında bellek
ayıran türlerin çalışabilmesinin ön koşuludur. Örtülü tanımlanan sonlandırıcı da şartı
kendiliğinden karşılayabilir. Kurucu ve sonlandırıcı dışındaki üye işlevlerin `constexpr`
olması literal tür şartını karşılamaz; onlar sabit ifadede çağrılabilmek için `constexpr`
yazılır.

Bir `constexpr` nesne aynı zamanda `const`'tur; `mutable` veri elemanları dışında
değiştirilemez.
