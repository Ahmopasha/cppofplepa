---
cilt: "I — Temel"
kisim: "18 — Exception Handling"
baslik: "18.8 Sonlandırıcı işlevler hata göndermemeli"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 18.8 Sonlandırıcı işlevler hata göndermemeli

Yığın geri sarılırken bir sonlandırıcı işlev hata gönderirse, ortada aynı anda iki hata
olur ve program `std::terminate` çağrısıyla sonlanır.

Bu yüzden sonlandırıcı işlevler C++11'den itibaren **örtülü olarak `noexcept`**'tir.
Gövdesinde hata gönderebilecek bir iş yapıyorsanız, onu sonlandırıcı işlevin içinde
yakalayıp yutmanız gerekir.

`noexcept` anahtar sözcüğü, bir işlevin hata göndermeyeceğini bildirir:

```cpp
void f() noexcept;
```

Taşıyan işlevlerde bu bildirimin performans üzerindeki belirleyici rolü Cilt II, Kısım
2.6'da anlatıldı.
