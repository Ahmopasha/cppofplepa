# Tarama — Cilt I Kısım 12 (Kasım 2026)

Kısım 12'deki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar C++20
(N4861) bölüm adlarıyla; C++23'te (N4950) farklıysa ayrıca. 12.0 normatif iddia içermiyor.
Kısım iki panelde işlendi: A (12.1–12.9) ve B (12.10–12.18).

**İşlem (2026-11):** "düzeltilmeli", "eksik", "gerçekleme" ve "biçim" sonuçlu bütün iddialar
düzeltildi; metinler iki AI hakem panelinden geçti
(`~/ai-panel/calismalar/2026-11-11_c1-12a-tarama`, beş tur;
`~/ai-panel/calismalar/2026-11-12_c1-12b-tarama`, dört tur). B panelinin 3. turundan
itibaren Claude hakemi xhigh eforla çalıştı. Panel ayrıca şunları düzeltti: `protected`
erişimi, `private` öğenin reddinin koşulu, `const` üye işlev kuralının kapsamı, açık
sonlandırıcı çağrısında ömür, sanal sonlandırıcı koşulu (Kısım 17.7 ile), `const` eleman
kuralı, dönüştüren kurucu işlevin `explicit(false)`'u da kapsaması, aggregate olmayan
sınıflarda `{}` ile geçici nesne oluşabilmesi. Türemiş sınıfın `protected` erişimi kitapta
anlatılmıyor (Aşama 3 kapsam envanteri); "taban sınıf" ve "türemiş sınıf" terimleri Kısım 17.1
taramasında tanıtılacak. 12.3'ün eski ikinci paragrafı yeni ilk paragrafla yinelendiği için
kaldırıldı; 12.8'deki kod yorumu kod denetimiyle uyumlu olacak biçimde yazıldı.

