---
cilt: "I — Temel"
kisim: "3 — İlk Değer Verme"
baslik: "3.8 Most vexing parse"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 3.8 Most vexing parse

Varsayılan kurucu işlevle değişken tanımlarken **boş normal parantez kullanmayın.**

```cpp
Myclass mx();      // nesne DEĞİL — parametresiz işlev bildirimi
Myclass my{};      // nesne
Myclass mz;        // nesne
```

Değişken tanımında boş normal parantez bir ilk değer verme ifadesi sayılmaz; bu yüzden ilk
satır, geriye `Myclass` döndüren `mx` adlı bir işlevin bildirimidir.

Ayrıca standardın şu kuralı vardır: bir yazım hem bildirim hem ifade olarak
okunabiliyorsa, standart onu bildirim sayar. Bu kuralın en bilinen tuzağına
**en can sıkıcı ayrıştırma** *(most vexing parse)* denir:

```cpp
struct Diger { };
struct Kutu { Kutu(Diger); };

Kutu mx(Diger());   // nesne DEĞİL — işlev bildirimi
Kutu my{Diger()};   // nesne
```

Buradaki `Diger()` geçici bir nesne olarak değil, bir parametre türü olarak okunur: `mx`
bir işlev bildirimidir. Küme parantezi iki tuzaktan da korur.
