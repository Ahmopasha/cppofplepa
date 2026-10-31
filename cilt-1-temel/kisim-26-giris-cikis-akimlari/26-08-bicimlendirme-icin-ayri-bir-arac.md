---
cilt: "I — Temel"
kisim: "26 — Giriş–Çıkış Akımları"
baslik: "26.8 Biçimlendirme için ayrı bir araç"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 26.8 Biçimlendirme için ayrı bir araç

Akım mekanizması güçlüdür ama ayrıntılıdır ve manipülatörlerin kalıcı olması hata
kaynağıdır. C++20, **çıktı biçimlendirmesi** için ayrı bir kütüphane getirdi:

```cpp
std::format("{:.2f}", 3.14159);
```

Bu kütüphane akımların yerini almaz; yalnızca biçimlendirme işini devralır. Girdi
ayrıştırma ve dosya/bellek üzerinde akım soyutlaması bu bölümde anlatıldığı gibi
kalır.

Ayrıntısı: **Cilt II, Kısım 10.**
