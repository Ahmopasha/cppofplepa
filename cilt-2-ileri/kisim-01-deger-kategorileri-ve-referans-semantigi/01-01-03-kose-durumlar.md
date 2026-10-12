---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.1.3 Köşe durumlar"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

### 1.1.3 Köşe durumlar

Cilt I'deki liste sık karşılaşılanlarla sınırlıydı. Aşağıdakiler kütüphane yazarken
karşınıza çıkar.

**Fonksiyon isimleri her zaman L-Value'dur**, geri dönüş türlerinden bağımsız olarak:

```cpp
void moo();  int foo();  int& bar();  int&& baz();

moo   // L-Value
foo   // L-Value
bar   // L-Value
baz   // L-Value
```

**Geri dönüş türü `T&&` olan işlev çağrısı X-Value üretir:**

```cpp
baz()   // X-Value
```

**Lambda ifadesi PR-Value'dur:**

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

**Üçlü operatör**, ikinci ve üçüncü operandın ikisi de L-Value ise L-Value, en az biri
R-Value ise R-Value üretir:

```cpp
int i{}, j{}, k{};
i < 100 ? j : k       // L-Value
i < 100 ? 100 : k     // PR-Value
i < 100 ? j : 100     // PR-Value
```

**Virgül operatörünün sonucu, sağ operandın kategorisidir.** Sol operandın kategorisi
sonucu etkilemez.
