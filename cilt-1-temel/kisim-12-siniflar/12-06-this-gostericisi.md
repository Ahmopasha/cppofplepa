---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.6 `this` göstericisi"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 12.6 `this` göstericisi

Her `static` (Kısım 12.14) olmayan üye işlevin gövdesinde `this` anahtar sözcüğü, işlevin
çağrıldığı nesnenin adresini verir. Gerçeklemeler bunu çoğunlukla nesnenin adresini işleve
gizli bir argüman olarak geçirerek sağlar.

```cpp
class Myclass {
    int x;
public:
    void set(int x)
    {
        this->x = x;      // parametre ismi veri elemanını gölgeliyor
    }
};
```

`this`'in türü, `const` olmayan üye işlevlerde `Myclass*`, `const` üye işlevlerde
`const Myclass*`'tır.
