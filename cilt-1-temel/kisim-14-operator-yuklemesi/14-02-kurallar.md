---
cilt: "I — Temel"
kisim: "14 — Operatör Yüklemesi"
baslik: "14.2 Kurallar"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 14.2 Kurallar

**Yüklenemeyen operatörler** vardır: `.`, `.*`, `::`, `?:`, `sizeof`, `typeid`,
`alignof`, `noexcept`.

**Yeni operatör uyduramazsınız.** `**` diye bir operatör tanımlayamazsınız.

**Önceliği, birleşme yönünü ve operand sayısını değiştiremezsiniz.** `+` operatörü iki
operand alır ve `*`'tan sonra değerlendirilir; yükleme bunu değiştirmez.

**En az bir operand kullanıcı tanımlı tür olmalıdır.** Yerleşik türler için operatör
yükleyemezsiniz.

**Operatör işlevleri ya isim alanı kapsamında (Kısım 16) bir işlev, ya da `static` olmayan bir üye işlev olmalıdır.**
C++20'de tek istisnası, üye olarak yazıldıklarında örtülü olarak `static` olan
`operator new`, `operator delete` ve dizi biçimleri `operator new[]`,
`operator delete[]`'tir (Kısım 15); C++23 ayrıca `operator()` ve `operator[]`'in `static`
olmasına izin verir.

Dördü üye işlev olmak **zorundadır**: `=`, `[]`, `()`, `->`.
