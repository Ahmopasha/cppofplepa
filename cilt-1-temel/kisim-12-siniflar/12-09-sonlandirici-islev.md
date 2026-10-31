---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.9 Sonlandırıcı işlev"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 12.9 Sonlandırıcı işlev

Nesnenin hayatını bitiren üye işlevdir. İsmi `~` ile başlar, parametre almaz, geri dönüş
türü yoktur, `static` olamaz ve bir sınıfta yalnızca bir tane bulunabilir.

```cpp
class Myclass {
public:
    ~Myclass();
};
```

Kurucu işlevden farklı olarak `.` operatörüyle **çağrılabilir**, ama bu kötü bir
alışkanlıktır; nesnenin hayatı bittiğinde ikinci kez çağrılır ve tanımsız davranış oluşur.

Sonlandırıcı işlev yazmanız gereken durum, sınıfın bir kaynak yönetmesidir. O durumda
Kısım 13'teki Big-Five kuralı devreye girer.
