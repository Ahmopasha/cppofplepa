---
cilt: "I — Temel"
kisim: "8 — Referanslar"
baslik: "8.3 `const` referanslar ve geçici nesneler"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++20)"
---

## 8.3 `const` referanslar ve geçici nesneler

Kısım 2.4.5'te `const T&`'nin R-Value bağlayabildiğini görmüştük. Bunun mekanizması
şudur: derleyici geçici bir nesne oluşturur ve referansı ona bağlar.

```cpp
const int& r = 100;      // arka planda geçici bir nesne var
```

Normalde geçici nesnenin hayatı, onu içeren **tam ifadenin** *(full-expression)* sonunda
biter. Tam ifade, başka bir ifadenin parçası olmayan ifadedir; çoğu zaman `;` ile biten
bir deyimin ifadesidir. Bir bildirimde değişkenin ilk değer alması da ilk değer
ifadeleriyle birlikte tek bir tam ifadedir. Referansa ilk değer verilirken oluşan geçici
nesne o referansa bağlandığında ise ömrü **referansın ömrü kadar uzatılır**; başka bir
referans ya da referans döndüren bir çağrı aracılığıyla yapılan bağlanma ömrü uzatmaz. Bu,
`const T&` için de `T&&` için de geçerlidir. Bu uzatmaya *life extension* denir.

```cpp
const std::string& r = std::string{"merhaba"};
std::cout << r;      // geçerli — geçici nesne hâlâ hayatta
```

Bu uzatmanın en sık karşılaşılan iki istisnası vardır ve ikisi de hata kaynağıdır.
**İşlevden döndürülen referans için geçerli değildir** (bkz. Kısım 8.6). Ve **referans
veri elemanı, kurucu işlevin (bkz. Kısım 12) referans parametresinden ilk değer alıyorsa
geçerli değildir**. Kurucu işleve argüman olarak verilen geçici nesne, kurucu işlev
çağrısını içeren tam ifade bitince yok olur ve veri elemanı **sarkan referans**
*(dangling reference)* olarak kalır.

İki istisnanın gerekçesi: **Cilt II, Kısım 17.6.**
