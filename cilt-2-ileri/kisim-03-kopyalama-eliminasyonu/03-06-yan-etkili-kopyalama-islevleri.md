---
cilt: "II — İleri"
kisim: "3 — Kopyalama Eliminasyonu"
baslik: "3.6 Yan etkili kopyalama işlevleri"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 3.6 Yan etkili kopyalama işlevleri

Eliminasyon, kopyalayan veya taşıyan kurucu işlevin **hiç çağrılmaması** demektir. O
işlevin gövdesinde gözlemlenebilir bir yan etki varsa, o yan etki de gerçekleşmez.

```cpp
class Sayac {
    static inline int adet = 0;
public:
    Sayac() = default;
    Sayac(const Sayac&) { ++adet; }      // yan etki
};
```

Bu sınıfta zorunlu eliminasyon bağlamlarında sayaç hiç artmaz. NRVO bağlamlarında artıp
artmayacağını standart belirtmez: eliminasyona izin verir, ama zorunlu kılmaz.

Kural: **kopyalayan ve taşıyan kurucuların ve onlarla eşleşen sonlandırıcı çağrılarının
sayısına programın doğruluğunu bağlamayın.** Bu işlevlerde günlükleme, sayaç ya da global
durum güncellemesi, programın davranışını gerçeklemenin eliminasyon tercihine bağımlı hâle
getirebilir.

Öğretim amaçlı kodda bu işlevlere yazdırma koymak yaygındır ve yararlıdır; üretim
kodunda değildir.
