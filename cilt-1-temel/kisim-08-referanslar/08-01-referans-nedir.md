---
cilt: "I — Temel"
kisim: "8 — Referanslar"
baslik: "8.1 Referans nedir"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 8.1 Referans nedir

Referans, var olan bir nesnenin **yerine geçen ikinci bir isimdir.** Yeni bir nesne
oluşturmaz, mevcut nesneye bir ad daha verir.

```cpp
int x = 10;
int& r = x;      // r, x'in başka bir adı

r = 20;
std::cout << x;  // 20 yazar — r ile x aynı nesne
```

Göstericiden farkı burada başlar: gösterici bir nesnedir ve başka bir nesnenin adresini
tutar; referans bir nesne değil, bir isimdir.
