---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.4.4 Sık karşılaşılan ifadelerin kategorileri"
kaynak: "ders notları"
kutular: ["Standart Notu — C ve C++ farkı"]
son_kontrol: "2026-09 (C++20)"
---

### 2.4.4 Sık karşılaşılan ifadelerin kategorileri

```cpp
int x = 100;
int* ptr = &x;

// L-Value
x
(x)
*ptr
++x            // önek biçimi
--x
"Ahmet"        // yazı sabitleri L-Value'dur, çünkü bellekte bir dizidirler

// R-Value
100
'A'
3.14
nullptr
x + 5
x++            // sonek biçimi
x--

// X-Value
std::move(x)
```

İşlevlerde kategori, geri dönüş türüne bakılarak belirlenir:

```cpp
int  foo();    foo()   // R-Value  — değer döndürenler
int& bar();    bar()   // L-Value  — referans döndürenler
```

`bar()` bir L-Value olduğu için atamanın solunda durabilir:

<!-- kod-baglam
int& bar();
-->
```cpp
bar() = 42;    // geçerlidir
```

> **Standart Notu — C ve C++ farkı**
> `++x` ve `--x` önek biçimleri C dilinde R-Value üretir, C++'ta L-Value üretir.
> Virgül operatörü de C'de R-Value üretirken C++'ta sağ operandın kategorisini üretir.
> `x + 5` gibi aritmetik ifadeler her iki dilde de R-Value'dur. C'den gelen kodu
> okurken bu farkları gözden kaçırmayın.
