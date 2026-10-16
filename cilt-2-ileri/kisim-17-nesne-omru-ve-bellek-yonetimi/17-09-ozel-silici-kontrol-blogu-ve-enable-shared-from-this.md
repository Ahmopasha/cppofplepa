---
cilt: "II — İleri"
kisim: "17 — Nesne Ömrü ve Bellek Yönetimi"
baslik: "17.9 Özel silici, kontrol bloğu ve `enable_shared_from_this`"
kaynak: "ders notları"
kutular: ["Standart Notu — C++17"]
son_kontrol: "2026-10 (C++23)"
---

## 17.9 Özel silici, kontrol bloğu ve `enable_shared_from_this`

Cilt I Kısım 25'te akıllı göstericilerin kullanımı anlatılmış, üç ayrıntı buraya
bırakılmıştı. Üçü de akıllı göstericinin nesnenin ömrünü nasıl bitirdiğiyle ilgilidir.

### Özel silici

Akıllı gösterici, sahip olduğu nesnenin ömrünü varsayılan olarak `delete` ile bitirir.
Kaynak `delete` ile geri verilmiyorsa, örneğin bir C kütüphanesinin açma–kapama işlev
çiftiyle yönetiliyorsa, bu iş bir **özel silici** *(custom deleter)* ile yapılır:
göstericiyi alıp kaynağı geri veren bir çağrılabilir.

`unique_ptr`'da silici **türün parçasıdır**; silicinin türü ikinci şablon parametresidir.
Varsayılanı `std::default_delete<T>`'dir.

```cpp
struct DosyaKapat {
    void operator()(std::FILE* f) const { if (f) std::fclose(f); }
};

std::unique_ptr<std::FILE, DosyaKapat> dosya{std::fopen("veri.txt", "r")};
```

İşlev ya da lambda da silici olabilir; türü `decltype` ile yazılır ve silicinin kendisi
kurucu işleve verilir:

```cpp
void kapat(std::FILE* f) { if (f) std::fclose(f); }
std::unique_ptr<std::FILE, decltype(&kapat)> d1{std::fopen("a.txt", "r"), kapat};

auto sil = [](std::FILE* f) { if (f) std::fclose(f); };
std::unique_ptr<std::FILE, decltype(sil)> d2{std::fopen("b.txt", "r"), sil};
```

İşlev göstericisinde silici kurucuya verilmek zorundadır, çünkü tür yalnızca imzayı
belirtir, hangi işlevin çağrılacağını belirtmez. C++20'den itibaren yakalamasız bir
lambdanın türü varsayılan olarak kurulabildiğinden `d2` silici verilmeden de kurulabilir.

Silicinin türün parçası olmasının iki sonucu vardır. Silici türleri farklı iki
`unique_ptr` farklı türlerdir; silici türü, tutulduğu kabın ve geçirildiği arayüzün
türüne de girer. Taşıyarak atama silici türlerinin birbirine atanabilmesine bağlıdır:
yakalamasız lambda işlev göstericisine dönüştüğü için `d1 = std::move(d2);` derlenir,
`DosyaKapat` ile işlev göstericisi arasında böyle bir dönüşüm olmadığı için
`d1 = std::move(dosya);` derlenmez. İkincisi, silici `unique_ptr` nesnesinin içinde
saklanır. Durumsuz bir işlev nesnesi ya da yakalamasız bir lambda, yaygın gerçeklemelerde
`unique_ptr`'ın boyutunu büyütmez (bkz. Kısım 6.8); işlev göstericisi ise `unique_ptr`'ın
boyutunu bir gösterici kadar büyütür; Cilt I Kısım 25.5'teki maliyet eşitliği varsayılan
ve durumsuz siliciler içindir.

`shared_ptr`'da silici **türün parçası değildir**; şablon argümanı olarak değil, kurucu
işleve argüman olarak verilir:

```cpp
std::shared_ptr<std::FILE> dosya{std::fopen("veri.txt", "r"), DosyaKapat{}};
```

Silici, aşağıda anlatılan kontrol bloğunda saklanır. Bu yüzden silicileri farklı iki
`shared_ptr<std::FILE>` aynı türdendir ve aynı kapta tutulabilir; silicinin türü type
erasure ile gizlenir (bkz. Kısım 14.3). `make_shared` özel silici kabul etmez; silici
gerekiyorsa `shared_ptr` doğrudan kurulur.

Örneklerdeki `if (f)` denetimi `shared_ptr` için gereklidir. `unique_ptr` boş bir
göstericiyi siliciye vermez; `shared_ptr` ise silicisini boş gösterici için de çağırır ve
`std::fclose`'a boş gösterici vermek tanımsız davranıştır. Silici çağrısı hata
göndermemelidir. Bu yüzden `std::fclose`'un bildirdiği kapatma hatası silicide kaybolur;
hatanın kullanıcıya iletilmesi gerekiyorsa ayrıca açık bir kapatma işlevi sunulur.

### Kontrol bloğu

