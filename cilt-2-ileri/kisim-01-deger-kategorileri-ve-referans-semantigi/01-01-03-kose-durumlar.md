---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.1.3 Köşe durumlar"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

### 1.1.3 Köşe durumlar

Cilt I'deki liste sık karşılaşılanlarla sınırlıydı. Aşağıdakiler kütüphane yazarken
karşınıza çıkar.

**İşlev isimleri L-Value'dur**, geri dönüş türlerinden bağımsız olarak:

```cpp
void moo();  int foo();  int& bar();  int&& baz();

moo   // L-Value
foo   // L-Value
bar   // L-Value
baz   // L-Value
```

İstisna statik olmayan üye işlevlerdir. Böyle bir işleve ister nesne üzerinden
(`nesne.uye`, `p->uye`) ister nitelenmiş adla (`Myclass::uye`; tekli `&`'nin operandı
olduğu durum dışında) başvuran ifade L-Value değildir. Nesne üzerinden erişen ifade
PR-Value'dur ve yalnızca bir çağrının sol tarafında kullanılabilir. Statik üye işleve
nesne üzerinden erişilse bile ifade L-Value'dur.

**Geri dönüş türü `T&&` olan (`T` referans olmayan bir tür) işlev çağrısı X-Value
üretir:**

<!-- kod-baglam
int&& baz();
-->
```cpp
baz()   // X-Value
```

Bunun istisnası: **`T` bir işlev türüyse, işleve R-Value referans döndüren çağrı L-Value
üretir.** **İşleve L-Value ya da R-Value referans türüne dönüştürülen bir işlev de L-Value
kalır:**

<!-- kod-baglam
void moo();
-->
```cpp
std::move(moo)                   // L-Value — X-Value değil
static_cast<void(&&)()>(moo)     // L-Value
```

**Lambda ifadesi PR-Value'dur:**

<!-- kod: atla -->
```cpp
[]() { return 31; }   // PR-Value
```

**Sınıf öğelerine erişimde kategori, nesnenin kategorisine bağlıdır:**

```cpp
struct Nec { int x{}; static int sx; };

Nec neco;
neco.x                 // L-Value
Nec{}.x                // X-Value — R-Value nesnenin non-static öğesi
std::move(neco).x      // X-Value
std::move(neco).sx     // L-Value — static öğe, nesneden bağımsız
```

R-Value bir nesnenin non-static veri elemanı **referans türündense**, o erişim ifadesi
yine L-Value olur.

**Üçlü operatörde** ikinci ve üçüncü operand aynı türden ve aynı kategoriden GL-Value ise
sonuç o tür ve kategoridedir (L-Value ya da X-Value). Türler farklıysa bir operand
öbürünün türüne ve kategorisine dönüştürülmeye çalışılır. Sınıf türü olmayan operandlarda
bu yalnızca ikisi aynı kategoriden GL-Value ise ve türleri yalnızca cv nitelemesiyle
farklıysa olur (ör. `int` ile `const int`). Operandlardan biri sınıf türündense, öbürü
onun türüne o kategoride bir referansla doğrudan bağlanabilmelidir (ör. türemiş ile taban
sınıf ya da `operator A&()` gibi bir dönüşüm işlevi). Bu bağlanma kurulamazsa (ya da hedef
operand PR-Value ise), öbür operandın türüne PR-Value olarak dönüşüm de denenir (ör.
dönüştüren bir kurucuyla). Bu denemeler iki yönde de bir dönüşüm buluyorsa ya da dönüşüm
belirsizse ifade sentaks hatasıdır. Yalnızca bir yönde buluyorsa o operand dönüştürülür;
operandlar böylece aynı tür ve kategoriden GL-Value olursa sonuç o tür ve kategoridedir.
Diğer durumlarda, ifade geçerliyse sonuç PR-Value'dur. Operandlardan biri `throw`
ifadesiyse sonuç diğer operandın türünde ve kategorisindedir:

```cpp
int i{}, j{}, k{};
long l{};
i < 100 ? j : k       // L-Value
i < 100 ? 100 : k     // PR-Value
i < 100 ? j : 100     // PR-Value
i < 100 ? j : l       // PR-Value — türler farklı
i < 100 ? j : throw 1 // L-Value — diğer operand j
```

**Virgül operatörünün sonucu, sağ operandın kategorisidir.** Sol operandın kategorisi
sonucu etkilemez.
