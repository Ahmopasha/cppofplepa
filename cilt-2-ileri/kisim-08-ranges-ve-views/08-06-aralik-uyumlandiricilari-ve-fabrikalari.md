---
cilt: "II — İleri"
kisim: "8 — Ranges ve Views"
baslik: "8.6 Aralık uyumlandırıcıları ve fabrikaları"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 8.6 Aralık uyumlandırıcıları ve fabrikaları

**Uyumlandırıcı** *(range adaptor)*, bir aralık alıp yeni bir görünüm üreten işlev
nesnesidir. **Fabrika** *(range factory)* ise girdisiz olarak aralık üretir.

Sık kullanılan uyumlandırıcılar:

| Uyumlandırıcı | Ne yapar |
|---|---|
| `views::filter` | Yüklemi sağlayan elemanları geçirir |
| `views::transform` | Her elemana işlev uygular |
| `views::take` | İlk `n` elemanı alır |
| `views::take_while` | Yüklem bozulana kadar alır |
| `views::drop` | İlk `n` elemanı atlar |
| `views::reverse` | Ters sırayla dolaşır |
| `views::join` | İç içe aralıkları düzleştirir |
| `views::split` | Ayırıcıya göre böler |
| `views::keys` / `views::values` | Çiftlerin ilk veya ikinci öğesi |
| `views::elements<N>` | Demetlerin `N`. öğesi |

Fabrikalar:

| Fabrika | Ne üretir |
|---|---|
| `views::iota` | Artan sayı dizisi; ikinci argüman verilmezse sonsuz |
| `views::empty` | Boş aralık |
| `views::single` | Tek elemanlı aralık |
| `views::istream` | Akımdan okunan aralık |

C++23 birkaçını daha ekledi: `views::stride` (belirli aralıklarla atlar), `views::chunk`
(parçalara böler), `views::zip` (birden fazla aralığı eşler), `views::enumerate`
(sıra numarasıyla eşler).
