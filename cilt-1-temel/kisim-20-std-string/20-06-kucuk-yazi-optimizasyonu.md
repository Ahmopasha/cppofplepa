---
cilt: "I — Temel"
kisim: "20 — `std::string`"
baslik: "20.6 Küçük yazı optimizasyonu"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 20.6 Küçük yazı optimizasyonu

Standart, kısa yazıların nesnenin içinde mi yoksa dinamik bellekte mi tutulacağını
belirlemez. Gerçeklemelerin çoğu, kısa yazıları dinamik bellek ayırmadan doğrudan nesnenin
içinde tutar. Buna **küçük yazı optimizasyonu** *(small string optimization)* denir. Bunun
hangi uzunluğa kadar yapıldığı gerçeklemeden gerçeklemeye değişir.

Pratik sonucu, kısa yazılarla çalışmanın sanıldığından ucuz olabilmesidir.

Bir işlev, parametresi olan yazıyı yalnızca okuyacaksa onu `const std::string&` olarak
almak, argüman bir `std::string` olduğunda kopyalamayı önler. `std::string_view` (Cilt II,
Kısım 11.2) çoğu zaman daha da iyidir.
