---
cilt: "I — Temel"
kisim: "19 — Çalışma Zamanı Tür Bilgisi"
baslik: "19.3 `typeid` ve `std::type_info`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 19.3 `typeid` ve `std::type_info`

`typeid` operatörü, bir ifadenin veya türün tür bilgisini `std::type_info` nesnesi olarak
verir.

```cpp
#include <typeinfo>

Sekil* s = new Daire;

if (typeid(*s) == typeid(Daire)) {
    // dinamik tür tam olarak Daire
}

std::cout << typeid(*s).name();
```

İki nokta önemlidir.

**`typeid(*s)` ile `typeid(s)` farklıdır.** İlki nesnenin dinamik türünü, ikincisi
göstericinin statik türünü (`Sekil*`) verir.

**`name()` işlevinin döndürdüğü yazı gerçeklemeye bağlıdır.** Derleyiciler farklı biçimler
üretir; bu yazıyı programın mantığında kullanmayın, yalnızca hata ayıklama çıktısında
kullanın.

`typeid` ile `dynamic_cast` arasındaki fark, `typeid`'in **tam eşleşme** aramasıdır.
`Daire`'den türetilmiş bir `RenkliDaire` nesnesi için `typeid(*s) == typeid(Daire)`
yanlış olur, ama `dynamic_cast<Daire*>(s)` başarılı olur.
