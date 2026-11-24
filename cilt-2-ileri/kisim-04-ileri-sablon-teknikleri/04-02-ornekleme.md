---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.2 Örnekleme"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++23)"
---

## 4.2 Örnekleme

Şablon bir kod değil, kod üreten bir kalıptır. Derleyicinin bir şablondan gerçek kod
üretmesine **örnekleme** *(instantiation)* denir; üretilen ürüne **özelleştirme**
*(specialization)* denir.

Terim karışıklığına dikkat: "specialization" hem örnekleme ürününü hem de 4.3–4.4'teki
özelleştirme mekanizmasını adlandırır. Bağlamdan ayırt edilir.

Örnekleme iki şekilde tetiklenir. **Örtülü örnekleme** *(implicit instantiation)*,
şablonun kullanıldığı yerde kendiliğinden olur. **Açık örnekleme** ise elle istenir:

<!-- kod-baglam
template<typename T>
class Kutu {
    T icerik;
};
-->
```cpp
template class Kutu<int>;      // açık örnekleme tanımı
```

Açık örnekleme, özelleştirmeyi tek bir çeviri biriminde örnekler. İşlev şablonlarının ve
sınıf şablonu üye işlevlerinin tanımları (dönüş türü çıkarılanlar ile `inline` ya da
`constexpr` olanlar dışında) bu sayede başlık dosyasından çıkarılıp o çeviri birimine,
açık örnekleme satırından önce konabilir; öteki çeviri birimleri yalnızca bildirimi görür
ve açıkça örneklenmiş özelleştirmeleri kullanır. Sınıf şablonunun tanımı ise başlıkta
kalır. Bedeli esnekliktir: hiçbir yerde açıkça örneklenmemiş bir özelleştirme, işlevin
tanımını görmeyen bir çeviri biriminde örnekleme gerektirecek biçimde kullanılırsa
derleyicinin bildirmek zorunda olmadığı bir hata olur.
