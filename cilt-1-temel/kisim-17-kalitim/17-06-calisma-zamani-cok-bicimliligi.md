---
cilt: "I — Temel"
kisim: "17 — Kalıtım"
baslik: "17.6 Çalışma zamanı çok biçimliliği"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 17.6 Çalışma zamanı çok biçimliliği

Şimdiye kadar hangi işlevin çağrılacağına derleyici derleme zamanında karar veriyordu;
buna *static binding* denir. Kalıtım, kararın çalışma zamanına bırakılmasına imkân verir;
buna *dynamic binding* veya *late binding* denir. Aynı çağrının, nesnenin gerçek türüne
göre farklı işlevleri çalıştırmasına **çok biçimlilik** *(polymorphism)* denir.

Bunun için taban sınıftaki işlevi `virtual` olarak bildirirsiniz; böyle bir işleve
**sanal işlev** *(virtual function)*, türemiş sınıfta aynı isim, parametre listesi ve
niteleyicilerle (ör. `const`) yeniden bildirilmesine **geçersiz kılma** *(overriding)*
denir. En az bir sanal işlev bildiren ya da devralan sınıfa **çok biçimli sınıf**
*(polymorphic class)* denir. Karar çalışma zamanına ancak çağrı gösterici ya da referans
üzerinden yapılırsa bırakılır; üye işlevin içinden yapılan nitelenmemiş çağrı da `this`
göstericisi (Kısım 12.6) üzerinden yapılmış sayılır (bkz. Kısım 17.9; istisnalar Cilt II,
Kısım 6.2):

```cpp
class Sekil {
public:
    virtual void ciz() const;
    virtual ~Sekil();
};

class Daire : public Sekil {
public:
    void ciz() const override;
};

void goster(const Sekil& s)
{
    s.ciz();     // hangi ciz()? Çalışma zamanında belli olur.
}
```

`goster` işlevi `Daire` sınıfını tanımaz, tanımak zorunda da değildir. Yarın yazacağınız
yeni bir `Sekil` türü için de aynı işlev çalışır. Kazanç budur.

**`override` yazın.** Yazmasanız da olur, ama yazarsanız derleyici gerçekten bir taban
sınıf işlevini geçersiz kıldığınızı doğrular. İmzada ufak bir hata yaptığınızda sessizce
yeni bir işlev tanımlamış olmazsınız, hata alırsınız.

Türemiş sınıfta `virtual` anahtar sözcüğünü tekrar yazmak gerekmez; sanal bir işlevi
geçersiz kılan işlev de sanaldır ve hiyerarşinin geri kalanında öyle kalır. Aynı isimli
ama parametre listesi ya da `const` niteleyicisi farklı bir işlev ise geçersiz kılmaz,
Kısım 17.5'teki gibi tabandaki ismi gölgeler.
