---
cilt: "II — İleri"
kisim: "16 — Sınıfların ve Operatörlerin İleri Araçları"
baslik: "16.4 Üç yollu karşılaştırma"
kaynak: "ders notları"
kutular: ["Standart Notu — C++20"]
son_kontrol: "2026-10 (C++23)"
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

`<=>` operatörü `bool` değil, bir **sıralama kategorisi** *(comparison category)* döndürür:

| Kategori | Anlamı |
|---|---|
| `std::strong_ordering` | Eşit olanlar birbirinin yerine geçebilir |
| `std::weak_ordering` | Eşdeğer ama ayırt edilebilir (büyük/küçük harf duyarsız yazı gibi) |
| `std::partial_ordering` | Bazı çiftler karşılaştırılamaz (`double` ve `NaN` gibi) |

Derleyici, `a < b` gibi ifadeleri `(a <=> b) < 0` biçimine yeniden yazar; `operator<=>`
burada bir **yeniden yazılmış aday** *(rewritten candidate)* olarak değerlendirilir.
Böylece `<=>` dört ilişkisel operatörü karşılar; `!=` ise `!(a == b)` biçiminde `==` ile
yeniden yazılır.

`==` operatörü ayrıdır ve `<=>`'den türetilmez; eşitlik denetimi çoğu zaman sıralamadan
ucuzdur. **Ancak `<=>` operatörü `= default` ile bildirilmişse ve sınıf üye ya da friend
olarak hiçbir `operator==` bildirmemişse, derleyici `==` operatörünü de örtülü olarak
bildirir.**

Elle yazmak da mümkündür:

<!-- kod-baglam
struct Kesir {
    int pay, payda;
@kod@
};
-->
```cpp
std::strong_ordering operator<=>(const Kesir& d) const
{
    return pay * d.payda <=> d.pay * payda;
}
```

**Elle yazılan `<=>` yalnızca dört ilişkisel operatörü sağlar; `==` örtülü olarak
bildirilmez, gerekiyorsa `<=>` ile aynı ölçütle ayrıca yazılır.**

> **Standart Notu — C++20**
> **C++20 öncesi:** Bir sınıfı tam karşılaştırılabilir yapmak için altı operatörü elle
> yazmak veya `boost::operators` gibi yardımcı kütüphanelere başvurmak gerekirdi.
> Operatörlerin birbiriyle tutarlı olması programcının sorumluluğundaydı.
> **C++20 ile:** Derleyici `<`, `>`, `<=` ve `>=` ifadelerini `<=>` ile, `!=` ifadesini
> `==` ile yeniden yazar; `<=>`'den türetilen dört işlem kendi aralarında, `!=` de `==` ile
> tutarlıdır; `==` ile `<=>`'nin tutarlılığı programcıya kalır. `<=>` `= default` ile
> bildirilirse ve sınıf hiçbir `operator==` bildirmemişse `==` operatörü de örtülü
> olarak bildirilir ve tek satır altısını birden sağlar.
> **Neden değişti:** Altı operatörü elle yazmak hem tekrar hem hata kaynağıydı; özellikle
> `<` ile `<=` arasındaki tutarsızlıklar sessizce yanlış çalışan koda yol açıyordu.
