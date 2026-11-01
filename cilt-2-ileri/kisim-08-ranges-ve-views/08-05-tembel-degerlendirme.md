---
cilt: "II — İleri"
kisim: "8 — Ranges ve Views"
baslik: "8.5 Tembel değerlendirme"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++23)"
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
alırsanız, geri kalan elemanlar işlenmez. `filter` gibi ilerlerken sonraki eşleşmeyi
arayan bir görünümün üzerinde fazladan bir ilerleme gerekebilir; bunun maliyeti tek
elemanla sınırlı değildir (Kısım 8.7).

**Sahiplenmeyen görünüm, kaynağa bağlıdır.** Aralık uyumlandırıcısıyla (Kısım 8.6) L-Value
bir kap üzerine kurulan görünüm o kaba bakar: kapta yapılan değişiklikler görünümden
görülür, kap yok olursa görünüm sarkar. Kısım 11.2'deki ömür uyarısı burada da aynen
geçerlidir. Aralık uyumlandırıcısına verilen R-Value bir kap ise görünümün içindeki
`owning_view`'a taşınır, bu yüzden görünüm sarkmaz. `filter_view` gibi bazı görünümler,
üzerinde durduğu aralık `forward_range` olduğunda ilk `begin()` sonucunu önbelleğe alır;
sonradan yapılan değişiklik bu ilk konumu güncellemez. Değişiklik önbellekteki iteratörü
geçersiz kılmışsa (ör. `vector` yeniden bellek ayırdıysa) görünümü yeniden dolaşmak
tanımsız davranıştır; kap değiştirildikten sonra görünüm yeniden kurulmalıdır.
