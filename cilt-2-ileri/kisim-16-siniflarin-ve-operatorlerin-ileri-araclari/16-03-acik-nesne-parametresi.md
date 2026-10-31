---
cilt: "II — İleri"
kisim: "16 — Sınıfların ve Operatörlerin İleri Araçları"
baslik: "16.3 Açık nesne parametresi"
kaynak: "ders notları"
kutular: ["Standart Notu — C++23"]
son_kontrol: "2026-10 (C++23)"
---

## 16.3 Açık nesne parametresi

C++23, `this`'in gizli parametre olmaktan çıkıp **açıkça yazılabilmesini** sağladı.
İngilizcede *deducing this* olarak anılır.

```cpp
class Myclass {
public:
    void func(this Myclass& self) { /* ... */ }
};
```

İlk parametre `this` anahtar sözcüğüyle başlarsa, o parametre nesnenin kendisidir. Gövdede
`this` göstericisi yoktur; `self` kullanılır.

Çözdüğü problem, 16.2'deki dört sürüm tekrarıdır. `const` olan ve olmayan, L-Value ve
R-Value sürümlerini ayrı ayrı yazmak yerine tek şablon yazılır:

```cpp
class Sarmal {
    std::vector<int> veri;
public:
    template<typename Self>
    auto&& al(this Self&& self) { return std::forward<Self>(self).veri; }
};
```

`Self`, nesnenin kategorisini ve `const`luğunu taşır; bu, Kısım 1.2'deki forwarding
reference mekanizmasının üye işlevlere uygulanmış hâlidir.

İkinci kullanımı, özyinelemeli lambda ifadeleridir (bkz. Kısım 12). Üçüncüsü, CRTP
deyimini `static_cast` yazmadan kurabilmektir (bkz. Kısım 6.13 ve 14).

> **Standart Notu — C++23**
> **C++23 öncesi:** Açık nesne parametresi yoktur; `const` ve referans nitelikli sürümler
> ayrı ayrı yazılır (Kısım 16.2).
> **C++23 ile:** Nesne parametresi açıkça yazılabilir ve tek şablonla bütün sürümler
> karşılanabilir.
