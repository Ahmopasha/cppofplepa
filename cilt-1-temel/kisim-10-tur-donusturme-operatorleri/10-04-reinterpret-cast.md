---
cilt: "I — Temel"
kisim: "10 — Tür Dönüştürme Operatörleri"
baslik: "10.4 `reinterpret_cast`"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 10.4 `reinterpret_cast`

Birbiriyle ilgisiz gösterici ya da referans türleri arasında, ve gösterici ile tamsayı
arasında dönüşüm yapar. Nesneyi değiştirmez; nesne göstericisi ve referansı dönüşümlerinde
aynı adresi başka türden bir gösterici ya da referans olarak verir (hedef türün hizalama
koşulu (Cilt II, Kısım 17.8) sağlanıyorsa); bu gösterici ya da referans üzerinden erişim
aşağıdaki kurala bağlıdır.

```cpp
int x = 65;
char* p = reinterpret_cast<char*>(&x);
```

Gösterici ile tamsayı arasındaki eşleme gerçeklemeye bağlıdır; standart yalnızca yeterince
geniş bir tamsayıya çevrilip aynı gösterici türüne geri çevrilen göstericinin özgün
değerini koruyacağını güvence altına alır. Nesneye kendi türünden farklı türde bir
gösterici ya da referans üzerinden erişmek, `char`, `unsigned char` ve `std::byte` (Cilt
II, Kısım 11.7) gibi istisnalar dışında tanımsız davranıştır (**katı örtüşme kuralı**
*(strict aliasing)*, Cilt II, Kısım 11.7); örnekteki `p` üzerinden `x`'i okumak bu
istisnalardandır. Donanım kaydı erişimi, seri hâle getirme ve benzeri düşük seviyeli işler
dışında gerekmez.
