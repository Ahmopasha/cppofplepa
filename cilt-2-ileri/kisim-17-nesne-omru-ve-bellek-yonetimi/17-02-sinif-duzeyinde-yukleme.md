---
cilt: "II — İleri"
kisim: "17 — Nesne Ömrü ve Bellek Yönetimi"
baslik: "17.2 Sınıf düzeyinde yükleme"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 17.2 Sınıf düzeyinde yükleme

Bir sınıf, kendi nesneleri için bellek ayırma biçimini değiştirebilir.

```cpp
class Myclass {
public:
    static void* operator new(std::size_t n)
    {
        std::cout << n << " bayt isteniyor\n";
        return std::malloc(n);
    }

    static void operator delete(void* p) noexcept
    {
        std::free(p);
    }
};
```

Üç nokta önemlidir.

**Bu işlevler örtülü olarak `static`'tir.** `static` yazmasanız da öyledirler; nesne
henüz yokken çağrıldıkları için `this` göstericileri olamaz.

**İkisi eşleştirilmelidir.** Yalnızca `operator new` yükleyip `operator delete`
yüklemezseniz, kurucu işlev hata gönderdiğinde ayrılan bellek serbest bırakılamaz.

**Dizi biçimleri ayrıdır.** `operator new[]` ve `operator delete[]` ayrıca yüklenmelidir.

C++14, boyut bilgisini alan sonlandırma biçimini ekledi:

<!-- kod-baglam
class Myclass {
public:
@kod@
};
-->
```cpp
static void operator delete(void* p, std::size_t n) noexcept;
```

Bu biçim varsa tercih edilir; ayırıcının boyutu ayrıca saklamasına gerek kalmaz.

Kullanım alanı, çok sayıda küçük nesne üreten sınıflarda havuz ayırıcı kurmaktır. Genel
amaçlı ayırıcı her çağrıda sistem çağrısına yaklaşır; havuz ayırıcı bir kez büyük blok
alıp parçalar.
