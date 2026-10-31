---
cilt: "I — Temel"
kisim: "9 — İşlev Yüklemesi ve Yükleme Çözümlemesi"
baslik: "9.4 Uygun aday listesi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 9.4 Uygun aday listesi

İkinci aşamanın ilk adımı, listedeki her işlev için şu sorunun sorulmasıdır: **"Bu işlev
tek başına olsaydı, bu çağrı geçerli olur muydu?"**

Cevabı hayır olanlar listeden düşer. Kalanlara *uygun adaylar* denir. Uygun aday yoksa
hata mesajı "eşleşen işlev yok" biçimindedir; birden fazla varsa ve aralarında seçim
yapılamazsa "çift anlamlılık" hatası alınır.
