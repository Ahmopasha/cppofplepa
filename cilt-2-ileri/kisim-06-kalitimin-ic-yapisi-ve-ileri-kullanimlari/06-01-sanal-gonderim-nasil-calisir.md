---
cilt: "II — İleri"
kisim: "6 — Kalıtımın İç Yapısı ve İleri Kullanımları"
baslik: "6.1 Sanal gönderim nasıl çalışır"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 6.1 Sanal gönderim nasıl çalışır

Sanal işlevi olan her sınıf için derleyici bir işlev adresi tablosu üretir; buna yaygın
olarak *vtable* denir. Böyle bir sınıf türünden her nesneye de bu tabloyu gösteren gizli
bir gösterici eklenir; buna *vptr* denir.

Sonuçları:

- Sanal işlevi olan bir sınıfın nesneleri, olmayana göre bir gösterici boyutu kadar daha
  büyüktür.
- Sanal çağrı, doğrudan çağrıdan bir dolaylılık katmanı daha pahalıdır ve `inline`
  edilemez.
- Nesnenin dinamik türü, çalışma zamanında `vptr`'nin hangi tabloyu gösterdiğinden
  okunur.

Bu maliyet çoğu uygulamada önemsizdir. Önem kazandığı yerler için Kısım 6.13'teki
alternatiflere bakın.
