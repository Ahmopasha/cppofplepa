---
cilt: "II — İleri"
kisim: "14 — Deyimler ve Kalıplar"
baslik: "14.8 Mixin sınıflar"
kaynak: "derleyen (ders notlarında yok)"
son_kontrol: "2026-09 (C++23)"
---

## 14.8 Mixin sınıflar

**Mixin**, bir sınıfa bağımsız bir davranış parçası eklemek için yazılan, tek başına
kullanılması amaçlanmayan sınıftır. Tekniğin kilit noktası, mixin'in **kendi taban
sınıfını şablon parametresi olarak almasıdır.**

```cpp
template<typename Taban>
class Sayilabilir : public Taban {
    mutable int erisim{};
public:
    using Taban::Taban;                        // kurucu işlevleri devral
    int erisim_sayisi() const { return erisim; }
protected:
    void say() const { ++erisim; }
};
```

Sıradan kalıtımda türemiş sınıf hangi tabandan türeyeceğini bilir. Mixin'de tersidir:
**taban, kullanım anında belirlenir.**

```cpp
class Cekirdek { public: void islem(); };

Sayilabilir<Cekirdek> nesne;
nesne.islem();                                 // Cekirdek'ten geldi
nesne.erisim_sayisi();                         // mixin'den geldi
```

### Zincirleme

Asıl kazanç, birden fazla mixin'in üst üste bindirilebilmesidir. Her biri bir öncekinin
üzerine bir katman ekler.

<!-- kod-baglam
class Cekirdek { };
-->
```cpp
template<typename Taban> class Gunlukleyen  : public Taban { /* ... */ };
template<typename Taban> class Kilitleyen   : public Taban { /* ... */ };
template<typename Taban> class Sayilabilir  : public Taban { /* ... */ };

using Nesne = Gunlukleyen<Kilitleyen<Sayilabilir<Cekirdek>>>;
```

Üç davranış birbirinden bağımsız yazılmıştır ve istediğiniz sırayla, istediğiniz
bileşimde kullanılabilir. Aynı şeyi sıradan kalıtımla yapmak, her bileşim için ayrı bir
sınıf yazmayı gerektirirdi.

Sıra önemlidir: dıştaki mixin, içtekinin üzerine kurulur. `Kilitleyen<Gunlukleyen<...>>`
ile `Gunlukleyen<Kilitleyen<...>>` farklı davranır; birinde günlükleme kilit altında,
diğerinde değildir.

### CRTP'den farkı

İkisi de şablon ve kalıtımı birleştirir ama yönleri terstir.

| | Bilgi yönü | Yazım |
|---|---|---|
| **CRTP** | Taban, türemiş sınıfı bilir | `class Somut : public Taban<Somut>` |
| **Mixin** | Türemiş sınıf, tabanı bilir | `class Mixin : public Taban` (Taban parametre) |

CRTP'de amaç, taban sınıfın türemiş sınıfın işlevlerini çağırabilmesidir; statik çok
biçimlilik kurulur (bkz. Kısım 6.13). Mixin'de amaç, davranışı katman katman
eklemektir; çok biçimlilik hedeflenmez.

İkisi birlikte de kullanılır: bir mixin, aynı zamanda CRTP tabanı olabilir.

### Boş taban sınıf optimizasyonu

Mixin'lerin çoğu **durumsuzdur**; yalnızca işlev ekler, veri elemanı eklemez. Durumsuz
bir sınıfın boyutu sıfır olamaz, ama taban sınıf olarak kullanıldığında derleyicinin ona
yer ayırmama izni vardır (bkz. Kısım 6.8).

Bu, mixin tekniğinin maliyetsiz olmasının sebebidir. Beş katmanlı bir zincir kurabilir ve
nesnenin boyutunu hiç artırmayabilirsiniz. Aynı davranışları composition ile eklemek —
her katmanı veri elemanı yapmak — her katman için en az bir bayt maliyet getirirdi.

### İlke sınıflarıyla karşılaştırma

**İlke sınıfı** *(policy class)* yaklaşımında, değiştirilebilir davranışlar şablon
parametresi olarak verilir ama kalıtım zorunlu değildir:

```cpp
template<typename Kilit, typename Gunluk>
class Nesne {
    Kilit kilit;
    Gunluk gunluk;
};
```

Aradaki fark, davranışın **arayüze çıkıp çıkmadığıdır.** Mixin'de eklenen işlevler
nesnenin `public` arayüzünde görünür; ilke sınıflarında görünmez, sınıf onları içeride
kullanır.

Seçim kuralı şudur: eklenen davranışı kullanıcının **doğrudan çağırması** gerekiyorsa
mixin, yalnızca sınıfın iç işleyişini değiştiriyorsa ilke sınıfı.

Standart kütüphanede ilke yaklaşımı yaygındır; `std::vector`'ün ayırıcı parametresi
(bkz. Kısım 17.7) ve birleşik kapların karşılaştırıcı parametresi ilke sınıflarıdır.
