---
cilt: "I — Temel"
kisim: "8 — Referanslar"
baslik: "8.5 İşlev parametresi olarak referanslar"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 8.5 İşlev parametresi olarak referanslar

Referansların asıl kullanım yeri burasıdır. Parametreyi referans yapmanın iki ayrı sebebi
olabilir ve hangisi için yaptığınızı `const` ile belirtirsiniz.

**Okumak için alıyorsanız `const T&`.** Kopyalama maliyeti doğmaz, çağıran koda kısıtlama
gelmez.

```cpp
void yazdir(const std::string& s);
```

**Değiştirmek için alıyorsanız `T&`.** İşlevin çağıranın nesnesini değiştireceği, imzadan
okunur.

```cpp
void buyut(std::string& s);
```

> **Okuma amaçlı kullanılan referans ve göstericiler `const` olmalı, yazma amaçlı
> kullanılanlar olmamalıdır.** Bu ayrımı tutarlı uygularsanız, işlev imzası tek başına
> ne yaptığını anlatır.

Yerleşik türlerde (`int`, `double`, gösterici) okuma için referans kullanmanın kazancı
yoktur; değerle geçin. Referans, kopyalaması pahalı olan türler içindir.

`call-by-value` ile `call-by-reference` arasında birinin diğerine mutlak üstünlüğü
yoktur; hangisinin doğru olduğu türün kopyalama maliyetine ve işlevin niyetine bağlıdır.
