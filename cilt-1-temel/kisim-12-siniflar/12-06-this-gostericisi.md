---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.6 `this` göstericisi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 12.6 `this` göstericisi

Her `static` olmayan üye işlev, çağrıldığı nesnenin adresini gizli bir parametre olarak
alır. Bu adrese `this` anahtar sözcüğüyle erişilir.

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
