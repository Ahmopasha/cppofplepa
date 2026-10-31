---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.4.5 Referans bağlama kuralları"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

### 2.4.5 Referans bağlama kuralları

Bölümün asıl işe yarar kısmı burasıdır. Üç referans türü ve bağladıkları:

| Referans | Neyi bağlar | Neyi bağlamaz |
|---|---|---|
| `T&` | const olmayan L-Value | R-Value, const L-Value |
| `const T&` | **her şeyi** | — |
| `T&&` | const olmayan R-Value | L-Value |

Başlangıçtaki dört satır artık açıklanabilir:

```cpp
int x = 10;

int& a = x;           // OK    — T& referansa L-Value
int& b = 10;          // HATA  — T& referansa R-Value bağlanamaz
const int& c = 10;    // OK    — const T& her şeyi bağlar
int&& d = x;          // HATA  — T&& referansa L-Value bağlanamaz
```

`const T&`'nin R-Value bağlayabilmesinin sebebi şudur: derleyici arka planda geçici bir
nesne oluşturur ve referansı ona bağlar. Referansın kapsamı bittiğinde geçici nesnenin
de ömrü biter. Bu mekanizma Kısım 8'de ayrıntılandırılıyor.

Referans türü ile bağlanacak nesnenin türü aynı olmak zorundadır. Bu kuralın istisnası
yine `const` referanslardır:

```cpp
int ival = 100;

double& dr = ival;         // HATA — tür uyuşmazlığı
const double& cdr = ival;  // OK   — geçici nesne oluşturulur
```
