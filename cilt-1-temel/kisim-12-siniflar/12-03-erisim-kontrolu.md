---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.3 Erişim kontrolü"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 12.3 Erişim kontrolü

Üç erişim belirleyicisi vardır: `public`, `private`, `protected`. `private` ve
`protected` öğelere sınıf dışından erişilemez; erişmeye çalışmak sentaks hatasıdır.

`protected`'in `private`'tan farkı yalnızca kalıtımda ortaya çıkar (bkz. Kısım 17).

Sınıf tasarımının temel kuralı şudur: **veri elemanları `private`, arayüz `public`
olmalıdır.** Veri elemanını `public` yaparsanız, sınıfın iç yapısını değiştirdiğinizde
onu kullanan bütün kodu da değiştirmek zorunda kalırsınız.
