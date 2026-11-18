---
cilt: "I — Temel"
kisim: "20 — `std::string`"
baslik: "20.5 C arayüzleriyle köprü"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 20.5 C arayüzleriyle köprü

`c_str()` üye işlevi, sonunda boş karakter bulunan bir `const char*` döndürür.

```cpp
std::string dosya{"veri.txt"};
std::FILE* f = std::fopen(dosya.c_str(), "r");
```

Döndürülen gösterici, `std::string` nesnesinin kendi belleğini gösterir. Nesnenin ömrü
bittiğinde gösterici geçersiz olur. Nesne üzerinde `const` olmayan üye işlevlerin çoğu
(ör. `append`, `+=`, `clear`) çağrıldığında ya da nesne `std::getline` gibi onu
değiştirebilecek bir işleve verildiğinde de geçersiz hâle gelebilir; saklamayın.

Sayı dönüşümleri için:

```cpp
int x = std::stoi("42");
double d = std::stod("3.14");
std::string s = std::to_string(42);
```
