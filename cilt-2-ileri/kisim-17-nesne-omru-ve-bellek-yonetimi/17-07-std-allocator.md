---
cilt: "II — İleri"
kisim: "17 — Nesne Ömrü ve Bellek Yönetimi"
baslik: "17.7 `std::allocator`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 17.7 `std::allocator`

Kapların bellek ayırma biçimini değiştirmeye yarayan ilke sınıfıdır. 17.2'deki
`operator new` yüklemesinden farkı, **kap düzeyinde** çalışmasıdır; sınıfı değil, kabı
özelleştirir.

```cpp
std::vector<int, KendiAyiricim<int>> v;
```

Bir ayırıcının sunması gereken asgari arayüz `allocate`, `deallocate` ve `value_type`
tür üyesidir; kalanını `std::allocator_traits` varsayılan değerlerle tamamlar.

Ayırıcılar, Kısım 6.8'deki boş taban sınıf optimizasyonunun standart kütüphanedeki en
yaygın uygulama alanıdır: durumsuz bir ayırıcı, kabın boyutunu artırmaz.

Özel ayırıcı yazmanın üç tipik gerekçesi vardır: çok sayıda küçük nesne için havuz
kurmak, gömülü sistemlerde sabit bir bellek bölgesiyle çalışmak, ve eşzamanlı kodda
genel amaçlı ayırıcının oluşturduğu darboğazı kaldırmak (bkz. Kısım 15.10).
