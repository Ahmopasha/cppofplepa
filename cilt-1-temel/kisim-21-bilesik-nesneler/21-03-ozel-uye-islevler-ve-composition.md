---
cilt: "I — Temel"
kisim: "21 — Bileşik Nesneler"
baslik: "21.3 Özel üye işlevler ve composition"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 21.3 Özel üye işlevler ve composition

Composition'ın en büyük pratik kazancı burada ortaya çıkar.

Veri elemanlarınızın hepsi kendi kaynaklarını doğru yönetiyorsa, **sizin hiçbir özel üye
işlev yazmanıza gerek kalmaz.** Derleyicinin yazdığı altı işlev, her veri elemanı için
o elemanın kendi işlevini çağırır ve doğru sonuç verir.

<!-- kod-baglam
struct Ek { };
-->
```cpp
class Kayit {
    std::string ad;
    std::vector<int> notlar;
    std::unique_ptr<Ek> ek;
};
```

Bu sınıf için kopyalama, taşıma ve yıkım doğru çalışır; tek satır yazmadınız. Kısım
13.9'daki Rule of Zero tam olarak budur ve composition onun uygulama aracıdır.
