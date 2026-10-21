---
cilt: "II — İleri"
kisim: "17 — Nesne Ömrü ve Bellek Yönetimi"
baslik: "17.6 Ömrün uzatılmasının iki istisnası"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
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

**Kurucu işlevle ilk değer alan referans veri elemanı için geçerli değildir.** Küme
parantezli bileşik tür ilk değer vermesinde ise, `new` ifadesi dışında, ömür uzar (bkz.
Kısım 16.6).

```cpp
class Sarmal {
    const std::string& r;
public:
    Sarmal(const std::string& s) : r{s} { }
};

Sarmal x{std::string{"gecici"}};      // geçici nesne bu bildirimin sonunda yok olur
```

Geçici nesne, kurucu işlevin `s` parametresine bağlanır. Bir işlev çağrısında referans
parametreye bağlanan geçici nesne, çağrıyı içeren tam ifadenin sonuna kadar yaşar; burada
bu, `x`'in bildiriminin sonudur. `r{s}` ile `r` de aynı geçici nesneye bağlanır, ama
geçici nesneyi oluşturan ifadeyle değil, `s` referansı üzerinden. **Var olan bir referans
üzerinden yapılan bağlama ömrü uzatmaz.** Bildirim bittiğinde geçici nesne yok olur ve
`x.r` sarkar; sarkan `r`'yi (ör. bir üye işlevde) kullanmak tanımsız davranıştır.

Geçici nesneyi doğrudan ilk değer verme listesinde bağlamak ise sentaks hatasıdır:

```cpp
class Bozuk {
    const std::string& r;
public:
    Bozuk() : r{std::string{"gecici"}} { }    // sentaks hatası
};
```

C++14 dahil önceki standart metinleri bu bağlamaya izin veriyor ve geçici nesneyi kurucu
işlevin sonuna kadar yaşatıyordu. CWG 1696 sorununun C++17 metnine giren çözümüyle bağlama
sentaks hatası oldu; çözüm bir **kusur raporu** *(defect report)* olduğundan eski dil
kiplerine de uygulanır.

İkisinin ortak nedeni şudur: ömür uzatma, derleyicinin **yerel olarak** görebildiği bir
bağlamda çalışır. İşlev sınırını veya nesne sınırını aştığında, geçici nesnenin ne kadar
yaşaması gerektiğini belirleyemez.

> **Referans türünden veri elemanı tutmaktan kaçının.** Kaçınamıyorsanız, bağlanan
> nesnenin sınıf nesnesinden uzun yaşadığını belgeleyin. Aynı uyarı `string_view` ve
> `span` için de geçerlidir (bkz. Kısım 11.2).
