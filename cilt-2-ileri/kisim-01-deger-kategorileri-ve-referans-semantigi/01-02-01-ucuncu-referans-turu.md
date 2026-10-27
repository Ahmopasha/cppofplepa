---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.2.1 `T&&`'nin şablondaki anlamı"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

### 1.2.1 `T&&`'nin şablondaki anlamı

Cilt I'de iki referans türü tanıtılmıştı: `T&` ve `T&&`. Bir işlev şablonunda, çağrıdan
çıkarılan ve cv nitelemesiz bir şablon parametresi için yazılan `T&&`, ikincisinin özel
bir kullanımına karşılık gelir:

<!-- kod-baglam
class Myclass {};
-->
```cpp
template<typename T>
void foo(T&& arg);        // forwarding reference

void bar(Myclass&& arg);  // R-Value referans
```

İkisi de türü bakımından R-Value referanstır; fark, `T`'nin nasıl çıkarıldığındadır.
`bar` yalnızca R-Value alır. `foo`'da ise argüman L-Value olduğunda `T` bir L-Value
referans türüne çıkarılır ve referans çökmesiyle (bkz. Kısım 1.2.2) parametre L-Value
referans olur. Böylece `foo`, `const` olsun olmasın, hem L-Value hem R-Value argümanları
kabul eder. Küme parantezli bir ilk değer listesi ise bu yolla geçirilemez; ondan `T`
çıkarılamaz.

Bu kullanıma standart metninde **forwarding reference** denir. Literatürde
**universal reference** adı da yaygındır; ikisi aynı şeydir. Bu kitapta
forwarding reference kullanılacak.

Forwarding reference yalnızca iki yerde oluşur:

```cpp
template<typename T>
void foo(T&& arg);        // 1. çağrıdan çıkarılan şablon parametresi
void func(auto&& x);      // 1'in C++20 kısaltılmış yazımı

auto&& r = 31;            // 2. auto ile

template<typename T>
void baz(const T&& arg);  // R-Value referans

template<typename T>
class Kap { void ekle(T&& x); };  // R-Value referans
```
