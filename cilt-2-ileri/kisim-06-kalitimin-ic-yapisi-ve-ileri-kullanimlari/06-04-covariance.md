---
cilt: "II — İleri"
kisim: "6 — Kalıtımın İç Yapısı ve İleri Kullanımları"
baslik: "6.4 Covariance"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 6.4 Covariance

Geçersiz kılan işlevin geri dönüş türü, taban sınıftakiyle aynı olmak zorunda değildir.
Taban sınıf `B*` döndürüyorsa türemiş sınıf, `B`'den türetilmiş bir `D*` döndürebilir.
Buna *covariant return type* denir.

```cpp
class Sekil {
public:
    virtual Sekil* clone() const;
};

class Daire : public Sekil {
public:
    Daire* clone() const override;    // Sekil* değil, Daire* — geçerlidir
};
```

Referanslar için de geçerlidir. Kazancı, türemiş türle çalışan kodun `cast` yapmak
zorunda kalmamasıdır.
