---
cilt: "II — İleri"
kisim: "12 — İleri Lambda Teknikleri"
baslik: "12.5 Hemen çağrılan lambda"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 12.5 Hemen çağrılan lambda

Bir lambda, tanımlandığı yerde hemen çağrılabilir. İngilizcede *IIFE* denir.

```cpp
const auto ayar = [] {
    if (kosul_a()) return 1;
    if (kosul_b()) return 2;
    return 3;
}();                                  // sondaki () çağırıyor
```

Kullanım amacı, karmaşık mantıkla hesaplanan bir değeri **`const` olarak** tanımlamaktır.
Lambda olmadan ya değişkeni `const` yapamazsınız ya da ayrı bir işlev yazmak zorunda
kalırsınız.
