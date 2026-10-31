---
cilt: "I — Temel"
kisim: "0 — C++'a Giriş"
baslik: "0.1 Dil hakkında"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 0.1 Dil hakkında

C++ çok paradigmalı bir dildir. Yordamsal, nesne yönelimli, jenerik ve işlevsel
programlama tekniklerinin hepsini destekler. Hangisini kullanacağınıza siz karar
verirsiniz; dil bir tanesini dayatmaz.

Tasarımının iki değişmezi vardır ve dilin bütün kararlarını bu ikisi açıklar:

**Kullanmadığınız şeyin bedelini ödemezsiniz.** Bir özellik, onu kullanmayan koda ek
maliyet getirmez. Sanal işlev yazmadığınız sınıfın nesnesinde `vptr` bulunmaz.

**Soyutlama bedelsiz olmalıdır.** Bir soyutlama, elle yazacağınız düşük seviyeli koddan
yavaş olmamalıdır. `std::vector`, elle yönetilen bir dizi kadar hızlıdır.

Bu iki ilke dilin karmaşıklığının da sebebidir. Kolaylık uğruna performanstan feragat
edilmediği için, kolaylığın maliyeti dilin kendisine yüklenmiştir.
