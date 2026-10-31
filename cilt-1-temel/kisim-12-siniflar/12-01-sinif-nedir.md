---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.1 Sınıf nedir"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 12.1 Sınıf nedir

Sınıf, veriyi ve o veri üzerinde çalışan işlevleri tek bir tür altında toplamanın yoludur.
Kullanıcı tanımlı bir tür oluşturursunuz ve o türden nesneler, yerleşik türlerden
nesneler gibi kullanılır.

`class` ve `struct` anahtar sözcüklerinin tek farkı **varsayılan erişim belirleyicisidir:**

```cpp
class  A { int x; };    // x private
struct B { int x; };    // x public
```

Bunun dışında hiçbir farkları yoktur. Kalıtımda da aynı ayrım geçerlidir (bkz. 17.2).
