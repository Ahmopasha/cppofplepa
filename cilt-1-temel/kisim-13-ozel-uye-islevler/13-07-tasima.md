---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.7 Taşıma"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 13.7 Taşıma

Kopyalanacak nesnenin hayatının biteceği garanti ise, kaynağını kopyalamak yerine
**devralmak** daha ucuzdur. Buna taşıma denir.

```cpp
class Yazi {
    char* p;
public:
    Yazi(Yazi&& other) noexcept : p{ other.p }      // kaynağı devral
    {
        other.p = nullptr;                          // kaynağı bırak
    }
};
```

Taşıyan işlevin iki görevi vardır ve ikisi de zorunludur: kaynağı almak, ve kaynağı
alınan nesneyi **sonlandırıcı işlevi güvenle çalışabilecek** bir duruma getirmek.
İkincisini ihmal ederseniz aynı belleği iki kez serbest bırakırsınız.

Taşıyan işlevler, argüman bir R-Value olduğunda seçilir. Bir L-Value'yu taşıtmak
istiyorsanız `std::move` ile işaretlersiniz (bkz. Kısım 2.4.7).

**Taşıyan işlev yoksa kopyalayan işlev çağrılır.** Taşıma bir iyileştirmedir; yokluğunda
program yanlış çalışmaz, yalnızca yavaş çalışır.
