---
cilt: "I — Temel"
kisim: "24 — Lambda İfadeleri"
baslik: "24.2 Sözdizimi"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
kutular: ["Standart Notu — C++23"]
---

## 24.2 Sözdizimi

<!-- kod: atla -->
```cpp
[yakalama](parametreler) -> geri_dönüş { gövde }
```

Parametre yoksa parantezler yazılmayabilir; geri dönüş türü yazılmazsa `return`
deyimlerinden çıkarılır (Kısım 4.6). C++20'de geri dönüş türü ya da `mutable` (Kısım 24.4)
yazılacaksa parantezler zorunludur: `[] -> int { return 1; }` sentaks hatasıdır,
`[]() -> int { return 1; }` geçerlidir.

> **Standart Notu — C++23**
> **C++23 öncesi:** Geri dönüş türü ya da `mutable` yazılacaksa parantezler zorunludur.
> **C++23 ile:** Parametre yoksa parantezler bu durumda da yazılmayabilir:
> `[] -> int { return 1; }` geçerlidir.

<!-- kod: atla -->
```cpp
[]{ return 42; }                        // en kısa biçim
[](int x) { return x * 2; }
[](int x) -> double { return x / 2.0; } // açıkça belirtilmiş
```
