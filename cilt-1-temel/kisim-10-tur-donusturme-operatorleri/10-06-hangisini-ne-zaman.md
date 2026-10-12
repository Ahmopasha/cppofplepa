---
cilt: "I — Temel"
kisim: "10 — Tür Dönüştürme Operatörleri"
baslik: "10.6 Hangisini ne zaman"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 10.6 Hangisini ne zaman

| İhtiyaç | Operatör |
|---|---|
| Sayısal dönüşüm, `void*` çözme, ilişkili türler | `static_cast` |
| Yalnızca `const` eklemek veya kaldırmak | `const_cast` |
| İlgisiz gösterici türleri | `reinterpret_cast` |
| Hiyerarşide denetimli aşağı dönüşüm | `dynamic_cast` |

> **C tarzı dönüşüm kullanmayın.** Derleyici sırayla `const_cast`, `static_cast`,
> `reinterpret_cast` ve bunların birleşimlerini dener; hangisinin uygulandığını
> bilemezsiniz. Dördünden birini seçemiyorsanız, muhtemelen o dönüşümü hiç yapmamalısınız.
