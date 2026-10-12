---
cilt: "II — İleri"
kisim: "9 — Coroutines"
baslik: "9.1 Askıya alınabilen işlev"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 9.1 Askıya alınabilen işlev

Sıradan bir işlev çağrıldığında baştan sona çalışır ve döner. Yığında bir çerçeve
oluşur, işlev bitince çerçeve yok olur; işlevin durumu geriye kalmaz.

**Eşyordam** *(coroutine)*, çalışmasının ortasında **askıya alınabilen** ve daha sonra
kaldığı yerden devam edebilen bir işlevdir. Askıya alındığında yerel değişkenleri ve
çalışma noktası korunur.

```cpp
Generator sayilar()
{
    co_yield 1;          // burada askıya alınır
    co_yield 2;          // devam edince buradan sürer
    co_yield 3;
}
```

Kullanım alanları iki gruptur. **Üreteçler**: değerleri talep edildikçe üretmek, hepsini
önceden hesaplayıp bir kaba doldurmak yerine. **Eşzamansız işlemler**: bir kaynağı
beklerken iş parçacığını bloklamamak.

C++20'de dile eklendi. `<coroutine>` başlığının dahil edilmesi gerekir.
