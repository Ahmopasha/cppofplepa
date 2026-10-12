---
cilt: "II — İleri"
kisim: "11 — Vocabulary Türleri"
baslik: "11.5 `std::variant`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 11.5 `std::variant`

Belirtilen türlerden **tam olarak birini** tutar. Tür güvenli `union`'dır.

```cpp
#include <variant>

std::variant<int, double, std::string> v;

v = 42;
v = 3.14;
v = "merhaba";

v.index();                    // hangi türün sırası
std::get<std::string>(v);     // yanlış türse std::bad_variant_access
std::get_if<int>(&v);         // yanlış türse nullptr
```

Erişimin asıl yolu `std::visit`'tir; bütün olasılıkları kapsamaya zorlar:

```cpp
std::visit([](const auto& deger) { std::cout << deger; }, v);
```

Ziyaretçi, her tür için çağrılabilir olmalıdır. Genelleştirilmiş lambda (bkz. Kısım 12)
bunu tek satırda sağlar; türlere göre farklı davranmak isterseniz aşırı yüklenmiş bir
çağrılabilir gerekir.

Cilt II Kısım 6.13'te, `variant`'ın kalıtıma alternatif olduğu söylenmişti. Tür kümesi
kapalı ve önceden biliniyorsa, sanal gönderim yerine `visit` kullanılabilir; `vptr`
maliyeti ve dinamik bellek ortadan kalkar. Bedeli, yeni tür eklemenin `variant`
bildirimine dokunmayı gerektirmesidir.
