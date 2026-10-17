---
cilt: "I — Temel"
kisim: "22 — Şablonlara Giriş"
baslik: "22.2 İşlev şablonları"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 22.2 İşlev şablonları

Çağrı yapıldığında derleyici, argümanlara bakarak `T`'nin ne olduğunu **çıkarır.**

<!-- kod-baglam
template<typename T>
T enbuyuk(T a, T b) { return a > b ? a : b; }
-->
```cpp
enbuyuk(3, 5);        // T = int
enbuyuk(3.1, 5.2);    // T = double
enbuyuk("a", "b");    // T = const char* — muhtemelen istediğiniz bu değil
```

Çıkarımı istemiyorsanız türü açıkça yazabilirsiniz:

<!-- kod-baglam
template<typename T>
T enbuyuk(T a, T b) { return a > b ? a : b; }
-->
```cpp
enbuyuk<double>(3, 5.2);
```

Çıkarımın başarısız olduğu bir durum yaygındır: iki argümanın türü farklıysa `T` tek bir
değere karar veremez.

<!-- kod-baglam
template<typename T>
T enbuyuk(T a, T b) { return a > b ? a : b; }
-->
```cpp
enbuyuk(3, 5.2);           // sentaks hatası
enbuyuk<double>(3, 5.2);   // açıkça belirtince çalışır
```

Şablon argüman çıkarımının kuralları, Kısım 4'teki `auto` kurallarıyla aynı temele
dayanır.
