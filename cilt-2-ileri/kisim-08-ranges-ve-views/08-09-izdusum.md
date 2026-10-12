---
cilt: "II — İleri"
kisim: "8 — Ranges ve Views"
baslik: "8.9 İzdüşüm"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 8.9 İzdüşüm

Ranges algoritmalarının eski STL'de bulunmayan bir parametresi vardır: **izdüşüm**
*(projection)*. Elemanın hangi parçasına bakılacağını belirler.

```cpp
struct Kisi { std::string ad; int yas; };
std::vector<Kisi> kisiler;

std::ranges::sort(kisiler, {}, &Kisi::yas);       // yaşa göre sırala
```

İkinci parametre karşılaştırıcı (boş bırakıldı, varsayılan `std::ranges::less`),
üçüncüsü izdüşümdür. Veri elemanı göstericisi, üye işlev göstericisi veya herhangi bir
çağrılabilir olabilir.

Eski STL'de aynı iş için lambda yazmak gerekirdi:

```cpp
std::sort(kisiler.begin(), kisiler.end(),
          [](const Kisi& a, const Kisi& b) { return a.yas < b.yas; });
```

İzdüşüm, karşılaştırma mantığını veri seçiminden ayırır; ikisini tek lambdaya sıkıştırmak
zorunda kalmazsınız.
