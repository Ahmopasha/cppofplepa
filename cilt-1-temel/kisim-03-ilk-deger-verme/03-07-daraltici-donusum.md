---
cilt: "I — Temel"
kisim: "3 — İlk Değer Verme"
baslik: "3.7 Daraltıcı dönüşüm"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 3.7 Daraltıcı dönüşüm

Küme parantezinin en önemli üstünlüğü budur. **Bilgi kaybına yol açan dönüşümlere izin
vermez.**

```cpp
int a = 3.14;      // derlenir, a = 3 — bilgi sessizce kayboldu
int b{3.14};       // sentaks hatası
int c(3.14);       // derlenir, c = 3

char ch = 1000;    // derlenir, taşma
char ch2{1000};    // sentaks hatası
```

Buna *narrowing conversion* denir. Küme parantezi bu hataları derleme zamanına taşır.
