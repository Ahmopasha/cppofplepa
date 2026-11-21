---
cilt: "I — Temel"
kisim: "25 — Akıllı Göstericiler"
baslik: "25.3 `std::shared_ptr`"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 25.3 `std::shared_ptr`

Gösterdiği nesnenin **birden fazla sahibi olabilir.** Kaç sahip olduğunu bir sayaçta
tutar; sayaç sıfıra düştüğünde nesne yok edilir.

```cpp
auto p = std::make_shared<Myclass>(10);
auto q = p;                  // iki sahip

std::cout << p.use_count();  // 2
```

Standart, sayacın ve benzeri yönetim bilgilerinin nerede tutulacağını belirtmez; bu
bilgilerin tutulduğu yapıya **kontrol bloğu** *(control block)* denir. Sayaç tutmak,
`std::unique_ptr`'da olmayan bir ek iştir. Standart, `std::make_shared`'in nesneyi ve
yönetim bilgilerini tek bir bellek ayırmayla kurmasını önerir; `new` ile oluşturulmuş bir
nesnenin adresinden kurulan `std::shared_ptr` ise ikinci bir ayırma gerektirebilir.
