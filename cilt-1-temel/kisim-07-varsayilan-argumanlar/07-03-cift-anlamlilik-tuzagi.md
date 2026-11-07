---
cilt: "I — Temel"
kisim: "7 — Varsayılan Argümanlar"
baslik: "7.3 Çift anlamlılık tuzağı"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 7.3 Çift anlamlılık tuzağı

Varsayılan argüman, işlev yüklemesiyle (Kısım 9.1) birlikte kullanılınca çift anlamlılığa
yol açabilir:

```cpp
void func(int);
void func(int, int = 10);

func(5);      // sentaks hatası: çift anlamlılık
```

İki bildirimin imzaları (Kısım 9.2) farklıdır, bu yüzden ikisi birden bildirilebilir. Ama
varsayılan argüman ikinci işlevi de tek argümanla çağrılabilir kılar ve ikisinin de ilk
parametresi `int` olduğu için yükleme çözümlemesi (Kısım 9.3) ikisi arasında seçim yapamaz
(Kısım 9.8).
