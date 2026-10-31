---
cilt: "I — Temel"
kisim: "0 — C++'a Giriş"
baslik: "0.4 Başlık ve kaynak dosya ayrımı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 0.4 Başlık ve kaynak dosya ayrımı

Kısım 2.1'deki bildirim/tanım ayrımının pratik karşılığı budur.

**Başlık dosyasına** konanlar: bildirimler, sınıf tanımları, `inline` işlevler, şablonlar,
`constexpr` işlevler.

**Kaynak dosyaya** konanlar: `inline` olmayan işlev tanımları, `static` veri elemanlarının
tanımları, yalnızca o dosyaya ait yardımcılar (bkz. Kısım 16.4).

Başlık dosyalarının birden fazla kez dahil edilmesini engellemek için koruma kullanılır:

```cpp
#ifndef MYCLASS_H
#define MYCLASS_H
// ...
#endif
```

Standart olmasa da bütün derleyicilerin desteklediği kısa yazım:

```cpp
#pragma once
```
