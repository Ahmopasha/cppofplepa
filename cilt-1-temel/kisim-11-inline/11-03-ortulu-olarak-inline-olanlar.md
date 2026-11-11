---
cilt: "I — Temel"
kisim: "11 — `inline`"
baslik: "11.3 Örtülü olarak `inline` olanlar"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 11.3 Örtülü olarak `inline` olanlar

Bazı durumlarda anahtar sözcüğü yazmanıza gerek kalmaz; başlıcaları şunlardır.

**Sınıf bloğu içinde tanımlanan üye işlevler.** Sınıflar Kısım 12'de anlatılır. Sınıf
tanımı genellikle başlık dosyasında durur ve her yere dahil edilir; sınıf bloğu içinde
tanımlanan üye işlevler örtülü olarak `inline`'dır (adlandırılmış bir modüle bağlı
sınıflar dışında).

```cpp
class Myclass {
public:
    int get() const { return x; }    // örtülü inline
private:
    int x;
};
```

**Derleyicinin yazdığı özel üye işlevler.** Kısım 13'teki altı işlevin örtülü olarak
bildirilen hâlleri `inline`'dır.

**`constexpr` ve `consteval` işlevler.** Kısım 6.6'daki bu belirteçlerle bildirilen
işlevler örtülü olarak `inline`'dır.
