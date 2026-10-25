# Tarama — Cilt II Kısım 8 (Ekim 2026)

Kısım 8'deki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış),
**doğrulanamadı** (birincil kaynakta karşılığı yok). Kaynaklar C++23 metninin
(n4950, timsong-cpp.github.io/cppwp/n4950) bölüm adlarıyla verilir. C++20'ye kusur raporu
olarak uygulanan ranges değişiklikleri ayrıca belirtilmiştir: P2325R3 (`view` artık
`default_initializable` istemez), P2415R2 (`owning_view`; `views::all` sağ değer kaba
`owning_view` döndürür; `view`'in sonlandırma karmaşıklığı şartı gevşetildi), P2432R1
(`views::istream`). Kusur raporu durumları cppreference'ın "Defect reports"
tablolarından alındı (`ranges/view`, `ranges/basic_istream_view`); P2415R2'nin kendi
metni DR ifadesi içermez, yalnızca LWG3452'yi çözdüğünü söyler.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 8.1 | İki ayrı kaptan iteratör geçirmek tanımsız davranıştır; örnek yorumu: "derlenir, çöker" | [iterator.requirements.general]/12: geçersiz aralığa kütüphane işlevi uygulamanın sonucu tanımsızdır. Tanımsız davranış çökmeyi garanti etmez | gerçekleme |
| 2 | 8.1 | Ranges sürümleri `std::ranges` isim alanında eski algoritmalara paralel olarak bulunur | [numeric.ops.overview]: `<numeric>`'te `std::ranges` altında yalnızca `iota` (C++23) vardır; `accumulate`, `reduce`, `inner_product`, `partial_sum` gibi sayısal algoritmaların ranges sürümü yoktur | eksik |
| 3 | 8.1 | Ranges, "güvenlik" sorununu (iki ayrı kaptan iteratör) da çözer | [sort]: `ranges::sort(I first, S last, ...)` yükü vardır; aynı türden iki iteratör `sentinel_for<S, I>`'yı sağlar. Sorun yalnızca aralığın kendisi geçirildiğinde ortadan kalkar | eksik (test 1) |
| 4 | 8.1 | `std::ranges::sort(v)` ile kabın kendisi yeterlidir | [algorithm.syn], [sort] | doğru |
| 5 | 8.2 | `range` bir sınıf değil kavramdır; tanımı `requires(T& t) { ranges::begin(t); ranges::end(t); }` | [range.range] | doğru |
| 6 | 8.2 | Her STL kabı zaten bir aralıktır | Kap uyumlandırıcıları (`stack`, `queue`, `priority_queue`; [container.adaptors]) `begin`/`end` sunmaz, `range`'i sağlamaz | eksik (test 2) |
| 7 | 8.2 | Ham diziler de aralıktır | [range.access.begin], [range.access.end]: sınırı bilinen diziler için; sınırı bilinmeyen dizide `ranges::end` geçersizdir (pratikte önemsiz) | doğru |
| 8 | 8.2 | `input_range` … `contiguous_range` ve `sized_range`, iteratör kategorilerinin aralık düzeyindeki karşılığıdır | [range.refinements], [range.sized]: `sized_range` iteratör kategorisine bağlı değildir, zincirin dışındadır (ör. `forward_list` ileri yönlü ama boyutlu değil). Listede `output_range`, `common_range`, `view`, `borrowed_range`, `viewable_range` (C++23'te `constant_range`) yok | eksik (test 3) |
| 9 | 8.3 | Eski STL algoritmalarında `begin` ve `end` aynı türden olmak zorundaydı | [sort] vb.: `std` yüklerinde tek iteratör şablon parametresi | doğru |
| 10 | 8.3 | `unreachable_sentinel` hiçbir iteratöre eşit olmayan bir sentineldir | [unreachable.sentinel]: `operator==` her zaman `false` döndürür | doğru |
| 11 | 8.3 | Sonsuz aralıklar bununla kurulur | [range.iota.view]: `iota_view`'ın `Bound` varsayılanı `unreachable_sentinel_t` | doğru |
| 12 | 8.3 | Bitiş denetimi tamamen elenir ve derleyici döngüyü daha iyi optimize eder | [unreachable.sentinel] örneği yalnızca çağrının "potansiyel olarak" daha verimli olabileceğini söyler; eniyileme gerçeklemenin işidir | gerçekleme |
| 13 | 8.4 | Görünüm kopyalanması ve taşınması ucuz olan bir aralıktır; veriyi sahiplenmez | [range.view]/1–2: `view = range && movable && enable_view`; kopyalanabilir olması gerekmez (kopyalanabiliyorsa O(1)). Sahiplenen görünümler vardır: `single_view` elemanı içinde tutar ([range.single.view]), `owning_view` kabı sahiplenir ve yalnızca taşınabilir ([range.owning.view]); [range.view]/4 örneği de sahipliği paylaşan bir görünümdür | düzeltilmeli (test 4) |
| 14 | 8.4 | `ciftler` yeni bir kap değildir; bellek ayrılmaz, eleman kopyalanmaz; dolaşıldıkça süzülür | [range.filter.view]: veri elemanları taban görünüm ve yüklemdir | doğru |
| 15 | 8.5 | İşlem görünüm oluşturulduğunda değil, üzerinde dolaşıldığında yapılır | [range.transform.iterator]: işlev `operator*`'da çağrılır | doğru |
| 16 | 8.5 | Bir milyon elemanlık aralıktan ilk üçü alınırsa yalnızca üç eleman işlenir | Boyutlu ve rastgele erişimli tabanda doğru ([range.take.view]). Boyutsuz tabanda `take_view` `counted_iterator` kullanır; üçüncü elemandan sonraki `++` tabanı da ilerletir ([counted.iter.nav]), ör. `filter` yüklemi dördüncü eşleşmeye kadar çalışır | eksik (test 5) |
| 17 | 8.5 | Kaynak kap değişirse görünüm de değişir; kaynak yok olursa görünüm sarkar | [range.filter.view]: `begin()` sonucunu önbelleğe alır, sonraki değişiklik ilk konumu güncellemez. [range.all.general]/2.3: sağ değer kap `owning_view`'a taşınır, görünüm sarkmaz (P2415R2, C++20'ye DR) | eksik (test 4, test 6) |
| 18 | 8.6 | Uyumlandırıcı, bir aralık alıp görünüm üreten işlev nesnesidir | [range.adaptor.object]/6: `viewable_range` alıp `view` döndüren özelleştirme noktası nesnesi | doğru |
| 19 | 8.6 | Fabrika "girdisiz olarak" aralık üretir | [range.factories]: "görünüm oluşturan araçlar"; aralık almazlar ama argüman alırlar (`iota(1, 10)`, `single(x)`, `istream<int>(is)`) | eksik |
| 20 | 8.6 | Uyumlandırıcı tablosu (`filter` … `elements<N>`) | [range.adaptors] | doğru |
| 21 | 8.6 | Fabrikalar: `iota` (ikinci argüman yoksa sonsuz), `empty`, `single`, `istream` | [range.factories]; `views::istream` P2432R1 ile C++20'ye DR. C++23'teki `views::repeat` tabloda yok (tablo tam olduğunu iddia etmiyor) | doğru |
| 22 | 8.6 | C++23, `stride`, `chunk`, `zip`, `enumerate`'i ekledi | [range.stride], [range.chunk], [range.zip], [range.enumerate]; cppreference C++23 olarak işaretler | doğru |
| 23 | 8.7 | Uyumlandırıcılar `|` ile zincirlenir; birinin ürettiği görünüm sonrakinin girdisidir | [range.adaptor.object]/1: `R | C` ≡ `C(R)` | doğru |
| 24 | 8.7 | Zincirin tamamı tek geçişte çalışır; ara kap oluşmaz | [range.adaptors]: görünümler iteratör düzeyinde zincirlenir | doğru |
| 25 | 8.7 | `take(3)` yüzünden yalnızca üç eleman üretilecek kadar iş yapılır | [range.take.view], [range.take.sentinel], [counted.iter.nav]: `filter` üzerinde `take`'in bitiş denetimi sayaç sıfır olduktan sonra yapılır, ama sayacı sıfırlayan `++` tabandaki `filter` iteratörünü dördüncü eşleşmeye (ya da sona) kadar ilerletir | eksik (test 5) |
| 26 | 8.7 | Boru hattı yazımı işlevsel programlamadan ödünç alınmıştır | Tarihsel değerlendirme; standartta ya da önergelerde karşılığı bulunamadı | doğrulanamadı |
| 27 | 8.8 | `views::all` bir aralığı görünüme çevirir; boru hattının başında örtülü uygulanır | [range.all.general]: görünümse kopya, değilse `ref_view`, o da olmuyorsa `owning_view`. Uyumlandırıcıların çıkarım kılavuzları `views::all_t` kullanır | doğru |
| 28 | 8.8 | `views::counted` bir iteratör ve sayı alıp aralık üretir | [range.counted]: bitişik iteratörde `span`, rastgele erişimlide `subrange(E, E + n)`, değilse `subrange(counted_iterator, default_sentinel)` | doğru |
| 29 | 8.8 | `subrange` iteratör çiftini tek nesnede paketler | [range.subrange.general]: bir iteratörü ve bir **sentineli** birleştirir; `S` varsayılan olarak `I`'dır | eksik |
| 30 | 8.8 | `views::common`, `begin`/`end` türleri farklı aralığı aynı türlü aralığa çevirir | [range.common] | doğru |
| 31 | 8.8 | Örnek: `v | std::views::take(3)` için `std::sort(g.begin(), g.end())` "türler uyuşmayabilir" | [range.take.view]: `v` bir `vector` olduğunda taban boyutlu ve rastgele erişimlidir; `begin` ve `end` ikisi de `vector` iteratörüdür, `g` zaten `common_range`'dir. Örnek, anlattığı sorunu göstermiyor | eksik (test 7) |
| 32 | 8.9 | `ranges::sort(kisiler, {}, &Kisi::yas)`; ikinci parametre karşılaştırıcı, varsayılanı `ranges::less` | [sort]: `class Comp = ranges::less, class Proj = identity` | doğru |
| 33 | 8.9 | İzdüşüm veri elemanı göstericisi, üye işlev göstericisi ya da herhangi bir çağrılabilir olabilir | [projected], [alg.req.sortable]: izdüşüm `std::invoke` ile çağrılır (`indirectly_regular_unary_invocable`) | doğru |
| 34 | 8.10 | `ranges::find(std::vector{1, 2, 3}, 2)` `ranges::dangling` döndürür; `*it` derlenmez | [range.dangling], [range.range]: `borrowed_iterator_t` sağ değer `vector` için `dangling` | doğru |
| 35 | 8.10 | `string_view`, `span`, `subrange` ödünç aralıktır; `enable_borrowed_range` ile işaretlenmiştir | [range.range]: `borrowed_range` tanımı; [string.view.synop], [span.syn], [range.subrange] özelleştirmeleri | doğru |
| 36 | 8.10 | Ödünç aralık istisnası "zaten sahiplenmeyen türler" içindir | Sahiplenmemek yetmez: `filter_view`/`transform_view` sahiplenmeyen ama ödünç olmayan görünümlerdir; iteratörleri görünümün kendisine bağlıdır. Belirleyici olan `enable_borrowed_range`'dir | eksik (test 8) |
| 37 | 8.11 | C++20'de zincirin sonunda kap için elle kopyalamak gerekir; C++23'te `ranges::to` | [range.utility.conv.to] (P1206R7, C++23) | doğru |
| 38 | 8.11 (not) | C++20 ile algoritmalar aralığın kendisini alır; görünümler tembel ve zincirlenebilir | [algorithms], [range.adaptors] | doğru |
| 39 | 8.11 (not) | "Uyumsuz iteratör geçirmek kavram ihlali olarak derleme zamanında yakalanır" | [sort]: iteratör–sentinel yükü aynı türden iki iteratörü kabul eder; iki iteratörün aynı aralığa ait olması kavramın değil, [iterator.requirements.general]/12'nin konusudur (tanımsız davranış) | düzeltilmeli (test 1) |

**Sayım:** 39 iddia — 23 doğru, 2 düzeltilmeli, 11 eksik, 2 gerçekleme, 1 doğrulanamadı.

## Önerilen düzeltmeler

- **1 (8.1):** Yorumdaki "çöker" yerine "derlenir; tanımsız davranış" yazılmalı.
- **2 (8.1):** "Paralel olarak bulunur" yerine sayısal algoritmaların (`accumulate`, `reduce`…) ranges sürümü olmadığı, C++23'te yalnızca `ranges::iota` eklendiği söylenmeli.
- **3 (8.1):** Güvenlik kazancının yalnızca aralığın kendisi geçirildiğinde olduğu, `ranges::sort(v1.begin(), v2.end())`'nin hâlâ derlenip tanımsız davranış olduğu eklenmeli.
- **6 (8.2):** "Her STL kabı" ifadesi kap uyumlandırıcılarını (`stack`, `queue`, `priority_queue`) dışarıda bırakacak biçimde daraltılmalı.
- **8 (8.2):** `sized_range`'in iteratör kategorisi zincirinin parçası olmadığı, ayrı bir özellik olduğu söylenmeli; liste "başlıcaları" diye nitelenmeli.
- **12 (8.3):** "Derleyici daha iyi optimize eder" yerine "döngü sınaması dallanma gerektirmediği için daha verimli olabilir" denmeli.
- **13 (8.4):** Tanım standardınkine çekilmeli: görünüm taşınması (ve kopyalanabiliyorsa kopyalanması) sabit zamanlı olan aralıktır; çoğu görünüm sahiplenmez ama `single_view` ve `owning_view` sahiplenir.
- **16 (8.5):** "Yalnızca üç eleman işlenir" cümlesi, `filter` gibi boyutsuz tabanlarda bir eleman ötesine kadar çalışılabileceği kaydıyla yumuşatılmalı (8.7'ye atıf).
- **17 (8.5):** `filter_view` gibi görünümlerin `begin()`'i önbelleğe aldığı ve sağ değer kabın `owning_view`'a taşındığı (sarkmadığı) eklenmeli.
- **19 (8.6):** "Girdisiz" yerine "girdi olarak aralık almadan" yazılmalı.
- **25 (8.7):** `take(3)` cümlesine, tabanın boyutsuz olduğu durumda son `++`'nın tabandaki iteratörü bir kez daha ilerlettiği eklenmeli.
- **29 (8.8):** "İteratör çifti" yerine "bir iteratörü ve bir sentineli" yazılmalı.
- **31 (8.8):** Örnek, `vector` yerine ortak olmayan bir aralıkla kurulmalı ve `std::sort` yerine rastgele erişim istemeyen bir algoritmayla gösterilmeli (ör. `views::iota(0) | views::take(3)` ve `std::accumulate`); `common_view` rastgele erişim sağlamaz.
- **36 (8.10):** "Zaten sahiplenmeyen türler" yerine ölçütün `enable_borrowed_range` olduğu, `filter_view` gibi sahiplenmeyen görünümlerin ödünç olmadığı söylenmeli.
- **39 (8.11 notu):** "Uyumsuz iteratör … derleme zamanında yakalanır" cümlesi silinmeli ya da "aralığın kendisi geçirildiğinde bu hata yapılamaz" diye düzeltilmeli.

## Test 1 — iddia 3 ve 39: iki ayrı kaptan iteratör `ranges::sort`'a geçirilebilir

```cpp
#include <algorithm>
#include <cstdio>
#include <vector>

using It = std::vector<int>::iterator;

// İki iteratörün aynı kaba ait olup olmadığı türde görünmez; çağrı kısıtları sağlar
static_assert(requires(It ilk, It son) { std::ranges::sort(ilk, son); });

int main()
{
    std::puts("v1.begin(), v2.end() kavram denetiminden geçer");
}
```

## Test 2 — iddia 6: kap uyumlandırıcıları aralık değildir

```cpp
#include <cstdio>
#include <queue>
#include <ranges>
#include <stack>
#include <vector>

static_assert(std::ranges::range<std::vector<int>>);
static_assert(!std::ranges::range<std::stack<int>>);
static_assert(!std::ranges::range<std::queue<int>>);
static_assert(!std::ranges::range<std::priority_queue<int>>);

int main()
{
    std::puts("stack, queue, priority_queue: range değil");
}
```

## Test 3 — iddia 8: `sized_range` iteratör kategorisi zincirinin dışındadır

```cpp
#include <cstdio>
#include <forward_list>
#include <ranges>

static_assert(std::ranges::forward_range<std::forward_list<int>>);
static_assert(!std::ranges::sized_range<std::forward_list<int>>);

int main()
{
    std::puts("forward_list: forward_range ama sized_range değil");
}
```

## Test 4 — iddia 13 ve 17: sahiplenen görünümler; sağ değer kap sarkmaz

```cpp
#include <concepts>
#include <cstdio>
#include <ranges>
#include <string>
#include <utility>
#include <vector>

static_assert(std::ranges::view<std::ranges::single_view<std::string>>);
static_assert(std::ranges::view<std::ranges::owning_view<std::vector<int>>>);
static_assert(!std::copyable<std::ranges::owning_view<std::vector<int>>>);

auto ciftler()
{
    // Geçici vector owning_view'a taşınır; döndürülen görünüm sarkmaz
    return std::vector{1, 2, 3, 4} | std::views::filter([](int x) { return x % 2 == 0; });
}

int main()
{
    auto g = ciftler();
    static_assert(std::same_as<decltype(std::move(g).base()),
                               std::ranges::owning_view<std::vector<int>>>);
    for (int x : g)
        std::printf("%d ", x);    // 2 4
    std::puts("");
}
```

## Test 5 — iddia 16 ve 25: `filter | take(3)` yüklemi dördüncü eşleşmeye kadar çalıştırır

```cpp
#include <cstdio>
#include <ranges>
#include <vector>

int main()
{
    std::vector<int> v{2, 4, 6, 1, 1, 1, 1, 8, 1, 1};
    int yuklem_cagrisi = 0;
    auto g = v
        | std::views::filter([&](int x) { ++yuklem_cagrisi; return x % 2 == 0; })
        | std::views::take(3);
    for (int x : g)
        std::printf("%d ", x);                // 2 4 6
    std::printf("\n%d\n", yuklem_cagrisi);    // 8: üç değil, 8'e kadar
}
```

## Test 6 — iddia 17: `filter_view` `begin()`'i önbelleğe alır

```cpp
#include <cstdio>
#include <ranges>
#include <vector>

int main()
{
    std::vector<int> v{1, 3, 4};
    auto f = v | std::views::filter([](int x) { return x % 2 == 0; });
    for (int x : f) { (void)x; }          // begin() hesaplandı: v[2]
    v[0] = 2;                             // v[0] artık yüklemi sağlıyor
    int sayi = 0;
    for (int x : f) { (void)x; ++sayi; }
    std::printf("%d\n", sayi);            // 1: önbellekteki begin() v[2]'den başlar
}
```

## Test 7 — iddia 31: `vector` üzerinde `take` zaten ortak aralıktır

```cpp
#include <concepts>
#include <cstdio>
#include <ranges>
#include <utility>
#include <vector>

using G = decltype(std::declval<std::vector<int>&>() | std::views::take(3));

static_assert(std::ranges::common_range<G>);
static_assert(std::same_as<std::ranges::iterator_t<G>, std::vector<int>::iterator>);

// Ortak olmayan örnek: sınırsız iota üzerinde take
using H = decltype(std::views::iota(0) | std::views::take(3));
static_assert(!std::ranges::common_range<H>);

int main()
{
    std::puts("vector | take(3): begin ve end aynı türden");
}
```

## Test 8 — iddia 36: sahiplenmeyen her görünüm ödünç aralık değildir

```cpp
#include <algorithm>
#include <concepts>
#include <cstdio>
#include <ranges>
#include <vector>

int main()
{
    std::vector<int> v{1, 2, 3, 4};
    auto cift = [](int x) { return x % 2 == 0; };
    using F = decltype(v | std::views::filter(cift));
    static_assert(!std::ranges::borrowed_range<F>);    // v'yi sahiplenmez ama ödünç değil
    auto it = std::ranges::find(v | std::views::filter(cift), 4);
    static_assert(std::same_as<decltype(it), std::ranges::dangling>);
    std::puts("filter_view geçici olarak geçirilince dangling");
}
```
