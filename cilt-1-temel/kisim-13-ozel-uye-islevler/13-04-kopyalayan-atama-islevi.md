---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.4 Kopyalayan atama işlevi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 13.4 Kopyalayan atama işlevi

Aynı türden nesneler birbirine atandığında çağrılır. Geri dönüş türü, zincirleme atamayı
mümkün kılmak için sınıfın kendisine referanstır:

```cpp
Myclass& operator=(const Myclass& other);
```

```cpp
a = b = c;      // zincirleme atama bu sayede çalışır
```
