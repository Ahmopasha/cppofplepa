---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.6 Tamamlanmış ve tamamlanmamış türler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 2.6 Tamamlanmış ve tamamlanmamış türler

Derleyici bir türün **boyutunu ve yapısını** biliyorsa o tür tamamlanmıştır. Yalnızca
bildirimini gördüyse tamamlanmamıştır.

```cpp
class Myclass;         // Myclass artık tamamlanmamış bir türdür
```

Tamamlanmamış bir türle **yapabilecekleriniz**:

```cpp
Myclass* p;                    // gösterici tanımlama
Myclass& f(Myclass&);          // işlev bildiriminde parametre ve geri dönüş türü
using Mc = Myclass;            // tür eş ismi
extern Myclass m;              // extern bildirim
```

Göstericiler ve referanslar çalışır, çünkü bir göstericinin boyutu gösterdiği nesneden
bağımsızdır.

**Yapamayacaklarınız**:

```cpp
Myclass m;                     // nesne oluşturma
sizeof(Myclass);               // sizeof operandı yapma
class Der : public Myclass {}; // kalıtımda taban sınıf yapma
```

Tamamlanmamış tür, başlık dosyaları arasındaki bağımlılığı azaltmak için kullanılır.
Yalnızca göstericisine ihtiyacınız varsa, o sınıfın başlık dosyasını dahil etmek yerine
ileri bildirim yapmanız yeterlidir; derleme süreniz kısalır ve bağımlılık zinciri
kırılır.

> Gereksiz başlık dosyası eklemekten kaçının. İleri bildirimle çözülebilecek bir
> bağımlılığı `#include` ile çözmek, projenin derleme süresini gereksiz yere büyütür.

`void` türü de tamamlanmamış bir türdür ve tamamlanması mümkün değildir.
