---
cilt: "I — Temel"
kisim: "10 — Tür Dönüştürme Operatörleri"
baslik: "10.6 Hangisini ne zaman"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 10.6 Hangisini ne zaman

| İhtiyaç | Operatör |
|---|---|
| Sayısal dönüşüm, `void*` çözme, ilişkili türler | `static_cast` |
| Yalnızca `const` eklemek veya kaldırmak | `const_cast` |
| İlgisiz gösterici türleri | `reinterpret_cast` |
| Hiyerarşide denetimli aşağı dönüşüm | `dynamic_cast` |

> **C tarzı dönüşüm kullanmayın.** Standart, C tarzı dönüşümün hangi biçimde
> yorumlanacağını şu sırayla belirler: `const_cast`; `static_cast`; `static_cast`
> ardından `const_cast`; `reinterpret_cast`; `reinterpret_cast` ardından `const_cast`.
> Hangisinin uygulandığı koddan okunmaz. Dört C++ tür dönüştürme operatöründen (Kısım
> 10.2–10.5) birini seçemiyorsanız, muhtemelen o dönüşümü hiç yapmamalısınız.
