---
cilt: "II — İleri"
kisim: "6 — Kalıtımın İç Yapısı ve İleri Kullanımları"
baslik: "6.5 Sanal kurucu işlev deyimi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 6.5 Sanal kurucu işlev deyimi

C++'ta kurucu işlevler `virtual` olamaz; nesne henüz yokken hangi tablonun kullanılacağı
bilinemez. Ama elinizde bir taban sınıf göstericisi varken, ardındaki nesnenin **kendi
türünden** bir kopyasını oluşturmak isteyebilirsiniz.

Çözüm, işi sanal bir işleve devretmektir:

```cpp
class Sekil {
public:
    virtual Sekil* clone() const = 0;
    virtual ~Sekil() = default;
};

class Daire : public Sekil {
public:
    Daire* clone() const override { return new Daire(*this); }
};

void kopyala(const Sekil& s)
{
    Sekil* yeni = s.clone();    // gerçek tür ne ise onun kopyası
}
```

Kısım 6.4'teki covariance sayesinde `Daire::clone` doğrudan `Daire*` döndürebilir.
