---
cilt: "II — İleri"
kisim: "17 — Nesne Ömrü ve Bellek Yönetimi"
baslik: "17.5 Statik ömürlü nesnelerin hayata gelme sırası"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 17.5 Statik ömürlü nesnelerin hayata gelme sırası

Cilt I Kısım 15.1'deki dört ömür kategorisinden statik olanı, iki aşamada hayata gelir.

**Statik ilk değer verme** derleme zamanında olur; değer doğrudan çalıştırılabilir
dosyaya yazılır. Sabit ifadeyle ilk değer verilen nesneler bu yolla hayata gelir.

**Dinamik ilk değer verme** ise `main` çağrılmadan önce, çalışma zamanında yapılır. İlk
değer veren ifade sabit değilse bu aşamaya kalır.

```cpp
int oku();

int a = 42;          // statik ilk değer verme
int b = oku();       // dinamik ilk değer verme
```

Sorun ikincisindedir. **Aynı çeviri birimindeki** nesnelerin sırası tanımlıdır: bildirim
sırasına göre hayata gelirler. **Farklı çeviri birimlerindeki** nesnelerin sırası ise
belirtilmemiştir *(unspecified)*; bkz. Cilt I Kısım 2.5.

Bir nesnenin kurucu işlevi, henüz hayata gelmemiş başka bir çeviri birimindeki nesneye
erişirse, program tanımsız davranışa girer. Bu duruma İngilizcede *static initialization
order fiasco* denir.

Üç çözüm vardır.

**Sabit ifadeyle ilk değer verin.** `constexpr` veya `constinit` kullanarak nesneyi
statik ilk değer verme aşamasına taşırsanız sorun ortadan kalkar (bkz. Kısım 18.4).

**Nesneyi işlev içine taşıyın.** Yerel `static` nesneler, işlev ilk çağrıldığında hayata
gelir; sıra, erişim sırasına bağlanmış olur.

<!-- kod-baglam
struct Ayarlar { };
-->
```cpp
Ayarlar& ayarlar()
{
    static Ayarlar a;        // ilk çağrıda hayata gelir
    return a;
}
```

Buna *Meyers singleton* denir. C++11'den itibaren bu ilk değer verme **iş parçacığı
güvenlidir**; derleyici gerekli kilitlemeyi kendisi ekler.

**Nifty Counter deyimini kullanın.** Nesnenin gerçekten global olması gerekiyorsa,
Kısım 14.5'teki deyim uygulanır. `std::cout` ve diğer akım nesneleri böyle kurulmuştur.

Hayatın sonlanma sırası, hayata gelme sırasının tersidir. Aynı belirsizlik orada da
geçerlidir; bir sonlandırıcı işlev, çoktan yok edilmiş bir global nesneye erişebilir.
