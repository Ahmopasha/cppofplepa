---
cilt: "I — Temel"
kisim: "1 — C ve C++ İçindeki C"
baslik: "1.5 `NULL` ve `nullptr`"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 1.5 `NULL` ve `nullptr`

C'de `NULL`, gerçeklemeye bağlı (bkz. Kısım 2.5) bir **boş gösterici sabitine**
*(null pointer constant)* genişleyen bir makrodur; `0` ya da `(void*)0` gibi bir sabit
olabilir. C++'ta da gerçeklemeye bağlıdır, ama `(void*)0` olamaz (bkz. Kısım 1.4); `0` ya
da `0L` gibi bir tanım alır.

Bu, işlev yüklemesinde (bkz. Kısım 9) sorun yaratır; sonuç `NULL`'ın tanımına bağlıdır ve
niyet edilen `func(char*)` seçilmeyebilir. `NULL` `0` ise `func(NULL)` çağrısı `func(0)`
gibi, `0L` ise `func(0L)` gibi davranır:

```cpp
void func(int);
void func(char*);

func(0);           // func(int), gösterici yüklemesi değil
func(0L);          // sentaks hatası: çağrı belirsiz
```

C++11 bu sorunu çözmek için `nullptr` anahtar sözcüğünü ekledi. Türü `std::nullptr_t`'dir;
göstericilere örtülü dönüşümü vardır, tamsayılara yoktur.

```cpp
func(nullptr);     // func(char*) — belirsizlik yok
```

> Yeni kodda `NULL` kullanmayın. `nullptr`, hem belirsizliği ortadan kaldırır hem niyeti
> açıkça yazar.
