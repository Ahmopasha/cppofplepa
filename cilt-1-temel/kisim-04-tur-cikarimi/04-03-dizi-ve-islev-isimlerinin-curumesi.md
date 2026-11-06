---
cilt: "I — Temel"
kisim: "4 — Tür Çıkarımı"
baslik: "4.3 Dizi ve işlev isimlerinin çürümesi"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 4.3 Dizi ve işlev isimlerinin çürümesi

`auto x = expr;` kalıbında dizi göstericiye, işlev de işlev göstericisine dönüşür. Bu
dönüşüme **çürüme** *(decay)* denir. Referans kalıplarında (`auto&`, `const auto&`,
`auto&&`) çürüme olmaz.

```cpp
int a[5]{};
void foo(int);

auto  p = a;       // int*
auto& r = a;       // int(&)[5]  — boyut korundu

auto  fp = foo;    // void(*)(int)
auto& fr = foo;    // void(&)(int)
```

Dizinin boyutunu tür bilgisi olarak korumak istiyorsanız `auto&` kullanmalısınız.
