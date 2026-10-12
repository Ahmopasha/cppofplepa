---
cilt: "II — İleri"
kisim: "8 — Ranges ve Views"
baslik: "8.5 Tembel değerlendirme"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 8.5 Tembel değerlendirme

Görünümlerin çalışma biçimi **tembeldir** *(lazy)*: işlem, görünüm oluşturulduğunda
değil, üzerinde dolaşıldığında yapılır.

```cpp
auto g = v | std::views::transform([](int x) {
    std::cout << "hesaplanıyor\n";
    return x * 2;
});
// buraya kadar hiçbir şey yazdırılmadı

for (int x : g) { }      // yazdırma şimdi oluyor
```

İki sonucu vardır.

**Kullanılmayan eleman hesaplanmaz.** Bir milyon elemanlık bir aralıktan ilk üçünü
alırsanız, yalnızca üç eleman işlenir.

**Aralık, kaynağa bağlıdır.** Kaynak kap değişirse görünüm de değişir; kaynak yok olursa
görünüm sarkar. Kısım 11.2'deki ömür uyarısı burada da aynen geçerlidir.
