---
cilt: "II — İleri"
kisim: "3 — Kopyalama Eliminasyonu"
baslik: "3.4 NRVO — hâlâ bir optimizasyon"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
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

- Derleyici bu eliminasyonu yapmak zorunda değildir.
- Yapabilmek zorunda bile değildir; davranış derleyiciye ve optimizasyon seviyesine
  bağlıdır.
- Kopyalayan veya taşıyan kurucu işlev **çağrılabilir olmak zorundadır.** İkisi de
  `delete` edilmişse kod derlenmez, eliminasyon yapılacak olsa bile.

NRVO uygulanmadığında kopyalama yapılmaz; önce **örtülü taşıma** denenir. Dönüş
ifadesindeki yerel nesne, yükleme çözümlemesinde R-Value muamelesi görür. Bu yüzden
`return mx;` yazmak, `return std::move(mx);` yazmakla aynı taşımayı zaten yapar.

Sıralama şudur: NRVO varsa hiçbir şey yapılmaz, yoksa taşınır, taşıma yoksa kopyalanır.
