---
cilt: "I — Temel"
kisim: "9 — İşlev Yüklemesi ve Yükleme Çözümlemesi"
baslik: "9.1 Ne zaman yükleme vardır"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 9.1 Ne zaman yükleme vardır

**Aynı kapsamda**, aynı isimli, farklı imzalara sahip birden fazla işlev bildirilmesine
işlev yüklemesi *(function overloading)* denir.

```cpp
void func(int);
void func(double);
void func(int, int);
```

"Aynı kapsam" koşulu vurgulanmalıdır. Farklı kapsamlardaki aynı isimli işlevler
birbirinin yüklemesi **değildir**; Kısım 2.3'teki isim arama kuralı gereği dıştaki isim
gölgelenir. Aynı durum kalıtımda da geçerlidir (bkz. Kısım 17.5).
