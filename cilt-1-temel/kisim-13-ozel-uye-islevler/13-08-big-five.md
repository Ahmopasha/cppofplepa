---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.8 Big-Five"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 13.8 Big-Five

Taşıma işlevleriyle birlikte kural beşe çıkar:

> **Big-Five:** Sonlandırıcı işlev, kopyalayan kurucu, kopyalayan atama, taşıyan kurucu
> ve taşıyan atama işlevlerinden **birini** yazmanız gerekiyorsa, **beşini birden**
> yazmanız gerekiyordur.

Bunun teknik bir sebebi de vardır: bu işlevlerden birini bildirmek, diğerlerinin bir
kısmının derleyici tarafından yazılmasını engeller. Hangi bildirimin neyi engellediği
Cilt II, Kısım 2.2'deki tabloda.
