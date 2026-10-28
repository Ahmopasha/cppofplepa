---
cilt: "II — İleri"
kisim: "15 — Eşzamanlılık"
baslik: "15.2 İş parçacığı yönetimi"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 15.2 İş parçacığı yönetimi

Cilt I, Kısım 27.1'de `std::thread` tanıtılmıştı. Bir iş parçacığını temsil eden
(`joinable()`) bir `std::thread` nesnesinin hayatı `join` veya `detach` çağrılmadan
biterse `std::terminate` çağrılır. Bu kural pratikte sık ihlal edilir; araya bir hata
girdiğinde `join` çağrısına hiç gelinmez.

C++20 bunu çözen bir tür ekledi:

```cpp
#include <thread>

void is(std::stop_token st)
{
    while (!st.stop_requested()) { /* ... */ }
}

int main()
{
    std::jthread t{is};
    // sonlandırıcı işlev önce stop ister, sonra join eder
}
```

`std::jthread`, sonlandırıcı işlevinde otomatik olarak `join` eder; RAII'yi iş parçacığı
yönetimine uygular. Ayrıca **iptal desteği** getirir: `std::stop_token` üzerinden iş
parçacığına durma isteği iletilir.

> Yeni kodda `std::jthread` kullanın. `std::thread`, ancak iptal ve otomatik birleşme
> istemediğiniz özel durumlarda gerekir.
