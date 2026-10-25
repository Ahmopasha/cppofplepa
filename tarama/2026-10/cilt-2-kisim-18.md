# Tarama — Cilt II Kısım 18 (Ekim 2026)

Kısım 18'deki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar bölüm
adlarıyla verilir; paragraf numaraları C++23 metnine (N4950) göredir. Eski standartlar için
N3337 (C++11), N4659 (C++17) ve N4861 (C++20) kullanıldı. 18.1 Ekim 2026'da panelden
geçmişti; bu turda yeniden tarandı ve kronolojisi önergelerle karşılaştırıldı: P2242R3,
P2448R2 ve P2647R1 C++23'e kusur raporu olmadan girdi; P2564R3 ise C++20'ye kusur raporudur
(cppreference, C++23 derleyici desteği tablosu).

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 18.1 | C++11'de gövde tek bir `return` deyiminden ibaret olmak zorundaydı | N3337 [dcl.constexpr]/3: gövde boş deyimler, `static_assert` bildirimleri, sınıf ya da numaralandırma tanımlamayan `typedef`/takma ad bildirimleri, `using` bildirimleri ve yönergeleri ile **tam bir** `return` deyimi içerebilirdi | eksik |
| 2 | 18.1 | C++11'de döngü, yerel değişken, `if` yazılamazdı; koşul üçlü operatörle, tekrar özyinelemeyle | N3337 [dcl.constexpr]/3 (izin listesinde yoklar) | doğru |
| 3 | 18.1 | C++14 yerel değişkenleri, döngüleri, `if`/`switch`'i ve birden çok `return`'ü serbest bıraktı | N3652 ("Relaxing constraints on constexpr functions"); cppreference [constexpr]. `static`/`thread_local`, ilk değersiz değişken, `goto` ve `try` yasak kaldı | doğru |
| 4 | 18.1 | C++17'de `if constexpr` gövdede kullanılabilir hâle geldi | P0292R2: `if constexpr` dile C++17'de girdi; "hâle geldi" anlatımı daha önce var olup gövdeye izin verilmiş izlenimi verebilir, ama iddia yanlış değil | doğru |
| 5 | 18.1 | C++17'de lambda ifadeleri örtülü olarak `constexpr` oldu | N4659 [expr.prim.lambda.closure]/4: çağrı işleci yalnızca `constexpr` işlev şartlarını sağlıyorsa `constexpr`'dir. C++23'te (N4950) şart *constexpr-suitable* olmaktır (eşyordam değil) | eksik |
| 6 | 18.1 | C++20: `try`/`catch`, sanal işlev çağrısı, `union` üyesi değiştirme, `constexpr` sonlandırıcı, geçici dinamik bellek | P1002R1, P1064R0, P1330R0, P0784R7 (cppreference, C++20 derleyici desteği). `throw` ifadesinin değerlendirilmesi C++23'te de sabit ifadeyi bozar ([expr.const]/5.25); metin bunu iddia etmiyor | doğru |
| 7 | 18.1 | Derleme zamanında ayrılan bellek derleme zamanında serbest bırakılmak zorundadır | [expr.const]/5.18–5.21 | doğru |
| 8 | 18.1 | Bu sayede `std::vector` ve `std::string` derleme zamanında kullanılabilir hâle geldi | P1004R2, P0980R1 (C++20) | doğru |
| 9 | 18.1 | C++23'te `static` ve `thread_local` değişkenler, literal olmayan yerel değişkenler ve `goto` gövdede yer alabilir | P2242R3: N4861 [dcl.constexpr]/3'teki yasak kaldırıldı | doğru |
| 10 | 18.1 | Derleme zamanında yürütülen yolda bu satırlara gelinirse çağrı sabit ifade olmaz | `static`/`thread_local` için [expr.const]/5.2, `goto` için /5.30 doğru. Literal olmayan değişken için böyle bir kural **yoktur** (P2242R3 yalnızca yasağı kaldırır, [expr.const]'a bunun için madde eklemez): değişkenin kurucusu ve sonlandırıcısı sabit değerlendirilebiliyorsa çağrı sabit ifade olur | eksik (test 1) |
| 11 | 18.1 | Sabit ifadelerde kullanılabilen `static`/`thread_local` değişkenler (ör. `static constexpr`) kuralın dışındadır | P2647R1; [expr.const]/5.2 ("unless that variable is usable in constant expressions") | doğru |
| 12 | 18.1 | Hiçbir argümanla sabit değerlendirilemeyen `constexpr` işlev C++23 öncesinde "geçersiz, tanı gerekmez" idi; artık geçerlidir | N4861 [dcl.constexpr]/6; P2448R2 bu kuralı kaldırdı (C++23, kusur raporu değil) | doğru |
| 13 | 18.1 | Böyle bir işlev sabit ifade gerektiren yerde çağrılırsa sentaks hatası olur | [expr.const]/5.3 ve ilgili bağlamın sabit ifade şartı | doğru |
| 14 | 18.1 | Parametre ve dönüş türlerinin literal tür olma zorunluluğu kalktı | P2448R2 (N4861 [dcl.constexpr]/3'teki iki madde silindi) | doğru |
| 15 | 18.1 | `constexpr` işlev derleme zamanında çalışmak zorunda değildir; argümanları sabit ifade değilse çalışma zamanında çalışır | [dcl.constexpr], [expr.const] | doğru |
| 16 | 18.2 | Sınıf türünden nesnenin derleme zamanında oluşabilmesi için kurucu işlevinin `constexpr` olması gerekir | Toplu türlerde *(aggregate)* kurucu çağrılmaz; örtülü tanımlanan varsayılan kurucu, elle yazılmışı *constexpr-suitable* olacaksa `constexpr`'dir ([class.default.ctor]/4). Kural yalnızca kullanıcının yazdığı kurucular için geçerlidir | eksik (test 2) |
| 17 | 18.2 | `constexpr` sınıf diye ayrı bir kavram yoktur; üye işlevlerin `constexpr` olması yeterlidir | [basic.types.general]/10: ilgili kavram **literal tür**dür; `constexpr` sonlandırıcı, `volatile` olmayan literal türden veri elemanları ve taban sınıflar da gerekir ([dcl.constexpr]/6: `constexpr` nesne literal türden olmalıdır) | eksik (test 3) |
| 18 | 18.2 | C++20'den itibaren sonlandırıcı `constexpr` olabilir; derleme zamanında bellek ayıran türlerin ön koşuludur | P0784R7; [basic.types.general]/10.5.1, [expr.const]/5.17 | doğru |
| 19 | 18.2 | `constexpr` nesne aynı zamanda `const`'tur; değiştirilemez | [dcl.constexpr]/6 (`const` yapar); [dcl.type.cv]/4 ve örneği: `mutable` veri elemanları `const` nesnede de değiştirilebilir | eksik (test 4) |
| 20 | 18.3 | `consteval` işlev yalnızca derleme zamanında çağrılabilir; her çağrısı derleme zamanında bir sabite dönüşmek zorundadır | [expr.const]: yalnızca ivedi işlev bağlamı *(immediate function context)* dışındaki çağrılar *(immediate invocation)* sabit ifade olmalıdır; başka bir `consteval` işlevin içindeki `kare(x)` sabit ifade değildir ve geçerlidir. P2564R3 (C++20'ye kusur raporu) ile `constexpr` işlev şablonu örneklerinde ve lambdalarda böyle bir çağrı hata değil, çevreleyen işlevi ivedi işleve dönüştürür | eksik (test 5) |
| 21 | 18.3 | `int b = kare(oku());` sentaks hatasıdır | [expr.const] (ivedi çağrı sabit ifade olmalı) | doğru |
| 22 | 18.3 | Bu işlevlere ivedi işlev *(immediate function)* denir | N4861 [dcl.constexpr]/2; N4950 [expr.const]: `consteval` bildirilenler ve ivediliği yayılan *(immediate-escalating)* işlevlerden ivedi ifade içerenler | doğru |
| 23 | 18.4 | Statik ilk değer verme derleme zamanında olur; değer çalıştırılabilir dosyaya yazılır | [basic.start.static]/2: statik ilk değer verme (sabit ilk değer verme ve sıfırla ilk değer verme) her dinamik ilk değer vermeden önce yapılır; "derleme zamanı" ve "dosyaya yazılır" gerçekleme anlatımıdır. (Cilt II 17.5'teki aynı cümle, 17 taramasının 10. iddiasıdır ve düzeltildi) | gerçekleme |
| 24 | 18.4 | Dinamik ilk değer verme program başlarken, `main` çağrılmadan önce çalışır | [basic.start.dynamic]/5: blok dışı, `inline` olmayan değişkenler için `main`'in ilk deyiminden önce mi yapılacağı yoksa ertelenebileceği **gerçeklemeye bağlıdır**; blok kapsamındaki statik değişkenler denetim bildirimden ilk geçtiğinde ilk değer alır ([stmt.dcl]/3). (17 taramasının 11. iddiası) | düzeltilmeli (test 6) |
| 25 | 18.4 | Farklı çeviri birimlerindeki nesnelerin sırası belirtilmemiştir | [basic.start.dynamic]/3 (belirsiz sıralı *(indeterminately sequenced)*) | doğru |
| 26 | 18.4 | `constinit`, nesnenin statik ilk değer verme ile hayata geleceğini garantiler; `constinit int bozuk = oku();` sentaks hatası | [dcl.constinit]/2: dinamik ilk değer alan `constinit` değişken, gerçekleme onu statik yapacak olsa bile geçersizdir. [dcl.constinit]/1: yalnızca statik ya da iş parçacığı ömürlü değişkenlere uygulanır (metin bağlamında zaten bu) | doğru |
| 27 | 18.4 | `constinit int genel = 42; // derleme zamanında ilk değer alır`; `constexpr` nesne "derleme zamanında ilk değer alır"; tablodaki "Derleme zamanında ilk değer" | [basic.start.static]/2, [dcl.constinit]/2: standardın terimi statik ilk değer vermedir; "derleme zamanında" 23. iddiadaki gerçekleme anlatımıdır. Otomatik ömürlü bir `constexpr` yerel nesne ise her girişte oluşturulur; derleme zamanında bilinen onun değeridir | gerçekleme |
| 28 | 18.4 | `constinit` nesne sonradan değiştirilebilir; `constexpr` nesne değiştirilemez | [dcl.constinit] nesneyi `const` yapmaz; [dcl.constexpr]/6 yapar (`mutable` istisnası için 19. iddia) | doğru |
| 29 | 18.4 | Tablo: `const` değişmezliği garantiler | [dcl.type.cv]/4 (`mutable` istisnası) | doğru |

**Özet:** 29 iddia — 19 doğru, 1 düzeltilmeli, 7 eksik, 2 gerçekleme.

## Önerilen düzeltmeler

- **İddia 1 (18.1):** "Gövde tek bir `return` deyiminden ibaret olmak zorundaydı" yerine
  "gövdede `return` dışında yalnızca `static_assert`, `typedef`/`using` gibi çalıştırılmayan
  bildirimler bulunabilirdi; çalışan tek deyim bir `return`'dü" denmeli.
- **İddia 5 (18.1):** "lambda ifadeleri örtülü olarak `constexpr` oldu" cümlesine "`constexpr`
  işlev şartlarını sağladıklarında" kaydı eklenmeli.
- **İddia 10 (18.1):** "bu satırlara gelinmemelidir" kuralı yalnızca `static`/`thread_local`
  bildirimleri ve `goto` için söylenmeli; literal olmayan yerel değişken için "kurucusu ya da
  sonlandırıcısı `constexpr` değilse o çağrı sabit ifade olmaz" denmeli.
- **İddia 16 (18.2):** İlk cümle "kullanıcının yazdığı kurucu işlev `constexpr` olmalıdır;
  toplu türler ve örtülü kurucular bu şartı kendiliğinden karşılayabilir" diye genişletilmeli.
- **İddia 17 (18.2):** "`constexpr` sınıf diye ayrı bir kavram yoktur" cümlesinden sonra ilgili
  kavramın **literal tür** olduğu ve veri elemanlarının da literal türden olması gerektiği
  eklenmeli.
- **İddia 19 (18.2):** "değiştirilemez" cümlesine "`mutable` veri elemanları dışında" kaydı
  eklenmeli.
- **İddia 20 (18.3):** "Her çağrısı ... sabite dönüşmek zorundadır" cümlesi "başka bir ivedi
  işlevin dışındaki her çağrısı" diye daraltılmalı; C++23 (C++20'ye kusur raporu P2564R3) ile
  `constexpr` şablon örneklerinin ve lambdaların ivedi işleve dönüşebildiği bir cümleyle anılmalı.
- **İddia 23 ve 27 (18.4):** "derleme zamanında olur; değer doğrudan çalıştırılabilir dosyaya
  yazılır" yerine Cilt II 17.5'in düzeltilmiş anlatımı (statik ilk değer verme her dinamik ilk
  değer vermeden önce yapılır) kullanılmalı; kod yorumları ve tablo "statik ilk değer" diye
  yazılmalı.
- **İddia 24 (18.4):** "`main` çağrılmadan önce çalışır" yerine "`main`'den önce mi yapılacağı
  yoksa ilk kullanıma kadar ertelenebileceği gerçeklemeye bağlıdır; blok kapsamındaki statik
  nesneler ise ilk geçişte ilk değer alır" denmeli (17.5'teki düzeltmeyle aynı dil).

## Test 1 — iddia 10: literal olmayan yerel değişken sabit değerlendirmeyi bozmayabilir

```cpp
struct Uclu {                        // volatile veri elemanı: literal tür değil
    volatile int deger = 0;
};

constexpr int uclu_kullan()
{
    Uclu u;                          // kurucu ve sonlandırıcı sabit değerlendirilebilir
    return 3;
}

static_assert(uclu_kullan() == 3);   // derleme zamanında
```

## Test 2 — iddia 16: kurucu işlevi olmayan toplu tür ve örtülü kurucu

```cpp
struct Nokta2 { int x, y; };         // toplu tür: kurucu işlev yok
constexpr Nokta2 m{3, 5};
static_assert(m.x == 3);

struct Varsayilan { int x = 1; };    // örtülü varsayılan kurucu constexpr
constexpr Varsayilan v1;
static_assert(v1.x == 1);
```

## Test 3 — iddia 17: üye işlevleri `constexpr` olan sınıf literal tür olmayabilir

```cpp
struct Kayit {
    volatile int v;
    constexpr Kayit() : v{0} { }
    constexpr int bir() const { return 1; }
};

constexpr Kayit kayit_nesnesi;       // sentaks hatası — Kayit literal tür değil
```

## Test 4 — iddia 19: `constexpr` nesnenin `mutable` elemanı değiştirilebilir

```cpp
struct Onbellek { mutable int sayac = 0; };

constexpr Onbellek onbellek{};

void say()
{
    ++onbellek.sayac;                // geçerli: mutable veri elemanı
}
```

## Test 5 — iddia 20: ivedi işlev bağlamındaki çağrı sabit ifade olmak zorunda değildir

```cpp
consteval int kare5(int x) { return x * x; }

consteval int iki_kare(int x)
{
    return kare5(x) + kare5(x);      // kare5(x) sabit ifade değil, ama geçerli
}

template <typename T>
constexpr T sar(T x) { return kare5(x); }   // sar<int> ivedi işleve dönüşür (P2564R3)

static_assert(iki_kare(3) == 18);
static_assert(sar(3) == 9);

int oku5();
int b5 = sar(oku5());                // sentaks hatası — sar<int> ivedi işlev
```

## Test 6 — iddia 24: blok kapsamındaki statik değişken `main`'den önce ilk değer almaz

```cpp
#include <cstdio>

int sayac = 0;
int artir() { return ++sayac; }

int yerel_oku()
{
    static int yerel = artir();     // dinamik ilk değer: denetim ilk geçtiğinde
    return yerel;
}

int main()
{
    std::printf("%d\n", sayac);     // 0
    yerel_oku();
    std::printf("%d\n", sayac);     // 1
}
```
