---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.6 Katlama ifadeleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 4.6 Katlama ifadeleri

C++17, paketleri özyineleme olmadan işlemenin yolunu ekledi. **İfade parantez içinde
olmak zorundadır.**

Dört biçimi vardır:

| Biçim | Yazım | Açılımı |
|---|---|---|
| Sol tekli | `(... op paket)` | `((a op b) op c)` |
| Sağ tekli | `(paket op ...)` | `(a op (b op c))` |
| Sol ikili | `(ilk op ... op paket)` | `(((ilk op a) op b) op c)` |
| Sağ ikili | `(paket op ... op ilk)` | `(a op (b op (c op ilk)))` |

```cpp
template<typename... Ts>
auto topla(const Ts&... args)
{
    return (... + args);        // sol tekli katlama
}

template<typename... Ts>
void yazdir(const Ts&... args)
{
    ((std::cout << args << ' '), ...);      // virgül operatörüyle
}
```

Tekli katlamada paket boşsa yalnızca birkaç operatör için tanımlı bir sonuç vardır
(`&&` için `true`, `||` için `false`, `,` için `void`). Diğer operatörlerde boş paket
sentaks hatası verir; ikili katlama bu sorunu ilk değerle çözer.
