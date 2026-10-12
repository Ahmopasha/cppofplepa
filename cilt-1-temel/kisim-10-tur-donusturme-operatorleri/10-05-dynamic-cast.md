---
cilt: "I — Temel"
kisim: "10 — Tür Dönüştürme Operatörleri"
baslik: "10.5 `dynamic_cast`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 10.5 `dynamic_cast`

Çok biçimli kalıtım hiyerarşilerinde, taban sınıf göstericisinin gerçekte hangi türemiş
sınıfı gösterdiğini **çalışma zamanında denetleyerek** dönüşüm yapar.

```cpp
Sekil* s = /* ... */;
Daire* d = dynamic_cast<Daire*>(s);

if (d) {
    // s gerçekten bir Daire'yi gösteriyordu
}
```

Başarısız olursa göstericilerde `nullptr` döndürür, referanslarda `std::bad_cast`
gönderir. Ayrıntısı ve maliyeti: **Kısım 19 (RTTI).**

Sınıfın en az bir sanal işlevi olmalıdır; yoksa sentaks hatası alırsınız.
