---
cilt: "I — Temel"
kisim: "7 — Varsayılan Argümanlar"
baslik: "7.2 Üç kural"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 7.2 Üç kural

**Varsayılan argüman alan parametreden sonraki bütün parametreler de varsayılan argüman
almalıdır.**

```cpp
void f1(int a, int b = 10, int c = 20);     // geçerli
void f2(int a = 10, int b, int c);          // sentaks hatası
```

Sebep basittir: argümanlar soldan sağa eşleştirilir, aradaki bir argüman atlanamaz.

**Aradaki argümanı atlayamazsınız.**

```cpp
f1(1, , 30);      // böyle bir yazım yok
f1(1, 10, 30);    // ortadakini yazmak zorundasınız
```

**Varsayılan argüman bir kez yazılır.** Hem bildirimde hem tanımda yazmak sentaks
hatasıdır. Yeri bildirimdir; yani başlık dosyası.

```cpp
// baslik.h
void yazdir(const std::string& s, char ayirici = '\n');

// kaynak.cpp
void yazdir(const std::string& s, char ayirici) { /* ... */ }
```
