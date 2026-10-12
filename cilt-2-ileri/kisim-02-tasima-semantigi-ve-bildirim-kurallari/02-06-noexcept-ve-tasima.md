---
cilt: "II — İleri"
kisim: "2 — Taşıma Semantiği ve Bildirim Kuralları"
baslik: "2.6 `noexcept` ve taşıma"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 2.6 `noexcept` ve taşıma

`std::vector` kapasitesini artırırken yeni bir alan ayırır ve mevcut öğeleri oraya
aktarır. Aktarım sırasında bir hata oluşursa vektörün eski hâlini bozmamış olması
gerekir; bu **güçlü garanti** demektir.

Kopyalama bu garantiyi sağlar: kaynak nesneler yerinde durur, kopya başarısız olursa
eskisi hâlâ sağlamdır. Taşıma sağlamaz: kaynak nesneler artık boşaltılmıştır, geri
dönüş yoktur.

Bu yüzden `vector`, taşıyan kurucu işlevi **yalnızca `noexcept` ise** kullanır. Değilse
kopyalar.

```cpp
class Yazi {
public:
    Yazi(Yazi&&) noexcept;     // noexcept olmazsa vector bunu kullanmaz
};
```

**Taşıyan işlevlerinizi `noexcept` yazın.** Yazmazsanız taşıma semantiğini
tanımlamış ama kullandırmamış olursunuz; kazanç tamamen kaybolur ve hiçbir uyarı almazsınız.

Taşıyan işlev zaten kaynak ayırmaz, yalnızca gösterici aktarır; dolayısıyla `noexcept`
olmaması için bir sebep de yoktur.
