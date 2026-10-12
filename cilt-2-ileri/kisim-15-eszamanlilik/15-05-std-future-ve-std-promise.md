---
cilt: "II — İleri"
kisim: "15 — Eşzamanlılık"
baslik: "15.5 `std::future` ve `std::promise`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 15.5 `std::future` ve `std::promise`

İki iş parçacığı arasında **tek seferlik bir değer kanalı** kurar. `promise` yazan
taraftır, `future` okuyan.

```cpp
#include <future>

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

`get()` yalnızca bir kez çağrılabilir. Birden fazla okuyucu gerekiyorsa `std::shared_future`
kullanılır.

**Hata da bu kanaldan taşınır.** Üretici tarafta oluşan bir hata `set_exception` ile
gönderilir ve `get()` çağrısında yeniden fırlatılır. Bu, Kısım 13.4'teki
`std::exception_ptr` mekanizmasının uygulamasıdır; iş parçacığı sınırını aşan tek hata
taşıma yolu budur.
