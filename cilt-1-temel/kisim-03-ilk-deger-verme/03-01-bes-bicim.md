---
cilt: "I — Temel"
kisim: "3 — İlk Değer Verme"
baslik: "3.1 Beş biçim"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 3.1 Beş biçim

C++'ta bir nesneye ilk değer vermenin beş temel yazımı vardır. Aralarındaki farklar çoğu
zaman önemsiz görünür ama bazı durumlarda davranış değişir.

<!-- kod: atla -->
```cpp
int x;              // default-initialization
int x{};            // value-initialization
Myclass mx(10);     // direct-initialization
Myclass mx = 10;    // copy-initialization
Myclass mx{10};     // direct-list-initialization
```

Eşittir ile küme parantezi birlikte de yazılabilir: `Myclass mx = {10};`. Bu yazıma
*copy-list-initialization* denir. Küme parantezinin kuralları (Kısım 3.7, 3.9) ona da
uygulanır; seçilen kurucu işlev `explicit` ise sentaks hatasıdır (Kısım 3.5).
