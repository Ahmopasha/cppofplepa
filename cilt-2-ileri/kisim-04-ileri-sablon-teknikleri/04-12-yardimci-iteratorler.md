---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.12 Yardımcı iteratörler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 4.12 Yardımcı iteratörler

Standart kütüphane, kap dışındaki şeyleri iteratör arayüzüne uyduran sınıflar sunar.

**Akım iteratörleri.** Bir akımı kap gibi gösterir.

```cpp
std::vector<int> v{1, 2, 3};

std::copy(v.begin(), v.end(),
          std::ostream_iterator<int>{std::cout, " "});

std::vector<int> okunan{std::istream_iterator<int>{std::cin},
                        std::istream_iterator<int>{}};
```

**Ekleme iteratörleri.** Yazma işlemini kaba ekleme çağrısına çevirir. Algoritmaların
kaba eleman eklememesi sorununu çözer (bkz. Cilt I Kısım 23.7).

```cpp
std::vector<int> hedef;
std::copy(v.begin(), v.end(), std::back_inserter(hedef));
```

`back_inserter`, `front_inserter` ve `inserter` biçimleri vardır.

**`move_iterator`.** Dolaşırken eleman kopyalamak yerine taşır.

```cpp
std::vector<std::string> kaynak{"a", "b", "c"};
std::vector<std::string> hedef{
    std::make_move_iterator(kaynak.begin()),
    std::make_move_iterator(kaynak.end())
};
```

Kaynak kaptaki elemanlar artık kaynağı devralınmış durumdadır (bkz. Kısım 2.5).
