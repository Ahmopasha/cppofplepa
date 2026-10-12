---
cilt: "II — İleri"
kisim: "5 — Derleme Zamanı Araçları"
baslik: "5.4 `if constexpr`"
kaynak: "ders notları"
kutular: ["Standart Notu — C++17"]
son_kontrol: "2026-09 (C++23)"
---

## 5.4 `if constexpr`

Derleyiciye derleme zamanında kod seçimi yaptırır. `static if` adıyla da anılır.

```cpp
template<typename T>
void yazdir(const T& t)
{
    if constexpr (std::is_pointer_v<T>)
        std::cout << *t;
    else
        std::cout << t;
}
```

Sıradan `if`'ten farkı belirleyicidir: **seçilmeyen dal örneklenmez.** Yukarıdaki kodda
`T` bir gösterici değilse `*t` ifadesi hiç derlenmez. Sıradan `if` kullanılsaydı her iki
dal da derlenir ve `*t` sentaks hatası verirdi.

İki sınır vardır. Koşul derleme zamanında bilinmelidir. Ve seçilmeyen dal örneklenmese
de **sözdizimsel olarak geçerli olmak zorundadır**; ayrıştırılabilir olmayan kod yine
hata verir.

`if constexpr`, 5.2'deki tag dispatching kalıbının ve 4.8'deki `enable_if` kullanımlarının
büyük kısmının yerini almıştır.

> **Standart Notu — C++17**
> **C++17 öncesi:** Derleme zamanında dallanmak için tag dispatching, `enable_if` ile
> SFINAE, veya sınıf şablonu özelleştirmesi kullanılırdı. Üçü de niyeti gizleyen
> dolaylı yöntemlerdi.
> **C++17 ile:** `if constexpr` ile doğrudan yazılır.
> **Neden değişti:** Derleme zamanı dallanma, şablon kodunun en yaygın ihtiyacıydı ve
> mevcut çözümlerin hiçbiri okunabilir değildi.
