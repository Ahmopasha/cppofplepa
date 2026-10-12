---
cilt: "II — İleri"
kisim: "2 — Taşıma Semantiği ve Bildirim Kuralları"
baslik: "2.3 Kopyalanabilirlik ve taşınabilirlik tasarımı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 2.3 Kopyalanabilirlik ve taşınabilirlik tasarımı

Tablodan iki yaygın tasarım doğrudan okunur.

**Ne kopyalanabilir ne taşınabilir:**

```cpp
class Myclass {
public:
    Myclass(const Myclass&) = delete;
    Myclass& operator=(const Myclass&) = delete;
};
```

Kopyalayan işlevleri bildirmek taşıyanları *not declared* yapar; ayrıca silmeye gerek
yoktur. `std::mutex` bu gruptadır.

**Kopyalanamaz ama taşınabilir:**

```cpp
class Myclass {
public:
    Myclass(Myclass&&) noexcept = default;
    Myclass& operator=(Myclass&&) noexcept = default;
};
```

Taşıyan işlevleri bildirmek kopyalayanları siler. `std::unique_ptr` ve `std::thread` bu
gruptadır.
