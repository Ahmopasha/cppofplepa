---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.1.4 `decltype` ile ilişkisi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

### 1.1.4 `decltype` ile ilişkisi

`decltype` operatörünün sonucu, operandının **isim mi ifade mi** olduğuna göre değişir.
Değer kategorisinin dile en doğrudan yansıdığı yer burasıdır.

Operand bir **isimse**, ismin bildirildiği tür ne ise sonuç odur:

```cpp
int x = 10;
int& r = x;
const int& cr = x;

decltype(x)   a;   // int
decltype(r)   b;   // int&        — ilk değer gerektiğinden bu satır sentaks hatası
decltype(cr)  c;   // const int&  — aynı şekilde sentaks hatası
```

Operand bir **ifadeyse**, ifadenin değer kategorisine bakılır:

| İfadenin kategorisi | `decltype` sonucu |
|---|---|
| PR-Value | `T` |
| L-Value | `T&` |
| X-Value | `T&&` |

```cpp
int&& foo();
int x = 3;
int* px = &x;

decltype(10)      a;  // int   — PR-Value
decltype(x + 5)   b;  // int   — PR-Value
decltype(*px)     c;  // int&  — L-Value
decltype((x))     d;  // int&  — (x) artık bir ifadedir, L-Value
decltype(foo())   e;  // int&& — X-Value
```

`decltype(x)` ile `decltype((x))` arasındaki fark buradan gelir ve kasıtlıdır.
Bir sonraki bölümde bu farkı kategori tespiti için kullanacağız.
