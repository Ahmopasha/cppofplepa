---
cilt: "II — İleri"
kisim: "10 — `std::format`"
baslik: "10.6 `std::print`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 10.6 `std::print`

C++23, doğrudan yazdırmak için iki işlev ekledi:

```cpp
#include <print>

std::print("{} yaşında\n", 30);
std::println("{} yaşında", 30);      // sonuna satır sonu ekler
```

Ara yazı oluşturulmadığı için `std::cout << std::format(...)` yazımından hızlıdır.
Unicode çıktısını da doğru işler.
