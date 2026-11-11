---
cilt: "I — Temel"
kisim: "10 — Tür Dönüştürme Operatörleri"
baslik: "10.3 `const_cast`"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 10.3 `const_cast`

Yalnızca `const` ve `volatile` niteleyicilerini ekler veya kaldırır.

```cpp
const int* cp = &x;
int* p = const_cast<int*>(cp);
```

> **`const`luğu kaldırıp nesneyi değiştirmek, nesne gerçekten `const` ise tanımsız davranıştır.**
> Meşru kullanımı, aslında `const` olmayan bir nesneye `const T*` ya da `const T&`
> türünden bir gösterici ya da referans üzerinden erişildiği ya da, nesne gerçekten
> `const` olsa bile, dönüşümden sonra nesnenin değiştirilmediği durumlardır; tipik
> olarak nesneyi değiştirmeyen ama `const` desteklemeyen eski C arayüzlerine çağrı
> yaparken.
