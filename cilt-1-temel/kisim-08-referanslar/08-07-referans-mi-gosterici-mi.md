---
cilt: "I — Temel"
kisim: "8 — Referanslar"
baslik: "8.7 Referans mı gösterici mi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 8.7 Referans mı gösterici mi

| | Gösterici | Referans |
|---|---|---|
| İlk değer verme | isteğe bağlı | **zorunlu** |
| Sonradan başkasına bağlama | mümkün | **mümkün değil** |
| Hiçbir şey göstermeme | `nullptr` | **mümkün değil** |
| Kendisine gösterici/referans | `T**` geçerli | `T& &` **geçersiz** |
| Dizisi | `T*[N]` geçerli | `T&[N]` **geçersiz** |
| Nesne midir | evet | hayır, isimdir |

Seçim kuralı şudur:

> **Referans kullanabildiğiniz her yerde referans, zorunda kaldığınız yerde gösterici
> kullanın.**

Göstericiye zorunda kaldığınız durumlar bellidir: bağlantının isteğe bağlı olması
gerekiyorsa (yokluğu `nullptr` ile ifade edilir), sonradan başka bir nesneye
yönlendirmeniz gerekiyorsa, ya da bir dizide tutmanız gerekiyorsa.
