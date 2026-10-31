---
cilt: "I — Temel"
kisim: "14 — Operatör Yüklemesi"
baslik: "14.3 Üye mi, global mi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 14.3 Üye mi, global mi

Seçim, sol operandın ne olduğuna bakılarak yapılır.

**Sol operand kendi sınıfınızsa** üye işlev yazabilirsiniz. Bu durumda sol operand
`this`, sağ operand parametre olur.

```cpp
class Kesir {
public:
    Kesir operator+(const Kesir&) const;    // a + b
};
```

**Sol operand başka bir türse** üye işlev yazamazsınız; o türün sınıfına müdahale
edemezsiniz. Akım operatörleri bu gruptadır:

```cpp
std::ostream& operator<<(std::ostream& os, const Kesir& k);
```

Sol operand `std::ostream` olduğu için bu işlev üye olamaz.

**Simetri gerektiren aritmetik ve karşılaştırma operatörlerinde global tercih edilir.**
Üye işlev yazarsanız sol operand dönüşüme uğrayamaz:

```cpp
Kesir k{1, 2};
k + 5;      // üye işlevle de çalışır
5 + k;      // üye işlevle çalışmaz, global işlevle çalışır
```
