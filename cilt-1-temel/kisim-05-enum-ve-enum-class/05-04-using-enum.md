---
cilt: "I — Temel"
kisim: "5 — `enum` ve `enum class`"
baslik: "5.4 `using enum`"
kaynak: "ders notları"
kutular: ["Standart Notu — C++20"]
son_kontrol: "2026-09 (C++23)"
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

Sabitler yalnızca o kapsama taşınır; `enum class`'ın sağladığı diğer güvenceler
korunur.

> **Standart Notu — C++20**
> **C++20 öncesi:** Kapsamlandırılmış `enum` sabitleri her kullanımda nitelenmek
> zorundaydı. Tek çözüm, her sabit için ayrı bir `constexpr` eş isim tanımlamaktı.
> **C++20 ile:** `using enum` bildirimiyle sabitler bir kapsama toplu olarak taşınabilir.
> **Neden değişti:** Niteleme zorunluluğu, `enum class`'a geçişin önündeki başlıca
> pratik engeldi.
