---
cilt: "I — Temel"
kisim: "21 — Bileşik Nesneler"
baslik: "21.1 has-a ilişkisi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 21.1 has-a ilişkisi

Bir sınıfın, başka bir sınıf türünden veri elemanı barındırmasına **composition** denir.
Kurulan ilişki has-a ilişkisidir (bkz. Kısım 17.1).

```cpp
class Motor { /* ... */ };
class Tekerlek { /* ... */ };

class Araba {
    Motor m;
    Tekerlek t[4];
};
```

Kalıtımla karşılaştırması Kısım 17.1'de verildi; sorulacak soru "B bir A mıdır" idi.
Cevap hayırsa composition kullanılır. Pratikte composition, kalıtımdan **çok daha sık**
ihtiyaç duyulan araçtır.
