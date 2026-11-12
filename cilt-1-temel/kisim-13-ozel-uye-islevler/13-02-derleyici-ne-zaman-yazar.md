---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.2 Derleyici ne zaman yazar"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 13.2 Derleyici ne zaman yazar

Siz hiçbirini ve başka bir kurucu işlevi bildirmezseniz altısı da örtülü olarak bildirilir
ve derleyici onları gerektiğinde yazar; herhangi bir kurucu işlev (kopyalayan ya da
taşıyan kurucu işlev dahil) bildirdiğinizde varsayılan kurucu işlev örtülü bildirilmez
(Kısım 12.8; tam tablo Cilt II, Kısım 2.2). Bazı durumlarda örtülü bildirilen işlev
silinmiş (Kısım 13.10) sayılır; örneğin referans ya da `const` veri elemanı olan bir
sınıfın kopyalayan atama işlevi.

Derleyicinin yazdığı kopyalama işlevleri, varsa önce taban sınıf kısımlarını (Kısım 17),
sonra her veri elemanını **bildirim sırasına göre** karşılıklı kopyalar. Buna
**üye üye kopyalama** *(memberwise copy)* denir.

Çoğu sınıf için bu davranış doğrudur ve hiçbir şey yazmanız gerekmez. Yetmediği başlıca
durumu Kısım 13.5'te göreceğiz.
