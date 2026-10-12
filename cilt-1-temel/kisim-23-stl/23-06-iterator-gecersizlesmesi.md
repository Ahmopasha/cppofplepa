---
cilt: "I — Temel"
kisim: "23 — STL"
baslik: "23.6 İteratör geçersizleşmesi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 23.6 İteratör geçersizleşmesi

Kaba ekleme veya silme yapmak, elinizdeki iteratörleri **geçersiz kılabilir.** Geçersiz
bir iteratörü kullanmak tanımsız davranıştır.

```cpp
std::vector<int> v{1, 2, 3};
auto it = v.begin();
v.push_back(4);       // vector yeniden yer ayırmış olabilir
*it;                  // tanımsız davranış
```

Kurallar kaba göre değişir. `vector`'de yeniden yer ayırma her şeyi geçersizleştirir;
`list` ve `map`'te yalnızca silinen elemanın iteratörü geçersizleşir.

Döngü içinde silme yaparken `erase`'in döndürdüğü iteratörü kullanın:

```cpp
for (auto it = v.begin(); it != v.end(); ) {
    if (*it % 2 == 0)
        it = v.erase(it);      // erase, sonraki konumu döndürür
    else
        ++it;
}
```