## A — 12.1–12.9

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 12.1 | `class` ile `struct`'ın tek farkı varsayılan erişim; kalıtımda da | [class.access]/2, [class.access.base]/2. Atıf "bkz. 17.2" biçimi | doğru (biçim) |
| 2 | 12.2 | Sınıf bloğu "üç tür öğe barındırır" | [class.mem]: `friend` bildirimleri, `using` bildirimleri, `static_assert`, üye şablonları da üyelik bildirimleridir — liste kapalı değil | eksik |
| 3 | 12.3 | `private` ve `protected` öğelere sınıf dışından erişilemez | [class.access]/1. `friend` istisnası (Kısım 12.16) söylenmiyor. "Erişim belirleyicisi" terimi tanıtılmıyor, sözlükte yok | eksik |
| 4 | 12.3 | Veri elemanları `private`, arayüz `public` | Öğüt | doğru |
| 5 | 12.4 | İsmin sınıf kapsamında aranmasını sağlayan "üç durum": `.`, `->`, `::` | Sınıfın içinden (üye işlev gövdesi, kurucu işlev ilk değer verme listesi, sınıf içi ilk değer) de sınıf kapsamında aranır ([basic.lookup.unqual]/8); "sınıfın dışından" nitelemesi eksik | eksik |
| 6 | 12.4 | "Derleyici Kısım 2.3'teki sırayı uygular": isim arama, "bağlam denetimi", erişim kontrolü | Kısım 2.3 ve 9.3'teki ikinci aşama yükleme çözümlemesidir; "bağlam denetimi" diye bir aşama yok. Öznenin "derleyici" olması | düzeltilmeli |
| 7 | 12.4 | Üye işlev gövdesinde isim "önce sınıf kapsamında" aranır | [basic.lookup.unqual]/8: önce işlevin blok kapsamı (yerel değişkenler, parametreler), sonra sınıf (taban sınıflar dahil), sonra dış kapsamlar. 12.6'nın örneği de parametrenin veri elemanını gölgelediğini gösteriyor | düzeltilmeli |
| 8 | 12.4 | `private` isim aramada bulunur, erişimde reddedilir; dıştaki ismi gölgeler | [class.access]/4 | doğru |
| 9 | 12.4 | Hata mesajı "böyle bir isim yok" değil "bu isme erişemezsiniz" olur | Derleyicinin tanı metni standardın konusu değil | gerçekleme |
| 10 | 12.4 | Üye işlevler sınıf bloğunda "`redeclare` edilemez" | [class.mem]/5. İngilizce sözcük terim biçimine uymuyor | doğru (biçim) |
| 11 | 12.5 | Sınıf içinde tanımlanan üye işlev örtülü `inline` (bkz. Kısım 11) | [class.mfct]/1; modül istisnası Kısım 11.3'te anlatılıyor — atıf 11.3'e gitmeli | doğru (atıf) |
| 12 | 12.5 | Bildirimi yapılmamış üye işlev sınıf dışında tanımlanamaz | [class.mfct]/1 | doğru |
| 13 | 12.6 | Her `static` olmayan üye işlev nesnenin adresini "gizli bir parametre olarak alır" | [expr.prim.this]/1, [class.this]/1: `this`'in değeri nesnenin adresidir; nasıl geçirildiği gerçeklemenin işi | gerçekleme |
| 14 | 12.6 | `this`'in türü `Myclass*` / `const Myclass*` | [class.this]/1 | doğru |
| 15 | 12.7 | `const` üye işlevde veri elemanları değiştirilemez | [class.this]/1. `mutable` istisnası (Kısım 12.15) söylenmiyor | eksik |
| 16 | 12.7 | `const` nesne üzerinden yalnızca `const` üye işlevler çağrılabilir | [over.match.funcs]/4–5 (`static` üye işlevler de çağrılabilir; basitleştirme) | doğru |
| 17 | 12.7 | Blok yorum biçimi (`/*` ardından `* `) | Kitabın biçimi ` * ` | biçim |
| 18 | 12.7 | `const` ve `const` olmayan sürümler birlikte bildirilebilir | [over.load], Kısım 9.2 | doğru |
| 19 | 12.8 | Kurucu işlev: sınıfla aynı isim, geri dönüş türü yok, `static` olamaz | [class.ctor]/1, /9 | doğru |
| 20 | 12.8 | "Nesne oluşturulurken derleyici çağırır" | Öznenin "derleyici" olması | biçim |
| 21 | 12.8 | Bir kurucu işlev bildirilince varsayılan kurucu işlev örtülü bildirilmez | [class.default.ctor]/1 | doğru |
| 22 | 12.8 | Kod yorumu "derlenmez" | Kitabın terimi "sentaks hatası" | biçim |
| 23 | 12.9 | Sonlandırıcı işlev: `~`, parametresiz, geri dönüş türsüz, `static` olamaz, tek | [class.dtor]/1–4 (C++20 olası sonlandırıcılar ayrıntı) | doğru |
| 24 | 12.9 | Açıkça çağırmak kötü alışkanlık; ikinci çağrı tanımsız davranış | [class.dtor]/18. Meşru kullanımı (yerinde oluşturulan nesneler, Cilt II 17.3) söylenmiyor | eksik |
| 25 | 12.9 | Sonlandırıcı yazmanız gereken durum kaynak yönetimidir; "Kısım 13'teki Big-Five" | Çok biçimli taban sınıfın sanal sonlandırıcısı (Kısım 17.7) da bir sebeptir; atıf 13.8'e gitmeli | eksik |

