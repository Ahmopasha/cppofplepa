---
cilt: "II — İleri"
kisim: "10 — `std::format`"
baslik: "10.4 Kendi türünüz için biçimlendirici"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 10.4 Kendi türünüz için biçimlendirici

Kullanıcı tanımlı bir türü `std::format` ile kullanmak için `std::formatter` şablonunun o
tür için özelleştirilmesi gerekir. Bu, Cilt II Kısım 14.7'deki `std::hash`
özelleştirmesiyle aynı mekanizmadır.

İki üye işlev yazılır: `parse` biçim belirtecini okur, `format` çıktıyı üretir.

```cpp
struct Kesir { int pay, payda; };

template<>
struct std::formatter<Kesir> {
    constexpr auto parse(std::format_parse_context& ctx)
    {
        return ctx.begin();                 // biçim belirteci almıyoruz
    }

    auto format(const Kesir& k, std::format_context& ctx) const
    {
        return std::format_to(ctx.out(), "{}/{}", k.pay, k.payda);
    }
};
```

```cpp
std::format("{}", Kesir{1, 2});      // "1/2"
```

Kendi biçim belirtecinizi desteklemek isterseniz `parse` işlevinde onu okur ve
saklarsınız. Daha kısa bir yol, mevcut bir biçimlendiriciden türemektir:

```cpp
template<>
struct std::formatter<Kesir> : std::formatter<std::string> {
    auto format(const Kesir& k, std::format_context& ctx) const
    {
        return std::formatter<std::string>::format(
            std::format("{}/{}", k.pay, k.payda), ctx);
    }
};
```

Bu yazımla `{:>10}` gibi yazı belirteçleri kendiliğinden çalışır.

Akımlar için `operator<<` yüklemesiyle karşılaştırması (bkz. Cilt I Kısım 14.5): orada
tek bir işlev yeterliydi, burada bir sınıf şablonu özelleştirmesi gerekiyor. Karşılığında
biçim belirteci desteği kazanıyorsunuz.
