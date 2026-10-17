---
cilt: "I — Temel"
kisim: "24 — Lambda İfadeleri"
baslik: "24.2 Sözdizimi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 24.2 Sözdizimi

<!-- kod: atla -->
```cpp
[yakalama](parametreler) -> geri_dönüş { gövde }
```

Parametre listesi ve geri dönüş türü isteğe bağlıdır. Geri dönüş türü yazılmazsa
`return` ifadesinden çıkarılır.

<!-- kod: atla -->
```cpp
[]{ return 42; }                        // en kısa biçim
[](int x) { return x * 2; }
[](int x) -> double { return x / 2.0; } // açıkça belirtilmiş
```
