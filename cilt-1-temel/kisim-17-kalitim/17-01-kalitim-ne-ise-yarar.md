---
cilt: "I — Temel"
kisim: "17 — Kalıtım"
baslik: "17.1 Kalıtım ne işe yarar"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 17.1 Kalıtım ne işe yarar

Kalıtım, bir sınıfın başka bir sınıfın arayüzünü devralarak yeni bir sınıf
oluşturmasıdır. Kurulan ilişkiye **is-a** ilişkisi denir: her türemiş sınıf nesnesi,
aynı zamanda bir taban sınıf nesnesidir.

Bunun karşısında **has-a** ilişkisi vardır ve buna *composition* denir. Bir sınıf,
başka bir sınıf türünden veri elemanı barındırıyorsa ilişki has-a'dır.

```cpp
class Motor { /* ... */ };

class Araba {
    Motor m;                    // has-a: arabanın bir motoru vardır
};

class Kamyon : public Arac {    // is-a: kamyon bir araçtır
};
```

Bu ayrım kalıtımı doğru kullanmanın temelidir. Kod paylaşmak için kalıtım kurmayın;
sorulacak soru "B, bir A mıdır?" sorusudur. Cevap hayırsa composition kullanın.

Taban sınıf **tamamlanmış tür** olmak zorundadır. Yalnızca bildirimi görülmüş bir
sınıftan kalıtım yapılamaz.
