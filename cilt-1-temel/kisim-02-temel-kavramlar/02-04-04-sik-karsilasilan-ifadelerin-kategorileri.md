---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.4.4 Sık karşılaşılan ifadelerin kategorileri"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
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

İşlev çağrısı ifadesinin kategorisi, geri dönüş türüne bakılarak belirlenir. Referans
döndürmeyen çağrı PR-Value, L-Value referans döndüren çağrı L-Value, bir nesneye R-Value
referans (`T&&`) döndüren çağrı X-Value'dur (Kısım 8.6):

```cpp
int  foo();    foo()   // PR-Value — referans döndürmeyenler
int& bar();    bar()   // L-Value  — L-Value referans döndürenler
int&& baz();   baz()   // X-Value  — nesneye R-Value referans döndürenler
```

`bar()` bir L-Value olduğu için atamanın solunda durabilir:

<!-- kod-baglam
int& bar();
-->
```cpp
bar() = 42;    // geçerlidir
```

Aşağıdaki farklar `int` gibi yerleşik türler içindir. `++x` ve `--x` önek biçimleri C
dilinde R-Value üretir, C++'ta L-Value üretir. Atama ifadesi de C'de R-Value, C++'ta
L-Value üretir. Koşul operatörü (`?:`) C'de R-Value üretir; C++'ta ise, örneğin iki
seçeneği de aynı türden L-Value ise, L-Value üretir. Virgül operatörü de C'de R-Value
üretirken C++'ta sağ operandın kategorisini üretir. `x + 5` gibi aritmetik ifadeler her
iki dilde de R-Value'dur.

> C ile ortak kullanılacak kodda (ör. başlık dosyalarında) bu ifadelerin L-Value olmasına dayanmayın.
