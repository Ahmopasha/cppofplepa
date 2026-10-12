---
cilt: "II — İleri"
kisim: "7 — Concepts"
baslik: "7.8 SFINAE'nin yerini alması"
kaynak: "ders notları"
kutular: ["Standart Notu — C++20"]
son_kontrol: "2026-09 (C++23)"
---

## 7.8 SFINAE'nin yerini alması

Kavramlar, Kısım 4.8'deki `enable_if` kullanımlarının neredeyse tamamını gereksiz kılar.

| İhtiyaç | C++20 öncesi | C++20 |
|---|---|---|
| Türü kısıtlamak | `enable_if_t` ile ek parametre | `requires` cümlesi |
| Yükleme seçmek | Tag dispatching | Kısıt sıralaması |
| Derleme zamanı dallanma | `enable_if` ile ikiz işlev | `if constexpr` (Kısım 5.4) |
| Kısıt ihlalini bildirmek | `static_assert` | Kavramın kendisi |

SFINAE hâlâ dilde vardır ve mevcut kodda karşınıza çıkacaktır; ama yeni kod yazarken
kavram kullanmak için bir sebep aramaya gerek yoktur.

> **Standart Notu — C++20**
> **C++20 öncesi:** Şablon kısıtları, SFINAE'nin yan etkisinden yararlanılarak dolaylı
> yoldan kurulurdu. Kısıt bir dil öğesi değildi; derleyici onu adlandıramaz, hata
> mesajında gösteremezdi.
> **C++20 ile:** Kısıtlar dilin birinci sınıf öğesi oldu. İsimlendirilebilir,
> birleştirilebilir, birbiriyle karşılaştırılabilir ve hata mesajlarında gösterilebilir.
> **Neden değişti:** Şablon kısıtı, dilin başından beri ihtiyaç duyulan ama araç
> sağlanmayan bir kavramdı. SFINAE bir çözüm değil, bir yan etkiden yararlanmaydı.
