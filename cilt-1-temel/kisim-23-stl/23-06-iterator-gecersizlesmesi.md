---
cilt: "I — Temel"
kisim: "23 — STL"
baslik: "23.6 İteratör geçersizleşmesi"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 23.6 İteratör geçersizleşmesi

Kaba ekleme veya silme yapmak, elinizdeki iteratörleri **geçersiz kılabilir.** Geçersiz
bir iteratörü kullanmak tanımsız davranıştır.

```cpp
std::vector<int> v{1, 2, 3};
auto it = v.begin();
v.push_back(4);       // std::vector yeniden yer ayırmış olabilir
*it;                  // yeniden yer ayrıldıysa tanımsız davranış
```

Kurallar kaba göre değişir. `std::vector`'de ekleme sırasında kabın önceden ayırdığı yer
(`capacity()`) yetmezse yeniden yer ayrılır ve bu, bütün iteratörleri geçersiz kılar;
yeniden yer ayrılmayan ekleme ve her silme, eklenen ya da silinen konumdaki ve
sonrasındaki iteratörleri (`end()` dahil) geçersiz kılar. `std::list` ve `std::map`'te
ekleme hiçbir iteratörü geçersiz kılmaz; silme yalnızca silinen elemanların iteratörlerini
geçersiz kılar. Bu kurallar elemanlara referans ve göstericiler için de geçerlidir.

Döngü içinde silme yaparken `erase`'in döndürdüğü iteratörü kullanın:

```cpp
for (auto it = v.begin(); it != v.end(); ) {
    if (*it % 2 == 0)
        it = v.erase(it);      // erase, sonraki konumu döndürür
    else
        ++it;
}
```
