---
cilt: "II — İleri"
kisim: "16 — Sınıfların ve Operatörlerin İleri Araçları"
baslik: "16.1 Tür dönüştürme operatör işlevleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 16.1 Tür dönüştürme operatör işlevleri

Cilt I Kısım 12.13'te, dönüştüren kurucu işlevin **başka türden sizin türünüze** dönüşüm
sağladığını görmüştük. Ters yön, yani **sizin türünüzden başka türe** dönüşüm, tür
dönüştürme operatör işleviyle sağlanır.

```cpp
class Kesir {
    int pay, payda;
public:
    operator double() const { return static_cast<double>(pay) / payda; }
};

Kesir k{1, 2};
double d = k;          // 0.5
```

Yazımın üç özelliği vardır: geri dönüş türü **yazılmaz** (isimden anlaşılır), parametre
almaz, ve `static` olamaz. Neredeyse her zaman `const` olmalıdır.

Bu işlevler örtülü dönüşüm zinciri oluşturur ve beklenmedik yerlerde devreye girer:

```cpp
if (k) { }             // double'a dönüşür, sonra bool'a
k + 1;                 // double aritmetiği
```

> **Tür dönüştürme operatör işlevlerini `explicit` yapın.** Dönüştüren kurucu işlevler
> için verilen tavsiyenin (Cilt I 12.13) aynısı; sebep de aynı.

<!-- kod: atla -->
```cpp
explicit operator double() const;

double d = k;                          // sentaks hatası
double d = static_cast<double>(k);     // açık çağrı
```

`explicit operator bool()` özel bir durumdur: `if`, `while` ve mantık operatörlerinin
koşul konumunda **açık çağrı olmadan** devreye girer. Buna *bağlamsal dönüşüm*
*(contextual conversion)* denir. Akıllı göstericiler ve akım sınıfları bu mekanizmayı
kullanır; `if (p)` ve `while (std::cin >> x)` böyle çalışır.
