---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.3 Kopyalayan kurucu işlev ne zaman çağrılır"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 13.3 Kopyalayan kurucu işlev ne zaman çağrılır

Üç yerde:

```cpp
void func(Myclass m);          // 1. call-by-value parametre
Myclass bar();                 // 2. sınıf türünden değer döndüren işlevin dönüşü

Myclass a;
Myclass b = a;                 // 3. aynı türden nesneden ilk değer alma
Myclass c{a};                  // aynı şey
```

Üçüncü maddedeki her iki yazım da kopyalayan kurucu işlevi çağırır; aralarında
davranış farkı yoktur.
