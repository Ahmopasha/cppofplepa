---
cilt: "II — İleri"
kisim: "14 — Deyimler ve Kalıplar"
baslik: "14.6 Hata yönetimi deyimleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 14.6 Hata yönetimi deyimleri

**Exception Tracker**, hangi sınıfın hata gönderdiğinin izlenmesini sağlar. Her sınıf,
kendi hata türünü ortak bir taban sınıftan türetir ve tür bilgisi hatayla birlikte taşınır.

**Exception Dispatcher**, yakalama mantığını tek yerde toplar. Her `catch` zincirini
tekrarlamak yerine, hata bir işleve devredilir:

<!-- kod-baglam
void riskli();
-->
```cpp
void isle()
{
    try { throw; }                        // yeniden gönder, burada yakala
    catch (const std::bad_alloc&)    { /* ... */ }
    catch (const std::logic_error&)  { /* ... */ }
}

// kullanım
try { riskli(); }
catch (...) { isle(); }
```

Parametresiz `throw;` yalnızca `catch` bloğu içinde geçerlidir, ama o blok tarafından
**çağrılan** bir işlevin içinde de çalışır. Deyimin dayandığı nokta budur.
