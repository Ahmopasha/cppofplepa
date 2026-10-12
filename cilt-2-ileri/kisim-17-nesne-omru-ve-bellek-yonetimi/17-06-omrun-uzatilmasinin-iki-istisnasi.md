---
cilt: "II — İleri"
kisim: "17 — Nesne Ömrü ve Bellek Yönetimi"
baslik: "17.6 Ömrün uzatılmasının iki istisnası"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 17.6 Ömrün uzatılmasının iki istisnası

Cilt I Kısım 8.3'te, `const` bir referansa bağlanan geçici nesnenin ömrünün referans
kadar uzadığı söylenmiş, iki istisnası kural olarak verilmişti. Gerekçeleri şunlardır.

**İşlevden döndürülen referans için geçerli değildir.**

```cpp
const std::string& bozuk()
{
    return std::string{"gecici"};      // ömür uzamaz
}
```

Uzatma, referansın **bağlandığı kapsamla** sınırlıdır. Referans işlevden döndüğünde o
kapsam kapanır ve geçici nesne yok edilir; çağırana sarkan bir referans döner.

**Sınıfın veri elemanı olan referans için geçerli değildir.**

```cpp
class Sarmal {
    const std::string& r;
public:
    Sarmal(const std::string& s) : r{s} { }
};

Sarmal x{std::string{"gecici"}};      // geçici nesne kurucu işlev bitince yok olur
x;                                    // x.r sarkıyor
```

Kurucu işlev ilk değer verme listesinde bağlanan geçici nesnenin ömrü, **kurucu işlevin
sonuna kadar** uzar; nesnenin ömrü kadar değil. Kurucu işlev bittiğinde geçici nesne yok
olur ve veri elemanı sarkar.

İkisinin ortak nedeni şudur: ömür uzatma, derleyicinin **yerel olarak** görebildiği bir
bağlamda çalışır. İşlev sınırını veya nesne sınırını aştığında, geçici nesnenin ne kadar
yaşaması gerektiğini belirleyemez.

> **Referans türünden veri elemanı tutmaktan kaçının.** Kaçınamıyorsanız, bağlanan
> nesnenin sınıf nesnesinden uzun yaşadığını belgeleyin. Aynı uyarı `string_view` ve
> `span` için de geçerlidir (bkz. Kısım 11.2).
