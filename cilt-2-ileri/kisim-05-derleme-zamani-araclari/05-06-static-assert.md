---
cilt: "II — İleri"
kisim: "5 — Derleme Zamanı Araçları"
baslik: "5.6 `static_assert`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 5.6 `static_assert`

Derleme zamanında bir koşulu denetler; sağlanmazsa derlemeyi durdurur.

```cpp
template<typename T>
class Kutu {
    static_assert(std::is_copy_constructible_v<T>,
                  "Kutu yalnızca kopyalanabilir türlerle kullanılabilir");
};
```

Mesajsız biçimi C++17'den beri geçerlidir:

```cpp
static_assert(sizeof(int) == 4);
```

Kazancı, hatanın **erken ve okunabilir** olmasıdır. Şablon kodunda kısıt ihlali edilince
oluşan hata mesajları genellikle onlarca satırdır ve asıl sebebi göstermez;
`static_assert` yazdığınız mesajı gösterir.

Bunun daha ileri ve daha okunabilir hâli C++20'nin kavramlarıdır: **Kısım 7.**
