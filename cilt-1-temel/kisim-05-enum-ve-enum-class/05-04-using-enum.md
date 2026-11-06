---
cilt: "I — Temel"
kisim: "5 — `enum` ve `enum class`"
baslik: "5.4 `using enum`"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 5.4 `using enum`

`enum class` kullanmanın maliyeti, her yerde nitelemek zorunda kalmaktır. Uzun bir
`switch` bloğunda bu yorucu olur.

C++20 bir kolaylık ekledi:

```cpp
void yazdir(Renk r)
{
    using enum Renk;          // C++20

    switch (r) {
    case Kirmizi: /* ... */ break;
    case Yesil:   /* ... */ break;
    case Mavi:    /* ... */ break;
    }
}
```

Sabitler yalnızca o kapsamda nitelenmeden kullanılabilir; `enum class`'ın sağladığı
diğer güvenceler korunur.

Kapsamlandırılmış bir `enum`'un numaralandırıcıları kendi kapsamı (Kısım 2.2) dışında
nitelenerek kullanılır. C++20'den itibaren `using enum` bildirimiyle bir kapsamda toplu
olarak nitelenmeden de kullanılabilir.
