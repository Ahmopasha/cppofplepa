---
cilt: "I — Temel"
kisim: "11 — `inline`"
baslik: "11.1 Çözdüğü problem"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 11.1 Çözdüğü problem

Kısım 2.7'deki ODR şunu söylüyordu: bütün programda, kullanılan her `inline` olmayan
işlevin **tam olarak bir** tanımı bulunmalıdır.

Bu kural, işlev tanımlarını başlık dosyasına koymanızı engeller. Başlık iki kaynak
dosyaya dahil edilirse iki tanım oluşur ve bağlayıcı hata verir.

```cpp
// yardimci.h
int kare(int x) { return x * x; }    // tanım

// a.cpp: #include "yardimci.h"
// b.cpp: #include "yardimci.h"
// → bağlayıcı hatası: kare iki kez tanımlandı
```

`inline` anahtar sözcüğü bu kısıtı kaldırır:

```cpp
inline int kare(int x) { return x * x; }
```

Artık işlev birden fazla çeviri biriminde tanımlanabilir. Karşılığındaki koşul ODR'nin
ikinci yarısıdır: **bütün tanımlar birbirinin aynısı olmak zorundadır.** Aynı başlık
dosyasını her yerde dahil ederek bunu zaten sağlarsınız.
