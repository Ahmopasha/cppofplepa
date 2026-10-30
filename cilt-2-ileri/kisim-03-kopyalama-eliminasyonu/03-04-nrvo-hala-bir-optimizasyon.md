---
cilt: "II — İleri"
kisim: "3 — Kopyalama Eliminasyonu"
baslik: "3.4 NRVO — hâlâ bir optimizasyon"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 3.4 NRVO — hâlâ bir optimizasyon

Geri dönüş ifadesi **isimlendirilmiş yerel bir nesne** ise durum farklıdır:

```cpp
Myclass bar()
{
    Myclass mx{31};
    return mx;          // isimlendirilmiş
}
```

Buna *Named Return Value Optimization* denir ve **zorunlu değildir.** Sonuçları:

- Gerçekleme bu eliminasyonu yapmak zorunda değildir; standart yapılıp yapılmayacağını
  belirtmez.
- Dönüş nesnesini kuracak kurucu **çağrılabilir olmak zorundadır**, eliminasyon yapılacak
  olsa bile. Kurucu, X-Value olan `mx` için yükleme çözümlemesiyle seçilir: X-Value'yu
  kabul eden bir taşıyan kurucu çözümlemeye katılıyorsa o, katılmıyorsa (bildirilmemişse
  ya da Kısım 2.1'deki gibi yok sayılıyorsa) ya da nesne `const` olduğu için `T&&`'ye
  bağlanamıyorsa X-Value'yu kabul eden kopyalayan kurucu seçilir. X-Value'yu kabul eden
  taşıyan kurucu açıkça silinmişse seçilen odur ve kopyalayan kurucu olsa bile sentaks
  hatasıdır.

NRVO yapılmadığında bu kurucu çağrılır. Adın `std::move` yazılmadan R-Value olarak ele
alınmasına **örtülü taşıma** denir; seçilen kurucu taşıyan kurucu olmayabilir. Örtülü
taşıma sayesinde `return mx;`, `return std::move(mx);` ile aynı kurucuyu seçer; üstelik
NRVO'yu engellemez (Kısım 3.5). C++23'ten itibaren `return` deyimindeki taşınmaya uygun ad
(Kısım 1.1.2) bir X-Value'dur. C++20'de bu ad bir L-Value'dur; kurucu önce ad R-Value
sayılarak seçilir, bu çözümleme başarısız olursa ad L-Value sayılarak yeniden seçilir.
C++11–17'de bu kurala ek bir koşul vardı.
