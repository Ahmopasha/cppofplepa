---
cilt: "I — Temel"
kisim: "3 — İlk Değer Verme"
baslik: "3.3 Value-initialization"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 3.3 Value-initialization

Boş küme parantezi kullanılır. Yerleşik türlerde **her zaman sıfırlama** yapar; ömür
türünden bağımsızdır.

```cpp
int x{};        // 0
double d{};     // 0.0
int* p{};       // nullptr
int a[10]{};    // hepsi 0
```

Bu, 3.2'deki çöp değer sorununu ortadan kaldırır.
