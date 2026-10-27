---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.2.3 Tür çıkarımının dört hâli"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

### 1.2.3 Tür çıkarımının dört hâli

`foo(T&& arg)` şablonuna dört farklı kategoride argüman geçirildiğinde `T` ve `arg` şu
değerleri alır:

```cpp
template<typename T>
void foo(T&& arg);
```

| Argüman | `T` | Çökme öncesi `arg` | Çökme sonrası `arg` |
|---|---|---|---|
| `Myclass m;` → `foo(m)` | `Myclass&` | `Myclass& &&` | `Myclass&` |
| `foo(Myclass{})` | `Myclass` | `Myclass&&` | `Myclass&&` |
| `const Myclass cm;` → `foo(cm)` | `const Myclass&` | `const Myclass& &&` | `const Myclass&` |
| `foo(std::move(cm))` | `const Myclass` | `const Myclass&&` | `const Myclass&&` |

Tablodan okunacak kural: **argüman L-Value ise `T` referans türüne çıkarılır, R-Value
ise referanssız çıkarılır.** Çökme kuralı gerisini halleder.

Sonuç olarak `T`'nin kendisi iki bilgiyi birden taşır: argümanın **L-Value mı R-Value mi**
olduğunu ve **cv nitelemesini** (`const`/`volatile`). PR-Value ile X-Value ayrımı
korunmaz; ikisi de aynı `T`'yi verir. Bölümün tamamı bu tek gözlemin üzerine kuruludur.
