---
cilt: "I — Temel"
kisim: "1 — C ve C++ İçindeki C"
baslik: "1.5 `NULL` ve `nullptr`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 1.5 `NULL` ve `nullptr`

C'de `NULL`, `0` veya `(void*)0` olarak tanımlanmış bir makrodur. C++'ta `(void*)0`
tanımı geçersizdir (bkz. 1.4), dolayısıyla `NULL` yalnızca `0`'dır.

Bu, işlev yüklemesinde belirsizlik yaratır:

```cpp
void func(int);
void func(char*);

func(NULL);        // hangisi? NULL bir tamsayı sabiti
```

C++11 bu sorunu çözmek için `nullptr` anahtar sözcüğünü ekledi. Türü `std::nullptr_t`'dir
ve yalnızca göstericilere dönüşür.

```cpp
func(nullptr);     // func(char*) — belirsizlik yok
```

> Yeni kodda `NULL` kullanmayın. `nullptr`, hem belirsizliği ortadan kaldırır hem niyeti
> açıkça yazar.
