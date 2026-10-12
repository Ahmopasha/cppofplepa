---
cilt: "I — Temel"
kisim: "25 — Akıllı Göstericiler"
baslik: "25.2 `std::unique_ptr`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 25.2 `std::unique_ptr`

Gösterdiği nesnenin **tek sahibidir.** Kopyalanamaz, taşınabilir.

```cpp
#include <memory>

auto p = std::make_unique<Myclass>(10, 20);

p->func();
(*p).func();

auto q = std::move(p);     // sahiplik q'ya geçti, p artık boş
```

Kopyalanamaz oluşu, Cilt II Kısım 2.2'deki bildirim tablosunun doğrudan sonucudur: taşıyan
işlevleri bildirmek kopyalayan işlevleri siler.

Dizi için ayrı bir sürümü vardır:

```cpp
auto a = std::make_unique<int[]>(100);
a[5] = 42;
```

`make_unique` kullanın, `unique_ptr<Myclass>(new Myclass)` yazmayın. Hem daha kısadır hem
de `new` ile kurucu işlev arasında hata oluşması ihtimalini ortadan kaldırır.
