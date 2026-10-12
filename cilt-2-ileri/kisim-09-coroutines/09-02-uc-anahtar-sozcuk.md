---
cilt: "II — İleri"
kisim: "9 — Coroutines"
baslik: "9.2 Üç anahtar sözcük"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 9.2 Üç anahtar sözcük

Bir işlevi eşyordam yapan şey, bildiriminde değil **gövdesindedir**. Gövdede şu üç
anahtar sözcükten biri geçiyorsa, derleyici o işlevi eşyordam olarak ele alır.

| Anahtar sözcük | Ne yapar |
|---|---|
| `co_await` | Akışı askıya alır; bir sonuç bekler |
| `co_yield` | Akışı askıya alır **ve** bir değer üretir |
| `co_return` | Eşyordamı bitirir |

`co_yield`, `co_await`'in bir kısaltmasıdır; ürettiği değeri çağırana ilettikten sonra
askıya alır.

Bunun bir sonucu, eşyordam olup olmamanın **arayüzden görünmemesidir.** İşlevin
bildirimine bakarak anlayamazsınız; tanımını görmeniz gerekir. Notlarda bu durum
*opaque* olarak nitelendirilmiş.

İkinci sonucu, eşyordamların bazı şeyleri yapamamasıdır: `main` işlevi, kurucu işlevler,
sonlandırıcı işlevler ve `constexpr` işlevler eşyordam olamaz.
