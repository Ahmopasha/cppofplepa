---
cilt: "I — Temel"
kisim: "9 — İşlev Yüklemesi ve Yükleme Çözümlemesi"
baslik: "9.8 Varsayılan argümanlar ve çift anlamlılık"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 9.8 Varsayılan argümanlar ve çift anlamlılık

Varsayılan argüman, yüklemeyle birlikte kullanılınca çift anlamlılığa yol açabilir (Kısım
7.3):

```cpp
void func(int);
void func(int, int = 10);

func(5);        // sentaks hatası: çift anlamlılık
```

İki işlevin imzaları farklıdır (Kısım 9.2). Ama varsayılan argüman ikincisini de tek
argümanla çağrılabilir kılar; tek argümanlı çağrıda ikisi de uygun adaydır (Kısım 9.4).
Yalnızca ilk argüman karşılaştırılır ve argüman iki parametreyle de aynı türde (`int`)
olduğu ve ikisinde de dönüşüm gerekmediği için hiçbiri diğerinden iyi değildir (Kısım
9.7).
