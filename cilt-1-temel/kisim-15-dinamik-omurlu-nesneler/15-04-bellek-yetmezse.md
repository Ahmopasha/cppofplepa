---
cilt: "I — Temel"
kisim: "15 — Dinamik Ömürlü Nesneler"
baslik: "15.4 Bellek yetmezse"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 15.4 Bellek yetmezse

Sıradan `new` ifadesi, bellek ayıramazsa `std::bad_alloc` ile yakalanabilen bir hata
gönderir (hata gönderme ve yakalama: Kısım 18). Bu biçim geriye `nullptr` döndürmez; C
alışkanlığıyla dönüş değerini denetlemek anlamsızdır. Bellek ayıramadığında hata göndermek
yerine `nullptr` döndüren biçimi (`new (std::nothrow)`) aşağıda göreceğiz.

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
