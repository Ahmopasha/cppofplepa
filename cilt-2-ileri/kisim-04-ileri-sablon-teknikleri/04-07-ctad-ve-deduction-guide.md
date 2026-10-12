---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.7 CTAD ve deduction guide"
kaynak: "ders notları"
kutular: ["Standart Notu — C++17"]
son_kontrol: "2026-09 (C++23)"
---

## 4.7 CTAD ve deduction guide

C++17, sınıf şablonlarında kurucu işlev argümanlarından tür çıkarımını mümkün kıldı.
Buna **CTAD** *(class template argument deduction)* denir.

```cpp
std::pair p{1, 2.5};           // std::pair<int, double>
std::vector v{1, 2, 3};        // std::vector<int>
```

Derleyici, kurucu işlevlerden örtülü çıkarım kuralları üretir. Bunlar yetmediğinde
**deduction guide** yazılır:

```cpp
template<typename T>
class Kutu {
    T icerik;
public:
    Kutu(T i) : icerik{i} { }
};

Kutu(const char*) -> Kutu<std::string>;     // deduction guide

Kutu k{"merhaba"};      // Kutu<const char*> değil, Kutu<std::string>
```

Deduction guide sınıfın dışında, sınıfla aynı kapsamda yazılır ve bir bildirimdir; gövdesi
yoktur.

> **Standart Notu — C++17**
> **C++17 öncesi:** Sınıf şablonlarında tür argümanları açıkça yazılmak zorundaydı.
> Bunu aşmak için `std::make_pair` ve `std::make_tuple` gibi yardımcı işlev şablonları
> yazılırdı; işlev şablonlarında çıkarım zaten vardı.
> **C++17 ile:** Kurucu işlev argümanlarından çıkarım yapılabilir. `make_` işlevlerine
> çoğu durumda gerek kalmadı.
> **Neden değişti:** Sınıf ve işlev şablonları arasındaki bu asimetri, dilin en sık
> şikâyet edilen tutarsızlıklarından biriydi.
