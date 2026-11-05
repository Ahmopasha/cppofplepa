---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.4.2 İki temel kategori"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

### 2.4.2 İki temel kategori

Bir ifade ya **L-Value**'dur ya **R-Value**.

**L-Value**, kabaca bellekte kalıcı bir yeri olan şeydir. Çoğunun adresini alabilirsiniz;
çoğuna, `const` değilse, atama yapabilirsiniz (diziler bunun dışındadır).

```cpp
int x = 10;
x           // L-Value
&x          // adresi alınabiliyor
x = 20;     // atamanın solunda durabiliyor
```

**R-Value**, kabaca geçici olan şeydir. Çoğu, kullanıldığı ifadenin sonunda ortadan kalkar
(bir istisnası Kısım 8.3'te).

<!-- kod-baglam
int x = 10;
int foo();
-->
```cpp
10          // R-Value
x + 5       // R-Value
foo()       // R-Value  (foo geriye değer döndürüyorsa)
```

Pratik ayırt etme yöntemi: **adresini alabiliyorsanız L-Value'dur.**

```cpp
&x          // geçerli          → x bir L-Value
&(x + 5)    // sentaks hatası   → x + 5 bir R-Value
```

C dilinde bu ikisi dışında kategori yoktur. C++'ta üçüncü bir kategori vardır ve
taşıma semantiğiyle birlikte gelmiştir.
