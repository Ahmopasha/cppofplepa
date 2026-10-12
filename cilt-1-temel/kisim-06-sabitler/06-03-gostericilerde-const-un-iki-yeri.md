---
cilt: "I — Temel"
kisim: "6 — Sabitler"
baslik: "6.3 Göstericilerde `const`un iki yeri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 6.3 Göstericilerde `const`un iki yeri

`const` anahtar sözcüğünün gösterici bildirimlerindeki yeri anlamı değiştirir.

```cpp
const int* p1;        // gösterilen nesne const — p1 başkasını gösterebilir
int* const p2 = &x;   // göstericinin kendisi const — *p2 değiştirilebilir
const int* const p3 = &x;   // ikisi de const
```

Okuma kuralı: `const`, kendisinden hemen soldaki şeyi niteler; solunda bir şey yoksa
sağındakini niteler.

Kendisi `const` olan göstericiye ilk değer vermek zorunludur ve sonradan başka bir
nesneye yönlendirilemez; bu yönüyle referansa benzer.
