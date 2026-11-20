---
cilt: "I — Temel"
kisim: "24 — Lambda İfadeleri"
baslik: "24.1 Ne olduğu"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 24.1 Ne olduğu

Lambda ifadesi, derleyiciye **isimsiz bir sınıf yazdırır** ve ondan bir nesne üretir;
bunlara **kapanış türü** *(closure type)* ve **kapanış nesnesi** *(closure object)* denir.
Kapanış türünün çağrı operatörünün (`operator()`, Kısım 14.2) gövdesi, lambdanın
gövdesidir.

```cpp
auto f = [](int x) { return x * 2; };
f(5);      // 10
```

Her lambda ifadesinin kapanış türü kendine özgü ve adsızdır; adıyla yazılamaz, bu yüzden
`auto` kullanılır (Kısım 4.4).

Asıl kullanım yeri, algoritmalara koşul ve karşılaştırma geçirmektir:

```cpp
std::sort(v.begin(), v.end(), [](int a, int b) { return a > b; });

auto it = std::find_if(v.begin(), v.end(), [](int x) { return x > 100; });
```
