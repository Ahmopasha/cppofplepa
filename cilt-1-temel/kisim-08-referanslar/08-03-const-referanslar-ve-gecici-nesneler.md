---
cilt: "I — Temel"
kisim: "8 — Referanslar"
baslik: "8.3 `const` referanslar ve geçici nesneler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 8.3 `const` referanslar ve geçici nesneler

Kısım 2.4.5'te `const T&`'nin R-Value bağlayabildiğini görmüştük. Bunun mekanizması
şudur: derleyici geçici bir nesne oluşturur ve referansı ona bağlar.

```cpp
const int& r = 100;      // arka planda geçici bir nesne var
```

Normalde geçici nesnenin hayatı, içinde bulunduğu ifadenin sonunda biter. Bir `const`
referansa bağlandığında ise ömrü **referansın ömrü kadar uzatılır.** Buna *life
extension* denir.

```cpp
const std::string& r = std::string{"merhaba"};
std::cout << r;      // geçerli — geçici nesne hâlâ hayatta
```

Bu uzatmanın iki istisnası vardır ve ikisi de hata kaynağıdır. **İşlevden döndürülen
referans için geçerli değildir** (bkz. 8.6). Ve **sınıfın veri elemanı olan referans
için geçerli değildir**; kurucu işlevin ilk değer verme listesinde bağlanan geçici nesne,
kurucu işlev biter bitmez yok olur.
