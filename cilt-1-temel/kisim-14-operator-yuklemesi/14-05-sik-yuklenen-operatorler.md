---
cilt: "I — Temel"
kisim: "14 — Operatör Yüklemesi"
baslik: "14.5 Sık yüklenen operatörler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 14.5 Sık yüklenen operatörler

**Aritmetik operatörler.** Global yazın, `const` referans alın, değer döndürün.

```cpp
Kesir operator+(const Kesir&, const Kesir&);
```

`+=` biçimini üye işlev olarak yazıp `+`'yı ona dayandırmak yaygın bir düzendir; tek
yerde mantık, iki operatör.

**Karşılaştırma operatörleri.** `==` ve `<` yazmak çoğu zaman yeterlidir; diğerleri
bunlardan türetilir. C++20'nin üç yollu karşılaştırma operatörü bu tekrarı tamamen
ortadan kaldırır: **Cilt II, Kısım 16.**

**İndisleme operatörü.** Üye işlev olmak zorundadır. `const` ve `const` olmayan iki sürüm
yazılır:

```cpp
int&       operator[](std::size_t i);
const int& operator[](std::size_t i) const;
```

**Akım operatörleri.** Global olmak zorundadır. Akımı referansla alır ve referansla
döndürür; zincirleme kullanım bu sayede çalışır.

```cpp
std::ostream& operator<<(std::ostream& os, const Kesir& k)
{
    return os << k.pay << '/' << k.payda;
}
```
