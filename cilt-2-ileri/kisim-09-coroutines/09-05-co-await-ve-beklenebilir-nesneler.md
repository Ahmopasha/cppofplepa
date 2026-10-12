---
cilt: "II — İleri"
kisim: "9 — Coroutines"
baslik: "9.5 `co_await` ve beklenebilir nesneler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 9.5 `co_await` ve beklenebilir nesneler

`co_await` operatörünün operandı bir **beklenebilir** *(awaitable)* nesne olmalıdır.
Beklenebilir bir nesne, üç üye işlev sunar:

```cpp
struct Bekleyici {
    bool await_ready();                                 // hemen hazır mı
    void await_suspend(std::coroutine_handle<> h);      // askıya alınırken
    void await_resume();                                // devam ederken
};
```

Sıra şudur. `await_ready` doğru dönerse askıya alma hiç olmaz; sonuç hazırdır.
Yanlış dönerse `await_suspend` çağrılır ve eşyordam askıya alınır; tutamak o işleve
verilir, böylece istediğiniz zaman devam ettirebilirsiniz. Devam edildiğinde
`await_resume` çağrılır ve döndürdüğü değer `co_await` ifadesinin değeri olur.

C++20 iki hazır beklenebilir sunar: `std::suspend_always` her zaman askıya alır,
`std::suspend_never` hiç almaz.

`operator co_await` yüklenerek, bir türün `co_await` operandı olması da sağlanabilir.
