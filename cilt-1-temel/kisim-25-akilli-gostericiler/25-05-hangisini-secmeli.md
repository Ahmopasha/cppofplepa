---
cilt: "I — Temel"
kisim: "25 — Akıllı Göstericiler"
baslik: "25.5 Hangisini seçmeli"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 25.5 Hangisini seçmeli

> **Varsayılan tercihiniz `unique_ptr` olsun.** Varsayılan silicide maliyeti çıplak
> göstericiyle aynıdır ve sahipliği açıkça yazar. Gerçekten paylaşılan sahiplik
> gerekiyorsa `shared_ptr`'a geçin; döngü riski varsa bir tarafı `weak_ptr` yapın.

Üç kural daha:

**Aynı çıplak adresi iki akıllı göstericiye vermeyin.** İkisi de sahiplendiğini sanır ve
nesne iki kez yok edilir.

```cpp
Myclass* raw = new Myclass;
std::shared_ptr<Myclass> a{raw};
std::shared_ptr<Myclass> b{raw};    // çifte yıkım
```

**Dinamik ömürlü olmayan bir nesnenin adresini akıllı göstericiye vermeyin.** Yığında
duran bir nesneyi `delete` etmek tanımsız davranıştır.

**Akıllı göstericileri kaplarda tutabilirsiniz.** `std::vector<std::unique_ptr<Sekil>>`,
çok biçimli nesneleri bir arada tutmanın standart yoludur (bkz. Kısım 17.9 — dilimlenme
olmaması için gösterici gerekir).

Özel silici tanımlama, kontrol bloğunun ayrıntıları ve `enable_shared_from_this`:
**Cilt II, Kısım 17.9.**
