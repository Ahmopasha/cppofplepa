---
cilt: "I — Temel"
kisim: "9 — İşlev Yüklemesi ve Yükleme Çözümlemesi"
baslik: "9.8 Varsayılan argümanlar ve çift anlamlılık"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 9.8 Varsayılan argümanlar ve çift anlamlılık

Varsayılan argüman kullanımı yüklemeyi tetikler ama çift anlamlılığa da yol açabilir:

```cpp
void func(int);
void func(int, int = 10);

func(5);        // çift anlamlılık
```

Varsayılan argümanlar imzanın parçası olmadığı için iki işlev de tek argümanla
çağrılabilir hâle gelir ve aralarında seçim yapılamaz.
