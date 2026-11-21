---
cilt: "I — Temel"
kisim: "25 — Akıllı Göstericiler"
baslik: "25.2 `std::unique_ptr`"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
kutular: ["Standart Notu — C++17"]
---

## 25.2 `std::unique_ptr`

Gösterdiği nesnenin **tek sahibidir.** Kopyalanamaz, taşınabilir.

```cpp
#include <memory>

auto p = std::make_unique<Myclass>(10, 20);

p->func();
(*p).func();

auto q = std::move(p);     // sahiplik q'ya geçti, p artık boş
```

Kopyalanamaz oluşu tasarımın gereğidir: standart, kopyalayan kurucu işlevi ve kopyalayan
atama işlevini silinmiş (`= delete`, Kısım 13.10) olarak bildirir. Böylece kopyalamayla
ikinci bir sahip oluşturulamaz; sahiplik taşımayla devredilir.

Dizi için ayrı bir sürümü vardır:

```cpp
auto a = std::make_unique<int[]>(100);
a[5] = 42;
```

`std::make_unique` kullanın, `std::unique_ptr<Myclass>(new Myclass)` yazmayın: tür adı bir
kez yazılır ve kodda çıplak `new` kalmaz (Kısım 15.5).

> **Standart Notu — C++17**
> **C++17 öncesi:** Bir işlev çağrısının argümanları birbirine karışarak
> değerlendirilebilirdi. `f(std::unique_ptr<Myclass>(new Myclass), g())` çağrısında
> `new Myclass` ile `std::unique_ptr`'ın kurulması arasında `g()` çalışıp hata
> gönderirse bellek sızardı; C++14'te gelen `std::make_unique` bunu önlerdi.
> **C++17 ile:** Her parametreye ilk değer verilmesi, ötekilerinkine karışmadan yapılır;
> bu sızıntı artık oluşmaz.
