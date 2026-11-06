# Tarama — Cilt I Kısım 3 (Kasım 2026)

Kısım 3'teki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar C++20
(N4861) bölüm adlarıyla; C++23'te (N4950) farklıysa ayrıca. 3.0 normatif iddia içermiyor.
3.6'daki iddialar doğru; dosya değişmedi.

**İşlem (2026-11):** "düzeltilmeli", "eksik", "gerçekleme" ve "biçim" sonuçlu bütün iddialar
düzeltildi; metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-05_c1-03-tarama`,
dört tur). Panel ayrıca şunları düzeltti: daraltıcı dönüşümde tamsayıdan gerçek sayıya dönüşüm,
`std::initializer_list` önceliğinin dönüşüm koşulu ve daraltıcı dönüşümle etkileşimi, işlev
parametresinin göstericiye ayarlanması, referans elemanların bileşik tür ilk değerinde
yazılmaması, `public` ve `std::initializer_list` için atıf ve tanım. `std::initializer_list`
kitapta hiçbir yerde anlatılmıyor; Aşama 3 kapsam envanterine bırakıldı.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 3.1 | İlk değer vermenin beş ayrı yazımı vardır | [dcl.init]/15–16, [dcl.init.list]/1: copy-list-initialization (`T x = {...};`) da ayrı bir biçimdir; 3.9 onu `auto x = {1};` ile kullanıyor ama tanıtmıyor | eksik |
| 2 | 3.2 | Yazılmayan ilk değer → default-initialization | [dcl.init]/12 | doğru |
| 3 | 3.2 | Otomatik ömürlü yerleşik türden değişken belirsiz değer tutar; okumak tanımsız davranıştır | [basic.indet]/1–2 (`unsigned char` ve `std::byte` istisnaları bu düzeyde gerekmiyor) | doğru |
| 4 | 3.2 | Statik ömürlü değişkenler önce sıfırlanır | [basic.start.static]/2 | doğru |
| 5 | 3.2 | Sınıf türünde varsayılan kurucu işlev çağrılır; yoksa sentaks hatası | [dcl.init]/7.1. "Varsayılan kurucu işlev" Kısım 12.8'de anlatılıyor; atıf yok | doğru (atıf eksik) |
| 6 | 3.3 | Value-initialization boş küme parantezidir | [dcl.init]/11, [expr.type.conv]/2: `int()` gibi ifadede `()` de value-initialization yapar; değişken tanımında yapmaz (3.8) | eksik |
| 7 | 3.3 | Yerleşik türlerde her zaman sıfırlar; `int* p{}` boş gösterici | [dcl.init]/8.3, /6.1 | doğru |
| 8 | 3.4 | Normal parantezle uygun kurucu işlev seçilir | [dcl.init]/17.6.2 | doğru |
| 9 | 3.5 | Copy-initialization eşittir işaretiyle yazılır | [dcl.init]/15: argüman geçirme, değer döndürme, `throw` ve `catch` da copy-initialization'dır; 3.5'in son paragrafındaki istenmeyen dönüşümlerin çoğu argüman geçirmede olur | eksik |
| 10 | 3.5 | Ortada mutlaka bir kopyalama olmaz | [dcl.init]/17.6.3, 17.6.1 (C++17'den beri geçici nesne oluşmaz) | doğru |
| 11 | 3.5 | Direct-initialization'dan "tek farkı" `explicit` kurucu işlevlerdir | [dcl.init]/17.6.3, [over.match.copy]: dönüşüm işlevleri de farklı ele alınır; fark tek değil | eksik |
| 12 | 3.5 | İstenmeyen dönüşümlere "tek parametreli" kurucu işlevler yol açar | [class.conv.ctor]/1: `explicit` olmayan her kurucu işlev dönüştürendir; tek argümanla çağrılabilmesi yeter (varsayılan argümanlar). 12.13 aynı kısaltmayı kullanıyor | doğru (kısaltma; 12.13 ile tutarlı) |
| 13 | 3.6 | Direct-list-initialization C++11 ile geldi | [dcl.init.list]; C++03'te yalnızca bileşik türler `= {...}` ile | doğru |
| 14 | 3.7 | Küme parantezi "bilgi kaybına yol açan" dönüşümlere izin vermez | [dcl.init.list]/7: daraltıcı dönüşüm tür çiftleriyle tanımlanır; kaynak sabit ifadeyse ve değer sığıyorsa daraltıcı değildir (`char c{65};`, `float f{0.1};` geçerli, ikincisinde bilgi kaybı olduğu hâlde) | eksik |
| 15 | 3.7 | `int b{3.14};` ve `char ch2{1000};` sentaks hatası | [dcl.init.list]/3.9, /7. İkincisi `char`'ın 1000'i tutamamasına bağlıdır (`CHAR_BIT` en az 8) | gerçekleme |
| 16 | 3.7 | `char ch = 1000;` "taşma" | [conv.integral]/3: C++20'de sonuç 2^N modülüne göre belirlidir; "taşma" kitapta işaretli aritmetik taşması (tanımsız davranış) için de kullanılıyor | düzeltilmeli |
| 17 | 3.7 | *narrowing conversion* terimi | Terim tanıtım biçimine uymuyor (sözlükte yok) | biçim |
| 18 | 3.8 | `Myclass mx();` işlev bildirimidir | [dcl.init]/11 Not: `()` ilk değer verme sözdiziminde yer almaz | doğru |
| 19 | 3.8 | "Derleyici belirsizlikte bildirimden yana karar verir"; bu davranışa most vexing parse denir | [dcl.ambig.res]/1: kural dilin kuralıdır. `mx()` aslında belirsizlik çözümü değildir; most vexing parse `Myclass mx(Diger());` türü belirsizliktir. Örnek anlatılanı göstermiyor | eksik |
| 20 | 3.9 | Küme parantezi `std::initializer_list` parametreli kurucu işlevi tercih eder | [over.match.list]/1: boş küme parantezi ve varsayılan kurucu işlev varsa value-initialization yapılır (`std::vector<int> v{};` boş) | eksik |
| 21 | 3.9 | `auto x{1};` `int`, `auto x = {1};` `std::initializer_list<int>` | [dcl.type.auto.deduct]/2 | doğru |
| 22 | 3.9 | "`auto` kullanırken eşittir yazımını tercih edin" | `auto x = {1};` da eşittirlidir; öğüt örneği göstermiyor (4.5: `auto a1 = 10;`) | eksik |
| 23 | 3.10 | "Kullanıcı tanımlı" kurucu işlevi olmayan, veri elemanları `public` yapılar bileşik türdür | [dcl.init.aggr]/1 (C++20): kullanıcının **bildirdiği** kurucu işlev de yeter (`S() = default;` bileşik değildir). Cilt II 16.6 bunu anlatıyor | eksik |
| 24 | 3.10 | Yazılmayan elemanlar value-initialize edilir | [dcl.init.aggr]/5: sınıf içi ilk değeri (Kısım 12.11) varsa ondan, yoksa `{}`'den ilk değer alır | eksik |
| 25 | 3.10 | *aggregate* terimi | Sözlük: "bileşik tür" (Cilt I 3.10); metinde Türkçe terim yok | biçim |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): `float f{0.1};`, `char c3{65};`,
`std::vector<int> v{};` geçerli; `Myclass mx(Diger());` bir işlev bildirimi
(`std::is_function_v`); `explicit Myclass(int)` ile `Myclass a = {10};` sentaks hatası;
`struct M2 { M2() = default; int a; }; M2 m{5};` C++20'de sentaks hatası, C++17'de geçerli.
