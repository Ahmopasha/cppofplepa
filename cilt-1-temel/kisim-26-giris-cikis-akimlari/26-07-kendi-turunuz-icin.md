---
cilt: "I — Temel"
kisim: "26 — Giriş–Çıkış Akımları"
baslik: "26.7 Kendi türünüz için `<<`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 26.7 Kendi türünüz için `<<`

Kısım 14.5'te anlatıldı; burada tekrarlanmıyor. Özet: global işlev olmak zorundadır,
akımı referansla alır ve referansla döndürür.

```cpp
std::ostream& operator<<(std::ostream& os, const Kesir& k)
{
    return os << k.pay << '/' << k.payda;
}
```

Akım nesnesini `std::ostream&` olarak alın, `std::cout` olarak değil; işleviniz böylece
dosya ve yazı akımlarıyla da çalışır.
