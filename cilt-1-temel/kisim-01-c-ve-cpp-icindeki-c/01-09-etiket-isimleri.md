---
cilt: "I — Temel"
kisim: "1 — C ve C++ İçindeki C"
baslik: "1.9 Etiket isimleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 1.9 Etiket isimleri

C'de `struct`, `union` ve `enum` isimleri ayrı bir isim uzayındadır ve kullanırken
anahtar sözcüğü tekrarlamak gerekir.

```c
struct Nokta { int x, y; };
struct Nokta n;        // C'de "struct" zorunlu
```

C++'ta tür ismi doğrudan kullanılır:

```cpp
Nokta n;               // C++'ta yeterli
```

Bu yüzden C kodunda sık görülen `typedef struct Nokta Nokta;` yazımı C++'ta gereksizdir.
