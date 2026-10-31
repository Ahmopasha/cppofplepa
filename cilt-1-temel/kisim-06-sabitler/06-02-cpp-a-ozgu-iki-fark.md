---
cilt: "I — Temel"
kisim: "6 — Sabitler"
baslik: "6.2 `const`luğu koruyan iki kural"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 6.2 `const`luğu koruyan iki kural

**`const T*` türünden `T*` türüne örtülü dönüşüm yoktur.** Böyle bir dönüşüm `const`luğun
sessizce delinmesine yol açardı; bu yüzden sentaks hatasıdır. C standardı da bu dönüşüme
izin vermez.

```cpp
const int* cp = &x;
int* p = cp;          // sentaks hatası
```

Aynı şekilde `const T&` türünden `T&` türüne de örtülü dönüşüm yoktur. Bu yüzden `const`
bir nesneyi `const` olmayan bir referansa bağlayamazsınız (bkz. Kısım 8.4).

**Yazı sabitlerinin türü `const char[N]`'dir.** Bu yüzden C++'ta yazı sabitini doğrudan
değiştirmeye çalışmak sentaks hatasıdır. `const_cast` ile (bkz. Kısım 10.3) denenirse
sentaks hatası oluşmaz, ama davranış tanımsızdır. C dilinde türü `char[N]`'dir, ama orada
da değiştirme girişimi tanımsızdır.

```cpp
"merhaba"[0] = 'M';         // C++'ta sentaks hatası
char* p = "merhaba";        // C++'ta sentaks hatası
const char* cp = "merhaba"; // doğrusu
```
