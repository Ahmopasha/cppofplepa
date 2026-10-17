---
cilt: "II — İleri"
kisim: "4 — İleri Şablon Teknikleri"
baslik: "4.2 Örnekleme"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 4.2 Örnekleme

Şablon bir kod değil, kod üreten bir kalıptır. Derleyicinin bir şablondan gerçek kod
üretmesine **örnekleme** *(instantiation)* denir; üretilen ürüne **specialization** denir.

Terim karışıklığına dikkat: "specialization" hem örnekleme ürününü hem de 4.3–4.4'teki
özelleştirme mekanizmasını adlandırır. Bağlamdan ayırt edilir.

Örnekleme iki şekilde tetiklenir. **Örtülü örnekleme**, şablonun kullanıldığı yerde
kendiliğinden olur. **Açık örnekleme** ise elle istenir:

<!-- kod-baglam
template<typename T>
class Kutu {
    T icerik;
};
-->
```cpp
template class Kutu<int>;      // açık örnekleme tanımı
```

Açık örnekleme, şablon tanımını başlık dosyasından çıkarıp tek bir çeviri biriminde
derlemeye yarar; derleme süresini kısaltır ama esnekliği azaltır.
