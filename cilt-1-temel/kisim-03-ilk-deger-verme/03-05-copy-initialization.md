---
cilt: "I — Temel"
kisim: "3 — İlk Değer Verme"
baslik: "3.5 Copy-initialization"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 3.5 Copy-initialization

Eşittir işaretiyle yazılır. İsmi yanıltıcıdır: ortada mutlaka bir kopyalama olmaz.

```cpp
Myclass mx = 10;
```

Direct-initialization'dan tek farkı önemlidir: **`explicit` kurucu işlevler bu yazımda
devreye giremez.** Kurucu işlev `explicit` ise bu satır sentaks hatası verir
(bkz. Kısım 12.13).

Bu yüzden `explicit` olmayan tek parametreli kurucu işlevlerin yol açtığı istenmeyen
dönüşümler tipik olarak bu yazımda ortaya çıkar.
