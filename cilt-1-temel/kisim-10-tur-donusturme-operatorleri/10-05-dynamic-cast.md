---
cilt: "I — Temel"
kisim: "10 — Tür Dönüştürme Operatörleri"
baslik: "10.5 `dynamic_cast`"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 10.5 `dynamic_cast`

Taban sınıfı çok biçimli (Kısım 17.6) olan kalıtım hiyerarşilerinde, taban sınıf
göstericisinin ya da referansının gerçekte hangi türemiş sınıfı gösterdiğini
**çalışma zamanında denetleyerek** dönüşüm yapar.

<!-- kod: atla -->
```cpp
Sekil* s = /* ... */;
Daire* d = dynamic_cast<Daire*>(s);

if (d) {
    // s gerçekten bir Daire'yi gösteriyordu
}
```

Başarısız olursa göstericilerde `nullptr` döndürür, referanslarda `std::bad_cast` gönderir
(Kısım 18). Ayrıntısı ve maliyeti: **Kısım 19 (RTTI).**

Bu denetimli aşağı dönüşüm için taban sınıfın çok biçimli olması, yani en az bir sanal
işlevi bulunması gerekir; yoksa sentaks hatası alırsınız. Türemiş sınıftan taban sınıfa
dönüşümde (Kısım 17.4) bu koşul aranmaz.
