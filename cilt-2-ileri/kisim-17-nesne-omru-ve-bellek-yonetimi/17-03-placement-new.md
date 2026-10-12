---
cilt: "II — İleri"
kisim: "17 — Nesne Ömrü ve Bellek Yönetimi"
baslik: "17.3 `placement new`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 17.3 `placement new`

Bellek **ayırmadan**, verilen adreste nesne oluşturur.

```cpp
#include <new>

alignas(Myclass) unsigned char tampon[sizeof(Myclass)];

Myclass* p = new (tampon) Myclass{10};     // tampon üzerinde oluştur
```

`new` anahtar sözcüğünden sonra parantez içinde adres verilir. Bellek ayırma adımı
atlanır; yalnızca kurucu işlev çağrılır.

**Sonlandırıcı işlevi elle çağırmanız gerekir.** `delete` yazamazsınız, çünkü ortada
`operator new` ile ayrılmış bellek yoktur:

```cpp
p->~Myclass();      // yıkımı elle yapın
```

Kullanım alanları: kapların ayırdıkları ham bellekte eleman oluşturması, `std::optional`
ve `std::variant` gibi türlerin içlerindeki nesneyi yönetmesi, gömülü sistemlerde sabit
adreslere nesne yerleştirmek.

`alignas` niteleyicisi, tamponun hizalamasının nesne için uygun olmasını sağlar; onsuz
hizalama hatası oluşabilir.

Uygulama kodunda doğrudan yazmanız nadiren gerekir. Kütüphane yazarken ve standart
kütüphanenin kaynak kodunu okurken karşınıza çıkar.
