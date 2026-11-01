---
cilt: "II — İleri"
kisim: "8 — Ranges ve Views"
baslik: "8.2 `range` bir tür değil, bir kavramdır"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++23)"
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

Bunun sonucu, **STL kaplarının zaten birer aralık olmasıdır.** Yeni bir tür öğrenmiyor,
mevcut türlere yeni bir arayüzden bakıyorsunuz. Ham diziler de aralıktır. Kap
uyumlandırıcılarından `stack`, `queue` ve `priority_queue`, `begin()` ve `end()` sunmadığı
için aralık değildir.

Kavram hiyerarşisi vardır. Başlıcaları `input_range`, `forward_range`,
`bidirectional_range`, `random_access_range` ve `contiguous_range`'dir; bunlar Cilt I,
Kısım 23.2'deki iteratör kategorilerinin aralık düzeyindeki karşılığıdır. `sized_range`
ise bu zincirin dışında, ayrı bir özelliktir: eleman sayısı `std::ranges::size` ile
**amortize sabit zamanda** *(amortized constant time)* alınabilen aralık demektir. Örneğin
`std::forward_list` ileri yönlü bir aralıktır, ama `sized_range` değildir.
