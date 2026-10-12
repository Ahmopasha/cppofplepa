---
cilt: "II — İleri"
kisim: "5 — Derleme Zamanı Araçları"
baslik: "5.5 `std::declval`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 5.5 `std::declval`

Bir türden nesne **oluşturmadan**, o türden bir ifadeye sahipmiş gibi davranmayı sağlar.

```cpp
template<typename T>
std::add_rvalue_reference_t<T> declval() noexcept;     // tanımı YOKTUR
```

Tanımı yoktur ve çağrılamaz; yalnızca **değerlendirilmeyen bağlamlarda** kullanılır.
`decltype` ve `sizeof` operandları böyle bağlamlardır.

Çözdüğü problem şudur: bir işlevin geri dönüş türünü sormak istiyorsunuz ama o işlevi
çağırabilmek için bir nesneye ihtiyacınız var; nesneyi oluşturmak için de kurucu işleve.
Sınıfın varsayılan kurucu işlevi yoksa sıkışırsınız.

```cpp
template<typename T>
using SonucTuru = decltype(std::declval<T>().func());
```

`std::declval<T>()` gerçekte hiçbir nesne üretmez; derleyiciye "farz et ki elimde `T&&`
türünden bir ifade var" der.

Geri dönüş türünün `T&&` olması kasıtlıdır: `T` bir referans türü değilse bile ifade
oluşturulabilir, ve referans çökmesi sayesinde `T` referanssa da doğru sonuç verir
(bkz. Kısım 1.2.2).
