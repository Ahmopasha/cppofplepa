---
cilt: "I — Temel"
kisim: "25 — Akıllı Göstericiler"
baslik: "25.1 Çözdükleri problem"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 25.1 Çözdükleri problem

Kısım 15.5'te çıplak `new` ve `delete` kullanmamanız gerektiğini söylemiştik. Kısım
18.6'da bunun gerekçesini görmüştük: yığın geri sarılırken yalnızca sonlandırıcı işlevi
olan nesneler temizlenir, çıplak bellek sızar.

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

`operator->` ve `operator*` yüklendiği için nesne, gösterici gibi kullanılır. Standart
kütüphanenin akıllı göstericileri bu fikrin tam hâlidir.
