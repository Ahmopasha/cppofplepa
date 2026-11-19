---
cilt: "I — Temel"
kisim: "21 — Composition"
baslik: "21.3 Özel üye işlevler ve composition"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 21.3 Özel üye işlevler ve composition

Composition'ın en büyük pratik kazancı burada ortaya çıkar.

Veri elemanlarınızın hepsi kendi kaynaklarını doğru yönetiyorsa,
**sizin hiçbir özel üye işlev yazmanıza gerek kalmaz.** Derleyicinin yazdığı işlevler,
sınıf türünden her veri elemanı için o elemanın kendi işlevini çağırır; kopyalama ve
taşıma işlevleri yerleşik türden (ör. `int`, gösterici) elemanları doğrudan kopyalar
(Kısım 13.2). Bir elemanın kopyalayan kurucu işlevi ya da kopyalayan atama işlevi silinmiş
ya da erişilemez ise, derleyicinin bildirdiği karşılık gelen işlev silinmiş (Kısım 13.10)
sayılır.

<!-- kod-baglam
struct Ek { };
-->
```cpp
class Kayit {
    std::string ad;
    std::vector<int> notlar;
    std::unique_ptr<Ek> ek;
};

Kayit a;
Kayit b = a;            // sentaks hatası
Kayit c = std::move(a); // geçerli
```

`std::unique_ptr` (Kısım 25) kopyalanamadığı için `Kayit`'in kopyalayan kurucu işlevi de
kopyalayan atama işlevi de silinmiş sayılır; `Kayit` kopyalanamaz, `b`'nin tanımı bu
yüzden sentaks hatasıdır. Taşıma işlevleri ve sonlandırıcı işlev ise doğru çalışır; tek
satır yazmadınız. Kısım 13.9'daki Rule of Zero tam olarak budur ve composition onun
uygulama aracıdır.
