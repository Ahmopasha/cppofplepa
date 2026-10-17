---
cilt: "II — İleri"
kisim: "8 — Ranges ve Views"
baslik: "8.11 Kaptan görünüme, görünümden kaba"
kaynak: "ders notları"
kutular: ["Standart Notu — C++20"]
son_kontrol: "2026-09 (C++23)"
---

## 8.11 Kaptan görünüme, görünümden kaba

Zincirin sonunda gerçek bir kap istiyorsanız C++20'de elle kopyalamanız gerekir:

<!-- kod-baglam
std::vector<int> v{1, 2, 3};
auto g = v | std::views::take(2);
-->
```cpp
std::vector<int> sonuc;
std::ranges::copy(g, std::back_inserter(sonuc));
```

C++23 bunu tek çağrıya indirdi:

<!-- kod-baglam
std::vector<int> v{1, 2, 3};
auto g = v | std::views::take(2);
-->
```cpp
auto sonuc = g | std::ranges::to<std::vector>();
```

> **Standart Notu — C++20**
> **C++20 öncesi:** Algoritmalar iteratör çiftiyle çağrılırdı; kabın tamamı üzerinde
> çalışmak için her seferinde `begin()` ve `end()` yazılırdı. Birbirine bağlı işlemler
> ara kap gerektirir, her adımda bellek ayrılırdı. Farklı kaplardan iteratör geçirmek
> derleme zamanında yakalanamazdı.
> **C++20 ile:** Algoritmalar aralığın kendisini alır. Görünümler tembel çalışır ve
> zincirlenebilir; ara kap oluşmaz. Uyumsuz iteratör geçirmek kavram ihlali olarak
> derleme zamanında yakalanır.
> **Neden değişti:** İteratör çifti soyutlaması, iki iteratörün aynı kaba ait olduğunu
> tür sisteminde ifade edemiyordu. Aralık, o bilgiyi tek nesnede taşır.
