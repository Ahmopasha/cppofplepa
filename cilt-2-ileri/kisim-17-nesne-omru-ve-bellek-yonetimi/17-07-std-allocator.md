---
cilt: "II — İleri"
kisim: "17 — Nesne Ömrü ve Bellek Yönetimi"
baslik: "17.7 `std::allocator`"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 17.7 `std::allocator`

Kapların bellek ayırma biçimini değiştirmeye yarayan ilke sınıfıdır. 17.2'deki
`operator new` yüklemesinden farkı, **kap düzeyinde** çalışmasıdır; sınıfı değil, kabı
özelleştirir.

<!-- kod-baglam
template<typename T>
struct KendiAyiricim {
    using value_type = T;
    T* allocate(std::size_t);
    void deallocate(T*, std::size_t) noexcept;
};
-->
```cpp
std::vector<int, KendiAyiricim<int>> v;
```

Bir ayırıcının sunması gereken asgari arayüz şunlardır: `value_type` tür üyesi, `allocate`
ve `deallocate` üye işlevleri, `==` karşılaştırması, başka bir türe yeniden bağlanmış
ayırıcıdan dönüştüren kurucu işlev ve kopyalama ile taşıma (çoğu zaman örtülü olanlar
yeter); bu kurucu işlevler, `==` ve `deallocate` hata göndermemelidir. Kalanını
`std::allocator_traits` varsayılan değerlerle tamamlar. Yalnızca `rebind` için varsayılan,
ayırıcının tür parametreleri alan ve ilk parametresi `value_type` olan bir şablon olmasına
bağlıdır. Değilse (ör. tür olmayan bir şablon parametresi varsa) `rebind` üye şablonunu
ayırıcı sağlamalıdır.

Ayırıcılar, Kısım 6.8'deki boş taban sınıf optimizasyonunun tipik kullanım alanıdır: kap,
durumsuz bir ayırıcıyı bu yolla tutarak boyutunu artırmayabilir. Standart bunu zorunlu
kılmaz.

Özel ayırıcı yazmanın üç tipik gerekçesi vardır: çok sayıda küçük nesne için havuz
kurmak, gömülü sistemlerde sabit bir bellek bölgesiyle çalışmak, ve eşzamanlı kodda
genel amaçlı ayırıcının oluşturduğu darboğazı kaldırmak (bkz. Kısım 15.10).
