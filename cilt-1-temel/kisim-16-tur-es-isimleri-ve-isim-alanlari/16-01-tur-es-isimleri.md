---
cilt: "I — Temel"
kisim: "16 — Tür Eş İsimleri ve İsim Alanları"
baslik: "16.1 Tür eş isimleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 16.1 Tür eş isimleri

Var olan bir türe ikinci bir isim vermenin iki yazımı vardır.

```cpp
typedef unsigned long ulong;       // C'den gelen yazım
using ulong = unsigned long;       // C++11 yazımı
```

İkisi de aynı işi yapar. `using` yazımı iki yerde açıkça üstündür.

**Gösterici ve dizi türlerinde okunabilir.** `typedef`'te tür ismi, bildirilen değişken
gibi yazılır ve eş isim ortada kalır:

```cpp
typedef void (*Geri)(int, int);        // Geri nerede?
using   Geri = void (*)(int, int);     // solda
```

**Şablonlaştırılabilir.** `typedef` şablon parametresi alamaz, `using` alır. Bu konu
Cilt II Kısım 4'te.

> Yeni kodda `using` kullanın. `typedef`, mevcut kodu okuyabilmek için bilmeniz gereken
> bir yazımdır.

Tür eş ismi **yeni bir tür oluşturmaz.** `ulong` ile `unsigned long` aynı türdür; işlev
yüklemesinde ayırt edici değildir.
