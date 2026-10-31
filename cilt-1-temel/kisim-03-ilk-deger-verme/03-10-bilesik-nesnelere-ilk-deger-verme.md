---
cilt: "I — Temel"
kisim: "3 — İlk Değer Verme"
baslik: "3.10 Bileşik nesnelere ilk değer verme"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 3.10 Bileşik nesnelere ilk değer verme

Kullanıcı tanımlı kurucu işlevi olmayan, veri elemanları `public` olan sade yapılar
*aggregate* sayılır ve küme parantezi içinde eleman eleman ilk değer alabilir.

```cpp
struct Nokta { int x; int y; };

Nokta n{3, 5};
```

Yazılmayan elemanlar value-initialize edilir. Aggregate olmanın tam koşulları ve
C++17/20 ile değişen kuralları için: **Cilt II, Kısım 16.**
