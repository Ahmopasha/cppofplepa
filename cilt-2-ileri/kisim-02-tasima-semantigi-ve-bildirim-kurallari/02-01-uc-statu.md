---
cilt: "II — İleri"
kisim: "2 — Taşıma Semantiği ve Bildirim Kuralları"
baslik: "2.1 Üç statü"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 2.1 Üç statü

Altı özel üye işlevin her biri, her sınıf için üç statüden **tam olarak birindedir.**

**Not Declared.** İşlev yoktur. Çağırmak sentaks hatası verir, ama hata "silinmiş işlev"
değil "böyle bir işlev yok" biçimindedir. Yükleme çözümlemesine hiç katılmaz.

**Implicitly Declared.** Kullanıcı bildirmemiştir, derleyici durumdan vazife çıkarıp
bildirmiştir. İki alt hâli vardır: *implicitly defaulted* (derleyici gövdesini de yazar)
ve *implicitly deleted* (bildirir ama silinmiş olarak; örneğin bir veri elemanı
kopyalanamıyorsa).

**User Declared.** Kullanıcı bizzat bildirmiştir. Üç alt hâli vardır: *user provided*
(gövdeyi de kullanıcı yazmıştır), *defaulted* (`= default`), *deleted* (`= delete`).

Bu ayrım önemlidir çünkü **Not Declared ile Deleted aynı şey değildir.** Silinmiş işlev
yükleme çözümlemesine katılır ve seçilirse hata verir; bildirilmemiş işlev çözümlemeye
hiç girmez, başka bir yükleme seçilebilir.