## B — 12.10–12.18

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 26 | 12.10 | Veri elemanları bildirim sırasına göre ilk değer alır; "derleyici genellikle uyarır" | [class.base.init]/13.3. Derleyici uyarısı standardın konusu değil | gerçekleme |
| 27 | 12.10 | Listede olmayan ve gövdede değer atanmayan veri elemanı "ilk değer almamış kalır" | [class.base.init]/9: sınıf içi ilk değeri varsa ondan, yoksa default-initialization ile ilk değer alır (sınıf türleri varsayılan kurucu işlevle); yalnızca yerleşik türlerde değer belirsiz kalır; gövdedeki atama ilk değer verme değildir | düzeltilmeli |
| 28 | 12.10 | Referans ve `const` veri elemanları "yalnızca bu listede" ilk değer alabilir | Sınıf içi ilk değer de verilebilir ([class.mem]/10, Kısım 12.11) | eksik |
| 29 | 12.11 | *default member initializer* | Terim Kısım 3.10'da "sınıf içi ilk değer" olarak tanıtıldı (sözlük); burada yalnızca İngilizce | biçim |
| 30 | 12.12 | Devreden kurucu işlev C++11; "devretme" | [class.base.init]/6. "Devretme" ve "devreden kurucu işlev" terim biçimiyle tanıtılmıyor | doğru (biçim) |
| 31 | 12.12 | Devretme listenin tek öğesi; kod yorumu "hata" | [class.base.init]/6. Kitabın terimi "sentaks hatası" | biçim |
| 32 | 12.12 | Devreden kurucu işlevin gövdesinde "hata oluşursa" sonlandırıcı çağrılır | [except.ctor]/4: gövdeden bir hata gönderilerek çıkılırsa. "Hata" burada istisna; Kısım 18 atfı yok | eksik |
| 33 | 12.12 | Devretme döngüsü "derleyicinin bildirmek zorunda olmadığı hata" | [class.base.init]/6: "ill-formed, no diagnostic required". Kitabın kalıbı "program hatalıdır; standart, gerçeklemenin bunu bildirmesini istemez"; özne "derleyici" | biçim |
| 34 | 12.12 | "Sınıf içi ilk değer verme yalnızca değer atar, kod çalıştırmaz" | Sınıf içi ilk değer atama değil ilk değer vermedir ve herhangi bir ifade (işlev çağrısı dahil) olabilir ([class.mem]/10) | düzeltilmeli |
| 35 | 12.13 | "Tek parametreli" kurucu işlevler örtülü dönüşüm sağlar; dönüştüren kurucu işlev | [class.conv.ctor]/1: `explicit` olmayan her kurucu işlev; örtülü dönüşüm için tek argümanla çağrılabilmesi yeter (varsayılan argümanlar). Terim tanıtım biçiminde değil | eksik |
| 36 | 12.13 | `explicit` ile `func(12)` ve `Myclass m = 20;` sentaks hatası, `Myclass m2{20};` geçerli | [over.match.copy], [dcl.init]/17.6.3 | doğru |
| 37 | 12.13 | Öğüt kutusu: "sessizce derlenmesine" | Kitabın terimi "geçerli" | biçim |
| 38 | 12.14 | `static` veri elemanı sınıfa aittir | [class.static.data]/1 | doğru |
| 39 | 12.14 | Sınıf içinde ilk değer: `const` tamsayı istisnası; C++17 `inline` | [class.static.data]/4: `constexpr` `static` veri elemanları da (C++17'den beri örtülü `inline`, Kısım 11.4) | eksik |
| 40 | 12.14 | `static` üye işlevler "gizli `this` parametresi almaz" | [class.static.mfct]/2: `this` göstericisi yoktur; "gizli parametre" gerçekleme ayrıntısı (Kısım 12.6) | gerçekleme |
| 41 | 12.14 | `static` olmayan veri elemanlarına erişemez, `static` olmayan üye işlev çağıramaz | Bir nesne belirtilirse erişebilir (`nesne.x`); yasak nesne belirtmeden kullanım içindir ([class.mfct.non-static]/2) | eksik |
| 42 | 12.14 | Aynı parametreli `static` ve `static` olmayan üye işlev birlikte bildirilemez | [over.load]/2.1 | doğru |
| 43 | 12.15 | `mutable` | [dcl.stc]/10 | doğru |
| 44 | 12.16 | `friend` bildiriminin yeri önemsiz; erişim belirleyicileri etkilemez | [class.friend]/9 | doğru |
| 45 | 12.16 | Sınıf içinde `friend` bildirilen işlev ADL ile "bulunabilir hâle gelir" | [namespace.memdef]/3 (C++20 [basic.lookup.argdep]): yalnızca sınıf içinde bildirilmişse sıradan aramayla bulunmaz, yalnızca ADL ile bulunur. Atıf Kısım 16.5 | eksik |
| 46 | 12.17 | Geçici nesneler "derleyicinin kendiliğinden oluşturması" ya da programcının istemesiyle oluşur | Özne "derleyici"; dilin kuralı ([class.temporary]/2) | biçim |
| 47 | 12.17 | Geçici nesne oluşturan ifadeler PR-Value'dur; `const` olmayan "sol taraf referanslarına" bağlanamaz | [basic.lval], [dcl.init.ref]/5. C++17'den beri PR-Value gerektiğinde geçici nesneye dönüşür (Cilt II 1.1.5); kitabın terimi "L-Value referans" | eksik |
| 48 | 12.17 | Geçici nesne "derleyiciye eliminasyon imkânını verir" | C++17'den beri PR-Value ile ilk değer vermede kopya oluşmaz (zorunlu); "imkân" ve özne | eksik |
| 49 | 12.18 | *nested types* veya *member types* | Sözlük: tür üyesi / içsel tür (Cilt I 12.2, 12.18); terim biçimi | biçim |
| 50 | 12.18 | İçsel tür erişim kontrolüne tabidir | [class.access]/1 | doğru |
