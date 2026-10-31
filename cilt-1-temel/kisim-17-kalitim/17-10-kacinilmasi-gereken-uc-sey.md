---
cilt: "I — Temel"
kisim: "17 — Kalıtım"
baslik: "17.10 Kaçınılması gereken üç şey"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 17.10 Kaçınılması gereken üç şey

**Kod paylaşmak için kalıtım kurmayın.** Taban sınıfın arayüzünde türemiş sınıf için
anlamsız olan bir öğe varsa o sınıftan kalıtım yapılmamalıdır. Bu duruma *improper
inheritance* denir; doğru araç composition'dır.

**Kurucu ve sonlandırıcı işlevlerin içinden sanal işlev çağırmayın.** Taban sınıfın
kurucu işlevi çalışırken nesne henüz türemiş tür değildir; sanal çağrı türemiş sınıfa
gitmez, taban sınıfta kalır. Sonlandırıcı işlevde durum simetriktir. Sebebi Cilt II,
Kısım 6.2'de anlatılıyor; şimdilik kural olarak alın.

**Geçersiz kılan işlevde farklı varsayılan argüman vermeyin.** Varsayılan argümanlar
çalışma zamanında değil, derleme zamanında ve göstericinin **statik türüne** göre
seçilir. Aşağıdaki kod, çağrılan gövde ile kullanılan argümanın uyuşmadığı, bulunması
zor bir hata üretir:

```cpp
class Base {
public:
    virtual void f(int x = 10);
};

class Der : public Base {
public:
    void f(int x = 20) override;    // yapmayın
};

Base* p = new Der;
p->f();     // Der::f çağrılır ama argüman 10 olur
```
