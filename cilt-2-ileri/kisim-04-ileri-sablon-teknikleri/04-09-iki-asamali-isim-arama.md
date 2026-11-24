---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.9 İki aşamalı isim arama"
kaynak: "ders notları"
kutular: ["Standart Notu — C++20"]
son_kontrol: "2026-11 (C++23)"
---

## 4.9 İki aşamalı isim arama

Şablon gövdesindeki isimler iki ayrı anda aranır.

**Bağımsız isimler** *(non-dependent)*, şablon parametresine bağlı olmayan isimlerdir;
şablonun **tanımlandığı** noktada aranır ve bağlanır.

**Bağımlı isimler** *(dependent)* şablon parametresine bağlıdır; her özelleştirme için,
argümanlar yerleştirildikten sonra aranır. Bağımlı çağrıdaki nitelenmemiş işlev adı olağan
aramayla tanım noktasından, argümana bağlı isim aramayla (Cilt I Kısım 16.5) örnekleme
noktasından da aranır. Şablondan sonra bildirilen işlevi yalnızca ikincisi, o da argüman
türüyle ilişkili bir isim alanındaysa bulur.

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

> **Standart Notu — C++20**
> **C++20 öncesi:** Bağımlı nitelenmiş bir isim tür belirtiyorsa, taban sınıf listesi ve
> üye ilk değer listesindeki taban sınıf adı gibi birkaç istisna dışında `typename`
> yazılırdı.
> **C++20 ile:** Yalnızca türün gelebileceği bağlamlarda `typename` yazılmayabilir: eş
> isim bildiriminin sağ tarafı (`using deger = T::deger_turu;`), `->` ile yazılan geri
> dönüş türü, sınıf kapsamındaki üye bildiriminin tür belirteci gibi. Yukarıdaki gibi
> blok kapsamındaki değişken bildirimlerinde ve şablon argüman listelerinde
> (`std::vector<typename T::deger_turu>`) hâlâ zorunludur.
> **Neden değişti:** Yalnızca türün gelebileceği yerlerde `typename` istemek gereksiz
> yazımdı ve okunabilirliği bozuyordu.
