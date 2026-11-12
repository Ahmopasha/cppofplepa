---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.12 Değer döndürmekten çekinmeyin"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 13.12 Değer döndürmekten çekinmeyin

Sınıf türünden değer döndüren bir işlev yazdığınızda, "burada bir kopyalama oluyor,
optimize etmeliyim" diye düşünmeyin. Döndürülen ifade aynı türden bir PR-Value ise
standart, C++17'den beri kopyalayan ya da taşıyan kurucu işlevin çağrılmamasını zorunlu
kılar; dönüş değerinden yeni bir nesneye ilk değer verildiğinde de (`Myclass y = foo();`)
kopya ya da taşıma olmaz. İşlev gövdesinde tanımlanmış, dönüş türüyle aynı türden yerel
(`static` olmayan) bir nesne döndürüldüğünde ise kopyalamanın elenmesine izin verir ama
bunu zorunlu kılmaz; elenmezse önce taşıma denenir; taşıyan işlev yoksa nesne kopyalanır
(Kısım 13.7). Değerle alınmış bir parametre döndürüldüğünde eleme olmaz, ama yine önce
taşıma denenir.

Doğrusu budur:

```cpp
Myclass foo()
{
    Myclass mx{31};
    return mx;          // olduğu gibi bırakın
}
```

Üç yaygın "iyileştirme" girişimi vardır ve üçü de zarar verir.

**`return std::move(mx);` yazmayın.** `std::move` eklediğiniz anda kopyalamanın elenmesi
mümkün olmaz ve taşıyan kurucu işlev çağrılır. Taşımak çoğu zaman kopyalamaktan ucuzdur,
ama **hiçbir şey yapmamak** ikisinden de ucuzdur. `return mx;` yazdığınızda nesne zaten
gerekirse taşınır.

**Geri dönüş türünü `const` yapmayın.**

```cpp
const Myclass foo();     // yapmayın
```

`const` bir dönüş değerinden taşıma yapılamaz: `x = foo();` gibi bir atamada taşıyan atama
işlevi yerine kopyalayan atama işlevi çağrılır. Değeri korumaya çalışırken performansı
kaybedersiniz.

**Referans döndürme kurnazlığına başvurmayın.** Yerel (`static` olmayan) bir nesneye
referans döndürürseniz nesne işlev bitince yok olur; döndürülen referansı kullanmak
tanımsız davranıştır. Kopyalamadan kaçınmak için bu yola girmeyin, zaten kaçınmanız
gereken bir kopyalama yok.

İlk iki kuralın nedeni Cilt II, Kısım 3.5'te.
