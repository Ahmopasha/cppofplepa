---
cilt: "I — Temel"
kisim: "1 — C ve C++ İçindeki C"
baslik: "1.6 İşlev bildirimleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 1.6 İşlev bildirimleri

C'de boş parantezli bildirim "parametreleri belirtilmemiş" demektir ve her türlü çağrıya
izin verir. C++'ta "parametre almıyor" demektir.

<!-- kod: c -->
```cpp
void func();
func(1, 2, 3);     // C'de geçerli, C++'ta sentaks hatası
```

C++'ta her işlevin çağrıdan önce bildirilmiş olması zorunludur; C'de örtülü bildirim
mümkündür (C99'a kadar).
