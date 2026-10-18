---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.7 `const` üye işlevler"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
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

İki sonucu vardır. Gövdesinde veri elemanlarını değiştiremezsiniz. Ve **`const` bir nesne
üzerinden yalnızca `const` üye işlevler çağrılabilir.**

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
