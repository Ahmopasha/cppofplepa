---
cilt: "I — Temel"
kisim: "17 — Kalıtım"
baslik: "17.4 upcasting"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 17.4 upcasting

Türemiş sınıf göstericisi taban sınıf göstericisine, türemiş sınıf nesnesi de taban sınıf
referansına örtülü olarak dönüşür (değerle kopyalama için bkz. Kısım 17.9). Buna
*upcasting* denir. `public` kalıtımda her türemiş nesne zaten bir taban sınıf nesnesi
olduğu için dönüşüm her yerde yapılabilir. `private` ya da `protected` kalıtımda taban
sınıfa her yerden erişilemez; erişilemeyen yerde (ör. sınıfı yalnızca kullanan kodda) bu
örtülü dönüşüm sentaks hatasıdır. Nerelerde geçerli olduğu Cilt II, Kısım 6.7'dedir.

```cpp
Der d;

Base* bp = &d;    // OK
Base& br = d;     // OK
Base  b  = d;     // derlenir, ama dikkat — bkz. 17.9
```

Çok biçimliliğin (Kısım 17.6) tamamı bu dönüşümün üzerine kuruludur: taban sınıf
göstericisi veya referansı tutarsınız, ardındaki gerçek nesnenin ne olduğunu bilmeden
çalışırsınız.
