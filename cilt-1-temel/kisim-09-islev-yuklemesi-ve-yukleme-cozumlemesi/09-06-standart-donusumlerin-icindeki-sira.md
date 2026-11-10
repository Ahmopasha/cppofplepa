---
cilt: "I — Temel"
kisim: "9 — İşlev Yüklemesi ve Yükleme Çözümlemesi"
baslik: "9.6 Standart dönüşümlerin içindeki sıra"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 9.6 Standart dönüşümlerin içindeki sıra

Standart dönüşüm kategorisi kendi içinde üçe ayrılır:

```
tam uyum  >  yükseltme  >  sıradan dönüşüm
```

**Tam uyum** *(exact match)* — dönüşüm gerekmez. Dizinin göstericiye çürümesi (Kısım 4.3),
işlevin işlev göstericisine dönüşmesi ve `const` eklenmesi gibi bazı dönüşümler de tam
uyum sayılır.

**Yükseltme** *(promotion)* — başlıcaları: `int`'ten küçük tamsayı türlerinin (`char`,
`short`, `unsigned char` …) ve `bool`'un `int`'e (değerleri `int`'e sığmıyorsa
`unsigned int`'e) dönüşmesi; kayan noktalı türlerde yalnızca `float` → `double`;
`wchar_t`, `char8_t`, `char16_t`, `char32_t` değerlerini temsil edebilen ilk tamsayı
türüne (`int`, `unsigned int`, `long` …) yükseltilir; kapsamlandırılmamış
numaralandırmalar (Kısım 5) da bir tamsayı türüne yükseltilir: temel türü belirtilmemişse
aynı kuralla, belirtilmişse o türe (ve o türün yükseltildiği türe).

**Sıradan dönüşüm** — tam uyum ya da yükseltme sayılmayan diğer standart dönüşümler: `int`
→ `double`, `double` → `int`, `int` → `bool`, türetilmiş sınıf göstericisinden taban sınıf
göstericisine dönüşüm (Kısım 17).

Pratikte en sık karşılaşılan sürpriz, `0`'ın hem tamsayı hem gösterici bağlamına
uyabilmesidir: `func(int)` ile `func(char*)` varken `func(0)` `int` yüklemesini seçer
(`int` için tam uyum, `char*` için sıradan dönüşüm); `func(long)` ile `func(char*)` varken
çağrı çift anlamlıdır (`int` → `long` de `0` → `char*` de sıradan dönüşümdür). `nullptr`
ile ikisinde de gösterici yüklemesi seçilir (`nullptr`'dan tamsayı türündeki bir
parametreye örtülü dönüşüm yoktur; tek uygun aday odur).
