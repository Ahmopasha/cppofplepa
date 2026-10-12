---
cilt: "I — Temel"
kisim: "7 — Varsayılan Argümanlar"
baslik: "7.4 İmzanın parçası değildir"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 7.4 İmzanın parçası değildir

Bunun iki sonucu daha vardır.

Varsayılan argüman **çalışma zamanında değil, çağrı yerinde ve statik türe göre**
seçilir. Sanal işlevlerde bu bir tuzağa dönüşür; geçersiz kılan işlevde farklı varsayılan
argüman vermeyin (bkz. Kısım 17.10).

Ve varsayılan argüman ekleyip çıkarmak işlevin imzasını değiştirmez; yalnızca bildirimi
gören çeviri birimlerini etkiler. Farklı başlıklarda farklı varsayılan argüman
tanımlarsanız, aynı çağrı farklı dosyalarda farklı davranır.
