---
cilt: "I — Temel"
kisim: "27 — Eşzamanlılığa Giriş"
baslik: "27.1 İş parçacığı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 27.1 İş parçacığı

**İş parçacığı** *(thread)*, bir süreç içinde bağımsız çalışan yürütme akışıdır. Aynı
süreçteki iş parçacıkları **aynı belleği paylaşır**; bölümün bütün zorluğu buradan
doğar.

```cpp
#include <thread>

void is() { /* ... */ }

int main()
{
    std::thread t{is};
    t.join();
}
```

`join()`, iş parçacığının bitmesini bekler. `detach()` ise bağı koparır; iş parçacığı
arka planda devam eder.

**`join` veya `detach` çağırmadan `std::thread` nesnesinin hayatının bitmesi, programı
sonlandırır.** Sonlandırıcı işlev `std::terminate` çağırır.

`std::thread` kopyalamaya kapalı, taşımaya açıktır; bir iş parçacığının iki sahibi
olamaz.
