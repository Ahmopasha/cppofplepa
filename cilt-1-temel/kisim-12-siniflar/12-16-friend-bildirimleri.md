---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.16 `friend` bildirimleri"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 12.16 `friend` bildirimleri

Bir sınıf, `private` ve `protected` bölümüne erişim hakkını başka bir varlığa verebilir.

<!-- kod-baglam
class Myclass;
class Baska {
public:
    void uye(Myclass&);
};
-->
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

Yalnızca sınıf içinde `friend` olarak bildirilen bir işlevin ismi sıradan isim aramayla
bulunmaz; yalnızca argümana bağlı isim arama (Kısım 16.5) ile, örneğin argümanlardan biri
bu sınıf türündeyse, bulunabilir. İşlev, sınıfın bulunduğu isim alanında (Kısım 16.2)
ayrıca bildirilirse sıradan aramayla da bulunur.

`friend`, kapsüllemeyi delen bir araçtır; ihtiyaç duyulan en dar biçimi tercih edin.
Bütün bir sınıfa `friend` vermek yerine, yalnızca erişmesi gereken üye işleve verin.
