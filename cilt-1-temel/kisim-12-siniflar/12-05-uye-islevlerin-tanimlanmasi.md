---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.5 Üye işlevlerin tanımlanması"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 12.5 Üye işlevlerin tanımlanması

Üye işlev iki yerde tanımlanabilir. Sınıf bloğu içinde tanımlanırsa **örtülü olarak
`inline`** olur (bkz. Kısım 11).

```cpp
class Myclass {
public:
    void f1() { /* ... */ }     // sınıf içinde — örtülü inline
    void f2();                  // bildirim
};

void Myclass::f2() { /* ... */ }    // sınıf dışında
```

Sınıf bloğunda bildirimi yapılmamış bir işlevin tanımını yapamazsınız. Genel uygulama,
bildirimlerin başlık dosyasında, tanımların kaynak dosyada olmasıdır.
