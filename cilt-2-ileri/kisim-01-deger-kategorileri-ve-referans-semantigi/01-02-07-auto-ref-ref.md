---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.2.7 `auto&&`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

### 1.2.7 `auto&&`

`auto&&` de forwarding reference'tır ve aynı çıkarım kurallarına uyar. Pratik sonucu,
**her şeye bağlanabilen** bir referans elde etmenizdir.

```cpp
auto&& r1 = 31;          // int&&
int x = 5;
auto&& r2 = x;           // int&
const int cx = 7;
auto&& r3 = cx;          // const int&
```

En sık kullanıldığı yer aralık tabanlı `for` döngüleridir. `auto&` bazı kaplarda
çalışmaz, çünkü o kapların `operator[]` ve iteratörleri gerçek bir elemana değil bir
vekil nesneye *(proxy)* erişir; vekil nesne geçicidir ve `auto&` ona bağlanamaz.
`auto&&` her iki durumda da çalışır.

Bir değişkeni `auto&&` ile tanımlayıp sonra başka bir işleve iletiyorsanız, orada da
`std::forward<decltype(r)>(r)` yazmanız gerekir.
