---
cilt: "I — Temel"
kisim: "19 — Çalışma Zamanı Tür Bilgisi"
baslik: "19.1 Ne işe yarar"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 19.1 Ne işe yarar

Çok biçimli bir hiyerarşide elinizde taban sınıf göstericisi vardır ve ardındaki gerçek
türü bilmezsiniz. Çoğu zaman bilmenize gerek de yoktur; sanal işlevler işi halleder.

Bazen gerekir. **RTTI** *(run-time type information)*, nesnenin dinamik türünü çalışma
zamanında sorgulamanın yoludur ve iki aracı vardır: `dynamic_cast` ve `typeid`.

Her ikisi de sınıfın **çok biçimli** olmasını gerektirir; yani en az bir sanal işlevi
bulunmalıdır. Nesnenin dinamik türü, Cilt II Kısım 6.1'de anlatılan `vptr` üzerinden
okunur.
