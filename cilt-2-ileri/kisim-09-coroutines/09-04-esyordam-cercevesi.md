---
cilt: "II — İleri"
kisim: "9 — Coroutines"
baslik: "9.4 Eşyordam çerçevesi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 9.4 Eşyordam çerçevesi

Sıradan işlevin çerçevesi yığındadır ve işlev bitince yok olur. Eşyordam askıya
alındığında durumunun korunması gerektiği için, çerçevesi **yığında tutulamaz.**

Derleyici, eşyordamın yerel değişkenlerini ve çalışma noktasını tutan bir çerçeveyi
dinamik bellekte ayırır. Ayırma için `operator new` kullanılır (bkz. Kısım 17.1);
`promise_type` içinde kendi `operator new`'ünüzü tanımlayarak bunu değiştirebilirsiniz.

Derleyicinin bu ayırmayı **eleme hakkı** vardır; eşyordamın ömrü çağıranın ömrünü
aşmıyorsa çerçeve yığına alınabilir. Buna *HALO* denir ve garanti değildir.

`std::coroutine_handle`, çerçeveye erişim sağlayan tutamaktır. `resume()` ile devam
ettirilir, `done()` ile bitip bitmediği sorulur, `destroy()` ile çerçeve yok edilir.

**Tutamak bir akıllı gösterici değildir.** Çerçevenin yok edilmesi sizin
sorumluluğunuzdadır; genellikle eşyordam türünün sonlandırıcı işlevine konur:

```cpp
~Generator() { if (tutamac) tutamac.destroy(); }
```
