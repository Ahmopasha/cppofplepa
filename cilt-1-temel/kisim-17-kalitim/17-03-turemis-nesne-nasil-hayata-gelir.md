---
cilt: "I — Temel"
kisim: "17 — Kalıtım"
baslik: "17.3 Türemiş nesne nasıl hayata gelir"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 17.3 Türemiş nesne nasıl hayata gelir

Bir türemiş sınıf nesnesi hayata gelirken sıra şudur:

1. Taban sınıfın kurucu işlevi
2. Veri elemanları, **bildirim sırasına göre**
3. Türemiş sınıfın kurucu işlevinin gövdesi

Nesnenin hayatı biterken sıra tam tersidir: önce türemiş sınıfın sonlandırıcı işlevi,
sonra veri elemanları, en son taban sınıfın sonlandırıcı işlevi.

Taban sınıfın kurucu işlevine argüman geçmek isterseniz, bunu türemiş sınıfın kurucu
işlev ilk değer verme listesinde yaparsınız:

```cpp
class Base {
public:
    Base(int x);
};

class Der : public Base {
public:
    Der(int x) : Base(x) { }    // taban sınıf ilk değer verme listesinde
};
```

Taban sınıfın varsayılan kurucu işlevi yoksa ve siz de listede çağrı yapmazsanız
sentaks hatası alırsınız.
