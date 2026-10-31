---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.11 Sınıf içi ilk değer verme"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 12.11 Sınıf içi ilk değer verme

Veri elemanına, bildirildiği yerde varsayılan bir değer verilebilir. Buna *default member
initializer* denir.

```cpp
class Myclass {
    int x{10};
    std::string s{"bos"};
public:
    Myclass() = default;            // x 10, s "bos"
    Myclass(int a) : x{a} { }       // x a, s "bos"
};
```

Kurucu işlev ilk değer verme listesinde aynı elemana değer verilirse, **listedeki
kazanır.** Sınıf içi değer yalnızca liste sessiz kaldığında devreye girer.

Bu, birden fazla kurucu işlevi olan sınıflarda tekrarı ortadan kaldırır.
