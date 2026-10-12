---
cilt: "I — Temel"
kisim: "4 — Tür Çıkarımı"
baslik: "4.2 Üç çıkarım kalıbı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 4.2 Üç çıkarım kalıbı

`auto`'nun nasıl yazıldığı, çıkarılan türü değiştirir. Üç kalıp vardır ve farkları
`const`luk ile referanslıkta ortaya çıkar.

### `auto x = expr;`

Referanslık ve üst düzey `const`luk **düşer**.

```cpp
int a = 10;
const int ca = 20;
int& ra = a;
const int& cra = a;

auto x1 = a;      // int
auto x2 = ca;     // int   — const düştü
auto x3 = ra;     // int   — referans düştü
auto x4 = cra;    // int   — ikisi de düştü
```

Sonuç her zaman bağımsız bir kopyadır. Kaynağı değiştirmez.

### `auto& x = expr;`

Referanslık korunur, `const`luk **korunur**.

```cpp
auto& y1 = a;      // int&
auto& y2 = ca;     // const int&  — const korundu
auto& y3 = cra;    // const int&
```

`const auto&` yazımı ise her durumda `const` referans üretir ve okuma amaçlı en yaygın
kullanımdır.

### `auto&& x = expr;`

Her şeye bağlanan bir referans üretir. Cilt I için bilmeniz gereken, bunun aralık tabanlı
`for` döngülerinde güvenli tercih olduğudur (bkz. Kısım 23). Ayrıntısı:
**Cilt II, Kısım 1.2.**
