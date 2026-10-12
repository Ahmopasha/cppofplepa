---
cilt: "II — İleri"
kisim: "5 — Derleme Zamanı Araçları"
baslik: "5.1 Meta işlev kavramı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 5.1 Meta işlev kavramı

Sıradan bir işlev değer alır, değer döndürür. **Meta işlev** tür alır, tür veya değer
döndürür. Çalıştığı yer çalışma zamanı değil, derleme zamanıdır.

C++'ta meta işlev diye ayrı bir dil öğesi yoktur; sınıf şablonları bu amaçla kullanılır.
Sonuç, sınıfın bir üyesi olarak sunulur.

```cpp
template<typename T>
struct KaldirConst { using type = T; };

template<typename T>
struct KaldirConst<const T> { using type = T; };     // kısmi özelleştirme

KaldirConst<const int>::type x;      // int
```

Bütün mekanizma 4.4'teki kısmi özelleştirmeye dayanır: derleyici, türe uyan
özelleştirmeyi seçer ve o özelleştirmedeki `type` okunur.

Tür döndüren meta işlevlerde sonuç `type`, değer döndürenlerde `value` adıyla sunulur.
Bu bir dil kuralı değil, standart kütüphanenin yerleştirdiği bir sözleşmedir.
