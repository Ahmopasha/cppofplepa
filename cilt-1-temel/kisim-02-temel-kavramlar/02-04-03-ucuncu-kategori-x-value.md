---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.4.3 Üçüncü kategori: X-Value"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

### 2.4.3 Üçüncü kategori: X-Value

Bazı durumlarda elimizde bellekte yeri olan ama artık kullanılmayacağını bildiğimiz
bir nesne olur. Böyle bir nesnenin kaynaklarını kopyalamak yerine devralmak isteriz.
`std::move` bunu işaretlemeye yarar:

```cpp
std::string s1 = "uzun bir yazı";
std::string s2 = std::move(s1);   // s1'in kaynağı kopyalanmaz, devralınır
```

`std::move(s1)` ifadesinin kategorisi **X-Value**'dur. Hem bellekte bir yeri vardır
(`s1` orada duruyor), hem de kaynağı devralınabilir.

Üç kategori arasındaki ilişki şudur: X-Value, R-Value'ların bir alt türüdür. Bir
R-Value ya geçici bir şeydir ya da `std::move` ile işaretlenmiş bir nesnedir.

> Kategorilerin tam listesi üçle sınırlı değildir; bunları gruplayan iki kategori daha
> vardır. Bunlar günlük kod yazarken gerekmez. Cilt II, Kısım 1.1'de ele alınıyorlar.
