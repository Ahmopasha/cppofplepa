---
cilt: "I — Temel"
kisim: "17 — Kalıtım"
baslik: "17.6 Çalışma zamanı çok biçimliliği"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 17.6 Çalışma zamanı çok biçimliliği

Şimdiye kadar hangi işlevin çağrılacağına derleyici derleme zamanında karar veriyordu;
buna *static binding* denir. Kalıtım, kararın çalışma zamanına bırakılmasına imkân
verir; buna *dynamic binding* veya *late binding* denir.

Bunun için taban sınıftaki işlevi `virtual` olarak bildirmek yeterlidir:

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

Türemiş sınıfta `virtual` anahtar sözcüğünü tekrar yazmak gerekmez; bir işlev bir kez
`virtual` olduysa hiyerarşinin geri kalanında öyle kalır.
