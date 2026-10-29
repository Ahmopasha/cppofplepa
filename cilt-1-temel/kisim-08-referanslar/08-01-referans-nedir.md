---
cilt: "I — Temel"
kisim: "8 — Referanslar"
baslik: "8.1 Referans nedir"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 8.1 Referans nedir

Referans, bağlandığı nesne için **ikinci bir isim gibi kullanılır.** Var olan bir nesneye
bağlandığında yeni bir nesne oluşturmaz, o nesneye bir ad daha verir. (Geçici bir değere
—`100` gibi, X-Value olmayan bir R-Value'ya— bağlanan referans ise o sırada oluşturulan
geçici bir nesneye bağlanır; bkz. Kısım 8.3. Türler uyumsuzsa da geçici nesne
oluşturulabilir; bkz. Kısım 8.4.)

```cpp
int x = 10;
int& r = x;      // r, x'in başka bir adı

r = 20;
std::cout << x;  // 20 yazar — r, x nesnesini belirtir
```

Göstericiden farkı burada başlar: gösterici bir nesnedir ve başka bir nesnenin adresini
tutar; referans ise bir nesne değildir, bağlandığı nesneyi belirtir.
