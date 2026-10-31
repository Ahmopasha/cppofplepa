---
cilt: "I — Temel"
kisim: "1 — C ve C++ İçindeki C"
baslik: "1.10 C kütüphanesini C++'tan çağırmak"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 1.10 C kütüphanesini C++'tan çağırmak

C ile yazılmış bir kütüphanenin işlevlerini kullanırken, bağlayıcının ismi C biçiminde
araması gerekir. Bunun sebebi ve yazımı Kısım 9.9'da (`extern "C"`) anlatıldı.

C başlık dosyalarının C++ karşılıkları da vardır: `<stdio.h>` yerine `<cstdio>`,
`<stdlib.h>` yerine `<cstdlib>`. Bu biçimdeki başlıklar isimleri `std` isim alanına
yerleştirir.
