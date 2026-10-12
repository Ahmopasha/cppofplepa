---
cilt: "I — Temel"
kisim: "14 — Operatör Yüklemesi"
baslik: "14.4 `friend` ve ADL bağlantısı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 14.4 `friend` ve ADL bağlantısı

Global operatör işlevlerinin sınıfın `private` bölümüne erişmesi gerekir. İki yol vardır:
sınıfın `public` arayüzünü kullanmak, veya işlevi `friend` bildirmek.

`friend` bildirimini **sınıf içinde tanımlayarak** yapmak yaygın bir uygulamadır:

```cpp
class Kesir {
    int pay, payda;
public:
    friend Kesir operator+(const Kesir& a, const Kesir& b)
    {
        return Kesir{a.pay * b.payda + b.pay * a.payda, a.payda * b.payda};
    }
};
```

Bu işlev sınıfın üyesi **değildir**; global bir işlevdir. Ama ismi yalnızca argümana bağlı
isim arama yoluyla bulunur (bkz. Kısım 16.5). Yani `a + b` yazınca bulunur, `Kesir::`
ile nitelenerek çağrılamaz.

ADL'in operatör yüklemesindeki asıl rolü budur: 16.5'te "operatör yüklemesi nitelenmeden
çağrılmak zorundadır" demiştik; bu bölüm o gerekçenin uygulaması.
