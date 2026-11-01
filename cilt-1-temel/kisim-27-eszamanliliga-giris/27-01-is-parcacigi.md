---
cilt: "I — Temel"
kisim: "27 — Eşzamanlılığa Giriş"
baslik: "27.1 İş parçacığı"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
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

**Bir iş parçacığını temsil eden (`joinable()`) bir `std::thread` nesnesinin hayatı `join`
veya `detach` çağrılmadan biterse program sonlanır:** nesnenin sonlandırıcı işlevi
`std::terminate` işlevini çağırır. Böyle bir nesneye taşıyarak atama yapmak da aynı sonucu
doğurur. Taşınmış ya da varsayılan kurulmuş nesne bir iş parçacığını temsil etmez.

`std::thread` kopyalamaya kapalı, taşımaya açıktır; bir iş parçacığının iki sahibi
olamaz.
