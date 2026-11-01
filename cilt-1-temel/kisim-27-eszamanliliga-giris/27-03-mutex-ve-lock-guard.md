---
cilt: "I — Temel"
kisim: "27 — Eşzamanlılığa Giriş"
baslik: "27.3 `mutex` ve `lock_guard`"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
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

> **`mutex` nesnesinin `lock()` ve `unlock()` işlevlerini doğrudan çağırmayın.** Arada bir
> `return` olursa veya hata gönderilirse kilit bırakılmaz; kilidi bekleyen iş parçacıkları
> süresiz bekleyebilir. Ayrıca kilidi tutan iş parçacığının onu bırakmadan yeniden almaya
> çalışması, bırakmadan bitmesi ya da kilitli `mutex`'in yok edilmesi tanımsız
> davranıştır. Kilidin bırakılmasını güvenceye almak için her zaman `lock_guard`,
> `scoped_lock` (C++17'den itibaren) veya `unique_lock` kullanın (son ikisi için bkz. Cilt
> II, Kısım 15.3).

Kilitlediğiniz bölge **mümkün olduğunca dar** olmalıdır; kilit altında yapılan her iş,
diğer iş parçacıklarını bekletir.
