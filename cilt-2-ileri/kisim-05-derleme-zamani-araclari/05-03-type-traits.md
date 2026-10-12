---
cilt: "II — İleri"
kisim: "5 — Derleme Zamanı Araçları"
baslik: "5.3 `type_traits`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 5.3 `type_traits`

Standart kütüphanenin hazır meta işlev koleksiyonudur. Üç gruba ayrılır.

**Tür sorgulayanlar** — `value` üzerinden `bool` döndürür.

```cpp
std::is_integral<T>::value
std::is_pointer<T>::value
std::is_class<T>::value
std::is_same<T, U>::value
std::is_base_of<Taban, Turemis>::value
std::is_nothrow_move_constructible<T>::value
```

**Tür dönüştürenler** — `type` üzerinden tür döndürür.

```cpp
std::remove_reference<T>::type
std::remove_const<T>::type
std::decay<T>::type
std::conditional<kosul, A, B>::type
```

**Kısaltmalar.** Her sorgunun `_v` ekli değişken şablonu, her dönüşümün `_t` ekli eş isim
şablonu vardır (bkz. 4.10).

```cpp
std::is_integral_v<T>          // ::value yerine
std::remove_reference_t<T>     // ::type yerine
```

Yeni kodda kısaltmaları kullanın. Uzun biçimler C++11 dönemine aittir.

`std::decay`, argümanın değerle geçirilmesi hâlinde oluşacak türü verir: referanslık ve
üst düzey `const`luk düşer, dizi ve işlev isimleri çürür. Cilt I Kısım 4.2'deki
`auto x = expr;` kalıbının meta işlev karşılığıdır.
