---
cilt: "I — Temel"
kisim: "9 — İşlev Yüklemesi ve Yükleme Çözümlemesi"
baslik: "9.7 Birden fazla parametre"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 9.7 Birden fazla parametre

Her parametre için ayrı ayrı karşılaştırma yapılır. Bir işlevin kazanması için:

- **Hiçbir parametrede diğerinden kötü olmaması**, ve
- **En az bir parametrede diğerinden iyi olması**

gerekir. İkisi de sağlanmıyorsa çift anlamlılık hatası oluşur.

```cpp
void func(int, double);
void func(double, int);

func(1, 2);     // çift anlamlılık: biri birinci, diğeri ikinci parametrede iyi
```
