---
cilt: "II — İleri"
kisim: "2 — Taşıma Semantiği ve Bildirim Kuralları"
baslik: "2.8 Copy-and-Swap deyimi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 2.8 Copy-and-Swap deyimi

Kopyalayan atama işlevinin iki zor tarafı vardır: kendine atama denetimi, ve işlem
ortasında hata oluşursa nesnenin tutarsız kalması.

Deyim ikisini birden çözer. Atama işlevi parametresini **değerle** alır, böylece kopya
zaten oluşmuştur; sonra `swap` ile içerikler değiştirilir.

```cpp
class Yazi {
    char* p;
public:
    void swap(Yazi& other) noexcept { std::swap(p, other.p); }

    Yazi& operator=(Yazi other) noexcept    // değerle alınıyor
    {
        swap(other);
        return *this;
    }
};
```

Kazançları: kendine atama denetimi gerekmez, çünkü zaten kopya üzerinde çalışılıyor.
Güçlü garanti sağlanır, çünkü kopyalama sırasında hata olursa `*this`'e henüz
dokunulmamıştır. Ve tek bir işlev hem kopyalayan hem taşıyan atama görevini görür;
argüman L-Value ise kopyalanarak, R-Value ise taşınarak gelir.

Bedeli, taşıyan atamanın elle yazılmış hâline göre bir miktar daha pahalı olmasıdır.
Sıcak yollarda ikisini ayrı yazmak tercih edilebilir.
