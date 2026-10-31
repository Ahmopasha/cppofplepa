---
cilt: "I — Temel"
kisim: "10 — Tür Dönüştürme Operatörleri"
baslik: "10.2 `static_cast`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 10.2 `static_cast`

Dilin normalde örtülü olarak yapabileceği veya birbiriyle ilişkili türler arasındaki
dönüşümler için kullanılır.

```cpp
double d = 3.9;
int i = static_cast<int>(d);              // sayısal dönüşüm

void* vp = malloc(100);
int* ip = static_cast<int*>(vp);          // void* → T*

int x = static_cast<int>(Renk::Yesil);    // enum class → int
```

Kalıtım hiyerarşisinde taban sınıf göstericisinden türemiş sınıf göstericisine
dönüşümde de kullanılabilir, ama denetim yapmaz; doğru olduğundan emin değilseniz
`dynamic_cast` kullanın.
