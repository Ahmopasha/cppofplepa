---
cilt: "I — Temel"
kisim: "25 — Akıllı Göstericiler"
baslik: "25.5 Hangisini seçmeli"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 25.5 Hangisini seçmeli

> **Varsayılan tercihiniz `std::unique_ptr` olsun.** Sayaç tutmaz, yalnızca göstericiyi
> ve **silici** *(deleter)* denen, nesneyi yok etmek için kullanılan işlemi (varsayılanı
> `delete`; Cilt II, Kısım 17.9) saklar; sahipliği de açıkça yazar. Gerçekten paylaşılan
> sahiplik gerekiyorsa `std::shared_ptr`'a geçin; döngüsel başvuru riski varsa bir
> tarafı `std::weak_ptr` yapın.

Üç kural daha:

**Aynı çıplak adresi iki akıllı göstericiye vermeyin.** İkisi de sahiplendiğini sanır ve
nesne iki kez yok edilir.

```cpp
Myclass* raw = new Myclass;
std::shared_ptr<Myclass> a{raw};
std::shared_ptr<Myclass> b{raw};    // ikisi de siler: ikinci silme tanımsız davranış
```

**`new` ile oluşturulmamış bir nesnenin adresini akıllı göstericiye vermeyin.** Akıllı
gösterici nesneyi varsayılan olarak `delete` ile siler; örneğin otomatik ömürlü (Kısım
15.1) bir nesneyi `delete` etmek tanımsız davranıştır.

**Akıllı göstericileri kaplarda tutabilirsiniz.** `std::vector<std::unique_ptr<Sekil>>`,
çok biçimli nesneleri bir arada tutmanın standart yoludur (bkz. Kısım 17.9 — dilimlenme
olmaması için gösterici gerekir).

Özel silici tanımlama, kontrol bloğunun ayrıntıları ve `std::enable_shared_from_this`:
**Cilt II, Kısım 17.9.**
