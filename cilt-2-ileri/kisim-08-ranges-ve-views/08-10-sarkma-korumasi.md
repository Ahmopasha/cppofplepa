---
cilt: "II — İleri"
kisim: "8 — Ranges ve Views"
baslik: "8.10 Sarkma koruması"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++23)"
---

## 8.10 Sarkma koruması

Geçici bir kaptan iteratör döndürmek tehlikelidir; kap yok olduğunda iteratör sarkar.
Ranges bunu tür sisteminde yakalar.

```cpp
auto it = std::ranges::find(std::vector{1, 2, 3}, 2);
// it'in türü std::ranges::dangling
*it;                                     // sentaks hatası
```

Geçici bir aralık geçirdiğinizde algoritma, iteratör yerine `std::ranges::dangling`
türünden bir nesne döndürür. Onu kullanmaya çalışmak **derleme zamanında** yakalanır.

İstisnası **ödünç aralıklardır** *(borrowed range)*: `string_view`, `span` ve `subrange`
gibi türlerde nesnenin yok olması iteratörleri geçersiz kılmaz; iteratörlerin gösterilen
veriye ya da başka nesnelere bağlılığı ise sürer (Kısım 11.2). Bu türler
`enable_borrowed_range` ile işaretlenmiştir. Belirleyici olan bu işarettir; sahiplenmemek
tek başına yetmez. `filter_view`, veriyi sahiplenmediğinde bile (ör. L-Value bir kap
üzerine kurulduğunda), iteratörleri görünümün kendisine bağlı olduğu için ödünç aralık
değildir.
