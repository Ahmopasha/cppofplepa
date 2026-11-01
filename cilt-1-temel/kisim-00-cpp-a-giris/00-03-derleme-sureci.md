---
cilt: "I — Temel"
kisim: "0 — C++'a Giriş"
baslik: "0.3 Derleme süreci"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 0.3 Derleme süreci

Standart, derleme sürecini dokuz **çeviri aşaması** *(phases of translation)* olarak
tanımlar ve gerçeklemelerin bunları birleştirmesine izin verir. Uygulamada bir C++
programı üç adımdan geçer.

**Önişlemci** *(preprocessor)* `#include`, `#define` gibi yönergeleri işler. `#include`,
adı geçen dosyanın içeriğini o satıra kopyalar. Sonuç, tek bir uzun metin gibi
düşünülebilir.

**Derleyici** *(compiler)* bu metni işler ve nesne dosyası *(object file)* üretir. Bir
kaynak dosya, `#include` ile dahil ettiği her şeyle birlikte (`#ifndef` gibi yönergelerle
atlanan satırlar hariç; bkz. Kısım 0.4) bir **çeviri birimi** *(translation unit)*
oluşturur; bu terim kitapta sık geçer.

**Bağlayıcı** *(linker)* nesne dosyalarını ve kütüphaneleri birleştirip çalıştırılabilir
dosyayı üretir. Programın tamamına ilişkin **One Definition Rule** *(ODR)* ihlallerinin
(Kısım 2.7) bir kısmını, örneğin eksik ya da çift tanımı, bu adım bildirebilir; ama
standart, gerçeklemenin bunları bildirmesini istemez ve program yine de hatalıdır.

Bu üç adımın ayrı olması, hata mesajlarını okumanın anahtarıdır. Kullanılan bir işlevin
bildirimi olup tanımı yoksa, bağlayıcı genellikle "tanımlanmamış başvuru"
*(undefined reference)* benzeri bir hata verir. Sentaks hatalarını ise çoğunlukla
derleyici bildirir.
