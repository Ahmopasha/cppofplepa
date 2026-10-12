---
cilt: "II — İleri"
kisim: "11 — Vocabulary Türleri"
baslik: "11.4 `std::optional`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 11.4 `std::optional`

Bir değeri **taşıyabilen veya taşımayabilen** sarmalayıcıdır. C++17 ile geldi.

```cpp
#include <optional>

std::optional<int> ara(const std::string& anahtar);

if (auto sonuc = ara("x")) {
    std::cout << *sonuc;
}
```

Çözdüğü problem, "değer yok" durumunu bildirmenin standart bir yolunun olmamasıdır.
Önceki çözümler ya özel bir değer ayırmak (`-1`, `npos`), ya gösterici döndürmek, ya da
çıkış parametresi kullanmaktı; üçü de niyeti gizler.

```cpp
std::optional<int> o;              // boş
o = 42;                            // değer aldı
o.has_value();                     // true
o.value();                         // değer yoksa std::bad_optional_access gönderir
*o;                                // denetimsiz erişim
o.value_or(0);                     // yoksa varsayılan
o.reset();                         // boşalt
o = std::nullopt;                  // aynı şey
```

Değer nesnenin **içinde** tutulur; dinamik bellek ayrılmaz. `bool` bağlamında
kullanılabilmesi, Kısım 16.1'deki `explicit operator bool` mekanizmasının uygulamasıdır.
