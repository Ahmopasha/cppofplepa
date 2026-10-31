---
cilt: "I — Temel"
kisim: "15 — Dinamik Ömürlü Nesneler"
baslik: "15.4 Bellek yetmezse"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 15.4 Bellek yetmezse

`new`, bellek ayıramazsa `std::bad_alloc` gönderir. Geriye `nullptr` döndürmez; C
alışkanlığıyla dönüş değerini denetlemek anlamsızdır.

```cpp
try {
    int* p = new int[1'000'000'000];
}
catch (const std::bad_alloc& ex) {
    // ...
}
```

Hata göndermeyen bir biçimi de vardır:

```cpp
int* p = new (std::nothrow) int[1'000'000'000];

if (!p) { /* ayrılamadı */ }
```

Pratikte bellek yetmezliğinden kurtulmak çoğu uygulamada mümkün değildir; bu hatayı
yakalamak yerine programın düzgün sonlanmasını sağlamak daha gerçekçidir.
