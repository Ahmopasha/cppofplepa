---
cilt: "I — Temel"
kisim: "20 — `std::string`"
baslik: "20.5 C arayüzleriyle köprü"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 20.5 C arayüzleriyle köprü

`c_str()` üye işlevi, sonunda boş karakter bulunan bir `const char*` döndürür.

```cpp
std::string dosya{"veri.txt"};
std::FILE* f = std::fopen(dosya.c_str(), "r");
```

Döndürülen gösterici, `std::string` nesnesine aittir. Nesne değiştirildiğinde veya
hayatı bittiğinde gösterici geçersiz olur; saklamayın.

Sayı dönüşümleri için:

```cpp
int x = std::stoi("42");
double d = std::stod("3.14");
std::string s = std::to_string(42);
```
