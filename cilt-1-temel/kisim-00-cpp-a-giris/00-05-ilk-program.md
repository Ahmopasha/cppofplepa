---
cilt: "I — Temel"
kisim: "0 — C++'a Giriş"
baslik: "0.5 İlk program"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 0.5 İlk program

```cpp
#include <iostream>

int main()
{
    std::cout << "Merhaba\n";
}
```

`main` işlevinin geri dönüş türü `int` olmak zorundadır ve `void` olamaz. `return`
yazmazsanız derleyici `return 0;` varsayar; `main` bu ayrıcalığa sahip tek işlevdir.

`std::cout` ve akım mekanizması Kısım 26'nın konusudur; buradaki kullanım yeterlidir.
