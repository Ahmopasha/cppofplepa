---
cilt: "II — İleri"
kisim: "7 — Concepts"
baslik: "7.6 Standart kavramlar"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 7.6 Standart kavramlar

`<concepts>` başlığı, sık ihtiyaç duyulan kısıtları hazır sunar.

| Grup | Örnekler |
|---|---|
| Tür ilişkileri | `same_as`, `derived_from`, `convertible_to`, `common_with` |
| Aritmetik | `integral`, `signed_integral`, `floating_point` |
| Karşılaştırma | `equality_comparable`, `totally_ordered` |
| Nesne | `movable`, `copyable`, `semiregular`, `regular` |
| Çağrılabilir | `invocable`, `regular_invocable`, `predicate` |

`<iterator>` başlığı iteratör kavramlarını sunar: `input_iterator`, `forward_iterator`,
`bidirectional_iterator`, `random_access_iterator`, `contiguous_iterator`. Bunlar, Cilt I
Kısım 23.2'deki iteratör kategorilerinin kavram karşılığıdır; artık etiket türü yerine
doğrudan kısıt olarak kullanılabilirler.

`std::regular`, bir türün "sıradan bir değer gibi" davrandığını söyler: varsayılan
kurucu işlevi, kopyalaması ve `==` operatörü vardır. Kendi türlerinizi tasarlarken
hedeflenecek sözleşme çoğu zaman budur.
