---
cilt: "I — Temel"
kisim: "3 — İlk Değer Verme"
baslik: "3.5 Copy-initialization"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 3.5 Copy-initialization

Eşittir işaretiyle yazılır. İsmi yanıltıcıdır: ortada mutlaka bir kopyalama olmaz.

```cpp
Myclass mx = 10;
```

Aynı ilk değer verme eşittir yazılmadan da olur: bir işleve argüman geçirmek ve bir
işlevden değer döndürmek de copy-initialization'dır.

Direct-initialization'dan en önemli farkı şudur:
**`explicit` kurucu işlevler bu yazımda devreye giremez.** Kurucu işlev `explicit` ise bu
satır sentaks hatası verir (Kısım 12.13).

Bu yüzden `explicit` olmayan tek parametreli kurucu işlevlerin yol açtığı istenmeyen
dönüşümler tipik olarak bu yazımda, özellikle argüman geçirirken ortaya çıkar.
