---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.4 Sınıf kapsamı ve isim arama"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 12.4 Sınıf kapsamı ve isim arama

Sınıf bloğu ayrı bir kapsamdır. Bir ismin sınıf kapsamında aranmasını sağlayan üç durum
vardır: `.` operatörü, `->` operatörü ve `::` operatörü.

Üye işlevlerin gövdesinde derleyici Kısım 2.3'teki sırayı uygular:

1. **İsim arama** — isim önce sınıf kapsamında, bulunamazsa dış kapsamlarda aranır
2. **Bağlam denetimi** — bulunan isim o bağlamda kullanılabilir mi
3. **Erişim kontrolü** — erişim hakkı var mı

Sıranın önemi şuradadır: `private` bir öğe isim aramada **bulunur**, erişim kontrolünde
reddedilir. Yani `private` bir isim, dıştaki aynı adlı ismi gölgeler ve hata mesajı
"böyle bir isim yok" değil "bu isme erişemezsiniz" olur.

Üye işlevler, sınıf bloğu içinde `redeclare` edilemez; global işlevlerden farkı budur.
