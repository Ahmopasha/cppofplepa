---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.5 Değişken sayıda parametre"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 4.5 Değişken sayıda parametre

Parametre sayısı önceden belli olmayan şablonlar yazılabilir.

```cpp
template<typename... Ts>
void yazdir(const Ts&... args);
```

`Ts` bir **parametre paketidir**; sıfır veya daha fazla türü temsil eder. `args` ise bir
**işlev parametre paketidir**.

Paketin eleman sayısı `sizeof...` ile alınır:

```cpp
template<typename... Ts>
constexpr std::size_t adet() { return sizeof...(Ts); }
```

Paketi kullanmaya **açma** *(pack expansion)* denir ve `...` ile yapılır. Açma, paketin
her elemanı için deseni tekrarlar:

```cpp
template<typename... Ts>
void ilet(Ts&&... args)
{
    hedef(std::forward<Ts>(args)...);     // her argüman ayrı ayrı iletilir
}
```

Bu, Cilt II Kısım 1.2.5'teki mükemmel gönderimin değişken sayıda parametreye
genellenmiş hâlidir; `emplace_back` tam olarak böyle yazılır.

C++17 öncesinde paketi işlemenin tek yolu özyinelemeydi:

```cpp
void yazdir() { }                          // özyinelemenin tabanı

template<typename T, typename... Ts>
void yazdir(const T& ilk, const Ts&... kalan)
{
    std::cout << ilk;
    yazdir(kalan...);
}
```
