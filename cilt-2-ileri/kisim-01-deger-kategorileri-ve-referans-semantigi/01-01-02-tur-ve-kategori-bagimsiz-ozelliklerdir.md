---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.1.2 Tür ve kategori bağımsız özelliklerdir"
kaynak: "ders notları"
kutular: ["Standart Notu — C++23"]
son_kontrol: "2026-10 (C++23)"
---

### 1.1.2 Tür ve kategori bağımsız özelliklerdir

C++ standardı her ifadeyi iki **bağımsız** özellikle tanımlar: bir türü vardır, bir de
değer kategorisi. Bu ikisinin karıştırılması, şablon kodu yazarken en çok hataya yol
açan yerlerden biridir.

**Bir ifadenin türü asla referans olamaz.** Değişkenin türü referans olabilir, ifadenin
türü olamaz.

```cpp
int x = 6;
int& rx = x;

rx = 66;    // buradaki "rx" ifadesinin türü "int&" DEĞİL, "int".
```

Kısıtlama göstericiler için geçerli değildir:

```cpp
int* px = &x;
*px = 99;   // "px" ifadesinin türü "int*".
```

**Değişkenlerin değer kategorisi yoktur, ifadelerin vardır.** Bir bildirim tek başına
ifade oluşturmaz:

```cpp
int x = 31;     // "x" burada ifade oluşturmuyor: kategori yok, tür "int".
int b;
b = x;          // "x" burada ifade: L-Value, tür "int".
b = +x;         // "+x" bir ifade: PR-Value, tür "int".

int&& rr = 10;  // "rr" burada ifade oluşturmuyor: tür "int&&".
+rr;            // "rr" burada ifade: L-Value, tür "int".
                // Referans niteliği düştü; ifadelerin türü referans olamaz.

int* p{};       // "p" burada ifade oluşturmuyor: tür "int*".
p;              // "p" burada ifade: L-Value, tür "int*".
                // İfadelerin türü referans olamaz ama gösterici olabilir.
```

`int&& rr` bildirimindeki `rr`'nin bir ifade olarak L-Value olması, ilk bakışta çelişkili
görünür. Çelişki değildir: `rr` bir değişkenin adıdır. Değişkenlerin kimliği vardır, ama
adları kaynaklarının devralınabileceğini kendiliğinden bildirmez; bu yüzden değişken
adları (aşağıdaki `return` ve `throw` istisnası dışında) L-Value'dur. (Her isim böyle
değildir; örneğin bir numaralandırma sabitinin adı PR-Value'dur.) Bu yüzden `T&&`
parametreli bir işlevin gövdesinde parametreyi başka bir işleve R-Value olarak aktarmak
için `std::move` (parametre forwarding reference ise, çağrıya R-Value geldiyse R-Value
olarak iletmek için `std::forward`; bkz. Kısım 1.2.1 ve 1.2.5) yazmanız gerekir. `return`
(ya da eşyordamlarda `co_return`; bkz. Kısım 9.2) ile döndürülen ya da `throw` ile atılan
yalın bir ad, en içteki işlevin ya da lambdanın içinde bildirilmiş, otomatik ömürlü bir
yerel değişkeni ya da parametreyi gösterebilir. Bu değişken `volatile` olmayan bir
nesneyse ya da (C++20'den itibaren) `volatile` olmayan bir nesne türüne R-Value referanssa
ad **taşınmaya uygundur** *(move-eligible)*. `throw`'da bir koşul daha vardır: `throw`'u
saran `try` blokları varsa, değişken en içtekinin içinde bildirilmiş olmalıdır; `throw`
ile atılan parametreler de C++20'den itibaren bu kapsamdadır. Bu durumlarda `std::move`
gerekmez; C++23'ten itibaren ifade X-Value'dur. L-Value referanslar (L-Value argüman almış
forwarding reference dahil) ve `static` yerel değişkenler bu kapsamda değildir.

> **Standart Notu — C++23**
> **C++23 öncesi:** Taşınmaya uygun ad L-Value'dur; örtülü taşıma kuralı uygulanır
> (bkz. Kısım 3.4).
> **C++23 ile:** Ad X-Value'dur. Bu yüzden `int& f(int&& r) { return r; }` artık sentaks
> hatasıdır.
> **Neden değişti:** Eski kural karmaşıktı ve referans döndüren işlevlerde işlemiyordu;
> örneğin `int&& g(int&& r) { return r; }` sentaks hatasıydı, C++23'te geçerlidir. Kural
> değer kategorisiyle ifade edilerek sadeleştirildi.
