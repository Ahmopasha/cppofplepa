---
cilt: "I — Temel"
kisim: "3 — İlk Değer Verme"
baslik: "3.1 Beş biçim"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 3.1 Beş biçim

C++'ta bir nesneye ilk değer vermenin beş ayrı yazımı vardır. Aralarındaki farklar
çoğu zaman önemsiz görünür ama bazı durumlarda davranış değişir.

```cpp
int x;              // default-initialization
int x{};            // value-initialization
Myclass mx(10);     // direct-initialization
Myclass mx = 10;    // copy-initialization
Myclass mx{10};     // direct-list-initialization
```
