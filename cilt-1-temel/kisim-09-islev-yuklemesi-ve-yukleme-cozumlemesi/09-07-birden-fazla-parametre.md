---
cilt: "I — Temel"
kisim: "9 — İşlev Yüklemesi ve Yükleme Çözümlemesi"
baslik: "9.7 Birden fazla parametre"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 9.7 Birden fazla parametre

Karşılaştırma çağrıdaki her argüman için ayrı ayrı yapılır. Bir işlevin kazanması için
diğer uygun adayların her birine karşı:

- **Hiçbir argümanda o adaydan kötü olmaması**, ve
- **En az bir argümanda o adaydan iyi olması**

gerekir. Diğer bütün uygun adaylara karşı bu iki koşulu sağlayan bir aday yoksa çift
anlamlılık oluşur.

```cpp
void func(int, double);
void func(double, int);

/*
 * biri birinci, diğeri ikinci argümanda iyi
 */
func(1, 2);     // sentaks hatası: çift anlamlılık
```
