---
cilt: "I — Temel"
kisim: "10 — Tür Dönüştürme Operatörleri"
baslik: "10.2 `static_cast`"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 10.2 `static_cast`

Dilin normalde örtülü olarak yapabileceği veya birbiriyle ilişkili türler arasındaki
dönüşümler için kullanılır.

```cpp
double d = 3.9;
int i = static_cast<int>(d);              // sayısal dönüşüm

void* vp = std::malloc(100);
int* ip = static_cast<int*>(vp);          // void* → T*

int x = static_cast<int>(Renk::Yesil);    // enum class → int (Kısım 5.3)
```

Kalıtım hiyerarşisinde (Kısım 17) taban sınıf göstericisinden ya da referansından türemiş
sınıfınkine dönüşümde — **aşağı dönüşüm** *(downcasting)* — de kullanılabilir, ama çalışma
zamanında denetim yapmaz: gösterilen nesne gerçekte o türemiş sınıftan değilse davranış
tanımsızdır. Doğru olduğundan emin değilseniz, taban sınıf çok biçimliyse (Kısım 17.6)
`dynamic_cast` (Kısım 10.5) kullanın.
