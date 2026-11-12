---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.18 İçsel türler"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 12.18 İçsel türler

Sınıf bloğu içinde başka bir sınıf, `enum` türü veya tür eş ismi tanımlanabilir. Bunlara
**içsel tür** *(nested type)* ya da tür üyesi (Kısım 12.2) denir.

```cpp
class Liste {
public:
    class Dugum { /* ... */ };      // içsel sınıf
    using boyut_turu = std::size_t;
};

Liste::Dugum d;
```

İçsel tür de erişim kontrolüne tabidir; `private` bölümde tanımlanırsa dışarıdan
kullanılamaz. Standart kütüphane kaplarının `iterator`, `value_type`, `size_type` gibi
isimleri bu mekanizmayla tanımlanmıştır.
