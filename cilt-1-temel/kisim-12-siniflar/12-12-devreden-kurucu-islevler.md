---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.12 Devreden kurucu işlevler"
kaynak: "derleyen (ders notlarında yok)"
son_kontrol: "2026-10 (C++23)"
---

## 12.12 Devreden kurucu işlevler

Birden fazla kurucu işlevi olan sınıflarda aynı ilk değer verme kodu tekrarlanır:

```cpp
class Baglanti {
    std::string adres;
    int port;
    int zaman_asimi;
public:
    Baglanti() : adres{"localhost"}, port{80}, zaman_asimi{30} { }
    Baglanti(std::string a) : adres{std::move(a)}, port{80}, zaman_asimi{30} { }
    Baglanti(std::string a, int p) : adres{std::move(a)}, port{p}, zaman_asimi{30} { }
};
```

C++11'den itibaren bir kurucu işlev, ilk değer verme listesinde **aynı sınıfın başka bir
kurucu işlevini** çağırabilir. Buna *devretme* denir; çağrılan işleve **hedef kurucu
işlev** *(target constructor)* denir.

```cpp
class Baglanti {
    std::string adres;
    int port;
    int zaman_asimi;
public:
    Baglanti(std::string a, int p, int z)
        : adres{std::move(a)}, port{p}, zaman_asimi{z} { }      // hedef

    Baglanti(std::string a, int p) : Baglanti{std::move(a), p, 30} { }
    Baglanti(std::string a)        : Baglanti{std::move(a), 80, 30} { }
    Baglanti()                     : Baglanti{"localhost", 80, 30} { }
};
```

Veri elemanlarına gerçekten değer veren tek bir kurucu işlev kalır; diğerleri ona
devreder.

### Üç kural

**Devretme, listenin tek öğesi olmak zorundadır.** Aynı listede hem devredip hem veri
elemanına değer veremezsiniz:

<!-- kod-baglam
class Baglanti {
    std::string adres;
    int port;
    int zaman_asimi;
public:
    Baglanti(std::string a, int p, int z);
@kod@
};
-->
```cpp
Baglanti(std::string a) : Baglanti{std::move(a), 80, 30}, port{8080} { }   // hata
```

Sebebi şudur: hedef kurucu işlev bittiğinde nesne **tamamen hayata gelmiş** sayılır.
O noktadan sonra ilk değer verme aşaması bitmiştir; yapılabilecek şey atamadır, ilk
değer verme değil. Farklı bir değer istiyorsanız devreden kurucu işlevin **gövdesinde**
atarsınız.

<!-- kod-baglam
class Baglanti {
    std::string adres;
    int port;
    int zaman_asimi;
public:
    Baglanti(std::string a, int p, int z);
@kod@
};
-->
```cpp
Baglanti(std::string a) : Baglanti{std::move(a), 80, 30} { port = 8080; }   // geçerli
```

**Nesne, hedef kurucu işlev bitince hayata gelmiş sayılır.** Bunun doğrudan sonucu şudur:
devreden kurucu işlevin gövdesinde hata oluşursa, **sonlandırıcı işlev çağrılır.**
Sıradan bir kurucu işlevde durum böyle değildir (bkz. Kısım 18.9); orada gövdede oluşan
hata nesnenin hiç hayata gelmediği anlamına gelir.

**Devretme döngüsü kurmayın.** Bir kurucu işlev doğrudan ya da dolaylı olarak kendine
devrederse (örneğin iki kurucu işlevin birbirine devretmesi), bu durum
**derleyicinin bildirmek zorunda olmadığı hata** *(ill-formed, no diagnostic required)*
sayılır.

<!-- kod: atla -->
```cpp
class Bozuk {
public:
    Bozuk(int)    : Bozuk{1.0} { }
    Bozuk(double) : Bozuk{1}   { }  // döngü — derleyicinin bildirmek zorunda olmadığı hata
};
```

### Sınıf içi ilk değer verme ile karşılaştırma

Kısım 12.11'deki sınıf içi ilk değer verme de tekrarı azaltır. İkisi arasındaki seçim
şuna bakar: **verilecek değer sabit mi, yoksa hesaplanıyor mu?**

Sabit varsayılan değerler için sınıf içi ilk değer verme daha kısadır:

```cpp
class Baglanti {
    std::string adres{"localhost"};
    int port{80};
    int zaman_asimi{30};
public:
    Baglanti() = default;
    Baglanti(std::string a) : adres{std::move(a)} { }
};
```

Ortak **iş** yapılması gerekiyorsa — doğrulama, dönüştürme, kaynak edinme — devretme
gerekir; sınıf içi ilk değer verme yalnızca değer atar, kod çalıştırmaz.

İkisi birlikte de kullanılabilir ve çoğu sınıfta doğru çözüm budur: varsayılan değerler
sınıf içinde, ortak mantık hedef kurucu işlevde.

### `init()` yardımcı işleviyle karşılaştırma

C++11 öncesinde ortak kod, `private` bir `init()` işlevinde toplanırdı. Devretme bunun
yerini alır ve iki üstünlüğü vardır.

`init()` işlevi **atama yapar, ilk değer vermez.** Dolayısıyla `const` ve referans
türünden veri elemanlarına dokunamaz (bkz. Kısım 12.10); devretme dokunabilir.

Ve `init()` çağrılmadan önce veri elemanları bir kez varsayılan olarak hayata gelir; iki
aşamalı bir kuruluş oluşur. Devretmede tek aşama vardır.
