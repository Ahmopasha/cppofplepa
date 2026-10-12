---
cilt: "II — İleri"
kisim: "14 — Deyimler ve Kalıplar"
baslik: "14.4 İsim arama ve gönderim deyimleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 14.4 İsim arama ve gönderim deyimleri

### Overloader

Birden fazla lambdayı tek bir çağrılabilir nesnede birleştirir. `std::visit` ile
kullanmak için yazılır (bkz. Kısım 11.5).

```cpp
template<typename... Ts>
struct Overloader : Ts... { using Ts::operator()...; };

template<typename... Ts>
Overloader(Ts...) -> Overloader<Ts...>;         // deduction guide
```

```cpp
std::visit(Overloader{
    [](int i)                { std::cout << "tamsayı: " << i; },
    [](const std::string& s) { std::cout << "yazı: " << s; }
}, v);
```

Deyim üç mekanizmayı bir arada kullanır: değişken sayıda parametreli kalıtım,
`using` bildirimiyle paket açma (bkz. Kısım 4.5), ve deduction guide (bkz. Kısım 4.7).

### ADL Fallback

Kullanıcının kendi türü için özelleştirebileceği bir işlevi, özelleştirmediğinde varsayılan
bir sürüme düşecek şekilde çağırmaktır.

```cpp
namespace detay {
    using std::swap;                 // varsayılanı görünür kıl
    template<typename T>
    void takasla(T& a, T& b) { swap(a, b); }    // nitelenmemiş çağrı
}
```

`swap` nitelenmeden çağrıldığı için, `T`'nin isim alanında bir `swap` varsa ADL onu bulur
(bkz. Cilt I Kısım 16.5); yoksa `using` ile getirilen `std::swap` kullanılır.

### Return Type Resolver

Geri dönüş türünün, atandığı değişkenin türüne göre belirlenmesini sağlar. Normalde
mümkün değildir; tür dönüştürme operatör işlevi şablonu ile kurulur (bkz. Kısım 16.1).

```cpp
struct Olustur {
    template<typename T>
    operator T() const { return T{}; }
};

int x = Olustur{};                  // T = int
std::string s = Olustur{};          // T = std::string
```
