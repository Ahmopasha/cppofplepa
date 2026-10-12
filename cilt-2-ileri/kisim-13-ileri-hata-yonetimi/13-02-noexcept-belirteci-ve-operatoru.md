---
cilt: "II — İleri"
kisim: "13 — İleri Hata Yönetimi"
baslik: "13.2 `noexcept` belirteci ve operatörü"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 13.2 `noexcept` belirteci ve operatörü

İkisi ayrı şeylerdir ve aynı anahtar sözcükle yazılırlar.

**Belirteç**, işlevin hata göndermeyeceğini bildirir:

```cpp
void f() noexcept;
```

Koşullu biçimi, başka bir ifadenin `noexcept`liğine bağlar:

```cpp
template<typename T>
void g(T t) noexcept(std::is_nothrow_copy_constructible_v<T>);
```

**Operatör**, bir ifadenin hata gönderip göndermeyeceğini derleme zamanında sorgular ve
`bool` üretir:

```cpp
static_assert(noexcept(f()));
```

Operatör ifadeyi **çalıştırmaz**; `sizeof` gibi değerlendirilmeyen bağlamdır
(bkz. Kısım 5.5).

`noexcept` bildirilmiş bir işlev yine de hata gönderirse, yakalanmaz;
`std::terminate` çağrılır. Belirteç bir dilek değil, bir taahhüttür.
