---
cilt: "I — Temel"
kisim: "14 — Operatör Yüklemesi"
baslik: "14.7 Bit bayrakları"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 14.7 Bit bayrakları

Kısım 5.3'te, kapsamlandırılmamış `enum` kullanmak için "bilinçli bir sebep" gerektiğini
ve bit bayraklarının o sebeplerden biri olduğunu söylemiştik. Sebep şudur:

```cpp
enum Yetki { Oku = 1, Yaz = 2, Calistir = 4 };

int y = Oku | Yaz;          // tamsayıya örtülü dönüşüm sayesinde çalışır
```

`enum class` ile aynı şeyi yazmak, `|`, `&` ve `~` operatörlerini yüklemeyi gerektirir:

```cpp
enum class Yetki : unsigned { Oku = 1, Yaz = 2, Calistir = 4 };

Yetki operator|(Yetki a, Yetki b)
{
    return static_cast<Yetki>(static_cast<unsigned>(a) | static_cast<unsigned>(b));
}
```

Karşılığında tür güvenliğini kazanırsınız; `Yetki` ile başka bir `enum class` yanlışlıkla
birleştirilemez. Birkaç satır operatör yüklemesi, bunun makul bir bedelidir.
