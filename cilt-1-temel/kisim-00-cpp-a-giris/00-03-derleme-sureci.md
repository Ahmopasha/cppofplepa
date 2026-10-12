---
cilt: "I — Temel"
kisim: "0 — C++'a Giriş"
baslik: "0.3 Derleme süreci"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 0.3 Derleme süreci

Bir C++ programı üç aşamadan geçer.

**Önişlemci** `#include`, `#define` gibi yönergeleri işler. `#include`, adı geçen dosyanın
içeriğini o satıra kopyalar. Çıktısı, tek bir uzun metin dosyasıdır.

**Derleyici** bu metni işler ve nesne dosyası üretir. Önişlemci çıktısına **çeviri
birimi** *(translation unit)* denir; kitapta sık geçen bu terim, bir kaynak dosya ve
onun dahil ettiği her şey demektir.

**Bağlayıcı** nesne dosyalarını ve kütüphaneleri birleştirip çalıştırılabilir dosyayı
üretir. Kısım 2.7'deki ODR ihlallerinin çoğu bu aşamada yakalanır.

Bu üç aşamanın ayrı olması, hata mesajlarını okumanın anahtarıdır. "Tanımlanmamış
başvuru" *(undefined reference)* bağlayıcı hatasıdır; bildirim var ama tanım yok
demektir. Sentaks hataları derleyiciden gelir.
