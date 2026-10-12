---
cilt: "II — İleri"
kisim: "11 — Vocabulary Türleri"
baslik: "11.6 `std::any`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 11.6 `std::any`

Kopyalanabilir **herhangi bir türü** tutar. `variant`'tan farkı, tür kümesinin önceden
belirtilmemesidir.

```cpp
#include <any>

std::any a = 42;
a = std::string{"merhaba"};

std::any_cast<std::string>(a);      // yanlış türse std::bad_any_cast
a.type();                           // std::type_info
a.has_value();
```

Tür bilgisi çalışma zamanında taşınır; bu, RTTI'ye dayanır (bkz. Cilt I Kısım 19) ve
dinamik bellek ayırabilir.

`variant` ile karşılaştırması: `variant` kapalı küme, derleme zamanında denetimli, daha
hızlı. `any` açık küme, çalışma zamanında denetimli, daha esnek. Hangi türlerin
geleceğini biliyorsanız `variant` kullanın.

`any` en çok eklenti mimarilerinde ve tür bilgisinin gerçekten önceden bilinemediği
yerlerde yararlıdır. İhtiyacınız olmadığı hâlde kullanmak, tür sistemini devre dışı
bırakmak demektir.
