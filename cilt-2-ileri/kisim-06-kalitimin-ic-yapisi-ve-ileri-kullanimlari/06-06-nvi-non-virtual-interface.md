---
cilt: "II — İleri"
kisim: "6 — Kalıtımın İç Yapısı ve İleri Kullanımları"
baslik: "6.6 NVI — Non-Virtual Interface"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 6.6 NVI — Non-Virtual Interface

Taban sınıfın arayüzü ile özelleştirme noktalarını ayırmaya yarar. Arayüz işlevleri
`public` ve sanal **değildir**; özelleştirme noktaları `private` ve sanaldır.

```cpp
class Rapor {
public:
    void yazdir() const          // arayüz: sanal değil
    {
        baslik();
        govde();                 // özelleştirme noktası
        altbilgi();
    }
private:
    virtual void govde() const = 0;
    void baslik() const;
    void altbilgi() const;
};
```

Türemiş sınıf `govde`'yi geçersiz kılar ama `yazdir`'ın akışını değiştiremez. Taban
sınıf, özelleştirmeden önce ve sonra kod çalıştırma hakkını elinde tutar; ön koşul ve
son koşul denetimi, kilitleme, günlükleme buraya konur.

`private` bir sanal işlevin türemiş sınıfta geçersiz kılınabilmesi, Kısım 6.3'teki
"erişim kontrolü statik türe bakar" kuralının sonucudur.
