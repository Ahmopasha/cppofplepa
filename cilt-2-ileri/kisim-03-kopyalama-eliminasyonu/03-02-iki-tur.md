---
cilt: "II — İleri"
kisim: "3 — Kopyalama Eliminasyonu"
baslik: "3.2 İki tür"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 3.2 İki tür

Eliminasyonun iki türü vardır ve aralarındaki fark, C++17'nin getirdiği en önemli
davranış değişikliğidir.

| | Zorunlu | Zorunlu olmayan |
|---|---|---|
| Derleyici yapmak zorunda mı | **Evet** | Hayır |
| Kopyalayan/taşıyan işlev çağrılabilir olmalı mı | **Hayır** | **Evet** |
| Statüsü | Dilin kuralı | Derleyici optimizasyonu |
| Geldiği standart | C++17 | Öncesinden beri |

İkinci satır pratikte en çok fark yaratan yerdir. Zorunlu eliminasyonda ilgili işlevin
`delete` edilmiş veya erişilemez olması sorun değildir; zorunlu olmayan eliminasyonda
işlev **çağrılabilir olmak zorundadır**, elimine edilecek olsa bile.
