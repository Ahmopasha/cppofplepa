---
cilt: "I — Temel"
kisim: "22 — Şablonlara Giriş"
baslik: "22.1 Jenerik programlama"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 22.1 Jenerik programlama

Şablonlar, **tek bir kodun birden fazla türe hizmet etmesini** sağlar.

Aynı algoritmayı her tür için ayrı ayrı yazmak yerine, türü bir parametre hâline
getirirsiniz:

```cpp
int    enbuyuk(int a, int b)       { return a > b ? a : b; }
double enbuyuk(double a, double b) { return a > b ? a : b; }
// ... her tür için bir tane
```

```cpp
template<typename T>
T enbuyuk(T a, T b) { return a > b ? a : b; }
```

`typename` yerine `class` yazmak da mümkündür; ikisi bu bağlamda aynıdır. Yeni kodda
`typename` tercih edilir, çünkü parametre bir sınıf olmak zorunda değildir.
