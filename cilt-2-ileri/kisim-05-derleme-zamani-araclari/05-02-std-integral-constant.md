---
cilt: "II — İleri"
kisim: "5 — Derleme Zamanı Araçları"
baslik: "5.2 `std::integral_constant`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 5.2 `std::integral_constant`

Değer döndüren meta işlevlerin ortak tabanıdır. Bir türü ve o türden bir değeri, tek bir
tür içinde paketler.

```cpp
template<typename T, T v>
struct integral_constant {
    static constexpr T value = v;
    using value_type = T;
    using type = integral_constant;
    constexpr operator value_type() const noexcept { return value; }
    constexpr value_type operator()() const noexcept { return value; }
};
```

İki eş ismi sürekli karşınıza çıkar:

```cpp
using true_type  = std::integral_constant<bool, true>;
using false_type = std::integral_constant<bool, false>;
```

Önemi şudur: `true` ile `false` **değerlerdir**, yükleme çözümlemesine katılamazlar.
`true_type` ile `false_type` ise **türlerdir**; birbirinden ayrı yüklemeler seçebilirler.
Derleme zamanında dallanmanın C++17 öncesindeki yolu buydu.

```cpp
void islem(std::true_type)  { /* tamsayı yolu */ }
void islem(std::false_type) { /* diğer yol */ }

template<typename T>
void func(T t) { islem(std::is_integral<T>{}); }
```

Buna *tag dispatching* denir. C++17'den itibaren aynı işi `if constexpr` çok daha kısa
yapar, ama mevcut kodda bu kalıbı sık göreceksiniz.
