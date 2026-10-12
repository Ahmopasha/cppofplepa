---
cilt: "I — Temel"
kisim: "10 — Tür Dönüştürme Operatörleri"
baslik: "10.4 `reinterpret_cast`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 10.4 `reinterpret_cast`

Birbiriyle ilgisiz gösterici türleri arasında dönüşüm yapar. Bit örüntüsüne dokunmaz,
yalnızca derleyiciye "buraya şu türden bakacağım" der.

```cpp
int x = 65;
char* p = reinterpret_cast<char*>(&x);
```

Taşınabilir değildir ve çoğu kullanımı tanımsız davranışa yakındır. Donanım kaydı
erişimi, seri hâle getirme ve benzeri düşük seviyeli işler dışında gerekmez.
