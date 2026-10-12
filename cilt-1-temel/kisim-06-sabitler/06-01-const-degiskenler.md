---
cilt: "I — Temel"
kisim: "6 — Sabitler"
baslik: "6.1 `const` değişkenler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 6.1 `const` değişkenler

`const` ile nitelenen bir değişkenin değeri, hayata geldikten sonra değiştirilemez.
Bunun doğrudan sonucu şudur: **`const` değişkenlere ilk değer vermek zorunludur.**

```cpp
const int x = 10;
const int y;          // sentaks hatası
```

C dilinde bu zorunluluk yoktur; orada ilk değer almamış `const` değişken bildirilebilir.
C++ bu kapıyı kapatmıştır.

`const` bir nesneyi, dilin araçlarını aşarak (C tarzı bir dönüşümle) değiştirmeye
çalışmak **tanımsız davranıştır.** Derleyici o değerin değişmeyeceğini varsayarak
optimizasyon yapma hakkına sahiptir.
