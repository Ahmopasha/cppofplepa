---
cilt: "I — Temel"
kisim: "1 — C ve C++ İçindeki C"
baslik: "1.6 İşlev bildirimleri"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 1.6 İşlev bildirimleri

C'de tanım olmayan boş parantezli bir bildirim "parametreleri bilinmiyor" demektir ve dil
böyle bildirilmiş bir işlevin çağrılarında argüman sayısı ile türleri için denetim şart
koşmaz; argümanlar tanımla uyuşmazsa davranış tanımsızdır (bkz. Kısım 2.5). C++'ta
"parametre almıyor" demektir.

<!-- kod: c -->
```cpp
void func();
func(1, 2, 3);     // C'de derlenir, C++'ta sentaks hatası
```

C++'ta **örtülü işlev bildirimi** *(implicit function declaration)* yoktur: bildirimi
bulunamayan bir işlevin çağrılması sentaks hatasıdır. C'de de örtülü bildirim C99 ile
kalkmıştır.
