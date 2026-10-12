---
cilt: "I — Temel"
kisim: "14 — Operatör Yüklemesi"
baslik: "14.6 Önek ve sonek ayrımı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 14.6 Önek ve sonek ayrımı

`++` ve `--` operatörlerinin iki biçimi vardır ve imzaları ayırt edilmelidir. Sonek
biçimi, hiçbir işe yaramayan bir `int` parametre alır; bu parametre yalnızca ayırt etme
amaçlıdır.

```cpp
class Sayac {
public:
    Sayac& operator++();        // önek:  ++x
    Sayac  operator++(int);     // sonek: x++
};
```

Geri dönüş türleri de farklıdır ve bu fark Kısım 2.4'teki değer kategorileriyle
tutarlıdır: önek biçimi L-Value üretir, dolayısıyla referans döndürür; sonek biçimi
PR-Value üretir, dolayısıyla değer döndürür.

Sonek biçimi eski değerin bir kopyasını döndürmek zorunda olduğu için daha pahalıdır.
Dönüş değerini kullanmıyorsanız önek biçimini tercih edin.
