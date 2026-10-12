---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.2.1 Üçüncü referans türü"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

### 1.2.1 Üçüncü referans türü

Cilt I'de iki referans türü tanıtılmıştı: `T&` ve `T&&`. Aslında üçüncü bir tür vardır ve
yazılışı `T&&` ile **aynıdır.**

```cpp
template<typename T>
void foo(T&& arg);        // forwarding reference

void bar(Myclass&& arg);  // R-Value referans
```

İkisi de `&&` ile yazılır ama davranışları taban tabana zıttır. `bar` yalnızca R-Value
alır; `foo` ise `const` olsun olmasın, her değer kategorisinden ifadeyi kabul eder.

Bu türe standart metninde **forwarding reference** denir. Ders anlatımlarında ve
literatürde **universal reference** adı da yaygındır; ikisi aynı şeydir. Bu kitapta
forwarding reference kullanılacak.

Forwarding reference yalnızca iki yerde oluşur:

```cpp
template<typename T>
void foo(T&& arg);        // 1. çağrıdan çıkarılan şablon parametresi

auto&& r = 31;            // 2. auto ile
void func(auto&& x);      // C++20 kısaltılmış şablon sözdizimi, yine auto
```
