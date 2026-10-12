---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.13 Demeti argüman listesine açmak"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 4.13 Demeti argüman listesine açmak

Elinizde bir `std::tuple` varsa ve onu bir işlevin argüman listesine dönüştürmek
istiyorsanız, paket açma sözdizimi işe yaramaz; demet bir paket değildir.

`std::apply`, demetin öğelerini ayrı argümanlar olarak çağrıya geçirir.

```cpp
#include <tuple>

int topla(int a, int b, int c) { return a + b + c; }

std::tuple<int, int, int> t{1, 2, 3};
std::apply(topla, t);                 // topla(1, 2, 3)
```

Genelleştirilmiş lambda ile birlikte, demetin üzerinde dolaşmanın yaygın yolunu verir
(bkz. Kısım 12.4):

```cpp
std::apply([](const auto&... ogeler) {
    ((std::cout << ogeler << ' '), ...);       // katlama ifadesi, 4.6
}, t);
```

Yakın akrabası `std::invoke`'tur. O, bir çağrılabilir nesneyi **tek tip** biçimde
çağırmaya yarar; sıradan işlevler, üye işlev göstericileri ve veri elemanı göstericileri
farklı sözdizimleri gerektirir, `std::invoke` bu farkı gizler.

```cpp
struct S { int x; void f(); };
S s;

std::invoke(&S::f, s);       // s.f()
std::invoke(&S::x, s);       // s.x
```

Şablon kodunda, elinizdeki çağrılabilirin hangi türden olduğunu bilmediğinizde `invoke`
kullanılır. `std::apply` da zaten arka planda onu çağırır.
