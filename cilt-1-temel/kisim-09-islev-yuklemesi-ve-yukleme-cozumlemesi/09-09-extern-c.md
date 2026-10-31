---
cilt: "I — Temel"
kisim: "9 — İşlev Yüklemesi ve Yükleme Çözümlemesi"
baslik: "9.9 `extern \"C\"`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 9.9 `extern "C"`

İşlev yüklemesi, C++ derleyicisinin işlev isimlerini imzayla birlikte kodlaması sayesinde
mümkündür; buna *name mangling* denir. C dilinde yükleme olmadığı için bu kodlama yapılmaz.

C ile yazılmış bir kütüphanenin işlevlerini kullanırken bağlayıcının ismi C biçiminde
aramasını sağlamak gerekir:

<!-- kod: atla -->
```cpp
extern "C" void c_islevi(int);

extern "C" {
    #include "c_kutuphanesi.h"
}
```

`extern "C"` bildirilen işlevler yüklenemez; C tarafında aynı isimden yalnızca bir tane
olabilir.
