---
cilt: "I — Temel"
kisim: "17 — Kalıtım"
baslik: "17.8 Soyut sınıflar"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 17.8 Soyut sınıflar

Bazı taban sınıfların kendi başına anlamı yoktur; yalnızca arayüz tanımlarlar. Böyle
sınıflarda işlevi, tanımlamak zorunda kalmadan bildirmek istersiniz. Bunun için
**saf sanal işlev** *(pure virtual function)* kullanılır:

```cpp
class Sekil {
public:
    virtual void ciz() const = 0;    // saf sanal
    virtual ~Sekil() = default;
};
```

En az bir saf sanal işlevi olan sınıfa **soyut sınıf** *(abstract class)* denir. Soyut
sınıf türünden nesne oluşturulamaz; yalnızca gösterici ve referans tanımlanabilir.
Hiyerarşide geçersiz kılınmamış bir saf sanal işlev kalırsa türemiş sınıf da soyut olur.

Soyut olmayan sınıflara **somut sınıf** *(concrete class)* denir.
