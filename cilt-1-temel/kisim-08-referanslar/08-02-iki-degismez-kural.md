---
cilt: "I — Temel"
kisim: "8 — Referanslar"
baslik: "8.2 İki değişmez kural"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 8.2 İki değişmez kural

**Referansa ilk değer vermek zorunludur.**

```cpp
int& r;      // sentaks hatası
```

İstisnalar, ilk değerin başka bir yerden geldiği bildirimlerdir: `extern` bildirimi (tanım
başka yerdedir), sınıf tanımı içindeki referans veri elemanı bildirimi (bkz. Kısım 12),
parametre bildirimi (işlev parametresine ilk değeri çağrı, `catch` yan tümcesindeki
parametreye yakalanan hata nesnesi verir; bkz. Kısım 18.2) ve referans döndüren işlevin
dönüş türü (ilk değerini `return` deyimi verir; bkz. Kısım 8.6).

**Referans bir kez bağlandıktan sonra başka bir nesneye bağlanamaz.** Sonraki atamalar
referansa değil, bağlandığı nesneye yapılır.

```cpp
int x = 10, y = 99;
int& r = x;

r = y;           // x'e 99 atandı; r hâlâ x'i gösteriyor
std::cout << x;  // 99
```

Gösterici `nullptr` tutabilir; referans ise ilk değer alırken geçerli bir nesneye (ya da
işleve) bağlanmak zorundadır. Bu yüzden tanımsız davranış içermeyen bir programda **boş
referans** *(null reference)* diye bir şey yoktur ve referans parametre alan bir işlevde
boş gösterici denetimine gerek kalmaz. Bu, referansın her zaman kullanılabilir olduğu
anlamına gelmez: bağlandığı nesnenin ömrü biterse referans sarkar (bkz. Kısım 8.3 ve 8.6)
ve onu kullanmak tanımsız davranıştır.
