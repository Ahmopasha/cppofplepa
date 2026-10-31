---
cilt: "I — Temel"
kisim: "15 — Dinamik Ömürlü Nesneler"
baslik: "15.2 `new` ve `delete`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
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

`new` iki iş yapar: bellek ayırır ve nesneyi hayata getirir, yani kurucu işlevi çağırır.
`delete` de iki iş yapar: sonlandırıcı işlevi çağırır ve belleği geri verir. `malloc` ve
`free` bunlardan yalnızca birincisini yapar; C++ sınıflarıyla kullanılmamalıdır.

**Eşleştirme kuralı kesindir.** `new` ile ayrılan `delete` ile, `new[]` ile ayrılan
`delete[]` ile bırakılır. Karıştırmak tanımsız davranıştır.

`nullptr` üzerinde `delete` çağırmak güvenlidir ve hiçbir şey yapmaz; denetim yazmanıza
gerek yoktur.
