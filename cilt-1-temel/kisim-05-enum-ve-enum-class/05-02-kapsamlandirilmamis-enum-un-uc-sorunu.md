---
cilt: "I — Temel"
kisim: "5 — `enum` ve `enum class`"
baslik: "5.2 Kapsamlandırılmamış `enum`'un üç sorunu"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 5.2 Kapsamlandırılmamış `enum`'un üç sorunu

**Birinci sorun: numaralandırma sabitlerinin ayrı bir kapsamı yoktur.** Sabitler, `enum`
türünün bildirildiği kapsama sızar.

```cpp
enum Renk  { Kirmizi, Yesil, Mavi };
enum Meyve { Elma, Armut, Kirmizi };   // sentaks hatası: Kirmizi zaten var
```

**İkinci sorun: tamsayı türlerine örtülü dönüşüm vardır.** Ters yön sentaks hatasıdır, ama
bu yön serbesttir ve anlamsız karşılaştırmalara izin verir.

```cpp
enum Renk  { Kirmizi, Yesil, Mavi };
enum Meyve { Elma, Armut };

if (Kirmizi == Elma) { }     // geçerli — ikisi de 0
int x = Yesil;               // geçerli
```

Farklı iki `enum` türünün değerlerini ya da bir `enum` değerini bir gerçek sayıyla böyle
karşılaştırmak ya da aritmetik işlemde birlikte kullanmak C++20'den beri
**artık önerilmiyor** *(deprecated)*: kod hâlâ geçerlidir, ama standart bu kullanımın
ileride kaldırılabileceğini bildirir. Tamsayıyla karşılaştırma (`Kirmizi == 0`) ve
tamsayıya dönüşüm ise artık önerilmeyenler arasında değildir.

**Üçüncü sorun: temel tür belirtilmezse seçim gerçeklemeye kalır.** Kapsamlandırılmamış
bir `enum`'un temel türünü belirtmezseniz, bütün sabitleri tutabilen bir tamsayı türünü
gerçekleme seçer: temel tür gerçeklemeye bağlıdır, `sizeof` değeri de bu seçime göre
değişir. Böyle bir `enum` ileri bildirilemez de (Kısım 2.6), çünkü temel türü ancak tanımı
görülünce belli olur:

```cpp
enum Renk;            // sentaks hatası: temel tür bilinmiyor
enum Boyut : int;     // geçerli: temel tür belirtilmiş (Kısım 5.3)
```

C'de de `enum` türünün temel aldığı tamsayı türü gerçeklemeye bağlıdır; C'de `int` olan,
numaralandırıcıların türüdür (Kısım 1.8). C++'ta kapsamlandırılmamış bir `enum`'un
numaralandırıcıları, tanımın kapanış süslü parantezinden sonra o `enum` türündendir.
