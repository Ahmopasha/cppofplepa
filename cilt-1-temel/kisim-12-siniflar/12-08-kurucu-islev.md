---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.8 Kurucu işlev"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 12.8 Kurucu işlev

Nesneyi hayata getiren üye işlevdir. Üç özelliği vardır: ismi sınıfın ismiyle aynıdır,
geri dönüş türü **yoktur** (`void` de değil), ve `static` olamaz.

```cpp
class Myclass {
public:
    Myclass();              // varsayılan kurucu işlev
    Myclass(int);           // parametreli
    Myclass(int, double);
};
```

Kurucu işlev doğrudan çağrılamaz; nesne oluşturulurken çağrılır.

**En az bir kurucu işlev bildirdiğinizde, varsayılan kurucu işlev artık örtülü olarak bildirilmez.**
İhtiyacınız varsa açıkça bildirmeniz gerekir; bunun bir yolu `= default`'tur (Kısım
13.10):

```cpp
class Myclass {
public:
    Myclass(int);
    Myclass() = default;    // yoksa Myclass m; tanımı geçersiz olur
};
```
