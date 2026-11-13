---
cilt: "I — Temel"
kisim: "15 — Dinamik Ömürlü Nesneler"
baslik: "15.5 Bunları neden yazmamalısınız"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 15.5 Bunları neden yazmamalısınız

Bu bölümdeki her şeyi bilmeniz gerekir, çünkü mevcut kodu okuyacaksınız. Ama **yeni kod
yazarken çıplak `new` ve `delete` kullanmamalısınız.**

Sebebini Kısım 18.5'te ayrıntısıyla göreceğiz: gönderilen bir hata yakalandığında, terk
edilen bloklardaki otomatik ömürlü nesnelerin sonlandırıcı işlevleri çalışır, ama çıplak
`new` ile ayrılan bellek geri verilmez. Buna programın her `return` ve `break` yolunu
düşünmek zorunda kalmayı ekleyin.

Doğru araçlar akıllı göstericiler (Kısım 25) ve `std::vector` gibi kaplardır (Kısım 23.4):

```cpp
auto p = std::make_unique<Myclass>(10);     // delete yazmanıza gerek yok
auto v = std::vector<int>(100);             // new[] yerine
```

> **Çıplak `new` yazdığınız her yerde, ona karşılık gelen `delete`'in her yoldan
> çalışacağını kanıtlamanız gerekir. Akıllı gösterici kullandığınızda bu yükümlülük
> ortadan kalkar.**

`operator new` ve `operator delete` işlevlerinin yüklenmesi, `placement new` ve
`std::set_new_handler`: **Cilt II, Kısım 17.**
