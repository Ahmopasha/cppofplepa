---
cilt: "II — İleri"
kisim: "6 — Kalıtımın İç Yapısı ve İleri Kullanımları"
baslik: "6.2 Sanal gönderimin devreye girmediği yerler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 6.2 Sanal gönderimin devreye girmediği yerler

Sanal işlev bildirmek, her çağrının dinamik olacağı anlamına gelmez.

**Nesnenin kendisi üzerinden yapılan çağrılarda.** Dinamik tür ile statik tür aynıysa
dolaylılığa gerek yoktur; derleyici doğrudan çağrı üretir.

**Nitelenmiş çağrılarda.** `p->Base::f()` yazdığınızda sanal gönderim baypas edilir.

**Kurucu ve sonlandırıcı işlevlerin içinde.** Cilt I, Kısım 17.10'daki kuralın sebebi
budur: `vptr`, kurucu işlevlerin çalışma sırasına göre kademeli olarak kurulur. Taban
sınıfın kurucu işlevi çalışırken `vptr` henüz taban sınıfın tablosunu gösterir, çünkü
türemiş kısım daha hayata gelmemiştir. Sonlandırma sırasında da simetrik olarak, türemiş
kısım yıkıldıktan sonra `vptr` geri alınır.

**Değerle geçildiğinde.** Dilimlenme olduğu için ortada zaten türemiş nesne kalmaz.
