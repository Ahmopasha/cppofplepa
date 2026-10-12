---
cilt: "II — İleri"
kisim: "11 — Vocabulary Türleri"
baslik: "11.2 `std::string_view`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 11.2 `std::string_view`

Bir karakter dizisine **sahiplenmeyen görünümdür.** İçinde yalnızca bir gösterici ve bir
uzunluk tutar; bellek ayırmaz, kopyalamaz.

```cpp
#include <string_view>

void yazdir(std::string_view sv);

std::string s{"merhaba"};
yazdir(s);              // kopyalama yok
yazdir("merhaba");      // geçici std::string oluşmuyor
yazdir(s.substr(0, 3)); // dikkat — substr yeni bir string döndürür
```

Cilt I Kısım 20.6'da yalnızca adı geçmişti. Kazancı şudur: `const std::string&`
parametreli bir işleve `const char*` geçirirseniz geçici bir `std::string` oluşur ve
bellek ayrılır. `string_view` ile bu maliyet yoktur.

**Tehlikesi sahiplenmemesidir.** Gösterdiği yazı yok olursa elinizde sarkan bir görünüm
kalır:

```cpp
std::string_view bozuk()
{
    std::string s{"gecici"};
    return s;              // s yok olacak, görünüm sarkacak
}
```

Kural şudur: **`string_view`'ü parametre olarak alın, veri elemanı olarak saklamayın.**
Bir işlev çağrısı süresince kaynağın yaşadığı garantilidir; nesnenin ömrü boyunca değil.

İkinci bir incelik: `string_view`'ün gösterdiği dizi **sonlandırıcı boş karakter
içermek zorunda değildir.** `data()` döndürdüğü göstericiyi C arayüzlerine vermeyin;
`std::string`'e çevirin.
