---
cilt: "II — İleri"
kisim: "16 — Sınıfların ve Operatörlerin İleri Araçları"
baslik: "16.5 Kullanıcı tanımlı literal operatörleri"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 16.5 Kullanıcı tanımlı literal operatörleri

Sayı ve yazı sabitlerine kendi son eklerinizi tanımlayabilirsiniz.

```cpp
constexpr long double operator""_km(long double d) { return d * 1000.0; }

auto mesafe = 2.5_km;      // 2500.0
```

**Son ek alt çizgiyle başlamalıdır.** Alt çizgisiz son ekler standart kütüphaneye
ayrılmıştır; `1s`, `2h`, `"abc"s` gibi kullanımlar oradan gelir.

Şablon olmayan bir literal operatörde parametre listesi yalnızca aşağıdaki biçimlerden biri
olabilir; başkası sentaks hatasıdır ve parametreye varsayılan argüman verilemez. Geri dönüş
türü serbesttir; aşağıda `R` ile gösterildi:

<!-- kod-baglam
using R = int;
-->
```cpp
R operator""_x(unsigned long long);        // tamsayı sabitleri
R operator""_x(long double);               // kayan noktalı sabitler
R operator""_x(const char*);               // ham biçim: tamsayı ve kayan noktalı sabitler
R operator""_x(char);                      // karakter sabitleri
R operator""_x(const char*, std::size_t);  // yazı sabitleri
```

Karakter ve yazı sabitlerinde `char` yerine `wchar_t`, `char8_t` (C++20'den itibaren),
`char16_t` ve `char32_t` de kullanılabilir. Ham biçim sabiti işlenmemiş metin olarak alır;
sayı tabanı dönüşümünü kendiniz yapmak istediğinizde kullanılır.

Standart kütüphanedeki örnekleri `std::chrono` süreleri, `std::string` ve
`std::complex` için tanımlanmıştır. Kendi kodunuzda birim taşıyan değerler için
yararlıdır; ölçü birimi tür sistemine taşınmış olur.
