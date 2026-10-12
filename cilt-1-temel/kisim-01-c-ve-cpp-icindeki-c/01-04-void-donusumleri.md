---
cilt: "I — Temel"
kisim: "1 — C ve C++ İçindeki C"
baslik: "1.4 `void*` dönüşümleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 1.4 `void*` dönüşümleri

C'de `void*` türünden herhangi bir nesne göstericisine örtülü dönüşüm vardır. C++'ta
yoktur.

```cpp
void* vp = malloc(100);
int* p = vp;                        // C'de geçerli, C++'ta sentaks hatası
int* p = static_cast<int*>(vp);     // C++'ta doğrusu
```

Bu, `malloc` kullanan C kodunun C++'ta derlenmemesinin en sık sebebidir.
