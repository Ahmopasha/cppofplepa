---
cilt: "II — İleri"
kisim: "16 — Sınıfların ve Operatörlerin İleri Araçları"
baslik: "16.2 Referans niteleyicili üye işlevler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 16.2 Referans niteleyicili üye işlevler

Cilt I Kısım 12.7'de `const` üye işlevler anlatılmıştı. `const`luk, `this`'in
gösterdiği nesnenin `const` olup olmadığını belirler. **Referans niteleyicisi** ise
nesnenin **değer kategorisini** belirler.

```cpp
class Myclass {
public:
    void func() &  { std::cout << "L-Value nesne\n"; }
    void func() && { std::cout << "R-Value nesne\n"; }
};

Myclass m;
m.func();               // L-Value nesne
Myclass{}.func();       // R-Value nesne
std::move(m).func();    // R-Value nesne
```

Aynı imzanın hem niteleyicili hem niteleyicisiz sürümünü bir arada bildiremezsiniz;
ya hepsi niteleyicili olur ya hiçbiri.

Asıl kullanım yeri, içerideki kaynağı döndüren işlevlerdir. Nesne bir R-Value ise
kaynağı kopyalamak yerine taşıyabilirsiniz:

```cpp
class Sarmal {
    std::vector<int> veri;
public:
    const std::vector<int>& al() const&  { return veri; }
    std::vector<int>        al() &&      { return std::move(veri); }
};
```

Birinci sürüm kopyalamayı önler, ikincisi geçici nesnenin kaynağını devralır. Bu, Kısım
2'deki taşıma semantiğinin üye işlev düzeyindeki karşılığıdır.

Bir kullanım daha vardır: atama operatörünü R-Value nesnelerde kapatmak.

```cpp
Myclass& operator=(const Myclass&) & ;    // yalnızca L-Value nesnelere atama
```

Bu olmadan `Myclass{} = m;` yazımı geçerlidir ve hiçbir anlamı yoktur.
