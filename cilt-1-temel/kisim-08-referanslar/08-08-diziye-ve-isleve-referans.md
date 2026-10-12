---
cilt: "I — Temel"
kisim: "8 — Referanslar"
baslik: "8.8 Diziye ve işleve referans"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 8.8 Diziye ve işleve referans

Referans yalnızca sıradan nesnelere bağlanmaz.

```cpp
int a[5]{};
int (&ra)[5] = a;        // diziye referans — boyut türün parçası

void foo(int);
void (&rf)(int) = foo;   // işleve referans
rf(10);                  // foo(10) çağrılır
```

Diziye referans, dizinin boyutunu tür bilgisi olarak koruduğu için göstericiye
dönüşmenin bilgi kaybını önler. İkisi de günlük kodda sık kullanılmaz; şablon yazarken
karşınıza çıkar.
