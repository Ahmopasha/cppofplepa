---
cilt: "I — Temel"
kisim: "19 — Çalışma Zamanı Tür Bilgisi"
baslik: "19.2 `dynamic_cast`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 19.2 `dynamic_cast`

Kısım 10.5'te tanıtılmıştı. Taban sınıftan türemiş sınıfa denetimli dönüşüm yapar.

```cpp
Sekil* s = listeden_al();

if (auto* d = dynamic_cast<Daire*>(s)) {
    d->yaricap_ayarla(5.0);       // s gerçekten bir Daire idi
}
```

Göstericilerde başarısızlık `nullptr` ile bildirilir. Referanslarda `nullptr` diye bir
şey olmadığı için `std::bad_cast` gönderilir:

```cpp
try {
    Daire& d = dynamic_cast<Daire&>(sekil_referansi);
}
catch (const std::bad_cast&) {
    // gerçek tür Daire değilmiş
}
```

`static_cast` ile de aynı dönüşümü yazabilirsiniz, ama o denetim yapmaz; tür yanlışsa
tanımsız davranış oluşur. Emin değilseniz `dynamic_cast` kullanın.
