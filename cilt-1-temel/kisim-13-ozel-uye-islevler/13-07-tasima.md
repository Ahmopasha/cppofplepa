---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.7 Taşıma"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 13.7 Taşıma

Kaynağı artık kullanılmayacak bir nesneden (örneğin geçici bir nesneden) kopyalamak yerine
kaynağını **devralmak** daha ucuzdur. Buna **taşıma** *(move)* denir.

```cpp
class Yazi {
    char* p;
public:
    Yazi(Yazi&& other) noexcept : p{ other.p }      // kaynağı devral
    {
        other.p = nullptr;                          // other artık kaynağı göstermez
    }
    ~Yazi() { delete[] p; }
};
```

`noexcept`, işlevin hata göndermeyeceğini (Kısım 18) bildirir; taşımadaki önemi Cilt II,
Kısım 13.2'dedir.

Taşıyan işlevin iki görevi vardır ve ikisi de zorunludur (taşıyan atama işlevi ayrıca
hedef nesnenin eski kaynağını sızdırmaz: ya serbest bırakır ya da kaynağı devralınmış
nesneye verir): kaynağı almak, ve kaynağı devralınmış nesneyi geçerli bir durumda, en
azından **sonlandırıcı işlevi güvenle çalışabilecek** ve yeniden atanabilecek biçimde
bırakmak (Kısım 2.4.7). İkincisini ihmal ederseniz aynı belleği iki kez serbest
bırakırsınız; bu tanımsız davranıştır.

Kopyalama ya da taşıma işlevlerinden biri çağrılacaksa (aynı türden bir PR-Value'dan ilk
değer verilirken hiçbiri çağrılmaz, Kısım 13.3), taşıyan işlevler, argüman `const` olmayan
bir R-Value olduğunda seçilir (`const` bir R-Value'da kopyalayan işlev seçilir, Kısım
13.12). Bir L-Value'yu taşıtmak istiyorsanız `std::move` ile işaretlersiniz (Kısım 2.4.7).

**Taşıyan işlev hiç bildirilmemişse kopyalayan işlev çağrılır** (Kısım 13.8; tam tablo
Cilt II, Kısım 2.2). Taşıma bir iyileştirmedir; yokluğunda, kopyalayan işlev
kullanılabiliyorsa program yanlış çalışmaz, en fazla daha yavaş çalışır (kopyalayan işlev
de silinmişse çağrı sentaks hatasıdır). Taşıyan işlev silinmiş (`= delete`, Kısım 13.10)
olarak bildirilmişse ise çağrı sentaks hatasıdır.
