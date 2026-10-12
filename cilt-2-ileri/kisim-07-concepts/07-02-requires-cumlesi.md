---
cilt: "II — İleri"
kisim: "7 — Concepts"
baslik: "7.2 `requires` cümlesi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 7.2 `requires` cümlesi

Bir şablona kısıt eklemenin en açık yoludur. Derleme zamanında `bool` üreten bir ifade
alır.

```cpp
template<typename T>
requires std::integral<T>
void func(T t);
```

Şablon parametre listesinden sonra yazılabildiği gibi, işlev bildiriminden sonra da
yazılabilir:

```cpp
template<typename T>
void func(T t) requires std::integral<T>;
```

İkinci biçim, üye işlevlerde sınıfın şablon parametrelerine kısıt koymak için gereklidir.

Kısıtlar mantık operatörleriyle birleştirilir:

```cpp
template<typename T>
requires std::integral<T> || std::floating_point<T>
void func(T t);
```
