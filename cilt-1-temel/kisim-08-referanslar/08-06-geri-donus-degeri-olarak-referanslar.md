---
cilt: "I — Temel"
kisim: "8 — Referanslar"
baslik: "8.6 Geri dönüş değeri olarak referanslar"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 8.6 Geri dönüş değeri olarak referanslar

Bir işlev referans döndürebilir. Döndürdüğünde, çağrı ifadesi L-Value olur ve atamanın
solunda durabilir.

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

Bu koda derleyici genellikle uyarı verir ama sentaks hatası değildir. Dönen referans,
artık var olmayan bir nesneyi gösterir; kullanmak tanımsız davranıştır.

Kural: referans döndürüyorsanız, döndürdüğünüz şeyin **işlev çağrısından daha uzun
yaşadığından** emin olun. Parametre olarak gelen bir nesnenin elemanı, sınıfın veri
elemanı ve `static` ömürlü nesneler bu koşulu sağlar; yerel nesneler sağlamaz.
