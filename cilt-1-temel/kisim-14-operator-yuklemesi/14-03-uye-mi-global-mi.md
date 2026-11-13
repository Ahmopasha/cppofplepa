---
cilt: "I — Temel"
kisim: "14 — Operatör Yüklemesi"
baslik: "14.3 Üye mi, global mi"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
kutular: ["Standart Notu — C++20"]
---

## 14.3 Üye mi, global mi

Seçim, sol operandın ne olduğuna bakılarak yapılır.

**Sol operand kendi sınıfınızsa** üye işlev yazabilirsiniz. Bu durumda sol operand işlevin
çağrıldığı nesne (`*this`), sağ operand parametre olur.

```cpp
class Kesir {
public:
    Kesir(int pay = 0, int payda = 1);   // bilerek explicit değil (Kısım 12.13)
    Kesir operator+(const Kesir&) const;    // a + b
};
```

**Sol operand başka bir türse** üye işlev yazamazsınız; o türün sınıfına müdahale
edemezsiniz. Akım operatörleri bu gruptadır:

```cpp
std::ostream& operator<<(std::ostream& os, const Kesir& k);
```

Sol operand `std::ostream` olduğu için bu işlev üye olamaz.

**Simetri gerektiren aritmetik operatörlerde üye olmayan işlev tercih edilir.** Üye işlev
yazarsanız sol operand kullanıcı tanımlı bir dönüşüme (örneğin dönüştüren kurucu işlevle)
uğrayamaz. Yukarıdaki kurucu işlev `int`'ten dönüştürdüğü için:

```cpp
Kesir k{1, 2};
k + 5;      // geçerli
5 + k;      // üye işlevle sentaks hatası, üye olmayan işlevle geçerli
```

> **Standart Notu — C++20**
> **C++20 öncesi:** `==` ve `!=` için de aynı kısıt vardı; üye `operator==` ile `5 == k`
> yazılamazdı.
> **C++20 ile:** `==` ve `!=` ifadelerinde `operator==`'nin operandları yer değiştirmiş
> biçimi de denenir; üye `bool operator==` ile `5 == k` ve `5 != k` de geçerlidir (Kısım
> 14.5; Cilt II, Kısım 16.4). C++23'ten itibaren, üye `operator==` ile aynı sınıfta ona
> karşılık gelen bir `operator!=` de bildirilmişse yer değiştirmiş biçim denenmez;
> `5 == k` ve `5 != k` sentaks hatasıdır. Üye `operator<` gibi sıralama operatörlerinde
> kısıt sürer (`<=>` için: Kısım 14.5; Cilt II, Kısım 16.4).
