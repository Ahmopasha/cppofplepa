---
cilt: "I — Temel"
kisim: "25 — Akıllı Göstericiler"
baslik: "25.4 `std::weak_ptr`"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 25.4 `std::weak_ptr`

İki nesne birbirini `std::shared_ptr` veri elemanlarıyla gösterirse, her birinin sayacı
ötekinin elemanı yüzünden sıfıra düşmez; nesneler kendiliğinden yok edilmez ve bellek
sızar. Buna **döngüsel başvuru** *(reference cycle)* denir.

`std::weak_ptr`, bir nesneyi sahiplenmeden gözlemler; sayacı artırmaz.

<!-- kod-baglam
auto p = std::make_shared<Myclass>();
-->
```cpp
std::weak_ptr<Myclass> w = p;

if (auto s = w.lock()) {     // hâlâ yaşıyorsa shared_ptr verir
    s->func();
}
```

Kullanılacağı yerde `lock()` ile geçici bir `std::shared_ptr`'a çevrilir; nesne yok
olmuşsa boş döner.
