---
cilt: "I — Temel"
kisim: "11 — `inline`"
baslik: "11.3 Örtülü olarak `inline` olanlar"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 11.3 Örtülü olarak `inline` olanlar

Üç durumda anahtar sözcüğü yazmanıza gerek kalmaz.

**Sınıf bloğu içinde tanımlanan üye işlevler.** Sınıf tanımı zaten başlık dosyasındadır
ve her yere dahil edilir; bu işlevler örtülü olarak `inline`'dır.

```cpp
class Myclass {
public:
    int get() const { return x; }    // örtülü inline
private:
    int x;
};
```

**Derleyicinin yazdığı özel üye işlevler.** Kısım 13'teki altı işlevin derleyici
tarafından üretilen hâlleri `inline`'dır.

**`constexpr` işlevler.** Kısım 6'daki `constexpr` anahtar sözcüğü `inline`'lığı da
kapsar.