Cilt I Kısım 25.3'te `shared_ptr`'ın sayacını ayrı bir kontrol bloğunda tuttuğu
söylenmişti. Blokta iki sayaç vardır: nesneye kaç `shared_ptr`'ın sahip olduğu
(`use_count`) ve nesneyi kaç `weak_ptr`'ın gözlediği. Silinecek gösterici, silici ve
varsa ayırıcı da bu blokta durur; `make_shared` ile kurulmuşsa blok, gösterici yerine
nesnenin kendisini içerir. Blok silinecek göstericiyi özgün türüyle tuttuğu için
`std::shared_ptr<Base> p{new Derived}` nesneyi `Derived` olarak yok eder.
`unique_ptr<Derived>`'dan `unique_ptr<Base>`'e dönüşümde ise silici
`default_delete<Base>` olur; dönüşüm derlenir, ama `Base`'in sonlandırıcı işlevi sanal
değilse nesnenin `Base*` üzerinden silinmesi tanımsız davranıştır (bkz. Cilt I Kısım 17.7).

İki sayacın ayrı olmasının sonucu şudur: son `shared_ptr` yok olunca **nesne** yok
edilir; son `weak_ptr` da yok olunca **kontrol bloğu** geri verilir. `weak_ptr`'ın
nesnenin hâlâ yaşayıp yaşamadığını sorabilmesi (Cilt I Kısım 25.4) bu sayede mümkündür.

Kontrol bloğu, nesneye sahip olan ilk `shared_ptr` kurulurken oluşur. Aynı çıplak adresten
iki ayrı `shared_ptr` kurmak, Cilt I Kısım 25.5'teki çifte yıkımın nedenidir: iki ayrı
kontrol bloğu oluşur ve ikisi de kendi sayacı sıfıra inince nesneyi yok etmeye çalışır.

`make_shared`, nesneyi ve kontrol bloğunu tek bir bellek bloğunda ayırır (Cilt I Kısım
25.3). Bunun bir bedeli vardır: nesne son `shared_ptr` ile yok edilir, ama ortak bellek
bloğu son `weak_ptr` da yok olana kadar geri verilemez. `sizeof`'u büyük bir nesne uzun
yaşayan `weak_ptr`'larla gözleniyorsa, `shared_ptr`'ı `new` ile ayrıca kurmak nesnenin
belleğinin daha erken geri verilmesini sağlar; geç geri verilen yalnızca nesnenin kendi
belleğidir, nesnenin sonlandırıcı işlevinde geri verdiği kaynaklar (ör. bir `std::vector`
üyesinin elemanları) son `shared_ptr` ile birlikte geri verilir.

### `enable_shared_from_this`

Bir üye işlevin içinde, işlevin çağrıldığı nesneyi gösteren bir `shared_ptr` gerekebilir;
örneğin nesne kendisini, sonra çalışacak bir işe vermek istediğinde.
`std::shared_ptr<Gorev>(this)` yazmak aynı adres için ikinci bir kontrol bloğu oluşturur
ve çifte yıkıma yol açar.

Çözüm, sınıfı `std::enable_shared_from_this`'ten türetmektir. Taban sınıf şablonuna
türemiş sınıfın kendisi argüman olarak verilir; bu, Kısım 6.13'teki CRTP kalıbıdır.
Taban, `shared_ptr` kurucusunun erişebileceği ve belirsiz olmayan bir taban olmalıdır;
bu yüzden kalıtım `public` olmalıdır.

```cpp
class Gorev : public std::enable_shared_from_this<Gorev> {
public:
    void kaydet(std::vector<std::shared_ptr<Gorev>>& kuyruk)
    {
        kuyruk.push_back(shared_from_this());     // var olan kontrol bloğunu paylaşır
    }
};

auto g = std::make_shared<Gorev>();
std::vector<std::shared_ptr<Gorev>> kuyruk;
g->kaydet(kuyruk);                                // g.use_count() == 2
```

Mekanizma şudur: taban sınıf, nesneyi gözleyen bir `weak_ptr` tutar. Nesneye sahip olan
ilk `shared_ptr` kurulurken bu `weak_ptr` doldurulur; `shared_from_this` ondan yeni bir
`shared_ptr` üretir. Bu yüzden **`shared_from_this` yalnızca nesne zaten bir
`shared_ptr` tarafından sahiplenilmişse çağrılabilir.** Sahiplenilmemiş bir nesnede
(örneğin yığında ya da `new` ile oluşturulup henüz bir `shared_ptr`'a verilmemiş) ya da
kurucu işlevin içinde çağrılırsa `std::bad_weak_ptr` gönderilir. Hata göndermeden
denetlemek için C++17 ile gelen `weak_from_this` kullanılır; nesnenin sahibi yoksa
döndürdüğü `weak_ptr`'ın `expired()` sonucu `true` olur (hiç sahiplenilmemiş nesnede bu
`weak_ptr` boştur), bu yüzden denetim `expired()` ya da `lock()` ile yapılır. `class`
bildiriminde `public` unutulursa kod yine derlenir, ama `shared_ptr` kurucusu tabanı
göremediği için `weak_ptr` doldurulmaz ve `shared_from_this` C++17'den itibaren çalışma
zamanında `std::bad_weak_ptr` gönderir.

> **Standart Notu — C++17**
> **C++17 öncesi:** Sahiplenilmemiş bir nesnede `shared_from_this` çağırmak tanımsız
> davranıştı.
> **C++17 ile:** `std::bad_weak_ptr` gönderilir.
> **Neden değişti:** C++17, taban sınıfın tuttuğu `weak_ptr`'ın ne zaman doldurulacağını
> kesinleştirdi. Sahiplenilmemiş nesnede bu `weak_ptr` boş kalır ve `shared_from_this`,
> süresi dolmuş bir `weak_ptr`'dan `shared_ptr` kurmakla aynı sonucu verir.
