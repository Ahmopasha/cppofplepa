---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.9 İki aşamalı isim arama"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 4.9 İki aşamalı isim arama

Şablon gövdesindeki isimler iki ayrı anda aranır.

**Bağımsız isimler** *(non-dependent)*, şablon parametresine bağlı olmayan isimlerdir;
şablonun **tanımlandığı** noktada aranır ve bağlanır.

**Bağımlı isimler** *(dependent)*, şablon parametresine bağlı olanlardır; şablonun
**örneklendiği** noktada aranır.

Bunun iki pratik sonucu vardır.

**Bağımlı bir nitelenmiş isim tür belirtiyorsa `typename` yazmanız gerekir.** Derleyici,
`T::X`'in bir tür mü yoksa bir statik veri elemanı mı olduğunu tanım anında bilemez ve
varsayılan olarak tür **olmadığını** varsayar.

```cpp
template<typename T>
void func()
{
    typename T::deger_turu x;      // typename zorunlu
}
```

**Bağımlı bir üye şablonu çağırıyorsanız `template` yazmanız gerekir.**

```cpp
template<typename T>
void func(T t)
{
    t.template uye_sablon<int>();      // template zorunlu
}
```

Onsuz `<` işareti karşılaştırma operatörü sanılır.

C++20, `typename`'in zorunlu olduğu yerlerin bir kısmında yazma zorunluluğunu kaldırdı.
