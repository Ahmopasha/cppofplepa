---
cilt: "I — Temel"
kisim: "3 — İlk Değer Verme"
baslik: "3.9 Hangisini kullanmalı"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 3.9 Hangisini kullanmalı

> **Varsayılan tercihiniz küme parantezi olsun.** Daraltıcı dönüşümü engeller, most
> vexing parse'tan korur, ve bütün türler için aynı biçimde çalışır.

İki istisnası vardır.

**`std::initializer_list` alan kaplar.** `std::initializer_list`, küme parantezi içindeki
değerleri taşıyan standart kütüphane türüdür; kaplar Kısım 23.4'te anlatılır. Küme
parantezi, varsa `std::initializer_list` parametreli kurucu işlevi, değerler listenin
eleman türüne dönüştürülebiliyorsa diğerlerine (dönüşüm daraltıcı olsa bile; o zaman
sentaks hatasıdır, Kısım 3.7) tercih eder. Boş küme parantezi bunun dışındadır: sınıfın
varsayılan kurucu işlevi (Kısım 12.8) varsa o çağrılır.

```cpp
std::vector<int> v1(10, 5);    // 5 değerli 10 eleman
std::vector<int> v2{10, 5};    // iki eleman: 10 ve 5
std::vector<int> v3{};         // varsayılan kurucu işlev: boş
```

Kaplarda boyut belirtirken normal parantez kullanın.

**`auto` ile birlikte.** `auto x{1};` ile `auto x = {1};` farklı türler üretir; ilki `int`
(C++17'den itibaren), ikincisi `std::initializer_list<int>`'tir. `auto` ile küme parantezi
yerine eşittir ve tek değer yazın: `auto x = 1;` (Kısım 4.5).
