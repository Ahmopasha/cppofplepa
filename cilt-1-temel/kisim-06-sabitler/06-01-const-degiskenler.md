---
cilt: "I — Temel"
kisim: "6 — Sabitler"
baslik: "6.1 `const` değişkenler"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++20)"
---

## 6.1 `const` değişkenler

`const` ile nitelenen bir değişkenin değeri, hayata geldikten sonra değiştirilemez.
Bu yüzden C++'ta **`const` bir değişken tanımlarken ilk değer vermek zorunludur.**

```cpp
const int x = 10;
const int y;          // sentaks hatası
```

`extern const int y;` ise tanım değil bildirimdir (bkz. Kısım 2.1). Bazı sınıf türlerinde
ise ilk değeri varsayılan kurucu işlev verebilir (bkz. Kısım 12.8).

C dilinde bu zorunluluk yoktur; orada `const` değişken ilk değer verilmeden
tanımlanabilir. C++ bu kapıyı kapatmıştır.

`const` bir nesneyi, dilin araçlarını aşarak (C tarzı bir dönüşümle) değiştirmeye
çalışmak **tanımsız davranıştır.** Derleyici o değerin değişmeyeceğini varsayarak
optimizasyon yapma hakkına sahiptir.
