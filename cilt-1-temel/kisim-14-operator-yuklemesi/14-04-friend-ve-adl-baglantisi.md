---
cilt: "I — Temel"
kisim: "14 — Operatör Yüklemesi"
baslik: "14.4 `friend` ve ADL bağlantısı"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 14.4 `friend` ve ADL bağlantısı

Global operatör işlevlerinin sınıfın `private` bölümüne erişmesi gerekir. İki yol vardır:
sınıfın `public` arayüzünü kullanmak, veya işlevi `friend` bildirmek.

`friend` bildirimini **sınıf içinde tanımlayarak** yapmak yaygın bir uygulamadır:

```cpp
class Kesir {
    int pay, payda;
public:
    Kesir(int p, int q) : pay{p}, payda{q} { }

    friend Kesir operator+(const Kesir& a, const Kesir& b)
    {
        return Kesir{a.pay * b.payda + b.pay * a.payda, a.payda * b.payda};
    }
};
```

Bu `operator+` işlevi sınıfın üyesi **değildir**; sınıfın bulunduğu isim alanının (burada
global isim alanının) bir işlevidir. Ama ismi yalnızca argümana bağlı isim arama yoluyla,
örneğin argümanlardan biri `Kesir` türündeyse, bulunur (Kısım 12.16, 16.5). Yani `a + b`
ya da `operator+(a, b)` yazınca bulunur; `::operator+(a, b)` gibi nitelenmiş bir çağrıyla
bulunmaz. Sınıfın üyesi olmadığı için `Kesir::operator+` diye bir isim de yoktur.

ADL'in operatör yüklemesindeki asıl rolü budur: Kısım 16.5'te göreceğiniz gibi ADL,
operatörlerin `a + b` biçiminde, nitelenmeden yazılabilmesini sağlar.
