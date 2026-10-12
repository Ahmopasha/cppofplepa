---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.16 `friend` bildirimleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 12.16 `friend` bildirimleri

Bir sınıf, `private` ve `protected` bölümüne erişim hakkını başka bir varlığa verebilir.

```cpp
class Myclass {
    int x;
    friend void global_func(Myclass&);        // global işleve
    friend void Baska::uye(Myclass&);         // başka sınıfın bir üye işlevine
    friend class Baska;                       // bütün bir sınıfa
};
```

`friend` bildirimi sınıfın neresinde yapıldığının önemi yoktur; erişim belirleyicileri
onu etkilemez.

Sınıf içinde `friend` olarak bildirilen bir işlevin ismi, argümana bağlı isim arama
yoluyla bulunabilir hâle gelir (bkz. Kısım 16).

`friend`, kapsüllemeyi delen bir araçtır; ihtiyaç duyulan en dar biçimi tercih edin.
Bütün bir sınıfa `friend` vermek yerine, yalnızca erişmesi gereken üye işleve verin.
