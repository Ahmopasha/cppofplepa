---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.6 Big-Three"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 13.6 Big-Three

Yukarıdaki sınıf sonlandırıcı işleve ihtiyaç duyuyordu; çünkü kaynak yönetiyordu. Kaynak
yönetiyorsa kopyalaması da özel olmalıydı. Bu gözlem bir kurala dönüşür:

> **Big-Three:** Sonlandırıcı işlev, kopyalayan kurucu işlev ve kopyalayan atama
> işlevinden **birini** yazmanız gerekiyorsa, muhtemelen **üçünü birden** yazmanız
> gerekiyordur.

Üçünden birini yazmanız, sınıfın derleyicinin varsayabileceğinden daha karmaşık bir şey
yönettiği anlamına gelir. Diğer ikisinin varsayılan hâli de büyük ihtimalle yanlıştır.
