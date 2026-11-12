---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.11 Sık yapılan hatalar"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 13.11 Sık yapılan hatalar

**Kopyalama işlevlerinde bir elemanı atlamak.** Kopyalayan kurucu işlevin ilk değer verme
listesinde atladığınız eleman kopyalanmaz; Kısım 12.10'daki kurala göre ilk değer alır
(yerleşik türlerde belirsiz değerle kalabilir). Kopyalayan atama işlevinde atladığınız
eleman ise **eski değerinde** kalır. İkisi de geçerli koddur (kopyalayan kurucuda, eleman
Kısım 12.10'daki kurala göre ilk değer alabiliyorsa) ve standart bir tanı istemez; program
sessizce yanlış çalışır. Belirsiz değerli bir `int` elemanı okumak ise tanımsız
davranıştır.

**Kendine atamayı düşünmemek.** Kaynak yöneten bir sınıfta kopyalayan atama işlevi, önce
eski kaynağı serbest bırakıp sonra yenisini kopyalıyorsa, `a = a;` durumunda kendi
kaynağını serbest bırakıp ardından serbest bırakılmış bellekten kopyalamaya çalışır; bu
tanımsız davranıştır.

**Taşıyan işlevde kaynağı devralınmış nesneyi kaynağın sahibi olarak bırakmak.** Kısım
13.7'de anlatıldı; çift serbest bırakmaya yol açar.

**Big-Five'ı ezberleyip Rule of Zero'yu atlamak.** Beş işlevi doğru yazabiliyor olmak,
onları yazmanız gerektiği anlamına gelmez.
