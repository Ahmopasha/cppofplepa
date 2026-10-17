---
cilt: "II — İleri"
kisim: "13 — İleri Hata Yönetimi"
baslik: "13.4 `std::exception_ptr`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 13.4 `std::exception_ptr`

Bir hatayı yakalayıp **işlemeyi başka bir yere ertelemenizi** sağlar. C++11 ile geldi.

<!-- kod-baglam
void riskli();
-->
```cpp
#include <exception>

std::exception_ptr tutulan;

try {
    riskli();
}
catch (...) {
    tutulan = std::current_exception();     // hatayı sakla
}

// ... başka bir zamanda, başka bir yerde
if (tutulan)
    std::rethrow_exception(tutulan);        // yeniden gönder
```

Üç işlev birlikte çalışır. `std::current_exception`, `catch` bloğu içinde çağrılır ve
işlenmekte olan hatayı bir nesnede tutar. `std::rethrow_exception` onu yeniden gönderir.
`std::make_exception_ptr` ise bir fabrika işlevidir; elinizdeki hata nesnesinden
doğrudan `exception_ptr` üretir.

Asıl kullanım alanı **iş parçacıkları arasıdır.** Bir iş parçacığında oluşan hata,
diğerine sıçramaz; `std::future` mekanizması hatayı `exception_ptr` olarak taşır ve
`get()` çağrıldığında yeniden gönderir (bkz. Kısım 15).
