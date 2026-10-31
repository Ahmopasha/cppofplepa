---
cilt: "I — Temel"
kisim: "3 — İlk Değer Verme"
baslik: "3.9 Hangisini kullanmalı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 3.9 Hangisini kullanmalı

> **Varsayılan tercihiniz küme parantezi olsun.** Daraltıcı dönüşümü engeller, most
> vexing parse'tan korur, ve bütün türler için aynı biçimde çalışır.

İki istisnası vardır.

**`std::initializer_list` alan kaplar.** Küme parantezi, varsa `initializer_list`
parametreli kurucu işlevi diğerlerine tercih eder:

```cpp
std::vector<int> v1(10, 5);    // 5 değerli 10 eleman
std::vector<int> v2{10, 5};    // iki eleman: 10 ve 5
```

Kaplarda boyut belirtirken normal parantez kullanın.

**`auto` ile birlikte.** `auto x{1};` ile `auto x = {1};` farklı türler üretir; ikincisi
`initializer_list`'tir. `auto` kullanırken eşittir yazımını tercih edin (bkz. Kısım 4).
