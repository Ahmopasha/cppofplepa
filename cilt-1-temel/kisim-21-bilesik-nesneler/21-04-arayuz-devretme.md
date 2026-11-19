---
cilt: "I — Temel"
kisim: "21 — Composition"
baslik: "21.4 Arayüz devretme"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 21.4 Arayüz devretme

Composition'da, içerdiğiniz nesnenin arayüzü dışarıya **otomatik olarak açılmaz.**
Açılmasını istediğiniz kısmı kendiniz yazarsınız.

```cpp
class Sozluk {
    std::map<std::string, std::string> veri;
public:
    void ekle(const std::string& k, const std::string& d) { veri[k] = d; }
    std::size_t boyut() const { return veri.size(); }
    // veri'nin öteki üye işlevleri dışarıya açılmadı
};
```

Bu bir kısıtlama değil, **üstünlüktür.** `public` kalıtımda taban sınıfın `public` üyeleri
türemiş sınıfın da `public` üyeleri olur; istemediğiniz işlevler de dışarıya açılır.
Composition'da ne açacağınıza siz karar verirsiniz.

`private` kalıtımın composition ile karşılaştırması ve hangi üç durumda tercih edilmesi
gerektiği: **Cilt II, Kısım 6.7.**
