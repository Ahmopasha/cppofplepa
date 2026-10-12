---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.7 One Definition Rule"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 2.7 One Definition Rule

Kısaca **ODR** denir ve iki kuraldan oluşur.

**Birincisi:** Bir çeviri biriminde, herhangi bir değişken, işlev, sınıf veya şablonun
**en fazla bir** tanımı bulunabilir.

**İkincisi:** Bütün programda, kullanılan her `inline` olmayan işlev ve değişkenin
**tam olarak bir** tanımı bulunmalıdır. Az olursa bağlayıcı hatası alırsınız, çok olursa
yine bağlayıcı hatası alırsınız.

Sınıflar, `inline` işlevler ve şablonlar bu ikinci kuralın istisnasıdır: birden fazla
çeviri biriminde tanımlanabilirler. Karşılığında bir koşul gelir — **bütün tanımlar
birbirinin aynısı olmak zorundadır.** Aynı olmazlarsa derleyici de bağlayıcı da uyarı
vermez; program sessizce yanlış çalışır.

Bu yüzden sınıf tanımları başlık dosyasına konur ve o başlık her yerde aynı şekilde
dahil edilir. `inline` anahtar sözcüğünün ODR ile ilişkisi Kısım 11'de.
