---
cilt: "I — Temel"
kisim: "10 — Tür Dönüştürme Operatörleri"
baslik: "10.1 Neden dört ayrı operatör"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 10.1 Neden dört ayrı operatör

C dilinde tek bir dönüştürme yazımı vardır:

<!-- kod-baglam
void* q = nullptr;
-->
```cpp
int* p = (int*)q;
```

Bu yazım her şeyi yapar: `const`luk kaldırır, ilgisiz gösterici türlerini birbirine
çevirir, sayısal dönüşüm yapar. Ne yaptığı okunmaz, aranamaz ve niyeti belirsizdir.

C++ bunu dört ayrı operatöre böldü. Her biri yalnızca belirli bir dönüşüm sınıfını yapar.
Kazancı üç yönlüdür: niyetiniz koddan okunur, yanlış dönüşüm sentaks hatası verir, ve
kod tabanında dönüşümleri arayabilirsiniz.
