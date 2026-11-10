---
cilt: "I — Temel"
kisim: "9 — İşlev Yüklemesi ve Yükleme Çözümlemesi"
baslik: "9.4 Uygun aday listesi"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 9.4 Uygun aday listesi

İkinci aşamanın ilk adımı, listedeki her işlev için şu sorunun sorulmasıdır:
**"Argüman sayısı bu işleve uyuyor mu, ve her argüman karşılık gelen parametreye örtülü olarak dönüştürülebiliyor mu?"**
Erişim hakkı bu adımda sorulmaz.

Cevabı hayır olanlar listeden düşer. Kalanlara **uygun aday** *(viable function)* denir.
Uygun aday yoksa ya da birden fazla uygun aday arasında seçim yapılamazsa çağrı sentaks
hatasıdır. İkinci duruma **çift anlamlılık** *(ambiguity)* denir.
