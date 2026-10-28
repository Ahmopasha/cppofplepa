---
cilt: "II — İleri"
kisim: "15 — Eşzamanlılık"
baslik: "15.5 `std::future` ve `std::promise`"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 15.5 `std::future` ve `std::promise`

İki iş parçacığı arasında **tek seferlik bir değer kanalı** kurar. `promise` yazan
taraftır, `future` okuyan.

```cpp
#include <future>
#include <thread>
#include <utility>

void uretici(std::promise<int> p)
{
    p.set_value(42);
}

int main()
{
    std::promise<int> p;
    std::future<int> f = p.get_future();

    std::jthread t{uretici, std::move(p)};

    int sonuc = f.get();      // değer gelene kadar bloklar
}
```

**Hata da bu kanaldan taşınır.** Üretici tarafta oluşan bir hata `set_exception` ile
saklanır ve `get()` çağrısında yeniden gönderilir. Bu, Kısım 13.4'teki
`std::exception_ptr` mekanizmasının hazır bir uygulamasıdır. Tek yol değildir:
`exception_ptr`, senkronizasyonla korunan sıradan bir değişkenle de başka bir iş
parçacığına aktarılabilir. `std::thread` ya da `std::jthread`'e verilen işlevden
yakalanmadan kaçan hatada ise `std::terminate` çağrılır.
