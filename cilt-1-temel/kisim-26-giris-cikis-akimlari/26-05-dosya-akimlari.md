---
cilt: "I — Temel"
kisim: "26 — Giriş–Çıkış Akımları"
baslik: "26.5 Dosya akımları"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 26.5 Dosya akımları

```cpp
#include <fstream>

std::ofstream cikis{"veri.txt"};
if (!cikis) { /* açılamadı */ }

cikis << "merhaba\n";
// sonlandırıcı işlev dosyayı kapatır — close() çağırmaya gerek yok
```

Dosya akımları RAII uygular (bkz. Kısım 18.6); nesnenin hayatı bittiğinde dosya kapanır.

Açma kipleri `|` ile birleştirilir:

```cpp
std::ofstream log{"log.txt", std::ios::app};        // sona ekle
std::fstream f{"veri.bin", std::ios::in | std::ios::out | std::ios::binary};
```

Dosyanın açılıp açılmadığını **her zaman denetleyin**; açılmamış bir akıma yazmak sessizce
başarısız olur.
