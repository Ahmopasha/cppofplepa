---
cilt: "I — Temel"
kisim: "11 — `inline`"
baslik: "11.1 Çözdüğü problem"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 11.1 Çözdüğü problem

Kısım 2.7'deki ODR şunu söylüyordu: bütün programda, kullanılan her `inline` olmayan
işlevin **tam olarak bir** tanımı bulunmalıdır.

Bu kural, işlev tanımlarını başlık dosyasına koymanızı engeller. Başlık iki kaynak dosyaya
dahil edilirse iki tanım oluşur ve program hatalıdır; standart, gerçeklemenin bunu
bildirmesini istemez, ama bağlama adımı bunu bildirebilir (Kısım 0.3).

```cpp
// yardimci.h
int kare(int x) { return x * x; }    // tanım

// a.cpp: #include "yardimci.h"
// b.cpp: #include "yardimci.h"
// → program hatalı: kare iki kez tanımlandı
```

`inline` anahtar sözcüğü bu kısıtı kaldırır:

```cpp
inline int kare(int x) { return x * x; }
```

Artık işlev birden fazla çeviri biriminde tanımlanabilir. Karşılığında iki koşul gelir:
**bütün tanımlar birbirinin aynısı olmak zorundadır** (Kısım 2.7), ve işlevin tanımı onu
kullanan her çeviri biriminde bulunmalıdır. Koşullardan biri sağlanmazsa program
hatalıdır; tanımlar aynı değilse standart, gerçeklemenin bunu bildirmesini de istemez.
Aynı başlık dosyasını her yerde dahil ederek bu koşulları çoğunlukla sağlarsınız; yeter ki
başlığın içeriği çeviri birimine göre değişmesin.
