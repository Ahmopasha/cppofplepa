---
cilt: "II — İleri"
kisim: "16 — Sınıfların ve Operatörlerin İleri Araçları"
baslik: "16.5 Kullanıcı tanımlı literal operatörleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 16.5 Kullanıcı tanımlı literal operatörleri

Sayı ve yazı sabitlerine kendi son eklerinizi tanımlayabilirsiniz.

```cpp
constexpr long double operator""_km(long double d) { return d * 1000.0; }

auto mesafe = 2.5_km;      // 2500.0
```

**Son ek alt çizgiyle başlamalıdır.** Alt çizgisiz son ekler standart kütüphaneye
ayrılmıştır; `1s`, `2h`, `"abc"s` gibi kullanımlar oradan gelir.

Parametre listesi sınırlıdır; yalnızca şu biçimler geçerlidir:

```cpp
operator""_x(unsigned long long);       // tamsayı sabitleri
operator""_x(long double);              // kayan noktalı sabitler
operator""_x(char);                     // karakter sabitleri
operator""_x(const char*, std::size_t); // yazı sabitleri
```

Ham biçim `operator""_x(const char*)` ise sabiti işlenmemiş metin olarak alır; sayı
tabanı dönüşümünü kendiniz yapmak istediğinizde kullanılır.

Standart kütüphanedeki örnekleri `std::chrono` süreleri, `std::string` ve
`std::complex` için tanımlanmıştır. Kendi kodunuzda birim taşıyan değerler için
yararlıdır; ölçü birimi tür sistemine taşınmış olur.
