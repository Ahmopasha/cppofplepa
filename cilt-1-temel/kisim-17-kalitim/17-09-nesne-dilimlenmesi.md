---
cilt: "I — Temel"
kisim: "17 — Kalıtım"
baslik: "17.9 Nesne dilimlenmesi"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 17.9 Nesne dilimlenmesi

Türemiş sınıf nesnesini taban sınıf türüne **değerle** kopyalarsanız türemiş kısım
kaybolur. Buna *object slicing* denir. Aşağıdaki örnekte `Sekil`, Kısım 17.6'daki soyut
olmayan sınıftır; Kısım 17.8'deki soyut `Sekil` ile `Sekil s = d;` yazımı sentaks hatası
olurdu, çünkü soyut sınıf türünden nesne oluşturulamaz.

```cpp
Daire d;

Sekil s = d;          // dilimlenme: sadece Sekil kısmı kopyalandı
s.ciz();              // Sekil::ciz çağrılır, Daire::ciz değil

const Sekil& r = d;   // dilimlenme YOK
r.ciz();              // Daire::ciz çağrılır
```

Kural buradan çıkar: **çok biçimli davranış istiyorsanız gösterici veya referans
kullanın, değer kullanmayın.** Bu, işlev parametreleri için de geçerlidir; taban sınıf
türünü değerle parametre olarak almayın.
