---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.1.4 `decltype` ile ilişkisi"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

### 1.1.4 `decltype` ile ilişkisi

`decltype` operatörünün sonucu, operandının **isim mi ifade mi** olduğuna göre değişir.
Değer kategorisinin dile en doğrudan yansıdığı yer burasıdır.

Operand parantezsiz bir **isim** ya da parantezsiz bir sınıf üyesi erişimiyse (`s.m`,
`p->m`), sonuç o ismin ya da üyenin bildirildiği türdür:

```cpp
int x = 10;
int& r = x;
const int& cr = x;

decltype(x)   a;   // int
decltype(r)   b;   // int&        — ilk değer gerektiğinden bu satır sentaks hatası
decltype(cr)  c;   // const int&  — aynı şekilde sentaks hatası
```

Operand parantezsiz bir **isim** ya da parantezsiz bir sınıf üyesi erişimi (`s.m`, `p->m`)
**değilse**, ifadenin değer kategorisine bakılır:

| İfadenin kategorisi | `decltype` sonucu |
|---|---|
| PR-Value | `T` |
| L-Value | `T&` |
| X-Value | `T&&` |

```cpp
int&& foo();
int x = 3;
int* px = &x;

using A = decltype(10);       // int   — PR-Value
using B = decltype(x + 5);    // int   — PR-Value
using C = decltype(*px);      // int&  — L-Value
using D = decltype((x));      // int&  — parantez, isim kuralını devre dışı bırakır; L-Value
using E = decltype(foo());    // int&& — X-Value
```

`decltype(x)` ile `decltype((x))` arasındaki fark buradan gelir ve kasıtlıdır.
Bir sonraki bölümde bu farkı kategori tespiti için kullanacağız.
