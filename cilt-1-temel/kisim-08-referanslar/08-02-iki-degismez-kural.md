---
cilt: "I — Temel"
kisim: "8 — Referanslar"
baslik: "8.2 İki değişmez kural"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 8.2 İki değişmez kural

**Referansa ilk değer vermek zorunludur.**

```cpp
int& r;      // sentaks hatası
```

**Referans bir kez bağlandıktan sonra başka bir nesneye bağlanamaz.** Sonraki atamalar
referansa değil, bağlandığı nesneye yapılır.

```cpp
int x = 10, y = 99;
int& r = x;

r = y;           // x'e 99 atandı; r hâlâ x'i gösteriyor
std::cout << x;  // 99
```

Bu iki kuralın sonucu şudur: **geçersiz referans diye bir şey yoktur.** Gösterici
`nullptr` tutabilir, referans hiçbir şeye bağlanmamış olamaz. Referans kullanabildiğiniz
her yerde bir denetim satırından kurtulmuş olursunuz.
