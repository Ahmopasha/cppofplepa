---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.7 `const` üye işlevler"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 12.7 `const` üye işlevler

Bildiriminin sonuna `const` yazılan üye işlev, çağrıldığı nesnenin **problem alanındaki
değerini değiştirmeyeceğini** taahhüt eder.

```cpp
class Myclass {
    int x;
public:
    int get() const { return x; }    // const üye işlev
    void set(int v) { x = v; }
};
```

İki sonucu vardır. Gövdesinde, işlevin çağrıldığı nesnenin veri elemanlarını doğrudan ya
da `this` üzerinden değiştiremezsiniz (`mutable` olanlar dışında, Kısım 12.15). Ve
**`const` bir nesne ya da `const` nesneye bağlı referans veya `const` nesneyi gösteren
gösterici (`const Myclass&`, `const Myclass*`) üzerinden, `static` olmayan üye işlevlerden
yalnızca `const` olanlar çağrılabilir** (sonlandırıcı işlev bunun dışındadır, Kısım 12.9).

```cpp
/*
 * const nesne ilk değer almalı (bkz. 6.1);
 * {} değerle ilk değer verir, x sıfırlanır (bkz. 3.3)
 */
const Myclass cm{};
cm.get();      // geçerli
cm.set(10);    // sentaks hatası
```

> **Nesnenin durumunu değiştirmeyen her üye işlevi `const` yapın.** Bunu ihmal ederseniz
> sınıfınız `const` nesnelerle ve `const` referanslarla kullanılamaz hâle gelir. Sonradan
> eklemek, o sınıfı kullanan bütün kodu gözden geçirmeyi gerektirir.

`const` ve `const` olmayan iki sürüm aynı anda bildirilebilir; `const`luk işlev
yüklemesinde ayırt edici bir özelliktir.
