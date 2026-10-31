---
cilt: "I — Temel"
kisim: "7 — Varsayılan Argümanlar"
baslik: "7.3 Çift anlamlılık tuzağı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 7.3 Çift anlamlılık tuzağı

Varsayılan argüman işlev yüklemesini tetikler ve çift anlamlılığa yol açabilir:

```cpp
void func(int);
void func(int, int = 10);

func(5);      // çift anlamlılık hatası
```

Varsayılan argümanlar imzanın parçası olmadığı için iki işlev de tek argümanla
çağrılabilir hâle gelir (bkz. Kısım 9.8).
