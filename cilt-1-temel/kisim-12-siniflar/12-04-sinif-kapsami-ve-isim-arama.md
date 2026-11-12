---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.4 Sınıf kapsamı ve isim arama"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 12.4 Sınıf kapsamı ve isim arama

Sınıf bloğu ayrı bir kapsamdır. Sınıfın dışından bir ismin sınıf kapsamında aranmasını
sağlayan üç operatör vardır: `.`, `->` ve `::`.

Üye işlevlerin gövdesinde de Kısım 2.3'teki sıra geçerlidir:

1. **İsim arama** — isim önce işlevin kendi kapsamında (yerel değişkenler ve
   parametreler), sonra sınıf kapsamında (taban sınıflar dahil, Kısım 17.5), bulunamazsa
   dış kapsamlarda aranır
2. **Yükleme çözümlemesi** — isim bir işlevse, bulunan adaylar arasından seçim yapılır
   (Kısım 9.3)
3. **Erişim kontrolü** — seçilen öğeye erişim hakkı var mı bakılır

Sıranın önemi şuradadır. Sınıfın kendi üye işlevinde kendi `private` öğelerine erişim
geçerlidir. Türemiş sınıfın üye işlevinde ise taban sınıfın `private` bir öğesi isim
aramada **bulunur** ve dıştaki aynı adlı ismi gölgeler; seçilen öğe (isim bir işlevse
yükleme çözümlemesinin seçtiği öğe) bu `private` öğeyse erişim kontrolünde reddedilir. Bu
durumda dıştaki isim kullanılmaz; hata isim aramadan değil erişim kontrolünden doğar ve
sonuç sentaks hatasıdır.

Üye işlevler yeniden bildirilemez: sınıf bloğu içinde bir kez bildirilir, sınıf dışında
tanımı yazılabilir (Kısım 12.5); global işlevlerden farkı budur.
