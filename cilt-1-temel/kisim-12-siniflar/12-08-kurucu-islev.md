---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.8 Kurucu işlev"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
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

Kurucu işlev doğrudan çağrılamaz; nesne oluşturulurken derleyici çağırır.

**En az bir kurucu işlev bildirdiğinizde, derleyici varsayılan kurucu işlevi artık
yazmaz.** İhtiyacınız varsa açıkça bildirmeniz gerekir:

```cpp
class Myclass {
public:
    Myclass(int);
    Myclass() = default;    // bunu yazmazsanız Myclass m; derlenmez
};
```
