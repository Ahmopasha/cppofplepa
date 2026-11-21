---
cilt: "I — Temel"
kisim: "25 — Akıllı Göstericiler"
baslik: "25.1 Çözdükleri problem"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 25.1 Çözdükleri problem

Kısım 15.5'te çıplak `new` ve `delete` kullanmamanız gerektiğini söylemiştik. Kısım
18.5'te bunun gerekçesini görmüştük: yığın geri sarılırken yalnızca otomatik ömürlü
nesneler yok edilir; çıplak `new` ile ayrılan bellek geri verilmez ve sızar.

Akıllı gösterici, bir göstericiyi sonlandırıcı işlevi olan bir nesnenin içine koyar. Bu
sayede RAII, dinamik belleğe de uygulanmış olur.

```cpp
class BasitAkilli {
    Myclass* p;
public:
    explicit BasitAkilli(Myclass* ptr) : p{ptr} { }
    ~BasitAkilli() { delete p; }           // temizlik burada
    Myclass* operator->() { return p; }
    Myclass& operator*()  { return *p; }
};
```

`operator->` ve `operator*` yüklendiği için nesne, gösterici gibi kullanılır. Bu sınıf
yalnızca fikri gösterir: derleyicinin yazdığı kopyalama işlevleri (Kısım 13.5) göstericiyi
kopyalar, bu yüzden bir `BasitAkilli` kopyalanırsa iki nesne aynı göstericiyi siler ve
ikinci silme tanımsız davranıştır. Standart kütüphanenin akıllı göstericileri bu fikrin
tam hâlidir ve bu sorunu da çözer.
