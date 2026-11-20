---
cilt: "I — Temel"
kisim: "24 — Lambda İfadeleri"
baslik: "24.4 Yakalanan değişkeni değiştirmek"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 24.4 Yakalanan değişkeni değiştirmek

Kopyalayarak yakaladığınız bir değişkeni lambda gövdesinde değiştiremezsiniz:

```cpp
int a = 10;
auto f = [a] { ++a; };        // sentaks hatası
```

Sebebi, kopyanın kapanış nesnesinin bir veri elemanı olması ve kapanış türünün çağrı
operatörünün `const` olmasıdır; kısıtı `mutable` kaldırır:

```cpp
auto f = [a]() mutable { ++a; return a; };
```

Değişiklik **yalnızca kapanış nesnesindeki kopyayı** etkiler; dışarıdaki `a` değişmez.
Referansla yakalamada `mutable` gerekmez: gövdedeki ad bir kopyayı değil, dışarıdaki
değişkenin kendisini gösterir.

Mekanizmanın tamamı ve kapanış türünün yapısı: **Cilt II, Kısım 12.1–12.2.**
