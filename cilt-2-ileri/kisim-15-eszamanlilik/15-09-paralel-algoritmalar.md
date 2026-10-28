---
cilt: "II — İleri"
kisim: "15 — Eşzamanlılık"
baslik: "15.9 Paralel algoritmalar"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 15.9 Paralel algoritmalar

C++17, STL algoritmalarının çoğuna **çalıştırma ilkesi** *(execution policy)* parametresi
ekledi. İş parçacığı ve bölme işini kütüphane üstlenir.

```cpp
#include <algorithm>
#include <execution>

std::sort(std::execution::par, v.begin(), v.end());
```

Standart dört ilke tanımlar: `seq` (sıralı), `par` (paralel), `par_unseq` (paralel ve
vektörleşmiş), `unseq` (yalnızca vektörleşmiş, C++20). `seq` dışındaki ilkeler birer
izindir, zorunluluk değildir: `par` paralel yürütmeye izin verir, ama gerçekleme işi
çağıran iş parçacığında da yapabilir.

Kullanım koşulları katıdır. Geçirdiğiniz çağrılabilir nesneler **data race üretmemeli**.
`par_unseq` ve `unseq` durumunda kilit almak gibi **vektörleşmeye uygun olmayan**
*(vectorization-unsafe)* kütüphane işlevleri de çağrılmamalıdır; çağrılırsa davranış
tanımsızdır, çünkü vektörleşme işlemlerin birbirine geçmesine yol açar. Standart ilkelerin
dördünde de algoritmanın çağırdığı bir **öğe erişim işlevinden**
*(element access function)*, örneğin geçirdiğiniz karşılaştırıcıdan, hata kaçarsa
`std::terminate` çağrılır; bu hata, ilkesiz çağrıdaki gibi çağırana ulaşmaz.

Kazanç her zaman oluşmaz. Standart bir iş parçacığı kurulmasını bile garanti etmez; küçük
kaplarda paralel yürütmenin ek maliyeti kazancı aşabilir. Ölçmeden kullanmayın.
