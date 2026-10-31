---
cilt: "I — Temel"
kisim: "5 — `enum` ve `enum class`"
baslik: "5.1 Numaralandırma türleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 5.1 Numaralandırma türleri

`enum`, sınırlı sayıda isimlendirilmiş değerden oluşan bir tür tanımlar.

```cpp
enum Renk { Kirmizi, Yesil, Mavi };
```

Değerler varsayılan olarak sıfırdan başlar ve birer artar. İstediğiniz sabite değer
verebilirsiniz; sonrakiler oradan devam eder.

```cpp
enum Durum { Bekliyor = 10, Calisiyor, Bitti = 50, Iptal };
// Bekliyor 10, Calisiyor 11, Bitti 50, Iptal 51
```

`enum` türleri hem kullanıcı tanımlı türlerdir hem de tamsayı türleridir. Bu ikili
konum, birazdan görülecek sorunların kaynağıdır.
