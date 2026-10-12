---
cilt: "I — Temel"
kisim: "3 — İlk Değer Verme"
baslik: "3.8 Most vexing parse"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 3.8 Most vexing parse

Varsayılan kurucu işlevle nesne oluştururken **boş normal parantez kullanmayın.**

```cpp
Myclass mx();      // nesne DEĞİL — parametresiz işlev bildirimi
Myclass my{};      // nesne
Myclass mz;        // nesne
```

İlk satır, geriye `Myclass` döndüren `mx` adlı bir işlev bildirimidir. Derleyici
belirsizlikte bildirimden yana karar verir. Bu davranışa *most vexing parse* denir ve
küme parantezi kullanarak tamamen kaçınılır.
