---
cilt: "II — İleri"
kisim: "14 — Deyimler ve Kalıplar"
baslik: "14.3 Çok biçimlilik deyimleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 14.3 Çok biçimlilik deyimleri

### Type Erasure

Ortak bir taban sınıf gerektirmeden çok biçimli davranış elde etmenin yoludur. Kısım
6.13'te alternatif olarak anılmıştı; mekanizması şudur.

Dışarıdan görünen sınıf şablon değildir; içeride şablon bir sarmalayıcı tutar. Şablon
sarmalayıcı, soyut bir taban sınıftan türer ve gerçek türü bilir; dış sınıf ise yalnızca
taban sınıf göstericisi tutar.

```cpp
class Cizilebilir {
    struct Taban {
        virtual void ciz() const = 0;
        virtual ~Taban() = default;
    };

    template<typename T>
    struct Sarmal : Taban {
        T nesne;
        Sarmal(T n) : nesne{std::move(n)} { }
        void ciz() const override { nesne.ciz(); }     // T'nin ciz'i
    };

    std::unique_ptr<Taban> p;
public:
    template<typename T>
    Cizilebilir(T n) : p{std::make_unique<Sarmal<T>>(std::move(n))} { }

    void ciz() const { p->ciz(); }
};
```

`Cizilebilir` nesnesi, `ciz()` üye işlevi olan **herhangi bir türü** tutabilir; o türün
hiçbir taban sınıftan türemesi gerekmez.

`std::function` bu deyimin standart kütüphanedeki uygulamasıdır; `std::any` de öyle.

### Strategy

Bir algoritmanın değişken kısmını dışarıdan alınabilir hâle getirir. C++'ta üç yolla
kurulur: sanal işlevle, şablon parametresiyle, veya çağrılabilir nesneyle.

```cpp
// Çağrılabilir ile — en esneği
class Siralayici {
    std::function<bool(int, int)> olcut;
public:
    Siralayici(std::function<bool(int, int)> o) : olcut{std::move(o)} { }
};
```

Şablon parametresiyle kurulan biçim derleme zamanında çözülür ve maliyetsizdir; STL
kaplarının karşılaştırıcı ve ayırıcı parametreleri bu biçimdedir.

### Polymorphic Exception

Elinizde taban sınıf referansıyla tutulan bir hata nesnesi varsa, onu yeniden göndermek
dilimlenmeye yol açabilir (bkz. Cilt I Kısım 18.3). Çözüm, hata sınıfına sanal bir
`raise()` işlevi eklemektir:

```cpp
struct Hata {
    virtual void raise() const { throw *this; }
    virtual ~Hata() = default;
};

struct AltHata : Hata {
    void raise() const override { throw *this; }        // doğru tür gönderilir
};
```
