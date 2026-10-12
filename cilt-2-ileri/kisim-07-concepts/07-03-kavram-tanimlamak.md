---
cilt: "II — İleri"
kisim: "7 — Concepts"
baslik: "7.3 Kavram tanımlamak"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 7.3 Kavram tanımlamak

Aynı kısıtı defalarca yazmak yerine isimlendirilir. **Kavram**, isimlendirilmiş bir
kısıttır.

```cpp
template<typename T>
concept Sayisal = std::integral<T> || std::floating_point<T>;

template<Sayisal T>
void func(T t);
```

`concept` bir `constexpr bool` değişken şablonu gibi davranır; doğrudan da
sorgulanabilir:

```cpp
static_assert(Sayisal<int>);
static_assert(!Sayisal<std::string>);
```

Kavramlar özelleştirilemez ve özyinelemeli olamaz.
