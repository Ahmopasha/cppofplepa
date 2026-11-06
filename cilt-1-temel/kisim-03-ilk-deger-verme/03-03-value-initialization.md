---
cilt: "I — Temel"
kisim: "3 — İlk Değer Verme"
baslik: "3.3 Value-initialization"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 3.3 Value-initialization

Değişken tanımında boş küme parantezi kullanılır. Yerleşik türlerde
**her zaman sıfırlama** yapar; ömür türünden bağımsızdır.

```cpp
int x{};        // 0
double d{};     // 0.0
int* p{};       // nullptr
int a[10]{};    // hepsi 0
```

Bu, Kısım 3.2'deki çöp değer sorununu ortadan kaldırır. `int()` gibi bir ifadede boş
normal parantez de value-initialization yapar; değişken tanımında ise boş normal parantez
değişken değil işlev bildirir (Kısım 3.8).
