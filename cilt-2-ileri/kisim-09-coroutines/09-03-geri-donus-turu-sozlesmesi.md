---
cilt: "II — İleri"
kisim: "9 — Coroutines"
baslik: "9.3 Geri dönüş türü sözleşmesi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 9.3 Geri dönüş türü sözleşmesi

Eşyordamın geri dönüş türü sıradan bir tür olamaz. Derleyicinin makineyi kurabilmesi
için, o türün **belirli bir sözleşmeyi** sağlaması gerekir.

Geri dönüş türü, `promise_type` adında içsel bir tür barındırmalıdır. Derleyici bütün
işlemleri o tür üzerinden yürütür.

```cpp
struct Generator {
    struct promise_type {
        int deger;

        Generator get_return_object();
        std::suspend_always initial_suspend()       { return {}; }
        std::suspend_always final_suspend() noexcept { return {}; }
        void unhandled_exception()                   { std::terminate(); }
        std::suspend_always yield_value(int v)       { deger = v; return {}; }
        void return_void()                           { }
    };

    std::coroutine_handle<promise_type> tutamac;
};
```

Her üyenin bir görevi vardır:

| Üye | Ne zaman çağrılır |
|---|---|
| `get_return_object` | Eşyordam nesnesi çağırana döndürülürken |
| `initial_suspend` | Gövde çalışmaya başlamadan önce |
| `final_suspend` | Gövde bittikten sonra |
| `unhandled_exception` | Gövdede yakalanmamış hata oluştuğunda |
| `yield_value` | `co_yield` kullanıldığında |
| `return_value` / `return_void` | `co_return` kullanıldığında |

`initial_suspend`'ın `std::suspend_always` döndürmesi, eşyordamın **tembel** çalışacağı
anlamına gelir; ilk `resume` çağrısına kadar gövde işlemez. `std::suspend_never`
döndürürse hemen başlar.

Bu sözleşme, C++'ın "kütüphane yazarına mekanizma ver, politikayı ona bırak" yaklaşımının
belki en uç örneğidir. Dil eşyordam makinesini sağlar; o makinenin nasıl davranacağını
`promise_type` belirler.
