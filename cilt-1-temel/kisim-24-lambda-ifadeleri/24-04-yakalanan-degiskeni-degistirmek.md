---
cilt: "I — Temel"
kisim: "24 — Lambda İfadeleri"
baslik: "24.4 Yakalanan değişkeni değiştirmek"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 24.4 Yakalanan değişkeni değiştirmek

Kopyalayarak yakaladığınız bir değişkeni lambda gövdesinde değiştiremezsiniz:

```cpp
int a = 10;
auto f = [a] { ++a; };        // sentaks hatası
```

Sebebi, derleyicinin ürettiği çağrı operatörünün `const` olmasıdır. Kısıtı kaldırmak için
`mutable` yazılır:

```cpp
auto f = [a]() mutable { ++a; return a; };
```

Değişiklik **yalnızca lambdanın kendi kopyasını** etkiler; dışarıdaki `a` değişmez.
Referansla yakalamada `mutable` gerekmez, çünkü `const`luk referansın kendisini niteler,
gösterdiği nesneyi değil.

Mekanizmanın tamamı ve kapanış türünün yapısı: **Cilt II, Kısım 12.1–12.2.**
