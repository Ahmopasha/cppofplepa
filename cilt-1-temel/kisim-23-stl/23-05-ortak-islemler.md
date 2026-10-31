---
cilt: "I — Temel"
kisim: "23 — STL"
baslik: "23.5 Ortak işlemler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 23.5 Ortak işlemler

<!-- kod-baglam
std::vector<int> v;
int x = 0;
auto konum = v.begin();
-->
```cpp
v.size();      v.empty();     v.clear();
v.push_back(x);               v.pop_back();
v.insert(konum, x);           v.erase(konum);
v.front();     v.back();
```

`emplace` ailesi, nesneyi kabın içinde **doğrudan oluşturur**; dışarıda oluşturup
kopyalamaz.

<!-- kod-baglam
std::vector<Myclass> v;
-->
```cpp
v.push_back(Myclass{1, 2});    // oluştur, sonra taşı
v.emplace_back(1, 2);          // doğrudan kabın içinde oluştur
```

`emplace_back`, argümanlarını kurucu işleve kategorileri bozulmadan iletir; bu mekanizma
Cilt II Kısım 1.2'de anlatılan mükemmel gönderimdir.
