---
cilt: "I — Temel"
kisim: "18 — Exception Handling"
baslik: "18.7 Nerede yakalamalı"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 18.7 Nerede yakalamalı

Hatayı, **müdahale edebileceğiniz** yerde yakalayın. Müdahale edemeyecekseniz
yakalamayın; bırakın üst katmana gitsin.

Yakaladıktan sonra seçenekleriniz şunlardır: sorunu çözüp devam etmek, kullanıcıya
bildirmek, günlüğe yazıp aynı hatayı yeniden göndermek, veya farklı bir hata nesnesine
çevirip göndermek.

<!-- kod-baglam
void gunluge_yaz(const char*);
void f()
{
    try { }
@kod@
}
-->
```cpp
catch (const std::exception& ex) {
    gunluge_yaz(ex.what());
    throw;                 // aynı nesneyi yeniden gönder
}
```

Tek başına `throw;` yazımı, o an yakalanmış ve işlenmekte olan hatayı yeniden gönderir;
yeni bir nesne oluşturulmaz. Genellikle `catch` bloğunun içinde yazılır, ama oradan
çağrılan bir işlevde de kullanılabilir. İşlenmekte olan bir hata yokken çalışırsa
`std::terminate` çağrılır. `throw ex;` yazarsanız kopyalama olur ve dilimlenme riski
doğar.
