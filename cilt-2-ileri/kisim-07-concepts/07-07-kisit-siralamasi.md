---
cilt: "II — İleri"
kisim: "7 — Concepts"
baslik: "7.7 Kısıt sıralaması"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 7.7 Kısıt sıralaması

İki yükleme de uygunsa, **daha kısıtlı olan** seçilir. Buna *subsumption* denir.

```cpp
template<std::integral T>          void func(T);     // 1
template<std::signed_integral T>   void func(T);     // 2

func(5);        // 2 seçilir — signed_integral daha kısıtlı
```

Derleyici, kısıtları atomik parçalara ayırıp birinin diğerini kapsayıp kapsamadığına
bakar. `signed_integral`, tanımı gereği `integral`'i içerdiği için daha kısıtlıdır.

Bu, C++20 öncesinde `enable_if` ile yapılan "en özel olanı seç" düzenlerinin yerini alır
ve onlardan farklı olarak derleyici tarafından anlaşılır.

**Sıralamanın çalışması için kısıtların sözdizimsel olarak ilişkili olması gerekir.**
Aynı anlama gelen ama farklı yazılmış iki kısıt birbirini kapsamaz; `std::is_integral_v<T>`
yazan bir kısıt ile `std::integral<T>` yazan bir kısıt arasında sıralama kurulamaz ve
çift anlamlılık hatası alırsınız.
