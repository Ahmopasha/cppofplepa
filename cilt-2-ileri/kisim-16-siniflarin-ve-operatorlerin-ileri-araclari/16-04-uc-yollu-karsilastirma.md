---
cilt: "II — İleri"
kisim: "16 — Sınıfların ve Operatörlerin İleri Araçları"
baslik: "16.4 Üç yollu karşılaştırma"
kaynak: "ders notları"
kutular: ["Standart Notu — C++20"]
son_kontrol: "2026-09 (C++23)"
---

## 16.4 Üç yollu karşılaştırma

Cilt I Kısım 14.5'te, karşılaştırma operatörlerinin altısını yazmak yerine `==` ve `<`
yazıp kalanını türetmenin yaygın olduğu söylenmişti. C++20 bu tekrarı tamamen ortadan
kaldırdı.

```cpp
class Kesir {
    int pay, payda;
public:
    auto operator<=>(const Kesir&) const = default;
};
```

Bu tek satır, altı karşılaştırma operatörünü birden sağlar. Derleyici veri elemanlarını
bildirim sırasına göre sırayla karşılaştırır.

`<=>` operatörü `bool` değil, bir **sıralama kategorisi** döndürür:

| Kategori | Anlamı |
|---|---|
| `std::strong_ordering` | Eşit olanlar birbirinin yerine geçebilir |
| `std::weak_ordering` | Eşdeğer ama ayırt edilebilir (büyük/küçük harf duyarsız yazı gibi) |
| `std::partial_ordering` | Bazı çiftler karşılaştırılamaz (`double` ve `NaN` gibi) |

Derleyici, `a < b` gibi ifadeleri `(a <=> b) < 0` biçimine **yeniden yazar**. Bu yüzden
tek operatör altısını birden sağlayabilir.

`==` operatörü ayrıdır ve `<=>`'den türetilmez; eşitlik denetimi çoğu zaman
karşılaştırmadan ucuz olduğu için ayrık tutulmuştur. Ancak `<=>` operatörünü
`= default` ile bildirirseniz, derleyici `==` operatörünü de örtülü olarak bildirir.

Elle yazmak da mümkündür:

```cpp
std::strong_ordering operator<=>(const Kesir& d) const
{
    return pay * d.payda <=> d.pay * payda;
}
```

> **Standart Notu — C++20**
> **C++20 öncesi:** Bir sınıfı tam karşılaştırılabilir yapmak için altı operatörü elle
> yazmak veya `boost::operators` gibi yardımcı kütüphanelere başvurmak gerekirdi.
> Operatörlerin birbiriyle tutarlı olması programcının sorumluluğundaydı.
> **C++20 ile:** Tek bir `operator<=>` bildirimi altısını birden üretir; tutarlılık
> derleyicinin garantisidir.
> **Neden değişti:** Altı operatörü elle yazmak hem tekrar hem hata kaynağıydı; özellikle
> `<` ile `<=` arasındaki tutarsızlıklar sessizce yanlış çalışan koda yol açıyordu.
