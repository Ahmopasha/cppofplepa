---
cilt: "II — İleri"
kisim: "8 — Ranges ve Views"
baslik: "8.2 `range` bir tür değil, bir kavramdır"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 8.2 `range` bir tür değil, bir kavramdır

Bunu vurgulamak gerekiyor çünkü isim yanıltıcıdır. `std::ranges::range` bir sınıf değil,
Kısım 7 anlamında bir **kavramdır**.

Kabaca şunu söyler: bir tür, üzerinde `begin()` ve `end()` çağrılabiliyorsa bir
aralıktır.

```cpp
template<typename T>
concept range = requires(T& t) {
    std::ranges::begin(t);
    std::ranges::end(t);
};
```

Bunun sonucu, **her STL kabının zaten bir aralık olmasıdır.** Yeni bir tür öğrenmiyor,
mevcut türlere yeni bir arayüzden bakıyorsunuz. Ham diziler de aralıktır.

Kavram hiyerarşisi vardır: `input_range`, `forward_range`, `bidirectional_range`,
`random_access_range`, `contiguous_range` ve `sized_range`. Bunlar Cilt I Kısım 23.2'deki
iteratör kategorilerinin aralık düzeyindeki karşılığıdır.
