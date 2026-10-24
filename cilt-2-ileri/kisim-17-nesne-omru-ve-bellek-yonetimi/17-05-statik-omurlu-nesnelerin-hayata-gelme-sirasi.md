---
cilt: "II — İleri"
kisim: "17 — Nesne Ömrü ve Bellek Yönetimi"
baslik: "17.5 Statik ömürlü nesnelerin hayata gelme sırası"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 17.5 Statik ömürlü nesnelerin hayata gelme sırası

Cilt I Kısım 15.1'deki dört ömür kategorisinden statik olanı, iki aşamada hayata gelir.

**Statik ilk değer verme**, her dinamik ilk değer vermeden önce tamamlanır. İlk değer
verme işleminin tamamı (çağrılan kurucu işlev dâhil) sabit ifade olan nesneler bu yolla,
**sabit ilk değer verme** *(constant initialization)* ile hayata gelir; geri kalan statik
ömürlü nesneler de bu aşamada sıfırla ilk değer alır; buna **sıfırla ilk değer verme**
*(zero-initialization)* denir.

**Dinamik ilk değer verme**, statik ilk değer verme dışında kalan her ilk değer vermedir.
Sabit ifade olmayan bir ilk değer verme gerektiren nesneler bu aşamaya kalır. Ancak
gerçekleme, belirli koşullar sağlanıyorsa böyle bir ilk değer vermeyi de statik olarak
yapabilir. Blok dışındaki, `inline` olmayan bir değişkende dinamik ilk değer vermenin
`main`'in ilk deyiminden önce mi yapılacağı, yoksa ertelenip mi yapılacağı gerçeklemeye
bağlıdır; ertelenirse, aynı çeviri biriminde tanımlı, `inline` olmayan bir işlevin ya da
değişkenin ilk değer verme dışındaki ilk **ODR kullanımı** *(odr-use)* gerçekleşmeden önce
yapılır (ODR için bkz. Cilt I, Kısım 2.7). Blok dışındaki statik ya da iş parçacığı ömürlü
bir değişkenin ilk değer verilmesinden (doğrudan ya da dolaylı) kaynaklanan kullanımlar bu
garantiye girmez.

```cpp
int oku();

int a = 42;          // statik ilk değer verme
int b = oku();       // dinamik ilk değer verme
```

Sorun ikincisindedir. **Aynı çeviri birimindeki** nesnelerin sırası tanımlıdır: tanım
sırasına göre hayata gelirler. Şablonların örneklenmiş özelleştirmeleri (sınıf
şablonlarının statik veri elemanları ve değişken şablonları) bu kuralın dışındadır; bunlar
**sırasızdır** *(unordered)*; sıraları garanti edilmez. Örneklenmiş özelleştirme olmayan
`inline` değişkenler (açık özelleştirmeler dâhil) ise yalnızca **kısmen sıralıdır**
*(partially-ordered)*; geri kalanlar **sıralıdır** *(ordered)*. Örneğin bir başlıkta
tanımlı `inline` değişken, o başlığı içeren çeviri biriminde ondan sonra tanımlanan sıralı
değişkenlerden önce hayata gelir. Aralarında **arayüz bağımlılığı**
*(interface dependency)* (modül içe aktarma) olmayan **farklı çeviri birimlerindeki**
nesnelerin sırası ise belirtilmemiştir; bkz. Cilt I Kısım 2.5.

Bir nesnenin kurucu işlevi, başka bir çeviri birimindeki, ilk değeri henüz verilmemiş bir
nesneye erişirse sonuç o nesnenin türüne bağlıdır: kurucu işlevi henüz çalışmamış bir
sınıf nesnesine erişim tanımsız davranıştır; skaler bir nesnede ise sıfır değeri
okunabilir; gerçekleme o nesnenin ilk değerini statik olarak vermişse son değeri de
okunabilir. Hangisinin okunacağı belirtilmemiştir. Bu duruma İngilizcede *static
initialization order fiasco* denir.

Üç çözüm vardır.

**Sabit ifadeyle ilk değer verin.** `constexpr` veya `constinit` kullanarak nesneyi
statik ilk değer verme aşamasına taşırsanız sorun ortadan kalkar (bkz. Kısım 18.4).

**Nesneyi işlev içine taşıyın.** Dinamik ilk değer alan yerel `static` nesneler, denetim
bildirimden ilk kez geçtiğinde hayata gelir; sıra, erişim sırasına bağlanmış olur.

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
güvenlidir**: ilk değer verme sürerken başka bir iş parçacığı bildirime ulaşırsa, ilk
değer verme bitene kadar bekler.

**Nifty Counter deyimini kullanın.** Nesnenin gerçekten global olması gerekiyorsa,
Kısım 14.5'teki deyim uygulanır. `std::cout` ve diğer akım nesneleri böyle kurulmuştur.

Hayatın sonlanma sırası, hayata gelme sırasının tersidir. Aynı belirsizlik orada da
geçerlidir; bir sonlandırıcı işlev, çoktan yok edilmiş bir global nesneye erişebilir.
