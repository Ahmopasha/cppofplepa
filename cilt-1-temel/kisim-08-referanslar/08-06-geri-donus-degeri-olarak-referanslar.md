---
cilt: "I — Temel"
kisim: "8 — Referanslar"
baslik: "8.6 Geri dönüş değeri olarak referanslar"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 8.6 Geri dönüş değeri olarak referanslar

Bir işlev L-Value referans döndürebilir. Döndürdüğünde çağrı ifadesi L-Value olur; `const`
olmayan bir L-Value referans döndürüyorsa atamanın solunda da durabilir. (Nesne türüne
R-Value referans (`T&&`) döndüren bir çağrı ise X-Value'dur; bkz. Kısım 2.4.3.)

<!-- kod-baglam
std::vector<int> vec(10);
-->
```cpp
int& eleman(std::vector<int>& v, int i)
{
    return v[i];
}

eleman(vec, 3) = 42;     // geçerli
```

**Yerel bir nesneye referans döndürmeyin.**

```cpp
int& bozuk()
{
    int x = 10;
    return x;        // x işlev bitince yok olur
}
```

Bu kod sentaks hatası değildir. Dönen referans, artık var olmayan bir nesneyi gösterir;
kullanmak tanımsız davranıştır.

Kural: referans döndürüyorsanız, döndürdüğünüz şeyin **işlev çağrısından daha uzun
yaşadığından** emin olun. Çağıranın referansla verdiği ve çağrıdan sonra da yaşayan bir
nesnenin kendisi ya da elemanı, yaşamaya devam eden bir nesnenin veri elemanı ve `static`
ömürlü nesneler bu koşulu sağlar; `static` olmayan yerel nesneler (değerle alınan
parametreler dahil) sağlamaz. Referans parametreye (`const T&` ya da `T&&`) bağlanan nesne
geçiciyse (argüman geçici bir değerse ya da tür dönüşümüyle geçici nesne oluştuysa; bkz.
Kısım 8.4), o nesne çağrıyı içeren tam ifadenin sonunda yok olur; ona ya da elemanına
dönen referans o noktadan sonra sarkar.
