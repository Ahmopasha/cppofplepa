---
cilt: "II — İleri"
kisim: "12 — İleri Lambda Teknikleri"
baslik: "12.3 İlk değerli yakalama"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 12.3 İlk değerli yakalama

C++14, yakalama listesinde **yeni bir değişken tanımlamayı** mümkün kıldı.

```cpp
auto p = std::make_unique<Myclass>();

auto f = [p = std::move(p)] { p->func(); };     // taşıyarak yakala
```

Cilt I'deki yakalama biçimlerinin hepsi mevcut bir değişkeni kopyalıyor veya referans
alıyordu; taşımak mümkün değildi. `unique_ptr` gibi kopyalanamaz türleri lambdaya
sokmanın tek yolu budur.

İkinci kullanımı, yakalanan değeri **dönüştürerek** almaktır:

```cpp
auto f = [n = v.size()] { return n; };          // size_t olarak sakla
auto g = [s = std::string{"ön ek: "}] { };      // yeni nesne oluştur
```

Sınıf üye işlevinde `this` yerine nesnenin kopyasını yakalamak da bu yolla yapılırdı;
C++17'den itibaren `[*this]` yazımı daha kısa.
