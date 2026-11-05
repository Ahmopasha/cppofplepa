# Tarama — Cilt I Kısım 2 (Kasım 2026)

Kısım 2'deki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar C++20
(N4861) bölüm adlarıyla; C++23'te (N4950) farklıysa ayrıca. 2.0, 2.4.0 ve 2.4.99 normatif iddia
içermiyor. Kod yorumlarındaki "HATA", "DERLENMEZ", "OK" kitabın "sentaks hatası"/"geçerli"
terimlerine çevrildi (biçim).

**İşlem (2026-11):** "düzeltilmeli", "eksik" ve "gerçekleme" sonuçlu bütün iddialar düzeltildi;
metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-03_c1-02-tarama`, beş tur ve
bir doğrulama turu; kotalar nedeniyle turların çoğu iki hakemle). Panel ayrıca şunları düzeltti:
parametre ve deyim başlığı kapsamları, `const` ve türemiş sınıfla referans bağlama, dönüşüm
işlevleri kaydı (Cilt II 16.1), dizilerin atanamaması, ODR'de `sizeof` ve modül kaydı, terim
tanıtımları. 2.4.4'teki C/C++ kutusu düz metne alındı.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 2.1 | Bildirim ismi tanıtır, tanım varlığı oluşturur; her tanım bildirimdir | [basic.def]/1–2 | doğru |
| 2 | 2.1 | Kod örneği (`extern int x;`, `class Myclass;` …) | [basic.def]/2 | doğru |
| 3 | 2.1 | Bir ismi kullanmak için bildirimini görmek yeterlidir | Nesne oluşturmak ve `sizeof` için tamamlanmış tür gerekir ([basic.def.odr]/12, Kısım 2.6) | eksik |
| 4 | 2.1 | "Başlık dosyalarında bildirimler, kaynak dosyalarda tanımlar bulunur" | Kısım 0.4 sınıf tanımlarını, `inline` işlevleri ve şablonları başlığa koyar | eksik |
| 5 | 2.2 | C'de dört kapsam: dosya, blok, işlev, işlev prototip | C11 6.2.1/2 | doğru |
| 6 | 2.2 | C++ kapsam tablosu | N4861 [basic.scope]: blok, işlev parametresi, işlev, isim alanı, sınıf, numaralandırma, şablon parametresi. N4950'de "işlev kapsamı" yoktur, lambda kapsamı eklenmiştir. Tablo numaralandırma ve şablon parametresi kapsamını atlıyor; "işlev prototip kapsamı" C++'ın terimi değildir | eksik |
| 7 | 2.2 | Gölgelenen isme `::` ile erişilebilir | `::x` yalnızca global isim alanındaki isme erişir; gölgelenen yerel isme erişim yolu yoktur ([basic.lookup.qual]) | eksik |
| 8 | 2.3 | Arama ismin bulunduğu ilk kapsamda durur | [basic.lookup.unqual]/1: "name lookup ends as soon as a declaration is found". İşlev çağrılarında argümana bağlı arama ek adaylar getirebilir (Kısım 16.5) | eksik |
| 9 | 2.3 | Örnek: yerel `func(double)` bildirimi `func(int)`'i gizler | [basic.lookup.unqual], [basic.lookup.argdep]/3 (blok kapsamındaki işlev bildirimi ADL'yi de kapatır) | doğru |
| 10 | 2.3 | İsim arama → yükleme çözümlemesi → erişim denetimi | [class.access]/4 | doğru |
| 11 | 2.4.1, 2.4.5 | `int& b = 10;` ve `int&& d = x;` geçersizdir | [dcl.init.ref]/5 | doğru |
| 12 | 2.4.2 | Bir ifade ya L-Value ya R-Value'dur | [basic.lval]/1 | doğru |
| 13 | 2.4.2 | L-Value'nun adresi alınabilir, ona atama yapılabilir, ismi vardır | `const` L-Value'ya atama yapılamaz; `*ptr` ve yazı sabiti isimsiz L-Value'dur | eksik |
| 14 | 2.4.2 | R-Value, kullanıldığı ifadenin sonunda ortadan kalkar | Geçici nesnenin ömrü referansa bağlanınca uzar ([class.temporary]/6, Kısım 8.3) | eksik |
| 15 | 2.4.2 | "Adresini alabiliyorsanız L-Value'dur" | Pratik yöntem olarak verilmiş; yerleşik `&` L-Value ister ([expr.unary.op]/3) | doğru |
| 16 | 2.4.2 | C'de iki kategori; üçüncüsü taşıma semantiğiyle geldi | C11 6.3.2.1; X-Value C++11 | doğru |
| 17 | 2.4.3 | `std::move(s1)` X-Value'dur; X-Value R-Value'nun alt türüdür | [basic.lval]/1; [forward] | doğru |
| 18 | 2.4.3 | R-Value "ya geçici ya da `std::move` ile işaretlenmiş" | `T&&` döndüren çağrı da X-Value'dur (Kısım 8.6) | eksik |
| 19 | 2.4.4 | İfade listesi (`(x)`, `*ptr`, `++x`, `"Ahmet"` L-Value; `100`, `nullptr`, `x++` R-Value …) | [basic.lval], [expr.prim.paren], [expr.post.incr] | doğru |
| 20 | 2.4.4 | İşlev çağrısının kategorisi: değer döndüren R-Value, "referans döndüren" L-Value | [expr.call]/14: L-Value referans döndüren L-Value, R-Value referans döndüren X-Value | eksik |
| 21 | 2.4.4 | Standart Notu: önek `++`/`--` ve virgül C'de R-Value, C++'ta L-Value | Atama ve koşul operatörü de C'de L-Value değildir (cppreference, C); Kısım 1.7 bunlara atıf veriyor | eksik |
| 22 | 2.4.5 | Bağlama tablosu (`T&`, `const T&`, `T&&`) | [dcl.init.ref]/5 | doğru |
| 23 | 2.4.5 | "Derleyici arka planda geçici bir nesne oluşturur"; "referansın kapsamı bittiğinde" geçici nesnenin ömrü biter | [class.temporary]/2, /6: ömür referansın ömrüne uzar; "kapsam" ve "derleyici" anlatımı kesin değil | gerçekleme |
| 24 | 2.4.5 | "Referans türü ile bağlanacak nesnenin türü aynı olmak zorundadır"; istisnası `const` referanslar | [dcl.init.ref]/5: türemiş sınıf nesnesi taban sınıf referansına bağlanır; farklı türden L-Value'dan `T&&` de geçici nesneye bağlanır (test 1) | düzeltilmeli |
| 25 | 2.4.6 | `const T&` okumak, `T&` değiştirmek, `T&&` devralmak için | Kılavuz | doğru |
| 26 | 2.4.6 | "Bir sınıf türünü değerle geçmek, kopyalama maliyeti getirir" | R-Value argüman taşınır ya da doğrudan kurulur ([class.copy.elision], [dcl.init]/17.6.1) | eksik |
| 27 | 2.4.7 | `std::move` taşıma yapmaz, ifadeyi X-Value olarak işaretler | [forward]/14: `static_cast<remove_reference_t<T>&&>`; işlev adına uygulanınca sonuç L-Value'dur | eksik |
| 28 | 2.4.7 | `str.size(); // 0 döner` | [string.cons]: "str is left in a valid but unspecified state" | düzeltilmeli |
| 29 | 2.4.7 | Standart kütüphane: "geçerlidir ama değeri belirsizdir" | [lib.types.movedfrom]/1: "Unless otherwise specified ... valid but unspecified state"; kitabın terimi "belirtilmemiş" | eksik |
| 30 | 2.4.7 | Üçüncü parti kütüphaneler bu garantiyi vermek zorunda değildir | [lib.types.movedfrom] yalnızca standart kütüphane türleri içindir | doğru |
| 31 | 2.5 | "Standart, derleyiciye ne yapması gerektiğini söylemez"; UB'de "derleyicinin sizi uyarma zorunluluğu yoktur" | [defns.undefined]: standart şart koymaz; öznesi gerçeklemedir | gerçekleme |
| 32 | 2.5 | Üç UB örneği (dizi taşması, `INT_MAX` artışı, ilk değersiz okuma) | [expr.add]/4, [expr.pre]/4, [basic.indet]/2 | doğru |
| 33 | 2.5 | Belirtilmemiş davranış; `f1` ve `f2`'nin sırası | [defns.unspecified], [intro.execution]/10 | doğru |
| 34 | 2.5 | "Aynı derleyici farklı yerlerde farklı seçim yapabilir"; "sonuç derleyiciye göre değişir" | Öznesi gerçeklemedir | gerçekleme |
| 35 | 2.5 | Gerçeklemeye bağlı davranış belgelenir; `sizeof(int)` "4 mü 8 mi" | [defns.impl.defined]; [basic.fundamental]: `int` en az 16 bittir, değer gerçeklemeye bağlıdır | eksik |
| 36 | 2.6 | Tamamlanmış ve tamamlanmamış tür; yapılabilenler ve yapılamayanlar | [basic.types.general]/5, [expr.sizeof]/1, [class.derived]/2 | doğru |
| 37 | 2.6 | "Bir göstericinin boyutu gösterdiği nesneden bağımsızdır" | [basic.compound]: tamamlanmamış türe gösterici tamamlanmış bir türdür; gösterici boyutunun her türde aynı olduğu söylenmez | eksik |
| 38 | 2.6 | İleri bildirim derleme süresini kısaltır | Gerçekleme; "kısalabilir" | gerçekleme |
| 39 | 2.6 | `void` tamamlanamayan bir tamamlanmamış türdür | [basic.fundamental]/13 | doğru |
| 40 | 2.7 | ODR'nin birinci kuralı | [basic.def.odr]/1 | doğru |
| 41 | 2.7 | İkinci kural; "az olursa da çok olursa da bağlayıcı hatası alırsınız" | [basic.def.odr]/10: "no diagnostic required" | gerçekleme |
| 42 | 2.7 | İstisnalar: sınıflar, `inline` işlevler, şablonlar | [basic.def.odr]/13: `inline` değişkenler de dahil | eksik |
| 43 | 2.7 | Tanımlar farklıysa "derleyici de bağlayıcı da uyarı vermez; program sessizce yanlış çalışır" | [basic.def.odr]/13–14: program geçersizdir, tanı istenmez | gerçekleme |
| 44 | 2.8 | "C++11 ve sonrası" ikilik sabit, basamak ayırıcı ve ham yazı sabiti ekledi | İkilik sabit ve basamak ayırıcı C++14 (N3472, N3781), ham yazı sabiti C++11 | eksik |
| 45 | 2.8 | `0b1010` 10'dur; `010` 8'dir | [lex.icon] | doğru |
| 46 | 2.8 | Basamak ayırıcı değeri etkilemez; "nereye koyacağınıza siz karar verirsiniz" | [lex.icon]: tırnak yalnızca iki basamak arasında; `0x'FF` geçersizdir (test 2) | eksik |
| 47 | 2.8 | `long bellek = 4'294'967'296;` | `long` 32 bit olabilir; değer sığmaz ve değişir (test 2) | gerçekleme |
| 48 | 2.8 | Ham yazı sabiti ve ayırıcı | [lex.string] | doğru |

**Sayım:** 48 iddia — 21 doğru, 2 düzeltilmeli, 18 eksik, 7 gerçekleme.

## Test 1 — iddia 24: referans farklı türden nesneye de bağlanabilir

```cpp
struct Taban { };
struct Turemis : Taban { };

Turemis t;
Taban& tr = t;           // geçerli: türemişten tabana

double d = 1.5;
int&& rr = d;            // geçerli: dönüştürülen değeri tutan geçici nesneye
```

## Test 2 — iddia 46 ve 47: basamak ayırıcının yeri; `long`'a sığmayan değer

```cpp
long long bellek = 4'294'967'296;    // her gerçeklemede sığar
int x = 0x'FF;                       // sentaks hatası
```
