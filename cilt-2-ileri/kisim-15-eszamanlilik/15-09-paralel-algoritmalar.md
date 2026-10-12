---
cilt: "II — İleri"
kisim: "15 — Eşzamanlılık"
baslik: "15.9 Paralel algoritmalar"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 15.9 Paralel algoritmalar

C++17, STL algoritmalarına çalıştırma ilkesi parametresi ekledi. Kilit, iş parçacığı ve
bölme işini kütüphane üstlenir.

```cpp
#include <execution>

std::sort(std::execution::par, v.begin(), v.end());
```

Dört ilke vardır: `seq` (sıralı), `par` (paralel), `par_unseq` (paralel ve vektörleşmiş),
`unseq` (yalnızca vektörleşmiş, C++20).

Kullanım koşulları katıdır. Geçirdiğiniz çağrılabilir nesneler **data race üretmemeli**
ve `par_unseq` durumunda kilit bile almamalıdır; vektörleşme, işlemlerin birbirine
geçmesine yol açar.

Kazanç her zaman oluşmaz; küçük kaplarda iş parçacığı kurma maliyeti kazancı aşar.
Ölçmeden kullanmayın.
