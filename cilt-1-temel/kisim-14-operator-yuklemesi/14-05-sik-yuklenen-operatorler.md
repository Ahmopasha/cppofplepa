---
cilt: "I — Temel"
kisim: "14 — Operatör Yüklemesi"
baslik: "14.5 Sık yüklenen operatörler"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 14.5 Sık yüklenen operatörler

**Aritmetik operatörler.** Global yazın, `const` referans alın, değer döndürün.

```cpp
Kesir operator+(const Kesir&, const Kesir&);
```

`+=` biçimini üye işlev olarak yazıp `+`'yı ona dayandırmak yaygın bir düzendir; tek
yerde mantık, iki operatör.

**Karşılaştırma operatörleri.** C++20 öncesinde altı karşılaştırma operatörünün her biri
ayrı yazılırdı; `==` ve `<` yazıp diğerlerini bunlar cinsinden tanımlamak yaygındı.
C++20'de `!=` ifadeleri `==` kullanılarak, sıralama ifadeleri de
**üç yollu karşılaştırma operatörü** *(three-way comparison operator)* `<=>` tanımlıysa o
kullanılarak yeniden yazılabilir; operatörü ayrıca yazdıysanız hangisinin kullanılacağına
yükleme çözümlemesi (Kısım 9) karar verir: **Cilt II, Kısım 16.4.**

**İndisleme operatörü.** Üye işlev olmak zorundadır. `const` ve `const` olmayan iki sürüm
yazılır:

<!-- kod-baglam
class Dizi {
public:
@kod@
};
-->
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
