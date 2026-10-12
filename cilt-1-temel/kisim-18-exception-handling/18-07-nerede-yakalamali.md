---
cilt: "I — Temel"
kisim: "18 — Exception Handling"
baslik: "18.7 Nerede yakalamalı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 18.7 Nerede yakalamalı

Hatayı, **müdahale edebileceğiniz** yerde yakalayın. Müdahale edemeyecekseniz
yakalamayın; bırakın üst katmana gitsin.

Yakaladıktan sonra seçenekleriniz şunlardır: sorunu çözüp devam etmek, kullanıcıya
bildirmek, günlüğe yazıp aynı hatayı yeniden göndermek, veya farklı bir hata nesnesine
çevirip göndermek.

```cpp
catch (const std::exception& ex) {
    gunluge_yaz(ex.what());
    throw;                 // aynı nesneyi yeniden gönder
}
```

Parametresiz `throw;` yazımı yalnızca `catch` bloğu içinde geçerlidir ve yakalanan
nesnenin kendisini yeniden gönderir. `throw ex;` yazarsanız kopyalama olur ve dilimlenme
riski doğar.
