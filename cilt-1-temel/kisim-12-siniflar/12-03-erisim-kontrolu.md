---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.3 Erişim kontrolü"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 12.3 Erişim kontrolü

Üç **erişim belirleyicisi** *(access specifier)* vardır: `public`, `private`, `protected`.
`private` öğelere sınıf dışından erişilemez; erişmeye çalışmak sentaks hatasıdır.
`protected` öğelere de sınıf dışından erişilemez; farkı kalıtımda ortaya çıkar: türemiş
sınıflar `protected` öğelere erişebilir (Kısım 17). İki durumda da istisna, sınıfın
`friend` olarak bildirdiği işlev ve sınıflardır (Kısım 12.16).

Sınıf tasarımının temel kuralı şudur: **veri elemanları `private`, arayüz `public`
olmalıdır.** Veri elemanını `public` yaparsanız, sınıfın iç yapısını değiştirdiğinizde
onu kullanan bütün kodu da değiştirmek zorunda kalırsınız.
