---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.3 Tam özelleştirme"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 4.3 Tam özelleştirme

Belirli bir tür için şablonun tamamen farklı bir sürümünü yazmaktır.

```cpp
template<typename T>
class Kutu {
public:
    void yaz() { std::cout << "genel\n"; }
};

template<>                      // tam özelleştirme
class Kutu<bool> {
public:
    void yaz() { std::cout << "bool için özel\n"; }
};
```

`template<>` yazımındaki boş açılı parantez, "hiçbir parametre açıkta kalmadı" demektir.

İşlev şablonları da tam özelleştirilebilir, ama **yapılmamalıdır.** İşlev
özelleştirmeleri yükleme çözümlemesine normal işlevler gibi katılmaz; önce hangi şablonun
seçileceğine karar verilir, sonra o şablonun özelleştirmesi aranır. Sonuç, sezgiye aykırı
seçimler olur.

> İşlev şablonlarında özelleştirme yerine **yükleme** kullanın. Normal bir işlev yazmak,
> özelleştirme yazmaktan hem daha basit hem daha öngörülebilirdir.
