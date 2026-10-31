---
cilt: "I — Temel"
kisim: "17 — Kalıtım"
baslik: "17.4 upcasting"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 17.4 upcasting

Türemiş sınıf türünden bir nesne, taban sınıf türüne örtülü olarak dönüşür. Buna
*upcasting* denir ve `public` kalıtımda güvenlidir; her türemiş nesne zaten bir taban
sınıf nesnesidir.

```cpp
Der d;

Base* bp = &d;    // OK
Base& br = d;     // OK
Base  b  = d;     // derlenir, ama dikkat — bkz. 17.9
```

Çok biçimliliğin tamamı bu dönüşümün üzerine kuruludur: taban sınıf göstericisi veya
referansı tutarsınız, ardındaki gerçek nesnenin ne olduğunu bilmeden çalışırsınız.
