---
cilt: "I — Temel"
kisim: "14 — Operatör Yüklemesi"
baslik: "14.6 Önek ve sonek ayrımı"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
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

Geri dönüş türleri de geleneksel olarak farklıdır ve yerleşik operatörleri, dolayısıyla
Kısım 2.4'teki değer kategorilerini taklit eder: önek biçimi L-Value üretir, bu yüzden
referans döndürür; sonek biçimi PR-Value üretir, bu yüzden değer döndürür. Standart geri
dönüş türünü belirlemez; bu bir gelenektir.

Sonek biçimi eski değerin bir kopyasını döndürmek zorunda olduğu için daha pahalıdır.
Dönüş değerini kullanmıyorsanız önek biçimini tercih edin.
