---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.4.2 İki temel kategori"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

### 2.4.2 İki temel kategori

Bir ifade ya **L-Value**'dur ya **R-Value**.

**L-Value**, bellekte kalıcı bir yeri olan şeydir. Adresini alabilirsiniz, ona atama
yapabilirsiniz, ismi vardır.

```cpp
int x = 10;
x           // L-Value
&x          // adresi alınabiliyor
x = 20;     // atamanın solunda durabiliyor
```

**R-Value**, geçici olan şeydir. Kullanıldığı ifadenin sonunda ortadan kalkar.

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
&x          // OK      → x bir L-Value
&(x + 5)    // HATA    → x + 5 bir R-Value
```

C dilinde bu ikisi dışında kategori yoktur. C++'ta üçüncü bir kategori vardır ve
taşıma semantiğiyle birlikte gelmiştir.
