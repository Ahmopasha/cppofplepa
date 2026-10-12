---
cilt: "I — Temel"
kisim: "4 — Tür Çıkarımı"
baslik: "4.5 `auto x{...}` tuzağı"
kaynak: "ders notları"
kutular: ["Standart Notu — C++17"]
son_kontrol: "2026-09 (C++23)"
---

## 4.5 `auto x{...}` tuzağı

Kısım 3.9'da değinilmişti. Küme parantezi `auto` ile birlikte farklı davranır:

```cpp
auto a1 = 10;      // int
auto a2{10};       // int         (C++17'den itibaren)
auto a3 = {10};    // std::initializer_list<int>
auto a4{10, 20};   // sentaks hatası (C++17'den itibaren)
```

Kural: `auto` ile eşittir yazımını kullanın.

> **Standart Notu — C++17**
> **C++17 öncesi:** `auto a2{10};` yazımı da `std::initializer_list<int>` üretiyordu.
> **C++17 ile:** Tek elemanlı küme parantezi elemanın türünü üretir; çok elemanlı olan
> `auto` ile sentaks hatasıdır.
> **Neden değişti:** Önceki davranış sezgiye aykırıydı ve `auto` ile küme parantezini bir
> arada kullanan kodda sık hataya yol açıyordu.
