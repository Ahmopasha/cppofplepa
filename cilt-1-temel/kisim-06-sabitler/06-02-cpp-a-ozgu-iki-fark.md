---
cilt: "I — Temel"
kisim: "6 — Sabitler"
baslik: "6.2 C++'a özgü iki fark"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 6.2 C++'a özgü iki fark

**`const T*` türünden `T*` türüne örtülü dönüşüm yoktur.** C dilinde bu dönüşüm
serbesttir ve `const`luğun sessizce delinmesine yol açar; C++ sentaks hatası verir.

```cpp
const int* cp = &x;
int* p = cp;          // C'de derlenir, C++'ta sentaks hatası
```

Aynı şekilde `const T&` türünden `T&` türüne de dönüşüm yoktur. Bu yüzden `const` bir
nesneyi `const` olmayan bir referansa bağlayamazsınız (bkz. Kısım 8.4).

**Yazı sabitlerinin türü `const char[N]`'dir.** C dilinde `char[N]`'dir. C++'ta yazı
sabitini değiştirmeye çalışan kod derlenmez.

```cpp
char* p = "merhaba";        // C++'ta sentaks hatası
const char* cp = "merhaba"; // doğrusu
```
