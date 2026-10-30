---
cilt: "II — İleri"
kisim: "2 — Taşıma Semantiği ve Bildirim Kuralları"
baslik: "2.6 `noexcept` ve taşıma"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 2.6 `noexcept` ve taşıma

`std::vector` kapasitesini artırırken yeni bir alan ayırır ve mevcut öğeleri oraya
aktarır. Aktarım sırasında bir hata oluşursa vektörün eski hâlini bozmamış olması
gerekir; bu **güçlü garanti** demektir (Kısım 13.1).

Kopyalama bu garantiyi sağlar: kaynak nesneler yerinde durur, kopya başarısız olursa
eskisi hâlâ sağlamdır. Taşıma sağlamaz: kaynak nesneler artık boşaltılmıştır, geri
dönüş yoktur.

Bu yüzden `reserve` ve tek öğeyi sona ekleme (`push_back`, `emplace_back`) gibi güçlü
garanti veren işlemlerde yer değiştirirken `vector`, tür kopyalanabiliyorsa taşıyan
kurucuyu **yalnızca `noexcept` ise** kullanır; değilse kopyalar. Tür kopyalanamıyorsa hata
gönderebilen taşıyan kurucuyu da kullanır, ama o durumda güçlü garanti yoktur (Kısım
13.1).

```cpp
class Yazi {
public:
    Yazi(const Yazi&);
    /* noexcept olmazsa reserve ve push_back, yer değiştirirken
     * var olan öğeleri kopyalar. */
    Yazi(Yazi&&) noexcept;
};
```

**Taşıyan işlevlerinizi `noexcept` yazın.** Taşıyan kurucu `noexcept` değilse,
kopyalanabilen türlerde, güçlü garanti isteyen yerlerde (`vector`'ün `reserve`'ü ve tek
öğeyi sona eklemesi gibi) yer değiştirirken var olan öğeler için taşıma kullanılmaz ve
kazanç kaybolur; kod yine de geçerlidir ve standart, gerçeklemenin bunu bildirmesini
istemez. `return`, atama ve `std::swap` ise taşıma yaptıklarında taşıyan işlevi
`noexcept`'ten bağımsız olarak kullanır. Örtülü bildirilen ya da ilk bildiriminde
`= default` yapılan taşıyan işlevlerde `noexcept` yazılmamışsa kendiliğinden belirlenir:
işlevin çağırdığı üye ve taban işlemleri `noexcept` ise işlev de `noexcept`'tir.

Taşıyan işlev çoğu zaman kaynak ayırmaz, yalnızca gösterici aktarır; böyle bir işlevin
`noexcept` olmaması için bir sebep yoktur. Bu her tür için geçerli değildir: standart
kütüphanede bile `std::deque`'in taşıyan kurucusunun `noexcept` olması garanti edilmez.
