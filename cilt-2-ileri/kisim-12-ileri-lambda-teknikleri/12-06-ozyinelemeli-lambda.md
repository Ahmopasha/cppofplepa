---
cilt: "II — İleri"
kisim: "12 — İleri Lambda Teknikleri"
baslik: "12.6 Özyinelemeli lambda"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 12.6 Özyinelemeli lambda

Lambdanın kendisini çağırması, C++23 öncesinde doğrudan mümkün değildir; `auto f = ...`
ifadesinde `f` henüz tanımlanmamıştır.

Eski çözüm `std::function` kullanmaktır, ama bu tür silme maliyeti getirir
(bkz. Kısım 14):

```cpp
std::function<int(int)> fak = [&fak](int n) {
    return n <= 1 ? 1 : n * fak(n - 1);
};
```

C++23'ün açık nesne parametresi (bkz. Kısım 16.3) bunu maliyetsiz çözer:

```cpp
auto fak = [](this auto&& self, int n) {
    return n <= 1 ? 1 : n * self(n - 1);
};
```

`self`, kapanış nesnesinin kendisidir.
