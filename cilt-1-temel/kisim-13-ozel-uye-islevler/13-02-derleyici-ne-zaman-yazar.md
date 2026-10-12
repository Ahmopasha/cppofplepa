---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.2 Derleyici ne zaman yazar"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 13.2 Derleyici ne zaman yazar

Siz hiçbir şey yazmazsanız derleyici altısını da yazar. Yazdığı kopyalama işlevleri,
sınıfın her veri elemanını **bildirim sırasına göre** karşılıklı kopyalar. Buna üye üye
kopyalama denir.

Çoğu sınıf için bu davranış doğrudur ve hiçbir şey yazmanız gerekmez. Yetmediği tek bir
durum vardır ve o durumu 13.5'te göreceğiz.
