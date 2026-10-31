---
cilt: "I — Temel"
kisim: "27 — Eşzamanlılığa Giriş"
baslik: "27.3 `mutex` ve `lock_guard`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 27.3 `mutex` ve `lock_guard`

Paylaşılan veriye erişimi senkronize etmenin en temel aracıdır.

```cpp
#include <mutex>

std::mutex m;
int paylasilan = 0;

void artir()
{
    std::lock_guard<std::mutex> kilit{m};
    ++paylasilan;
}       // kilit burada otomatik bırakılır
```

`std::lock_guard`, RAII uygular (bkz. Kısım 18.6): kurucu işlevinde kilidi alır,
sonlandırıcı işlevinde bırakır. Hata gönderilse bile kilit bırakılır.

> **`mutex` nesnesinin `lock()` ve `unlock()` işlevlerini doğrudan çağırmayın.** Arada
> bir `return` veya hata olursa kilit bırakılmaz ve program kilitlenir. Her zaman
> `lock_guard` veya `unique_lock` kullanın.

Kilitlediğiniz bölge **mümkün olduğunca dar** olmalıdır; kilit altında yapılan her iş,
diğer iş parçacıklarını bekletir.
