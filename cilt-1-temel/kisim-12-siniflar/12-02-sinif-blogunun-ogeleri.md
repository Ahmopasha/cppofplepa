---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.2 Sınıf bloğunun öğeleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 12.2 Sınıf bloğunun öğeleri

Bir sınıf bloğu üç tür öğe barındırır:

**Veri elemanları** *(data members)* — sınıf bloğunda bildirilen değişkenler. `static`
olan ve olmayan diye ikiye ayrılır.

**Üye işlevler** *(member functions)* — sınıf bloğunda bildirilen işlevler. Yine `static`
olan ve olmayan diye ikiye ayrılır.

**Tür üyeleri** *(type members)* — sınıf bloğu içindeki tür eş isimleri, başka sınıf
bildirimleri, `enum` türleri.

```cpp
class Myclass {
public:
    using deger_turu = int;        // tür üyesi
    static int sayac;              // static veri elemanı
    int x;                         // veri elemanı
    void func();                   // üye işlev
    static void yardimci();        // static üye işlev
};
```
