---
cilt: "II — İleri"
kisim: "15 — Eşzamanlılık"
baslik: "15.4 `std::condition_variable`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 15.4 `std::condition_variable`

Bir iş parçacığının, belirli bir koşul sağlanana kadar beklemesini sağlar. Meşgul bekleme
*(busy wait)* yerine iş parçacığı uyutulur.

```cpp
#include <condition_variable>

std::mutex m;
std::condition_variable cv;
bool hazir = false;

void bekleyen()
{
    std::unique_lock kilit{m};
    cv.wait(kilit, [] { return hazir; });      // koşullu bekleme
    // hazir artık true ve kilit elimizde
}

void bildiren()
{
    { std::lock_guard kilit{m}; hazir = true; }
    cv.notify_one();
}
```

Üç nokta önemlidir.

**`std::unique_lock` gerekir**, `lock_guard` yetmez; `wait` çağrısı kilidi geçici olarak
bırakır ve uyandığında yeniden alır.

**Koşul yüklemi yazılmalıdır.** İkinci parametresiz `wait` biçimi, *yalancı uyanma*
*(spurious wakeup)* durumunda hatalı devam eder. Yüklemli biçim, uyandığında koşulu
yeniden denetler.

**Koşulu değiştiren kod kilit altında olmalıdır**, aksi hâlde bildirim kaçırılabilir.

`notify_one` bir bekleyeni, `notify_all` hepsini uyandırır.
