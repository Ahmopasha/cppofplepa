---
cilt: "I — Temel"
kisim: "17 — Kalıtım"
baslik: "17.8 Soyut sınıflar"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 17.8 Soyut sınıflar

Bazı taban sınıfların kendi başına anlamı yoktur; yalnızca arayüz tanımlarlar. Böyle
sınıflarda işlevi bildirip tanımlamamak istersiniz. Bunun için **saf sanal işlev**
kullanılır:

```cpp
class Sekil {
public:
    virtual void ciz() const = 0;    // saf sanal
    virtual ~Sekil() = default;
};
```

En az bir saf sanal işlevi olan sınıfa **soyut sınıf** denir. Soyut sınıf türünden nesne
oluşturulamaz; yalnızca gösterici ve referans tanımlanabilir. Türemiş sınıf saf sanal
işlevlerin hepsini geçersiz kılmazsa o da soyut kalır.

Soyut olmayan sınıflara **somut sınıf** denir.
