---
cilt: "I — Temel"
kisim: "25 — Akıllı Göstericiler"
baslik: "25.3 `std::shared_ptr`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 25.3 `std::shared_ptr`

Gösterdiği nesnenin **birden fazla sahibi olabilir.** Kaç sahip olduğunu bir sayaçta
tutar; sayaç sıfıra düştüğünde nesne yok edilir.

```cpp
auto p = std::make_shared<Myclass>(10);
auto q = p;                  // iki sahip

std::cout << p.use_count();  // 2
```

Sayaç için ayrı bir **kontrol bloğu** tutulur; bu, `unique_ptr`'a göre hem bellek hem
hız maliyeti getirir. `make_shared` kullanmak, nesneyi ve kontrol bloğunu tek seferde
ayırdığı için bu maliyeti azaltır.
