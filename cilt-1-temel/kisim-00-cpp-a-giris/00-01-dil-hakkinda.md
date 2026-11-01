---
cilt: "I — Temel"
kisim: "0 — C++'a Giriş"
baslik: "0.1 Dil hakkında"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 0.1 Dil hakkında

C++ çok paradigmalı bir dildir. Yordamsal, nesne yönelimli, jenerik ve işlevsel
programlama tekniklerinin hepsini destekler. Hangisini kullanacağınıza siz karar
verirsiniz; dil bir tanesini dayatmaz.

Tasarımının iki temel ilkesi vardır ve dilin birçok kararını bu ikisi açıklar. Bunlar
standardın güvencesi değil, tasarım hedefleridir:

**Kullanmadığınız şeyin bedelini ödemezsiniz.** Bir özellik, onu kullanmayan koda ek
maliyet getirmemelidir. Örneğin birçok **gerçekleme**
*(implementation; derleyici, ona eşlik eden araçlar ve standart kütüphane)* sanal işlevler
(bkz. Kısım 17.6) için nesneye `vptr` adlı bir gösterici ekler; sanal işlevi olmayan bir
sınıfta buna gerek yoktur.

**Soyutlama bedelsiz olmalıdır.** Bir soyutlama, elle yazacağınız düşük seviyeli koddan
daha verimsiz olmamalıdır. `std::vector<int>` bu ilkenin tipik örneğidir: elemanlarını
elle yönetilen bir dizi gibi bitişik tutar ve onlara sabit zamanda erişir.

Bu iki ilke dilin karmaşıklığının da sebebidir. Kolaylık uğruna performanstan feragat
edilmediği için, kolaylığın maliyeti dilin kendisine yüklenmiştir.
