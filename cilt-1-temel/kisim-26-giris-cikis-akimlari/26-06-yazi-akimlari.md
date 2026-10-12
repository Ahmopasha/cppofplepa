---
cilt: "I — Temel"
kisim: "26 — Giriş–Çıkış Akımları"
baslik: "26.6 Yazı akımları"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 26.6 Yazı akımları

Bellekteki bir yazıyı akım gibi kullanmaya yarar. Metin ayrıştırma ve biçimlendirme için
kullanılır.

```cpp
#include <sstream>

std::istringstream giris{"42 3.14 merhaba"};
int i; double d; std::string s;
giris >> i >> d >> s;

std::ostringstream cikis;
cikis << "deger: " << 42;
std::string sonuc = cikis.str();
```
