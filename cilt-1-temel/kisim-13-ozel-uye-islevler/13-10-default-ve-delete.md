---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.10 `= default` ve `= delete`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 13.10 `= default` ve `= delete`

Derleyicinin yazacağı hâli açıkça istemek için `= default` kullanılır:

```cpp
class Myclass {
public:
    Myclass() = default;
    ~Myclass() = default;
};
```

Bir işlevin **hiç olmamasını** istiyorsanız `= delete` kullanılır. Silinmiş bir işlevi
çağırmak sentaks hatasıdır:

```cpp
class Myclass {
public:
    Myclass(const Myclass&) = delete;              // kopyalanamaz
    Myclass& operator=(const Myclass&) = delete;
};
```

Bu, kopyalanmaması gereken türleri ifade etmenin doğru yoludur. Eskiden aynı iş,
işlevleri `private` bölüme tanımsız olarak bildirerek yapılırdı; artık gerekmiyor.
