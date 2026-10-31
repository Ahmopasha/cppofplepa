---
cilt: "I — Temel"
kisim: "8 — Referanslar"
baslik: "8.4 Tür uyumu"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++20)"
---

## 8.4 Tür uyumu

Referansın nesneye doğrudan bağlanabilmesi için türler uyumlu olmalıdır: aynı tür ya da
türemiş sınıftan bir nesne için taban sınıf türü (bkz. Kısım 17); her ikisinde de
referansa `const` eklenebilir, bağlanan ifadenin `const` niteliği ise (nesnenin kendisi
`const` olmasa bile) düşürülemez; düşürmek geçici nesne oluşturmaz, sentaks hatasıdır.
Türler uyumluysa referans nesneye doğrudan bağlanır. Türler uyumlu değilse:

```cpp
int ival = 100;

double& dr = ival;         // sentaks hatası
const double& cdr = ival;  // geçerli
```

İkincisinin neden geçerli olduğu 8.3'ten çıkar: derleyici `ival`'den bir `double` geçici
nesnesi üretip referansı ona bağlar. Bu da `const` olmayan referansların neden aynı şeyi
yapamadığını açıklar: `dr = 5.0;` yazsaydınız geçici nesneyi değiştirmiş olurdunuz,
`ival` etkilenmezdi. Dil, sessizce yanlış çalışacak bu koda izin vermez.

Benzer biçimde, `const` bir nesneyi `const` olmayan bir referansa bağlayamazsınız:

```cpp
const int cx = 5;
int& r = cx;         // sentaks hatası — cx'in const'luğu delinirdi
const int& cr = cx;  // geçerli
```
