---
cilt: "II — İleri"
kisim: "10 — `std::format`"
baslik: "10.1 Çözdüğü problem"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 10.1 Çözdüğü problem

Cilt I Kısım 26.8'de, akım mekanizmasının ayrıntılı olduğu ve manipülatörlerin kalıcı
olmasının hata kaynağı olduğu söylenmişti. C++ biçimlendirme için iki mirasa sahiptir ve
ikisinin de kendine göre sorunları vardır.

**C'den gelen `printf` ailesi.** Kısa ve okunaklıdır, ama **tür güvenli değildir.**
Biçim dizgisiyle argümanlar arasındaki uyum derleyici tarafından denetlenmez; uyumsuzluk
tanımsız davranıştır. Kullanıcı tanımlı türlerle de çalışmaz.

```cpp
std::printf("%d\n", 3.14);      // tanımsız davranış, derleyici uyarabilir ama zorunda değil
```

**Akımlar.** Tür güvenlidir ve genişletilebilir, ama ayrıntılıdır ve biçimlendirme
durumu kalıcıdır.

```cpp
std::cout << std::setw(10) << std::fixed << std::setprecision(2) << x << '\n';
```

C++20'nin `std::format` kütüphanesi ikisinin üstünlüklerini birleştirir: `printf`
kadar kısa, akımlar kadar tür güvenli ve genişletilebilir.

<!-- kod-baglam
double x = 3.14159;
-->
```cpp
#include <format>

std::cout << std::format("{:10.2f}\n", x);
```
