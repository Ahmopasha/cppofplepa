---
cilt: "II — İleri"
kisim: "15 — Eşzamanlılık"
baslik: "15.7 `std::packaged_task`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 15.7 `std::packaged_task`

Bir çağrılabilir nesneyi sarmalar ve sonucunu bir `future` üzerinden sunar. `async`'ten
farkı, **ne zaman çalışacağına siz karar verirsiniz.**

```cpp
std::packaged_task<int()> gorev{[] { return 42; }};
std::future<int> f = gorev.get_future();

std::jthread t{std::move(gorev)};     // istediğiniz yerde çalıştırın
int sonuc = f.get();
```

İş parçacığı havuzu kurarken temel yapı taşıdır: görevler `packaged_task` olarak
kuyruğa konur, havuzdaki iş parçacıkları sırayla alıp çalıştırır.
