---
cilt: "II — İleri"
kisim: "7 — Concepts"
baslik: "7.4 `requires` ifadesi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 7.4 `requires` ifadesi

Kısıtın kendisini yazmanın aracıdır. `requires` cümlesiyle karıştırılmamalıdır: cümle
kısıt **uygular**, ifade kısıt **oluşturur.**

```cpp
template<typename T>
concept Toplanabilir = requires(T a, T b) {
    a + b;
};
```

Parantez içindeki değişkenler gerçek değildir; yalnızca gövdedeki ifadeleri yazabilmek
için vardır. Gövdedeki ifadeler **çalıştırılmaz**, yalnızca geçerli olup olmadıklarına
bakılır.

Dört tür gereklilik yazılabilir.

**Basit gereklilik.** İfade geçerli olmalıdır.

<!-- kod-baglam
template<typename T>
concept Ornek =
@kod@
-->
```cpp
requires(T a) { a.func(); };
```

**Tür gerekliliği.** Belirtilen tür var olmalıdır.

<!-- kod-baglam
template<typename T>
concept Ornek =
@kod@
-->
```cpp
requires { typename T::value_type; };
```

**Bileşik gereklilik.** İfade geçerli olmalı, ayrıca sonucunun türü bir kısıtı
sağlamalıdır.

<!-- kod-baglam
template<typename T>
concept Ornek =
@kod@
-->
```cpp
requires(T a) {
    { a.size() } -> std::convertible_to<std::size_t>;
    { a.func() } noexcept;
};
```

Süslü parantez zorunludur ve `->` sağındaki, bir türü değil bir **kavramı** belirtir.

**İç içe gereklilik.** Başka bir kısıtın sağlanmasını ister.

<!-- kod-baglam
template<typename T>
concept Ornek =
@kod@
-->
```cpp
requires(T a) {
    requires std::integral<T>;
    a + a;
};
```

İçerideki `requires` olmadan yazarsanız, `std::integral<T>` yalnızca "bu ifade geçerli mi"
diye sorgulanır ve **her zaman doğru çıkar**; değeri denetlenmez. Bu, kavram yazarken en
sık yapılan hatadır.
