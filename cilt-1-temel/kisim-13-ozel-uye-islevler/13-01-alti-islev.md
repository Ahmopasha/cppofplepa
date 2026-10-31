---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.1 Altı işlev"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 13.1 Altı işlev

Her sınıf için derleyicinin sizin adınıza yazabileceği altı üye işlev vardır:

| İşlev | Ne zaman devreye girer |
|---|---|
| Varsayılan kurucu işlev | Argümansız nesne oluşturulurken |
| Sonlandırıcı işlev | Nesnenin hayatı biterken |
| Kopyalayan kurucu işlev | Aynı türden bir nesneden **hayata gelirken** |
| Kopyalayan atama işlevi | Hayattaki bir nesneye aynı türden atama yapılırken |
| Taşıyan kurucu işlev | Kaynağı devralınacak bir nesneden hayata gelirken |
| Taşıyan atama işlevi | Hayattaki bir nesneye kaynak devralınarak atanırken |

Kurucu ile atama arasındaki ayrım sürekli karıştırılır. Ölçüt tektir: **nesne o anda
hayata mı geliyor, yoksa zaten hayatta mı?**

```cpp
Myclass a;
Myclass b = a;      // b hayata geliyor    → kopyalayan kurucu
Myclass c;
c = a;              // c zaten hayatta     → kopyalayan atama
```
