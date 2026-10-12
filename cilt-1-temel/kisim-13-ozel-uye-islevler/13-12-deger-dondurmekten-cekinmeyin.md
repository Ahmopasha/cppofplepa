---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.12 Değer döndürmekten çekinmeyin"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 13.12 Değer döndürmekten çekinmeyin

Sınıf türünden değer döndüren bir işlev yazdığınızda, "burada bir kopyalama oluyor,
optimize etmeliyim" diye düşünmeyin. Derleyici bu kopyalamayı çoğu durumda **tamamen
ortadan kaldırır**; bir kısmında bunu yapmak zorundadır bile.

Doğrusu budur:

```cpp
Myclass foo()
{
    Myclass mx{31};
    return mx;          // olduğu gibi bırakın
}
```

Üç yaygın "iyileştirme" girişimi vardır ve üçü de zarar verir.

**`return std::move(mx);` yazmayın.** `std::move` eklediğiniz anda derleyici kopyalamayı
eleme imkânını kaybeder ve taşıyan kurucu işlevi çağırmak zorunda kalır. Taşımak
kopyalamaktan ucuzdur, ama **hiçbir şey yapmamak** ikisinden de ucuzdur. `return mx;`
yazdığınızda zaten gerekirse taşınır.

**Geri dönüş türünü `const` yapmayın.**

```cpp
const Myclass foo();     // yapmayın
```

`const` bir dönüş değeri taşınamaz; kopyalanmak zorunda kalır. Değeri korumaya
çalışırken performansı kaybedersiniz.

**Referans döndürme kurnazlığına başvurmayın.** Yerel bir nesneye referans döndürmek
tanımsız davranıştır; nesne işlev bitince yok olur. Kopyalamadan kaçınmak için bu yola
girmeyin, zaten kaçınmanız gereken bir kopyalama yok.

Bu üç kuralın nedeni Cilt II, Kısım 3'te.
