---
cilt: "II — İleri"
kisim: "13 — İleri Hata Yönetimi"
baslik: "13.3 `noexcept` ve geçersiz kılma"
kaynak: "ders notları"
kutular: ["Standart Notu — C++17"]
son_kontrol: "2026-09 (C++23)"
---

## 13.3 `noexcept` ve geçersiz kılma

Sanal bir işlevi geçersiz kılarken `noexcept` **eklenebilir, kaldırılamaz.**

```cpp
class Base { public: virtual void f(int);          };
class Der  { public: void f(int) noexcept override; };   // geçerli

class Base2 { public: virtual void f(int) noexcept; };
class Der2  { public: void f(int) override;         };   // sentaks hatası
```

Sebep, Cilt II Kısım 6.3'teki ilkeyle aynıdır: çağıran kod taban sınıfın sözleşmesine
güvenir. Taban sınıf "hata göndermem" demişse, türemiş sınıf bu vaadi bozamaz; tersi
serbesttir çünkü daha güçlü bir vaat vermek sözleşmeyi ihlal etmez.

> **Standart Notu — C++17**
> **C++17 öncesi:** `noexcept` bir işlevin türünün parçası değildi; yalnızca bir
> belirteçti. İşlev göstericilerine atamada denetlenmezdi.
> **C++17 ile:** `noexcept` işlev türünün parçası oldu. `void(*)() noexcept` ile
> `void(*)()` artık farklı türlerdir ve geçersiz kılmada yukarıdaki kural uygulanır.
> **Neden değişti:** Taşıma semantiğinin `noexcept`e bağımlı hâle gelmesi (bkz. Kısım
> 2.6), belirtecin tür sistemine dahil edilmesini gerekli kıldı.
