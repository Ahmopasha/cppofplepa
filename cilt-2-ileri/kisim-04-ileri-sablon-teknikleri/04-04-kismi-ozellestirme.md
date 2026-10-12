---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.4 Kısmi özelleştirme"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 4.4 Kısmi özelleştirme

Parametrelerin bir kısmını sabitleyip kalanını serbest bırakmaktır. Tam
özelleştirmeden daha kapsayıcıdır.

```cpp
template<typename T, typename U>
class Cift { };

template<typename T>
class Cift<T, int> { };         // ikinci parametre int olanlar

template<typename T>
class Cift<T*, T*> { };         // ikisi de aynı türden gösterici olanlar
```

**Kısmi özelleştirme yalnızca sınıf şablonlarında ve değişken şablonlarında yapılabilir.**
İşlev şablonlarında mümkün değildir; orada yine yükleme kullanılır.

Cilt II Kısım 1.1.7'deki değer kategorisi tespit kodu, değişken şablonunun kısmi
özelleştirmesine dayanıyordu; oradaki `p<T&>` ve `p<T&&>` tanımları bu mekanizmanın
örnekleridir.
