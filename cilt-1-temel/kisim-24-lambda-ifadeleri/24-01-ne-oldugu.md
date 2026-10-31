---
cilt: "I — Temel"
kisim: "24 — Lambda İfadeleri"
baslik: "24.1 Ne olduğu"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 24.1 Ne olduğu

Lambda ifadesi, derleyiciye **isimsiz bir sınıf yazdırır** ve o sınıf türünden bir nesne
üretir. Yazdırılan sınıfın `operator()` işlevi, lambdanın gövdesidir.

```cpp
auto f = [](int x) { return x * 2; };
f(5);      // 10
```

`f`'in türünü yazamazsınız; derleyicinin ürettiği isimsiz bir türdür. `auto` anahtar
sözcüğünün en çok ihtiyaç duyulduğu yerlerden biri budur (bkz. Kısım 4.4).

Asıl kullanım yeri, algoritmalara koşul ve karşılaştırma geçirmektir:

```cpp
std::sort(v.begin(), v.end(), [](int a, int b) { return a > b; });

auto it = std::find_if(v.begin(), v.end(), [](int x) { return x > 100; });
```
