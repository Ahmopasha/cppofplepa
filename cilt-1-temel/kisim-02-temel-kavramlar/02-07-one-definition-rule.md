---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.7 One Definition Rule"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 2.7 One Definition Rule

Kısaca **ODR** denir ve iki kuraldan oluşur.

**Birincisi:** Bir çeviri biriminde, herhangi bir değişken, işlev, sınıf veya şablonun
**en fazla bir** tanımı bulunabilir.

**İkincisi:** Bütün programda, kullanılan her `inline` olmayan işlev ve değişkenin
**tam olarak bir** tanımı bulunmalıdır (yalnızca `sizeof` içinde geçmek gibi bazı
kullanımlar bu sayıya girmez). Az ya da çok olursa program hatalıdır; standart,
gerçeklemenin bunu bildirmesini istemez; bağlama adımı bir kısmını bildirebilir (Kısım
0.3).

Sınıflar, numaralandırmalar, `inline` işlevler (`constexpr` işlevler de örtük olarak
`inline`'dır), C++17'den itibaren `inline` değişkenler ve şablonlar ise bu kurala bağlı
değildir: birden fazla çeviri biriminde tanımlanabilirler (adlandırılmış bir modüle bağlı
tanımlar bunun dışındadır). Karşılığında bir koşul gelir —
**bütün tanımlar birbirinin aynısı olmak zorundadır.** Aynı olmazlarsa program hatalıdır,
ama standart bunun bildirilmesini istemez; program sessizce yanlış çalışabilir.

Bu yüzden sınıf tanımları başlık dosyasına konur ve o başlık her yerde aynı şekilde
dahil edilir. `inline` anahtar sözcüğünün ODR ile ilişkisi Kısım 11'de.
