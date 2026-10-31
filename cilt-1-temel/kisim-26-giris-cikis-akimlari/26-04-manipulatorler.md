---
cilt: "I — Temel"
kisim: "26 — Giriş–Çıkış Akımları"
baslik: "26.4 Manipülatörler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 26.4 Manipülatörler

Akımın davranışını değiştiren nesnelerdir. Çoğu `<iomanip>` başlığındadır.

```cpp
#include <iomanip>

std::cout << std::setw(10) << std::setfill('.') << 42 << '\n';
std::cout << std::fixed << std::setprecision(2) << 3.14159 << '\n';
std::cout << std::hex << 255 << '\n';
std::cout << std::boolalpha << true << '\n';
```

Çoğu manipülatör **kalıcıdır**; bir kez ayarlandığında sonraki işlemleri de etkiler.
İstisnası `setw`'dir, yalnızca bir sonraki işleme uygulanır.

`std::endl` ile `'\n'` arasındaki fark bilinmelidir: `endl` satır sonu yazar **ve tamponu
boşaltır.** Boşaltma maliyetlidir; döngü içinde `endl` kullanmayın, `'\n'` yeterlidir.
