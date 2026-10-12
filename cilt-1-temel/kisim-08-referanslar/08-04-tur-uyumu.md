---
cilt: "I — Temel"
kisim: "8 — Referanslar"
baslik: "8.4 Tür uyumu"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 8.4 Tür uyumu

Referansın türü ile bağlanacak nesnenin türü aynı olmak zorundadır.

```cpp
int ival = 100;

double& dr = ival;         // sentaks hatası
const double& cdr = ival;  // geçerli
```

İkincisinin neden geçerli olduğu 8.3'ten çıkar: derleyici `ival`'den bir `double` geçici
nesnesi üretip referansı ona bağlar. Bu da `const` olmayan referansların neden aynı şeyi
yapamadığını açıklar: `dr = 5.0;` yazsaydınız geçici nesneyi değiştirmiş olurdunuz,
`ival` etkilenmezdi. Dil, sessizce yanlış çalışacak bu koda izin vermez.

Aynı sebeple, `const` bir nesneyi `const` olmayan bir referansa bağlayamazsınız:

```cpp
const int cx = 5;
int& r = cx;         // sentaks hatası — cx'in const'luğu delinirdi
const int& cr = cx;  // geçerli
```
