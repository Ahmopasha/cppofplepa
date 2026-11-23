---
cilt: "I — Temel"
kisim: "26 — Giriş–Çıkış Akımları"
baslik: "26.4 Manipülatörler"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 26.4 Manipülatörler

**Manipülatörler** *(manipulators)*, akım işlemine (`<<` ya da `>>`) katılarak akımın
ayarlarını değiştiren ya da akımda bir iş yapan (ör. `std::endl`) işlev ya da nesnelerdir.
`std::hex` gibi argümansız biçim ayarları `<ios>`, `std::setw` gibi argüman alanlar
`<iomanip>`, `std::endl` `<ostream>` başlığındadır.

```cpp
#include <iomanip>

std::cout << std::setw(10) << std::setfill('.') << 42 << '\n';
std::cout << std::fixed << std::setprecision(2) << 3.14159 << '\n';
std::cout << std::hex << 255 << '\n';
std::cout << std::boolalpha << true << '\n';
```

Biçim ayarları **kalıcıdır**: sonraki işlemleri etkiler. İstisnası **alan genişliğidir**
*(field width)*: `std::setw` yalnızca bir sonraki değerin yazımına (örnekte `42`) ya da
`>>` ile bir sonraki `std::string` ya da `char` dizisi okumasına uygulanır; sayı okuması
onu kullanmaz.

`std::endl` ile `'\n'` arasındaki fark bilinmelidir: `std::endl` satır sonu yazar
**ve tamponu boşaltır.** Boşaltma maliyetlidir; döngü içinde `std::endl` kullanmayın,
`'\n'` yeterlidir.
