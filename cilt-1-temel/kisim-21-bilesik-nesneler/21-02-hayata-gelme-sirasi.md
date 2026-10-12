---
cilt: "I — Temel"
kisim: "21 — Bileşik Nesneler"
baslik: "21.2 Hayata gelme sırası"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 21.2 Hayata gelme sırası

Bir bileşik nesne hayata gelirken sıra şudur:

1. Varsa taban sınıfın kurucu işlevi
2. Veri elemanları, **sınıf tanımındaki bildirim sırasına göre**
3. Sınıfın kendi kurucu işlevinin gövdesi

Hayat biterken sıra tam tersidir. Bu, Kısım 17.3'te kalıtım için verilen sıranın aynısıdır;
ikisi tek bir kuraldır.

Veri elemanlarına ilk değer, kurucu işlev ilk değer verme listesinde verilir:

```cpp
class Araba {
    Motor m;
    std::string plaka;
public:
    Araba(int guc, const std::string& p) : m{guc}, plaka{p} { }
};
```

Listedeki yazım sırasının hiçbir etkisi yoktur; sıralama bildirim sırasına göredir
(bkz. Kısım 12.10).
