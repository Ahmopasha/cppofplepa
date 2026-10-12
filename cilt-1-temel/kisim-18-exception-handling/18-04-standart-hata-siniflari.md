---
cilt: "I — Temel"
kisim: "18 — Exception Handling"
baslik: "18.4 Standart hata sınıfları"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 18.4 Standart hata sınıfları

Standart kütüphane, gönderdiği bütün hata nesnelerini `std::exception` sınıfından türeyen
sınıflardan üretir. Bu sayede tek bir `catch` bloğu hepsini karşılayabilir.

```
std::exception
├── std::logic_error          — programcı hatası, önceden önlenebilirdi
│   ├── std::invalid_argument
│   ├── std::out_of_range
│   └── std::length_error
└── std::runtime_error        — çalışma zamanında ortaya çıkan durum
    ├── std::overflow_error
    └── std::range_error
```

`std::exception` sınıfının `what()` üye işlevi, hatayı açıklayan bir yazı döndürür.
Sanal bir işlevdir; kendi hata sınıflarınızda geçersiz kılabilirsiniz.

Kendi hata sınıfınızı yazarken bu hiyerarşiden türetin:

```cpp
class VeritabaniHatasi : public std::runtime_error {
public:
    using std::runtime_error::runtime_error;    // kurucu işlevleri devral
};
```

Böylece sizin hatanız da `catch (const std::exception&)` ile yakalanabilir hâle gelir.

İlkel türleri (`int`, `const char*`) göndermek mümkündür ama yapılmamalıdır; hata
nesnesinin taşıdığı bilgi ve hiyerarşiye dahil olması kaybolur.
