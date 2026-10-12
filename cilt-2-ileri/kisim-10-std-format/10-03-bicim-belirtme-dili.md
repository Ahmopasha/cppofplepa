---
cilt: "II — İleri"
kisim: "10 — `std::format`"
baslik: "10.3 Biçim belirtme dili"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 10.3 Biçim belirtme dili

Yer tutucunun içine iki nokta üst üsteden sonra biçim belirtilir. Genel yapısı şudur:

```
{: [dolgu][hizalama][işaret][#][0][genişlik][.duyarlık][tür] }
```

| Alan | Değerler | Anlamı |
|---|---|---|
| Hizalama | `<` `>` `^` | Sola, sağa, ortaya |
| İşaret | `+` `-` ` ` | Pozitif sayılarda işaret gösterimi |
| `#` | — | Alternatif biçim (`0x`, `0b` ön ekleri) |
| `0` | — | Sıfırla doldur |
| Genişlik | sayı | En az kaç karakter |
| Duyarlık | `.sayı` | Ondalık basamak veya yazı uzunluğu |
| Tür | `d` `x` `b` `o` `f` `e` `g` `s` | Gösterim biçimi |

```cpp
std::format("{:>10}", "sag");         // "       sag"
std::format("{:*^11}", "orta");       // "***orta****"
std::format("{:08.3f}", 3.14159);     // "0003.142"
std::format("{:#x}", 255);            // "0xff"
std::format("{:#b}", 5);              // "0b101"
std::format("{:+d}", 42);             // "+42"
```

Genişlik ve duyarlık, argümandan da alınabilir:

```cpp
std::format("{:{}.{}f}", 3.14159, 10, 2);      // genişlik 10, duyarlık 2
```

Akımlardaki manipülatörlerden farkı, **her yer tutucunun kendi biçimini taşımasıdır.**
Kalıcı durum yoktur; bir yerde yaptığınız ayar başka bir çağrıyı etkilemez.
