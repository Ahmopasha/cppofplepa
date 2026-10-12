---
cilt: "I — Temel"
kisim: "9 — İşlev Yüklemesi ve Yükleme Çözümlemesi"
baslik: "9.6 Standart dönüşümlerin içindeki sıra"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 9.6 Standart dönüşümlerin içindeki sıra

Standart dönüşüm kategorisi kendi içinde üçe ayrılır:

```
tam uyum  >  yükseltme  >  sıradan dönüşüm
```

**Tam uyum** *(exact match)* — dönüşüm gerekmez. Dizi isminin göstericiye çürümesi,
işlev isminin işlev göstericisine dönüşmesi ve `const` eklenmesi de tam uyum sayılır.

**Yükseltme** *(promotion)* — `char` → `int`, `short` → `int`, `float` → `double`,
`bool` → `int`.

**Sıradan dönüşüm** — geri kalan her şey: `int` → `double`, `double` → `int`,
`int` → `bool`, türetilmiş sınıf göstericisinden taban sınıf göstericisine dönüşüm.

Pratikte en sık karşılaşılan sürpriz, `0`'ın hem tamsayı hem gösterici bağlamına
uyabilmesidir; `nullptr` bu belirsizliği ortadan kaldırmak için eklendi.
