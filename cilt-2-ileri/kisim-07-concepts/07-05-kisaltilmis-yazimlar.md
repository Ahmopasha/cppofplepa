---
cilt: "II — İleri"
kisim: "7 — Concepts"
baslik: "7.5 Kısaltılmış yazımlar"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 7.5 Kısaltılmış yazımlar

Aynı kısıt dört ayrı biçimde yazılabilir. Hepsi eşdeğerdir.

```cpp
// 1 — requires cümlesi
template<typename T>
requires std::integral<T>
void f1(T t);

// 2 — şablon parametre listesinde
template<std::integral T>
void f2(T t);

// 3 — kısaltılmış şablon sözdizimi (C++20)
void f3(std::integral auto t);

// 4 — kısıtsız auto parametresi
void f4(auto t);
```

Üçüncü biçim, Cilt II Kısım 1.2.1'de değinilen `auto` parametreli işlevlerin kısıtlı
hâlidir. En kısa ve en okunaklı olanıdır; birden fazla parametreye **aynı** türü
dayatmanız gerekmiyorsa tercih edin.

Dikkat edilecek nokta: `void f(std::integral auto a, std::integral auto b)` yazımında
`a` ile `b` **farklı türlerden** olabilir. Aynı tür gerekiyorsa ikinci biçimi kullanın.
