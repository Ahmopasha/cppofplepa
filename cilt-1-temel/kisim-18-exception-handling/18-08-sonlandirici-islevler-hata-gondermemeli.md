---
cilt: "I — Temel"
kisim: "18 — Exception Handling"
baslik: "18.8 Sonlandırıcı işlevler hata göndermemeli"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
kutular: ["Standart Notu — C++11"]
---

## 18.8 Sonlandırıcı işlevler hata göndermemeli

Yığın geri sarılırken bir sonlandırıcı işlev hata gönderirse, ortada aynı anda iki hata
olur ve program `std::terminate` çağrısıyla sonlanır.

Bu yüzden sonlandırıcı işlevler C++11'den itibaren **örtülü olarak `noexcept`**'tir;
`noexcept(false)` yazılırsa (işlevin hata gönderebileceğini açıkça bildirir; Cilt II,
Kısım 13) ya da bir veri elemanının veya taban sınıfın sonlandırıcısı hata gönderebilirse
bu geçerli olmaz. `noexcept` bir işlevden hata dışarı çıkarsa `std::terminate` çağrılır.
Gövdede hata gönderebilecek bir iş yapıyorsanız, onu sonlandırıcı işlevin içinde yakalayıp
yutmanız gerekir.

> **Standart Notu — C++11**
> **C++11 öncesi:** Hata gönderebileceği belirtilmemiş bir sonlandırıcı da hata
> gönderebilirdi; gönderdiği hata (yığın geri sarılırken değilse) çağırana yayılırdı.
> **C++11 ile:** Böyle bir sonlandırıcı, yukarıdaki koşullar dışında örtülü olarak
> `noexcept`'tir; hata dışarı çıkarsa `std::terminate` çağrılır.

`noexcept` anahtar sözcüğü, bir işlevin hata göndermeyeceğini bildirir:

```cpp
void f() noexcept;
```

Taşıyan işlevlerde `noexcept` bildiriminin performans üzerindeki belirleyici rolü Cilt II,
Kısım 2.6'da anlatılıyor.
