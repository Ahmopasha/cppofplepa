---
cilt: "II — İleri"
kisim: "12 — İleri Lambda Teknikleri"
baslik: "12.1 Kapanış türünün anatomisi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 12.1 Kapanış türünün anatomisi

Cilt I Kısım 24.1'de lambdanın derleyiciye isimsiz bir sınıf yazdırdığı söylenmişti.
O sınıfa **kapanış türü** *(closure type)* denir ve yapısı şudur:

```cpp
int a = 10;
auto f = [a](int x) { return x + a; };
```

Derleyicinin ürettiği karşılık, kabaca:

```cpp
class __Kapanis {
    int a;                                  // yakalanan değişken veri elemanı oldu
public:
    __Kapanis(int a_) : a{a_} { }
    int operator()(int x) const { return x + a; }    // const olduğuna dikkat
};
```

Buradan üç sonuç çıkar.

**Yakalanan değişkenler veri elemanına dönüşür.** Kopyalayarak yakalamak kopyalama,
referansla yakalamak referans veri elemanı demektir. Cilt I Kısım 24.3'teki sarkma
tehlikesinin sebebi budur: referans veri elemanı, gösterdiği nesne yok olursa sarkar.

**`operator()` varsayılan olarak `const`'tur.** 12.2'nin konusu.

**Her lambda ifadesi ayrı bir türdür.** İki lambda birebir aynı yazılmış olsa bile
türleri farklıdır; bu yüzden `auto` zorunludur.

Hiçbir şey yakalamayan lambdalar, aynı imzalı işlev göstericisine örtülü olarak dönüşür:

```cpp
int (*fp)(int) = [](int x) { return x * 2; };     // yakalama yoksa geçerli
```

Yakalama varsa dönüşüm yoktur; veri taşıyan bir nesne, işlev göstericisine sığmaz.
