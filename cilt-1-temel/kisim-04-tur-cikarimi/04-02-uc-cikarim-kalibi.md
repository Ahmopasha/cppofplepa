---
cilt: "I — Temel"
kisim: "4 — Tür Çıkarımı"
baslik: "4.2 Üç çıkarım kalıbı"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 4.2 Üç çıkarım kalıbı

`auto`'nun nasıl yazıldığı, çıkarılan türü değiştirir. Üç kalıp vardır ve farkları
`const`luk ile referanslıkta (Kısım 8) ortaya çıkar.

### `auto x = expr;`

Referanslık ve **üst düzey `const`luk** *(top-level const)*, yani nesnenin kendisinin
`const` olması **düşer**. Bir göstericinin gösterdiği nesneye ait `const`luk ise düşmez.

```cpp
int a = 10;
const int ca = 20;
int& ra = a;
const int& cra = a;
const int* pc = &ca;
const int* const cpc = &ca;

auto x1 = a;      // int
auto x2 = ca;     // int   — const düştü
auto x3 = ra;     // int   — referans düştü
auto x4 = cra;    // int   — önce referans, sonra kalan const düştü
auto x5 = pc;     // const int*  — gösterilen nesnenin const'luğu korundu
auto x6 = cpc;    // const int*  — göstericinin const'u düştü
```

`x` bir referans değildir; ilk değer veren ifadeden oluşturulan yeni bir nesnedir.
Gösterici kopyalandığında yalnızca gösterici kopyalanır, gösterilen nesne ortak kalır.

### `auto& x = expr;`

Sonuç her zaman bir L-Value referanstır ve `const`luk **korunur**.

```cpp
auto& y1 = a;      // int&
auto& y2 = ca;     // const int&  — const korundu
auto& y3 = cra;    // const int&
auto& y4 = 10;     // sentaks hatası — int& R-Value'ya bağlanamaz (Kısım 2.4.5)
```

`const auto&` yazımı ise `const` bir L-Value referans üretir, R-Value'ya da bağlanır ve
okuma amaçlı en yaygın kullanımdır.

### `auto&& x = expr;`

Hem L-Value'ya hem R-Value'ya bağlanabilen bir referans üretir; bir forwarding
reference'tır (Kısım 8.9). Cilt I için bilmeniz gereken, bunun aralık tabanlı `for`
döngülerinde güvenli tercih olduğudur (Kısım 23.3). Ayrıntısı: **Cilt II, Kısım 1.2.**
