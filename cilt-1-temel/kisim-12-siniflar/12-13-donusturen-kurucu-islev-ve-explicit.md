---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.13 Dönüştüren kurucu işlev ve `explicit`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 12.13 Dönüştüren kurucu işlev ve `explicit`

Tek parametreli kurucu işlevler, sınıf türünden olmayan bir değerin sınıf türüne
**örtülü olarak dönüşmesini** sağlar. Buna dönüştüren kurucu işlev denir.

```cpp
class Myclass {
public:
    Myclass(int);
};

void func(Myclass);

func(12);           // int → Myclass örtülü dönüşümü
Myclass m = 20;     // yine örtülü dönüşüm
```

Bu dönüşüm bazen istenir, çoğu zaman istenmez. İstenmediğinde `explicit` kullanılır:

```cpp
class Myclass {
public:
    explicit Myclass(int);
};

func(12);              // artık sentaks hatası
Myclass m = 20;        // sentaks hatası
Myclass m2{20};        // geçerli — açık çağrı
```

> **Tek parametreli kurucu işlevlerinizi `explicit` yapın.** Örtülü dönüşümü bilinçli
> olarak isteyene kadar varsayılan bu olmalıdır. `explicit` olmayan bir kurucu işlev,
> yanlışlıkla yazılmış bir çağrının sessizce derlenmesine yol açar.

Parametre türünün `int` olması şart değildir; `double`, `const char*` ve diğer türler de
aynı sonucu doğurur.
