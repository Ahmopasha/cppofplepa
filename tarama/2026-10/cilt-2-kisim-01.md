# Tarama — Cilt II Kısım 1 (Ekim 2026)

Kısım 1'deki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar C++23
metninin (N4950, timsong-cpp.github.io/cppwp/n4950) bölüm adları ve paragraf numaralarıyla
verilir; C++17 öncesine ilişkin iddialar için C++11 (N3337) ve C++14 (N4140) metinleri
kullanıldı. Tasarım tavsiyeleri (1.1.6'daki "güvenli varsayılan" gibi) normatif olmadığı
için tabloya alınmadı. Testler `araclar/kod_denetimi.py` ile `-std=c++23` altında derlendi
ve çalıştırıldı.

**İşlem (2026-10):** "düzeltilmeli" ve "eksik" sonuçlu iddialar düzeltildi; iddia 15
(yapılandırılmış bağlamaların `decltype` sonucu) ve iddia 26'nın bit alanı kısmı, dayandıkları
kavramlar kitapta anlatılmadığı için yazar kararıyla dışarıda kaldı. Metinler AI hakem
panelinden geçti (`~/ai-panel/calismalar/2026-10-25_c2-01-tarama`, beş tur). Panel ayrıca
şunları ekletti: statik olmayan üye işlev istisnası (1.1.3), üçlü operatörde dönüşüm
yolları (1.1.3), `void` türünden PR-Value'lar (1.1.5), C++20'de parametrelerin `throw`'da
kapsama girmesi ve `co_return` için Kısım 9.2 atfı (1.1.2), ilk forwarding reference
örneğine `baz` ve `Kap` karşı örnekleri (1.2.1).

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 1.1.1 | "Kimlik" = bellekte bir yere karşılık gelmek, "yani `&` operatörünün operandı olabilmek" | [basic.lval]/1.1: glvalue, değerlendirilmesi bir nesnenin ya da işlevin kimliğini belirleyen ifadedir; [expr.unary.op]/3: `&`'nin operandı **L-Value** olmalıdır. X-Value'nun kimliği vardır (kitabın kendi tablosu) ama adresi alınamaz | düzeltilmeli (test 1) |
| 2 | 1.1.1 | Kategoriler kimlik ve "kaynağı devralınabilir" eksenlerinin kesişiminden doğar; dördüncü göze karşılık gelen kategori yoktur | [basic.lval]/1: glvalue kimliği belirler, X-Value "kaynakları yeniden kullanılabilen" nesneyi belirtir, R-Value = PR-Value ∪ X-Value. İki eksen standardın değil, kategorileri öneren yazının (N3055 dönemi, Stroustrup'un "New Value Terminology" notu) anlatımıdır; tablo standartla tutarlıdır | doğru |
| 3 | 1.1.1 | R-Value = PR-Value ∪ X-Value, GL-Value = L-Value ∪ X-Value; her ifade birincil kategorilerden tam olarak birine aittir | [basic.lval]/1–2 | doğru |
| 4 | 1.1.2 | Her ifadenin iki bağımsız özelliği vardır (tür ve değer kategorisi); ifadenin türü asla referans olamaz | [basic.lval]/2, [expr.type]/1: "referans to T" türündeki ifadenin türü her çözümlemeden önce `T`'ye ayarlanır | doğru |
| 5 | 1.1.2 | `+x` PR-Value'dur | [expr.unary.op]/7: sonuç, argümanın (yükseltilmiş) değeridir | doğru |
| 6 | 1.1.2, 1.2.5 | İsimler L-Value'dur ("`rr` bir isimdir, isimlerin bellekte yeri vardır") | [expr.prim.id.unqual]/3: isim ifadesi, varlık işlev, değişken, yapılandırılmış bağlama, veri elemanı ya da şablon parametre nesnesiyse L-Value'dur; numaralandırıcı ve sınıf türünden olmayan şablon parametresi PR-Value'dur. C++23'te `return`/`co_return` ve `throw` operandı olan, taşınmaya uygun *(move-eligible)* isim ifadesi X-Value'dur ([expr.prim.id.unqual]/3–4, P2266R3) | eksik (test 2) |
| 7 | 1.1.2 | `rr`'nin L-Value olması, `T&&` parametreli işlevlerin gövdesinde `std::move` çağırmak **zorunda** kalmanızın sebebidir | [expr.prim.id.unqual]/4.1: `T&&` parametresi örtük taşınabilir varlıktır; `return r;` yazıldığında `r` X-Value'dur ve `std::move` gerekmez (C++20'de P1825R0 ile kopya yerine taşıma, C++23'te P2266R3 ile doğrudan X-Value) | eksik (test 2) |
| 8 | 1.1.3 | İşlev isimleri her zaman L-Value'dur | [expr.ref]/6.3.2: statik olmayan üye işleve erişen `E1.E2` PR-Value'dur ve yalnızca çağrının sol operandı olarak kullanılabilir; sınıf içinde niteleyicisiz yazılan üye işlev adı da `(*this).f` biçimine dönüşür ([class.mfct.non.static]/2). İfade çağrı dışında kullanılamadığı için test yazılamaz | eksik |
| 9 | 1.1.3 | `T&&` döndüren çağrı X-Value; işleve R-Value referans döndüren çağrı L-Value | [expr.call]/13 | doğru |
| 10 | 1.1.3 | `std::move(moo)` ve `static_cast<void(&&)()>(moo)` L-Value'dur | [expr.static.cast]/1: hedef işleve R-Value referanssa sonuç L-Value; [forward]: `std::move` `remove_reference_t<T>&&` döndürür, [expr.call]/13 | doğru |
| 11 | 1.1.3 | Lambda ifadesi PR-Value'dur | [expr.prim.lambda.general]/2 | doğru |
| 12 | 1.1.3 | `neco.x` L-Value, `Nec{}.x` ve `std::move(neco).x` X-Value, `std::move(neco).sx` L-Value; referans türündeki veri elemanına erişim L-Value | [expr.ref]/6, /6.1, /6.2 (`Nec{}` sınıf PR-Value'su üye erişiminde somutlaşır: [class.temporary]/2.2) | doğru |
| 13 | 1.1.3 | Üçlü operatör, iki operand da L-Value ise L-Value, en az biri R-Value ise R-Value üretir | [expr.cond]/5: L-Value sonucu için iki operandın **aynı türden** glvalue olması gerekir (ya da [expr.cond]/4'teki dönüşümle aynı türe getirilebilmesi); `int` ve `long` L-Value'ları PR-Value verir ([expr.cond]/6). [expr.cond]/2.1: operandlardan biri `throw` ifadesiyse sonuç diğer operandın tür ve kategorisindedir (L-Value olabilir) | eksik (test 3) |
| 14 | 1.1.3 | Virgül operatörünün sonucu sağ operandın kategorisindedir | [expr.comma]/1 (yerleşik operatör) | doğru |
| 15 | 1.1.4 | Parantezsiz isim ya da üye erişiminde `decltype` "ismin bildirildiği türü" verir | [dcl.type.decltype]/1.3; ama /1.1: yapılandırılmış bağlamada sonuç bildirimdeki tür değil, *başvurulan türdür* (`auto& [a, b] = pair` için `decltype(a)` `int`'tir, `int&` değil) | eksik (test 4) |
| 16 | 1.1.4 | Diğer ifadelerde PR-Value → `T`, L-Value → `T&`, X-Value → `T&&`; tablodaki örnekler | [dcl.type.decltype]/1.4–1.6 ve örnek 1 | doğru |
| 17 | 1.1.5 | C++17 öncesinde PR-Value bir nesneyi temsil ederdi | C++11 [basic.lval]/1: R-Value "bir X-Value, geçici nesne ya da alt nesnesi, **ya da bir nesneyle ilişkili olmayan değer**"dir; `12` gibi değişmezler örnek olarak verilir. Nesne belirten PR-Value'lar sınıf türündekilerdi | eksik |
| 18 | 1.1.5 | C++17 ile PR-Value nesne değil, nesneye ilk değer vermenin tarifidir | [basic.lval]/1.2, P0135R1 | doğru |
| 19 | 1.1.5 | "Materialization olmazsa ortada bir nesneden söz edilemez"; Standart Notu: "nesne yalnızca materialization anında oluşur" | [basic.lval]/5: PR-Value'nun *sonuç nesnesi*, ilk değer verdiği nesnedir. [dcl.init.general]/16.6.1: aynı sınıf türünden PR-Value, hedef nesneyi doğrudan kurar; somutlaştırma yoktur ama nesne vardır (değişkenin kendisi). Somutlaştırma ([conv.rval]) yalnızca bir **geçici** nesne gerektiğinde olur | düzeltilmeli (test 5) |
| 20 | 1.1.5 | Somutlaştırma; nesneye ilk değer verirken, parametre olurken, geri dönüş değerini tutarken, atılırken *(discard)* ya da `const T&`/`T&&`'ye bağlanırken olur | [class.temporary]/2: referansı PR-Value'ya bağlama, sınıf PR-Value'sunda üye erişimi, dizi PR-Value'sunda dizi-gösterici dönüşümü ve indisleme, `std::initializer_list` kurma, bazı değerlendirilmeyen operandlar, atılan değer ifadesi. Nesneye, parametreye ve geri dönüş değerine ilk değer vermek **somutlaştırma değildir**: aynı paragrafın örneği "`X(2)`, `f()`'nin argümanını tutan yerde kurulur; `f()`'nin sonucu doğrudan `b`'de kurulur" der | düzeltilmeli (test 5) |
| 21 | 1.1.5 | Örnekte tek `Myclass(int)` çağrısı; kopyalayan kurucu silinmişken geçerli; C++17 öncesinde sentaks hatası | [dcl.init.general]/16.6.1, [dcl.init.list]/3; C++14 [class.temporary]/1: oluşturma önlense bile anlamsal kısıtlar (erişilebilir, silinmemiş kurucu) aranır | doğru |
| 22 | 1.1.5 | Standart Notu: C++17 öncesi eleme isteğe bağlıydı; C++17 ile dilin garantisi oldu | C++14 [class.copy]/31 ("izin verilir"); C++17 [dcl.init]/17.6.1. Not: kopyalanabilir ve sonlandırıcısı trivial olan türlerde işlev argümanı/sonucu için gerçeklemenin geçici nesne oluşturmasına hâlâ izin vardır ([class.temporary]/3); örnekteki `Myclass` bu izne girmez | doğru |
| 23 | 1.1.6 | Dört yüklemeli tercih tablosu ve örnek çıktıları | [dcl.init.ref]/5, [over.ics.rank]/3.2.3 (R-Value'ya R-Value referans bağlamak L-Value referansa üstündür), /3.2.6 (daha az nitelenmiş referans üstündür) | doğru |
| 24 | 1.1.7 | `decltype((e))`'deki iç parantez zorunludur: "onsuz operand isim sayılır" | [dcl.type.decltype]/1.3 yalnızca `e` parantezsiz bir isim ya da üye erişimiyse uygulanır; `x + 5` gibi ifadelerde parantez sonucu değiştirmez. Makro için parantez gerekir, ama gerekçe "e bir isim olabilir" olmalıdır | eksik |
| 25 | 1.2.1 | Forwarding reference "üçüncü bir referans türüdür"; R-Value referansla "davranışları taban tabana zıttır" | [temp.deduct.call]/3: forwarding reference, cv niteleyicisiz şablon parametresine **R-Value referanstır**; farkı yalnızca çıkarım kuralındadır. [dcl.ref]/2: iki referans türü vardır. `T` açıkça verilirse düz R-Value referans gibi davranır | düzeltilmeli (test 6) |
| 26 | 1.2.1, 1.2.7 | `foo(T&&)` her değer kategorisinden ifadeyi kabul eder; `auto&&` "her şeye bağlanabilir" | Bit alanı L-Value'larına bağlanamaz: `T` `int&` çıkarılır ve L-Value referans bit alanına bağlanamaz ([dcl.ref]/5 notu, [class.bit]/3). Küme ilk değer listesinden `T` çıkarılamaz ([temp.deduct.call]/1) | eksik (test 7) |
| 27 | 1.2.1 | Standart metninde adı *forwarding reference*'tır | [temp.deduct.call]/3 (N4164 ile C++17'de) | doğru |
| 28 | 1.2.1 | Forwarding reference yalnızca iki yerde oluşur: çağrıdan çıkarılan şablon parametresi ve `auto` | [temp.deduct.call]/3; [dcl.type.auto.deduct]/3: `auto` çıkarımı, işlev çağrısından şablon argümanı çıkarma kurallarıyla yapılır. (Sınıf şablonu argümanı çıkarımı sırasında sınıf şablonunun parametresi hariçtir) | doğru |
| 29 | 1.2.2 | Referansa referans elle yazılamaz; `typedef`, şablon parametresi ve `decltype` yoluyla oluşursa çöker; çökme tablosu ve kuralı | [dcl.ref]/5–6 (şablon tür parametresi bir *typedef-name*'dir: [temp.param]/3) | doğru |
| 30 | 1.2.3 | Dört argüman için `T` ve `arg` tablosu; L-Value argümanda `T` referans türüne, R-Value'da referanssız çıkarılır | [temp.deduct.call]/3, [dcl.ref]/6 | doğru |
| 31 | 1.2.3 | `T`, argümanın "değer kategorisini" ve `const`luğunu taşır | Yalnızca L-Value/R-Value ayrımı taşınır: PR-Value ile X-Value aynı `T`'yi verir ([temp.deduct.call]/3 yalnızca L-Value'yu ayırır) | eksik (test 8) |
| 32 | 1.2.4 | `T&&` parametreli işleve gönderilebilen her ifade `const T&` parametreli işleve de gönderilebilir | [dcl.init.ref]/5.2: `volatile` nitelenmiş L-Value referans R-Value'ya bağlanamaz; `volatile int` X-Value'su `T&&`'ye gider, `const T&`'ye (`const volatile int&`) gitmez | eksik (test 9) |
| 33 | 1.2.5 | `std::forward<T>`, `T` referans türüne çıkarılmışsa L-Value, değilse R-Value verir | [forward]/3: `static_cast<T&&>(t)` | doğru |
| 34 | 1.2.5 | Mükemmel gönderimde aracı kullanmakla doğrudan çağırmak arasında "hiçbir fark kalmaz" | PR-Value argüman parametreye bağlanırken somutlaşır ([class.temporary]/2.1) ve X-Value olarak iletilir: doğrudan çağrıda zorunlu eleme varken aracıda taşıyan kurucu gerekir ([dcl.init.general]/16.6.1). `0` iletildiğinde artık değişmez değildir, boş gösterici sabiti sayılmaz ([conv.ptr]/1). Küme ilk değer listesi iletilemez ([temp.deduct.call]/1) | düzeltilmeli (test 10) |
| 35 | 1.2.5 | `emplace` argümanları kategorileri ve `const`lukları korunarak kurucuya iletilir | [sequence.reqmts]/22: "`std::forward<Args>(args)...` ile kurulan nesne" | doğru |
| 36 | 1.2.5 | `std::forward`'ın şablon argümanı açıkça yazılmalıdır | [forward]/1: parametre `remove_reference_t<T>&`; iç içe ad belirleyicisindeki `T` çıkarılamayan bağlamdır ([temp.deduct.type]/5.1), yani argümansız `std::forward(arg)` derlenmez. Bu bir tavsiye değil, zorunluluktur | doğru |
| 37 | 1.2.5 | Bir argüman iki kez iletilirse "ikinci kullanımda nesnenin kaynağı çoktan devralınmış olur" | `std::forward` kendisi taşımaz; kaynak yalnızca ilk alıcı taşırsa devralınır ("olabilir"). Taşınan kütüphane nesneleri geçerli ama belirtilmemiş durumdadır ([lib.types.movedfrom]/1) | eksik |
| 38 | 1.2.6 | `const T&&`, `vector<T>&&`, sınıf şablonu parametresiyle `T&&` ve şablon olmayan işlevde `&&` forwarding reference değildir; üye şablonda `U&&` öyledir | [temp.deduct.call]/3 | doğru |
| 39 | 1.2.7 | `auto&& r1 = 31` → `int&&`, `r2 = x` → `int&`, `r3 = cx` → `const int&` | [dcl.type.auto.deduct]/3, [temp.deduct.call]/3, [dcl.ref]/6 | doğru |
| 40 | 1.2.7 | Bazı kaplarda (`vector<bool>`) eleman erişimi vekil nesne döndürür; geçici vekile `auto&` bağlanamaz, `auto&&` bağlanır | [vector.bool.pspc]/4: `reference` tek bir biti temsil eden sınıftır; [dcl.init.ref]/5.2 | doğru |
| 41 | 1.2.7 | `auto&&` değişkeni `std::forward<decltype(r)>(r)` ile iletilir | [dcl.type.decltype]/1.3, [forward]/3 | doğru |

## Önerilen düzeltmeler

- **İddia 1:** "Yani `&` operatörünün operandı olabiliyor mu?" ifadesi çıkarılmalı ya da "L-Value'larda adres alınabilir; X-Value'ların kimliği olduğu hâlde adresi alınamaz" diye sınırlanmalı.
- **İddia 6:** "İsimler L-Value'dur" yerine "değişken ve işlev isimleri L-Value'dur" denmeli; numaralandırıcıların PR-Value olduğu ve C++23'te `return` operandı olan yerel ismin X-Value sayıldığı tek cümleyle eklenmeli.
- **İddia 7:** "`std::move` çağırmak zorunda kalmanız" cümlesine "başka bir işleve aktarırken; `return` deyiminde C++23'ten beri gerekmez" kaydı eklenmeli.
- **İddia 8:** "Her zaman" yerine "statik üye işlevler dahil, nesne üzerinden erişilmeyen işlev isimleri" denmeli; `nesne.uye_islev` ifadesinin PR-Value olduğu not edilmeli.
- **İddia 13:** Kural "iki operand da aynı türden L-Value ise (ya da biri diğerinin türüne L-Value olarak dönüştürülebiliyorsa) L-Value" diye daraltılmalı; `throw` operandı istisnası eklenmeli.
- **İddia 15:** "Bildirildiği tür" kuralına yapılandırılmış bağlamaların istisna olduğu (başvurulan tür) eklenmeli.
- **İddia 17:** "C++17 öncesinde PR-Value bir nesneyi temsil eder" yerine "sınıf türündeki PR-Value'lar geçici bir nesneyi temsil ederdi" denmeli.
- **İddia 19:** "Materialization olmazsa ortada bir nesneden söz edilemez" cümlesi "PR-Value'nun ilk değer verdiği nesneye sonuç nesnesi denir; o nesne bir değişkense somutlaştırma gerekmez, yalnızca geçici bir nesne gerektiğinde somutlaştırma olur" diye değiştirilmeli; Standart Notu'ndaki "yalnızca materialization anında oluşur" ifadesi de buna uydurulmalı.
- **İddia 20:** Somutlaştırma listesi [class.temporary]/2'ye göre yeniden yazılmalı; nesneye, parametreye ve geri dönüş değerine ilk değer verme listeden çıkarılıp "bu durumlarda PR-Value hedef nesneyi doğrudan kurar" denmeli.
- **İddia 24:** Gerekçe "e bir isim ya da üye erişimiyse parantezsiz `decltype` bildirilen türü verir" diye yazılmalı.
- **İddia 25:** "Üçüncü bir tür" ve "taban tabana zıt" ifadeleri yerine "yazılışı ve türü R-Value referanstır; `T`'nin çıkarılma kuralı onu her kategoriye bağlanabilir kılar" denmeli.
- **İddia 26:** "Her değer kategorisinden ifadeyi kabul eder" cümlesine bit alanları ve küme ilk değer listeleri istisna olarak eklenmeli.
- **İddia 31:** "Değer kategorisini" yerine "L-Value mı R-Value mu olduğunu" yazılmalı.
- **İddia 32:** Cümle "pratikte" diye yumuşatılmalı ya da `volatile` R-Value istisnası dipnotla belirtilmeli.
- **İddia 34:** "Hiçbir fark kalmaz" yerine "argümanın türü, `const`luğu ve L-Value/R-Value ayrımı korunur" denmeli; PR-Value'nun X-Value olarak iletilmesi (ek taşıma, zorunlu elemenin kaybı), `0`/`NULL` ve küme ilk değer listesi istisnaları anılmalı.
- **İddia 37:** "Çoktan devralınmış olur" yerine "devralınmış olabilir" yazılmalı.

## Test 1 — iddia 1: X-Value'nun kimliği var ama adresi alınamaz

```cpp
#include <utility>

int main()
{
    int x = 0;
    int&& rx = std::move(x);    // std::move(x) X-Value: rx aynı nesneye bağlanır
    &std::move(x);              // sentaks hatası — & operatörünün operandı L-Value olmalı
    return &rx == &x ? 0 : 1;
}
```

## Test 2 — iddia 6 ve 7: PR-Value isim; `return` operandında X-Value isim

```cpp
enum Renk { kirmizi };

int&& geri_ver(int&& r) { return r; }   // C++23: r burada X-Value, std::move gerekmez

int main()
{
    &kirmizi;                   // sentaks hatası — numaralandırıcı ismi PR-Value'dur
    int n = 1;
    int&& r = geri_ver(static_cast<int&&>(n));
    return r == 1 ? 0 : 1;
}
```

## Test 3 — iddia 13: iki L-Value PR-Value verebilir; `throw` operandı L-Value bırakır

```cpp
#include <type_traits>

int i{};
long l{};
bool kosul = true;

static_assert(std::is_same_v<decltype((kosul ? i : l)), long>);         // iki L-Value, PR-Value sonuç
static_assert(std::is_same_v<decltype((kosul ? i : throw 1)), int&>);   // throw operandı: L-Value sonuç

int main() { }
```

## Test 4 — iddia 15: yapılandırılmış bağlamada `decltype` başvurulan türü verir

```cpp
#include <type_traits>
#include <utility>

std::pair<int, int> cift{1, 2};
auto& [ilk, ikinci] = cift;

static_assert(std::is_same_v<decltype(ilk), int>);   // int& değil

int main() { }
```

## Test 5 — iddia 19 ve 20: PR-Value somutlaşmadan değişkeni ve parametreyi doğrudan kurar

```cpp
#include <cstdio>

struct Kendi {
    Kendi* adres = this;
    ~Kendi() { }                // trivial olmayan sonlandırıcı: [class.temporary]/3 izni yok
};

Kendi uret() { return Kendi{}; }
bool kendisi_mi(Kendi k) { return k.adres == &k; }

int main()
{
    Kendi a = uret();           // ara geçici nesne yok: PR-Value a'yı kurar
    std::printf("%d %d\n", a.adres == &a, kendisi_mi(Kendi{}));   // 1 1
}
```

## Test 6 — iddia 25: `T` açıkça verilince forwarding reference düz R-Value referanstır

```cpp
template<typename T>
void ilet(T&& x) { }

int main()
{
    int n = 0;
    ilet(n);                    // T = int&, parametre int& (çökme)
    ilet<int>(n);               // sentaks hatası — T = int iken parametre int&&, L-Value bağlanmaz
}
```

## Test 7 — iddia 26: forwarding reference'ın bağlanamadığı ifadeler

```cpp
template<typename T>
void kabul(T&& x) { }

struct Bitler {
    int b : 3;
};

int main()
{
    Bitler s{};
    kabul(s.b);                 // sentaks hatası — T = int&, referans bit alanına bağlanamaz
    auto&& r = s.b;             // sentaks hatası — aynı sebep
    kabul({1, 2});              // sentaks hatası — küme ilk değer listesinden T çıkarılamaz
}
```

## Test 8 — iddia 31: PR-Value ile X-Value aynı `T`'yi verir

```cpp
#include <type_traits>
#include <utility>

struct Nesne { };

template<typename T>
void incele(T&&) { static_assert(std::is_same_v<T, Nesne>); }

int main()
{
    Nesne n;
    incele(Nesne{});            // PR-Value: T = Nesne
    incele(std::move(n));       // X-Value: yine T = Nesne
}
```

## Test 9 — iddia 32: `volatile` R-Value `T&&`'ye gider, `const T&`'ye gitmez

```cpp
#include <utility>

template<typename T>
void ileten(T&&) { }

template<typename T>
void sabit_ref(const T&) { }

int main()
{
    volatile int vi = 0;
    ileten(std::move(vi));      // T = volatile int, parametre volatile int&&
    sabit_ref(vi);              // L-Value: geçerli
    sabit_ref(std::move(vi));   // sentaks hatası — const volatile int& R-Value'ya bağlanamaz
}
```

## Test 10 — iddia 34: aracıyla doğrudan çağrı arasındaki farklar

```cpp
#include <utility>
#include <vector>

struct Sabit {
    explicit Sabit(int) { }
    Sabit(Sabit&&) = delete;    // ne kopyalanabilir ne taşınabilir
};

void al(Sabit) { }
void gosterici_al(int*) { }
void liste_al(std::vector<int>) { }

template<typename T>
concept al_iletilebilir = requires(T&& a) { al(std::forward<T>(a)); };

template<typename T>
concept gosterici_iletilebilir = requires(T&& a) { gosterici_al(std::forward<T>(a)); };

template<typename T>
void araci_liste(T&& a) { liste_al(std::forward<T>(a)); }

static_assert(!al_iletilebilir<Sabit>);       // X-Value'dan Sabit kurmak taşıyan kurucuyu ister
static_assert(!gosterici_iletilebilir<int>);  // iletilen 0 int'tir, boş gösterici sabiti değil

int main()
{
    al(Sabit{1});               // doğrudan: zorunlu eleme, geçerli
    gosterici_al(0);            // doğrudan: 0 boş gösterici sabiti, geçerli
    liste_al({1, 2});           // doğrudan: geçerli
    araci_liste({1, 2});        // sentaks hatası — küme ilk değer listesinden T çıkarılamaz
}
```
