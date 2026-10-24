---
cilt: "II — İleri"
kisim: "17 — Nesne Ömrü ve Bellek Yönetimi"
baslik: "17.2 Sınıf düzeyinde yükleme"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 17.2 Sınıf düzeyinde yükleme

Bir sınıf, kendi nesneleri için bellek ayırma biçimini değiştirebilir.

```cpp
class Myclass {
public:
    static void* operator new(std::size_t n)
    {
        std::cout << n << " bayt isteniyor\n";
        if (void* p = std::malloc(n))
            return p;
        throw std::bad_alloc{};
    }

    static void operator delete(void* p) noexcept
    {
        std::free(p);
    }
};
```

Üç nokta önemlidir.

**Bu işlevler örtülü olarak `static`'tir.** `static` yazmasanız da öyledirler;
`operator new` nesne henüz yokken, `operator delete` ise nesne yok edildikten sonra
çağrıldığı için `this` göstericileri olamaz.

**İkisi eşleştirilmelidir.** Yalnızca `operator new` yükleyip `operator delete`
yüklemezseniz, hem `delete` ifadesi hem de kurucu işlev hata gönderdiğinde yapılan
temizlik global `operator delete`'i çağırır. Örnekteki gibi bellek `malloc` ile ayrılmışsa
bu, eşleşmeyen ayırma ve bırakmadır; tanımsız davranıştır.

**Dizi biçimleri ayrıdır.** `operator new[]` ve `operator delete[]` ayrıca yüklenmelidir.

Sınıf düzeyindeki `operator delete`, boyut bilgisini ikinci parametre olarak da alabilir:

<!-- kod-baglam
class Myclass {
public:
@kod@
};
-->
```cpp
static void operator delete(void* p, std::size_t n) noexcept;
```

Sınıfta yalnızca bu biçim varsa `delete` ifadesi nesnenin boyutunu ona geçirir;
ayırıcının boyutu ayrıca saklamasına gerek kalmaz. İki biçim birlikte bildirilirse
boyutsuz olan seçilir.

Kullanım alanı, çok sayıda küçük nesne üreten sınıflarda havuz ayırıcı kurmaktır. Havuz
ayırıcı bir kez büyük bir blok alıp onu aynı boyutlu parçalara böler.
