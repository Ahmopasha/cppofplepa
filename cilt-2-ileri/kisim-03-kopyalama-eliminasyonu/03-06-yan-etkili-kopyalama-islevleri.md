---
cilt: "II — İleri"
kisim: "3 — Kopyalama Eliminasyonu"
baslik: "3.6 Yan etkili kopyalama işlevleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
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

Bu sınıfta kopya sayısı, derleyiciye ve optimizasyon seviyesine göre değişir. Zorunlu
eliminasyon bağlamlarında sayaç hiç artmaz; NRVO bağlamlarında artıp artmayacağı
belirsizdir.

Kural: **özel üye işlevlerin gövdesine, nesnenin kendi durumu dışında hiçbir şeyi
değiştiren kod yazmayın.** Günlükleme, sayaç, global durum güncellemesi — hepsi
programın davranışını derleyiciye bağımlı hâle getirir.

Öğretim amaçlı kodda bu işlevlere yazdırma koymak yaygındır ve yararlıdır; üretim
kodunda değildir.
