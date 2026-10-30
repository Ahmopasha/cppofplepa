---
cilt: "II — İleri"
kisim: "2 — Taşıma Semantiği ve Bildirim Kuralları"
baslik: "2.8 Copy-and-Swap deyimi"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
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
    ~Yazi();                                 // kaynağı geri verir
    Yazi(const Yazi& other);                 // derin kopya
    Yazi(Yazi&& other) noexcept;             // göstericiyi devralır
    void swap(Yazi& other) noexcept { std::swap(p, other.p); }

    Yazi& operator=(Yazi other) noexcept    // değerle alınıyor
    {
        swap(other);
        return *this;
    }
};
```

Kazançları: kendine atama denetimi gerekmez, çünkü işlem ayrı bir parametre nesnesi
üzerinden yürür. Güçlü garanti sağlanır, çünkü kopyalama sırasında hata olursa `*this`'e
henüz dokunulmamıştır. Ve tek bir işlev hem kopyalayan hem taşıyan atama görevini görür;
argüman L-Value ise parametre kopyalayan, const olmayan bir X-Value ise (ör.
`std::move(t)`) taşıyan kurucuyla kurulur; PR-Value'da parametre doğrudan kurulur (Kısım
3.3). X-Value'nun taşınabilmesi için taşıyan kurucu ayrıca yazılmalıdır: `operator=(Yazi)`
standarda göre bir kopyalayan atama işlevidir ve kullanıcı bildirdiği için taşıyan kurucu
örtülü olarak bildirilmez (Kısım 2.2).

Bedeli, taşıyan atamanın elle yazılmış hâline göre bir miktar daha pahalı olmasıdır.
Sıcak yollarda ikisini ayrı yazmak tercih edilebilir.
