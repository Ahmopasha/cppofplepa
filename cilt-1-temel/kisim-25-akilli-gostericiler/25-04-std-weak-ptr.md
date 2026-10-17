---
cilt: "I — Temel"
kisim: "25 — Akıllı Göstericiler"
baslik: "25.4 `std::weak_ptr`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 25.4 `std::weak_ptr`

İki `shared_ptr` birbirini gösterirse sayaçlar hiç sıfıra düşmez ve bellek sızar. Buna
**döngüsel başvuru** denir.

`weak_ptr`, bir nesneyi sahiplenmeden gözlemler; sayacı artırmaz.

<!-- kod-baglam
auto p = std::make_shared<Myclass>();
-->
```cpp
std::weak_ptr<Myclass> w = p;

if (auto s = w.lock()) {     // hâlâ yaşıyorsa shared_ptr verir
    s->func();
}
```

Kullanılacağı yerde `lock()` ile geçici bir `shared_ptr`'a çevrilir; nesne yok olmuşsa
boş döner.
