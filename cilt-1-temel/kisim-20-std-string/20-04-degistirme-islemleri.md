---
cilt: "I — Temel"
kisim: "20 — `std::string`"
baslik: "20.4 Değiştirme işlemleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 20.4 Değiştirme işlemleri

```cpp
s.append("ek");
s.insert(3, "araya");
s.erase(2, 4);            // 2. indisten itibaren 4 karakter sil
s.replace(0, 3, "yeni");
s.substr(2, 5);           // yeni bir string döndürür
s.push_back('a');
s.pop_back();
```

`substr` dışındakiler nesnenin kendisini değiştirir.
