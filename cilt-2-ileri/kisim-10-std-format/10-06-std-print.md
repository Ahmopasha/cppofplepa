---
cilt: "II — İleri"
kisim: "10 — `std::format`"
baslik: "10.6 `std::print`"
kaynak: "ders notları"
kutular: ["Standart Notu — C++23"]
son_kontrol: "2026-10 (C++23)"
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

> **Standart Notu — C++23**
> **C++23 öncesi:** `<print>` yoktur; C++20'de biçimlendirilmiş çıktı
> `std::cout << std::format(...)` ile yazılabilir.
> **C++23 ile:** `std::print` ve `std::println` eklendi; akım alan biçimleri de (Kısım 10.7)
> bunlara dahildir.
