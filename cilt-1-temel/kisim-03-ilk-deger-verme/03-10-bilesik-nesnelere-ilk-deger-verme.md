---
cilt: "I — Temel"
kisim: "3 — İlk Değer Verme"
baslik: "3.10 Bileşik nesnelere ilk değer verme"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 3.10 Bileşik nesnelere ilk değer verme

Kullanıcının bildirdiği kurucu işlevi olmayan, veri elemanları `public` (Kısım 12.3) olan
sade yapılar **bileşik tür** *(aggregate)* sayılır ve küme parantezi içinde eleman eleman
ilk değer alabilir.

```cpp
struct Nokta { int x; int y; };

Nokta n{3, 5};
Nokta n2{3};      // n2.y = 0
```

Yazılmayan elemanlar, **sınıf içi ilk değerleri** *(default member initializer)* (Kısım
12.11) varsa onu, yoksa (referans değillerse, Kısım 8) boş küme parantezinden ilk değer
alır; yerleşik türlerde bu sıfırdır. Sınıf içi ilk değeri olmayan bir referans elemanını
yazmamak sentaks hatasıdır. Bileşik tür olmanın tam koşulları ve C++17/20 ile değişen
kuralları için: **Cilt II, Kısım 16.6.**
