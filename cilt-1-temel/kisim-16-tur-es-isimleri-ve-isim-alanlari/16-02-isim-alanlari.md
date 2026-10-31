---
cilt: "I — Temel"
kisim: "16 — Tür Eş İsimleri ve İsim Alanları"
baslik: "16.2 İsim alanları"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 16.2 İsim alanları

Büyük projelerde ve kütüphanelerde aynı ismin farklı anlamlarda kullanılması
kaçınılmazdır. İsim alanı, isimleri gruplayarak çakışmayı önler.

```cpp
namespace grafik {
    class Nokta { /* ... */ };
    void ciz(const Nokta&);
}

grafik::Nokta n;
grafik::ciz(n);
```

İsim alanları iç içe yazılabilir. C++17 bunun için kısa bir yazım ekledi:

```cpp
namespace a::b::c { /* ... */ }      // C++17
```

Aynı isim alanı **birden fazla yerde açılabilir**; parçalar birleşir. Standart kütüphane
de bu şekilde, `std` isim alanını onlarca başlık dosyasına dağıtarak çalışır.

İsim alanına eş isim verilebilir:

<!-- kod-baglam
namespace grafik::ileri_seviye { }
-->
```cpp
namespace gfx = grafik::ileri_seviye;
```

Hiçbir isim alanı içinde olmayan isimler **global isim alanındadır** ve `::` ile
nitelenebilir (bkz. Kısım 2.2).
