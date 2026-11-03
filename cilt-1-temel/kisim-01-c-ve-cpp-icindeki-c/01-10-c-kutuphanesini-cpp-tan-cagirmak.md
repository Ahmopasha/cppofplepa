---
cilt: "I — Temel"
kisim: "1 — C ve C++ İçindeki C"
baslik: "1.10 C kütüphanesini C++'tan çağırmak"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 1.10 C kütüphanesini C++'tan çağırmak

C ile yazılmış bir kütüphanenin işlevlerini kullanırken bu işlevlerin C++ tarafında C dil
bağlantısıyla bildirilmesi gerekir. Bunun sebebi ve yazımı Kısım 9.9'da (`extern "C"`)
anlatılır.

C başlık dosyalarının C++ karşılıkları da vardır: `<stdio.h>` yerine `<cstdio>`,
`<stdlib.h>` yerine `<cstdlib>`. Bu biçimdeki başlıklar makrolar dışındaki isimleri `std`
isim alanına (bkz. Kısım 16.2) yerleştirir; bu isimlerin küresel kapsamda da bulunup
bulunmayacağı belirtilmemiştir (bkz. Kısım 2.5).
