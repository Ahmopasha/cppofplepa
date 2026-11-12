---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.9 Sonlandırıcı işlev"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 12.9 Sonlandırıcı işlev

Nesnenin hayatını bitiren üye işlevdir. İsmi `~` ile başlar, parametre almaz, geri dönüş
türü yoktur, `static` olamaz ve bir sınıfta yalnızca bir tane bulunabilir.

```cpp
class Myclass {
public:
    ~Myclass();
};
```

Kurucu işlevden farklı olarak `.` ya da `->` operatörüyle **çağrılabilir**, ama bu kötü
bir alışkanlıktır: açık çağrı nesnenin ömrünü bitirir; nesne kapsamdan çıkarken
sonlandırıcı işlev yeniden çağrılır ve ömrü bitmiş nesne için yapılan bu çağrı tanımsız
davranıştır. Açık çağrının başlıca meşru kullanımı, `placement new` ile yerinde
oluşturulan nesnelerdir (Cilt II, Kısım 17.3).

Sonlandırıcı işlev yazmanız gereken başlıca durum, sınıfın bir kaynak yönetmesidir; o
durumda Big-Five kuralı (Kısım 13.8) devreye girer. Türemiş sınıf nesneleri taban sınıf
göstericisiyle siliniyorsa taban sınıfın sonlandırıcı işlevi `virtual` olmalıdır (Kısım
17.7).
