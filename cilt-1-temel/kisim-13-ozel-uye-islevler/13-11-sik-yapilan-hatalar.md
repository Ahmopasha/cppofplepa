---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.11 Sık yapılan hatalar"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 13.11 Sık yapılan hatalar

**Kopyalama işlevlerinde bir elemanı atlamak.** Kopyalayan kurucu işlevin ilk değer verme
listesinde atladığınız eleman **ilk değer almamış** olarak kalır. Kopyalayan atama
işlevinde atladığınız eleman ise **eski değerinde** kalır. İkisi de derleyicinin uyarı
vermediği, sessizce yanlış çalışan hatalardır.

**Kendine atamayı düşünmemek.** Kaynak yöneten bir sınıfta kopyalayan atama işlevi, önce
eski kaynağı serbest bırakıp sonra yenisini kopyalıyorsa, `a = a;` durumunda kendi
kaynağını silip ardından silinmiş bellekten kopyalamaya çalışır.

**Taşıyan işlevde kaynağı bırakmamak.** 13.7'de anlatıldı; çift serbest bırakmaya yol
açar.

**Big-Five'ı ezberleyip Rule of Zero'yu atlamak.** Beş işlevi doğru yazabiliyor olmak,
onları yazmanız gerektiği anlamına gelmez.
