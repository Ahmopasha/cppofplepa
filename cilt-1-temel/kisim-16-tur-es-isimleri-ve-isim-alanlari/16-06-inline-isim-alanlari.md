---
cilt: "I — Temel"
kisim: "16 — Tür Eş İsimleri ve İsim Alanları"
baslik: "16.6 `inline` isim alanları"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 16.6 `inline` isim alanları

İçindeki isimler, dıştaki isim alanına aitmiş gibi görünür.

```cpp
namespace kutuphane {
    inline namespace v2 {
        void islev();
    }
    namespace v1 {
        void islev();
    }
}

kutuphane::islev();        // v2::islev çağrılır
kutuphane::v1::islev();    // eski sürüm hâlâ erişilebilir
```

Kullanım amacı sürümlemedir: kütüphanenin güncel sürümü varsayılan olur, eski sürüm
niteleyerek erişilebilir kalır. Uygulama kodunda nadiren gerekir.
