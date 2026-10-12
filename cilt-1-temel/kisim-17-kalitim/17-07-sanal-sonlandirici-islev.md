---
cilt: "I — Temel"
kisim: "17 — Kalıtım"
baslik: "17.7 Sanal sonlandırıcı işlev"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 17.7 Sanal sonlandırıcı işlev

Dinamik ömürlü bir nesneyi taban sınıf göstericisi üzerinden siliyorsanız, taban sınıfın
sonlandırıcı işlevi **`virtual` olmak zorundadır.**

```cpp
Sekil* p = new Daire;
delete p;        // Sekil::~Sekil virtual değilse tanımsız davranış
```

Kural: **çok biçimli olarak kullanılacak her taban sınıfın sonlandırıcı işlevi `virtual`
olmalıdır.** Bunu unutmak kaynak sızıntısına yol açan gerçek bir hatadır ve derleyici
sizi uyarmaz.
