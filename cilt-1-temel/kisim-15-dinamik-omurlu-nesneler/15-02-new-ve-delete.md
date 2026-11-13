---
cilt: "I — Temel"
kisim: "15 — Dinamik Ömürlü Nesneler"
baslik: "15.2 `new` ve `delete`"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 15.2 `new` ve `delete`

C dilinde dinamik bellek işlemleri kütüphane işlevleriyle yapılır. C++'ta bunlar
**operatör düzeyinde** işlemlerdir.

```cpp
Myclass* p = new Myclass{10};
delete p;

int* a = new int[100];
delete[] a;
```

`new` iki iş yapar: bellek ayırır ve nesneyi hayata getirir. `new Myclass{10}` örneğinde
bu, kurucu işlevin çağrılmasıdır; `new int[100]` gibi yerleşik türde ilk değer
belirtilmezse elemanlara değer verilmez ve bu değerleri okumak tanımsız davranıştır
(default-initialization, Kısım 3.2); `new int[100]{}` yazılırsa elemanlar sıfırla ilk
değer alır. `delete` de iki iş yapar: sınıf türünde sonlandırıcı işlevi çağırır ve belleği
geri verir. `std::malloc` ve `std::free` bunlardan yalnızca bellekle ilgili olanı yapar;
sınıf nesnesi oluşturup yok etmek için `new` ve `delete` yerine kullanılmamalıdır.

**Eşleştirme kuralı kesindir.** `new` ile ayrılan `delete` ile, `new[]` ile ayrılan
`delete[]` ile bırakılır. Karıştırmak tanımsız davranıştır.

Değeri `nullptr` olan bir göstericiye `delete` ya da `delete[]` uygulamak güvenlidir ve
hiçbir şey yapmaz; denetim yazmanıza gerek yoktur.
