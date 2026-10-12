---
cilt: "I — Temel"
kisim: "20 — `std::string`"
baslik: "20.6 Küçük yazı optimizasyonu"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 20.6 Küçük yazı optimizasyonu

Gerçeklemelerin çoğu, kısa yazıları dinamik bellek ayırmadan doğrudan nesnenin içinde
tutar. Buna *small string optimization* denir.

Pratik sonucu, kısa yazılarla çalışmanın sanıldığından ucuz olmasıdır. Eşiğin kaç karakter
olduğu gerçeklemeye bağlıdır ve tipik olarak 15 civarındadır.

Bu, `std::string`'i işlev parametresi olarak `const` referansla almanın yeterli olduğunu
söyler; daha ileri optimizasyonlara gerek yoktur. Yazıyı yalnızca okuyacaksanız
`std::string_view` kullanmak daha da iyidir: **Cilt II, Kısım 11.**
