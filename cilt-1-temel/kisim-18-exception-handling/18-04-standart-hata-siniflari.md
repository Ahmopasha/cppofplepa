---
cilt: "I — Temel"
kisim: "18 — Exception Handling"
baslik: "18.4 Standart hata sınıfları"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 18.4 Standart hata sınıfları

Standardın kütüphane işlevleri için yazdığı hatalar `std::exception` sınıfından türeyen
sınıflardandır. Bu sayede `std::exception` türüne referans alan tek bir `catch` bloğu
bunların hepsini yakalayabilir; standartta hangi hataları gönderebileceği yazılmamış
işlevlerin hatalarının türü ise gerçeklemeye bağlıdır. (Sizin türlerinizin işlemlerinden
çıkan hatalar ise `std::exception`'dan türemek zorunda değildir.) Aşağıda bu hiyerarşinin
bir kısmı var:

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

Yerleşik türden değerleri (`int`, `const char*`) göndermek mümkündür ama yapılmamalıdır;
bunlar `std::exception`'dan türemediği için `catch (const std::exception&)` bloğu onları
yakalamaz ve `what()` ile açıklama alınamaz.
