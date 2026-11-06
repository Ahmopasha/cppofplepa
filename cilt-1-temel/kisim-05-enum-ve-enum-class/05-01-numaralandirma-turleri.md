---
cilt: "I — Temel"
kisim: "5 — `enum` ve `enum class`"
baslik: "5.1 Numaralandırma türleri"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 5.1 Numaralandırma türleri

`enum`, isimlendirilmiş sabitler, yani numaralandırıcılar (Kısım 1.8) içeren bir tür
tanımlar.

```cpp
enum Renk { Kirmizi, Yesil, Mavi };
```

Değerler varsayılan olarak sıfırdan başlar ve birer artar. İstediğiniz sabite değer
verebilirsiniz; sonrakiler oradan devam eder.

```cpp
/*
 * Bekliyor 10, Calisiyor 11, Bitti 50, Iptal 51
 */
enum Durum { Bekliyor = 10, Calisiyor, Bitti = 50, Iptal };
```

Bir `enum` türünün alabileceği değerler numaralandırıcılarla sınırlı olmayabilir. Her
`enum` kendi başına bir türdür; C'den farklı olarak tamsayı türlerinden biri değildir. Ama
kapsamlandırılmamış `enum` türleri tamsayı türlerine örtülü olarak dönüşür. Bu ikili
konum, Kısım 5.2'deki ikinci sorunun kaynağıdır.
