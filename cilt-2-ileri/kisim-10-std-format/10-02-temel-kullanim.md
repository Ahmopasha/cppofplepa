---
cilt: "II — İleri"
kisim: "10 — `std::format`"
baslik: "10.2 Temel kullanım"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 10.2 Temel kullanım

`std::format`, bir yazı döndürür; yazdırmaz.

```cpp
std::string s = std::format("{} yaşında {}", 30, "Ahmet");
```

Yer tutucular `{}` ile yazılır ve sırayla argümanlara karşılık gelir. Sırayı
değiştirmek için indis verilir:

```cpp
std::format("{1} {0}", "dünya", "merhaba");      // "merhaba dünya"
```

Süslü parantezin kendisini yazdırmak için ikilenir:

```cpp
std::format("{{}}");      // "{}"
```

**Biçim dizgisi derleme zamanında denetlenir.** Argüman sayısı veya türü uymuyorsa
sentaks hatası alırsınız; bu, `printf`'e göre en belirgin kazançtır.

```cpp
std::format("{} {}", 1);          // sentaks hatası — argüman eksik
std::format("{:d}", "yazi");      // sentaks hatası — tür uyumsuz
```

Denetim, biçim dizgisinin `consteval` bir sarmalayıcıdan geçirilmesiyle yapılır
(bkz. Kısım 18.3). Çalışma zamanında belirlenen bir biçim dizgisi kullanmanız gerekiyorsa
`std::vformat` çağrılır; orada denetim yoktur ve hata `std::format_error` olarak gelir.
