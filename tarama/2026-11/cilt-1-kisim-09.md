# Tarama — Cilt I Kısım 9 (Kasım 2026)

Kısım 9'daki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar C++20
(N4861) bölüm adlarıyla; C++23'te (N4950) farklıysa ayrıca. 9.0 ve 9.99 normatif iddia
içermiyor.

**İşlem (2026-11):** "düzeltilmeli", "eksik", "gerçekleme" ve "biçim" sonuçlu bütün iddialar
ile atıf eksikleri düzeltildi; metinler AI hakem panelinden geçti
(`~/ai-panel/calismalar/2026-11-07_c1-09-tarama`, beş tur). Panel ayrıca şunları düzeltti:
erişilemeyen yüklemenin koşulu, kullanıcı tanımlı dönüşümün kütüphane sınıflarını da kapsaması,
yükseltmenin genel kuralı, çok adaylı durumda kazanma koşulu, `extern "C" { #include }`
kalıbı, blok biçiminin kapsamı. Aynı sıradaki dönüşümleri ayıran kurallar ve "bağlantı"
(linkage) kavramı kitapta anlatılmıyor; Aşama 3 kapsam envanterine bırakıldı.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 9.1 | Aynı kapsamda, aynı isimli, farklı imzalı işlevler yüklemedir | [over]/1. Terim tanıtım biçimine uymuyor (kalın değil) | doğru (biçim) |
| 2 | 9.1 | Farklı kapsamlardaki aynı isimli işlevler yükleme değildir; dıştaki gölgelenir | [basic.lookup.unqual]/1, [basic.scope.hiding] | doğru |
| 3 | 9.2 | İmza: isim, parametre türleri; geri dönüş türü imzada değil | [defns.signature]: isim alanı da imzanın parçasıdır; [defns.signature.templ]: işlev şablonlarında geri dönüş türü imzanın parçasıdır | eksik |
| 4 | 9.2 | Üye işlevlerde `const`luk ve referans niteleyicisi imzada | [defns.signature.member]. `const` üye işlev Kısım 12.7'de, referans niteleyicisi Cilt II 16.2'de; atıf yok | doğru (atıf eksik) |
| 5 | 9.2 | Yalnızca geri dönüş türü farklı iki bildirim sentaks hatası | [over.load]/2 (C++20 [basic.scope]/[over]) | doğru |
| 6 | 9.2 | Değer parametresindeki üst düzey `const` yok sayılır; ikinci tanım sentaks hatası | [dcl.fct]/5, [basic.def.odr]/1 | doğru |
| 7 | 9.2 | Referansta ve gösterilen nesnede `const` imzanın parçası | [dcl.fct]/5 | doğru |
| 8 | 9.3 | "Derleyici şu sırayı izler" | Sıra standardın kuralıdır ([class.access]/4); öznenin "derleyici" olması | biçim |
| 9 | 9.3 | İsim arama, o kapsamdaki aynı isimli bütün işlevleri listeler | Argümana bağlı arama ek adaylar getirir ([basic.lookup.argdep]); Kısım 2.3 bunu Kısım 16.5'e atıfla söylüyor | eksik |
| 10 | 9.3 | `private` yükleme seçilirse başka yükleme denenmez; "hata verir" | [class.access]/4. `private` Kısım 12.3'te; atıf yok. Kitabın terimi "sentaks hatası" | doğru (atıf ve biçim) |
| 11 | 9.4 | Uygun aday: "Bu işlev tek başına olsaydı, bu çağrı geçerli olur muydu?" | [over.match.viable]/2–3: argüman sayısı ve her argüman için örtülü dönüşüm dizisi. Erişim ve silinmiş işlevler uygunluğu etkilemez — soru, uygunluktan geniş | eksik |
| 12 | 9.4 | *uygun adaylar* terimi; "çift anlamlılık" | Terim tanıtım biçimine uymuyor; "çift anlamlılık" (ambiguity) tanıtılmıyor, sözlükte yok | biçim |
| 13 | 9.4 | Hata mesajı "eşleşen işlev yok" biçimindedir | Derleyicinin tanı metni standardın konusu değil; standart yalnızca programın sentaks hatası olduğunu söyler ([over.match.best]/2) | gerçekleme |
| 14 | 9.5 | Standart > kullanıcı tanımlı > `...` dönüşüm dizisi; sıra kesin | [over.ics.rank]/2 | doğru |
| 15 | 9.5 | Kullanıcı tanımlı dönüşüm: dönüştüren kurucu işlev veya tür dönüştürme operatör işlevi (bkz. Kısım 12.13) | Tür dönüştürme operatör işlevleri Cilt I'de anlatılmıyor (Cilt II 16.1) | doğru (atıf eksik) |
| 16 | 9.5 | "Aynı kategoriden birden fazla aday varsa çift anlamlılık hatası oluşur" | Yanlış: aynı kategoride kategori içi sıraya bakılır ([over.ics.rank]/3; Kısım 9.6 bunu anlatıyor) — `k(int)`/`k(short)` ile `k('a')` geçerli | düzeltilmeli |
| 17 | 9.6 | Tam uyum > yükseltme > sıradan dönüşüm | [over.ics.scs]/3, Tablo 17 | doğru |
| 18 | 9.6 | Tam uyuma dahil: dizi isminin çürümesi, işlev isminin dönüşümü, `const` eklenmesi | [over.ics.scs] Tablo 17. Kısım 4.3 "dizi" diyor (isim değil, ifade); "çürüme" orada tanıtıldı | doğru (tutarlılık) |
| 19 | 9.6 | Yükseltme: `char`, `short`, `bool` → `int`; `float` → `double` | [conv.prom]/1, /6, [conv.fpprom] | doğru |
| 20 | 9.6 | Sıradan dönüşüm örnekleri, türetilmiş → taban sınıf göstericisi | [conv.ptr]/3. Kalıtım Kısım 17'de; atıf yok | doğru (atıf eksik) |
| 21 | 9.6 | `0` hem tamsayı hem gösterici; `nullptr` belirsizliği kaldırır | [conv.ptr]/1, [lex.nullptr]. `g(int)`/`g(char*)` ile `g(0)` geçerli (tam uyum); `h(long)`/`h(char*)` ile `h(0)` çift anlamlı | doğru |
| 22 | 9.7 | Kazanmak için hiçbir parametrede kötü olmamak ve en az birinde iyi olmak | [over.match.best]/2 | doğru |
| 23 | 9.7 | "İkisi de sağlanmıyorsa çift anlamlılık" | Mantık hatası: koşullardan biri sağlanmasa da kazanılamaz; doğrusu "hiçbir aday iki koşulu birlikte sağlamıyorsa" | düzeltilmeli |
| 24 | 9.7, 9.8 | Kod yorumları "çift anlamlılık" | Kitabın terimi "sentaks hatası: çift anlamlılık" (Kısım 7.3) | biçim |
| 25 | 9.8 | "Varsayılan argüman kullanımı yüklemeyi tetikler"; "imzanın parçası olmadığı için iki işlev de çağrılabilir" | Kısım 7.3'te düzeltilen iki yanlışın aynısı (tarama/2026-11/cilt-1-kisim-07.md, 7 ve 9) | düzeltilmeli |
| 26 | 9.9 | Yükleme, "C++ derleyicisinin" isimleri imzayla kodlaması sayesinde mümkündür (name mangling); C'de bu kodlama yapılmaz | Standart isim kodlamasından söz etmez, dil bağlantısını *(language linkage)* tanımlar ([dcl.link]); kodlama gerçeklemenin yöntemidir | gerçekleme |
| 27 | 9.9 | `extern "C"` bildirilen işlevler yüklenemez | [dcl.link]/6: belli bir isimde C dil bağlantılı en fazla bir işlev olabilir; ama C++ bağlantılı yüklemeleri olabilir (`extern "C" void f(int); void f(double);` geçerli) | eksik |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): `extern "C" void f(int); void
f(double);` geçerli, iki `extern "C" f` sentaks hatası; `g(int)`/`g(char*)` ile `g(0)`
geçerli; `h(long)`/`h(char*)` ile `h(0)` çift anlamlı; `k(int)`/`k(short)` ile `k('a')`
geçerli (yükseltme kazanır).
