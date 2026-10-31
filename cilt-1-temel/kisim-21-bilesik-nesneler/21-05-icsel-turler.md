---
cilt: "I — Temel"
kisim: "21 — Bileşik Nesneler"
baslik: "21.5 İçsel türler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 21.5 İçsel türler

Sınıf bloğu içinde tanımlanan türler Kısım 12.18'de ele alındı; burada tekrarlanmıyor.

Composition ile birlikte kullanıldıkları tipik durum, bir sınıfın yalnızca kendi
içinde anlamlı olan yardımcı türleri barındırmasıdır:

```cpp
class BagliListe {
    struct Dugum {             // yalnızca BagliListe için anlamlı
        int veri;
        Dugum* sonraki;
    };
    Dugum* bas;
};
```

`Dugum` sınıfı `private` bölümde olduğu için dışarıdan kullanılamaz. Bu, ayrı bir
dosyada global bir `Dugum` sınıfı tanımlamaktan hem daha güvenli hem daha okunaklıdır.
