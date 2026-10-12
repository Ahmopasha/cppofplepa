---
cilt: "II — İleri"
kisim: "16 — Sınıfların ve Operatörlerin İleri Araçları"
baslik: "16.6 Bileşik türler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 16.6 Bileşik türler

Cilt I Kısım 3.10'da, sade yapıların küme parantezi içinde eleman eleman ilk değer
alabildiği söylenmiş ve tam koşullar buraya bırakılmıştı.

Bir sınıfın **bileşik tür** *(aggregate)* sayılması için:

- Kullanıcı tanımlı, `explicit` veya kalıtılmış **kurucu işlevi olmamalı**
- `private` veya `protected` **static olmayan veri elemanı olmamalı**
- **Sanal işlevi olmamalı**
- **Sanal, `private` veya `protected` taban sınıfı olmamalı**

```cpp
struct A { int x; int y; };                 // bileşik
struct B { int x; B(int); };                // değil — kurucu işlev var
struct C { int x; private: int y; };        // değil — private veri elemanı
struct D : A { int z; };                    // C++17'den beri bileşik
```

Koşullar standarttan standarda gevşedi. C++11'de taban sınıfı olan hiçbir sınıf bileşik
değildi; C++17 `public` taban sınıfa izin verdi ve ilk değer verme listesinde taban sınıf
kısmı ilk sırada yazılır hâle geldi:

```cpp
D d{{1, 2}, 3};       // A kısmı {1,2}, z ise 3
```

C++20 ise iki değişiklik getirdi. Kullanıcı tanımlı kurucu işlev **bildirilmiş** olması
bile yeter hâle geldi (önceden yalnızca "sağlanmış" olması bakılıyordu), ve **belirteçli
ilk değer verme** *(designated initializers)* eklendi:

```cpp
struct Nokta { int x; int y; };
Nokta n{.x = 3, .y = 5};      // C++20
```

Belirteçler bildirim sırasına uymak zorundadır; C dilindeki karşılığı bu kısıtı taşımaz.
