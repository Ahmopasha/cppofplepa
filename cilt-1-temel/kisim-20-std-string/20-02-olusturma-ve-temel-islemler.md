---
cilt: "I — Temel"
kisim: "20 — `std::string`"
baslik: "20.2 Oluşturma ve temel işlemler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 20.2 Oluşturma ve temel işlemler

```cpp
#include <string>

std::string s1;                       // boş
std::string s2{"merhaba"};
std::string s3(5, 'x');               // "xxxxx"
std::string s4{s2};                   // kopya
std::string s5{s2, 2, 3};             // s2'nin 2. indisinden 3 karakter

s2.size();        // uzunluk — length() ile aynı
s2.empty();       // boş mu
s2.clear();       // boşalt
```

Eleman erişiminin iki yolu vardır ve aradaki fark önemlidir:

```cpp
s2[0];        // denetim yok — geçersiz indis tanımsız davranış
s2.at(0);     // denetimli — geçersiz indis std::out_of_range gönderir
```

Birleştirme `+` ve `+=` ile yapılır; karşılaştırma operatörleri beklendiği gibi çalışır.
