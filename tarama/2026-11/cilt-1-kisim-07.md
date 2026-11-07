# Tarama — Cilt I Kısım 7 (Kasım 2026)

Kısım 7'deki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar C++20
(N4861) bölüm adlarıyla; C++23'te (N4950) farklıysa ayrıca. 7.0 normatif iddia içermiyor.

**İşlem (2026-11):** "düzeltilmeli", "eksik" ve "biçim" sonuçlu bütün iddialar düzeltildi;
metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-06_c1-07-tarama`, beş tur).
12 numaralı iddia panelde genişledi: N4861 [basic.def.odr]/1, /13, /15 varsayılan argümanı
ODR'ye tabi tanım sayar; `inline` olmayan işlevler için bu kural C++17'de (N4659
[basic.def.odr]/6) yoktu — 7.4'e Standart Notu — C++20 açıldı. Değişikliğin gerekçesi
doğrulanamadı; yazar kararıyla gerekçe satırı yazılmadı.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 7.1 | Varsayılan argümanı olan parametrenin argümanı yazılmayabilir | [dcl.fct.default]/1 | doğru |
| 2 | 7.1 | "Aynı işi iki yükleme yazarak da yapabilirdiniz" | İşlev yüklemesi Kısım 9'da anlatılıyor; atıf yok | doğru (atıf eksik) |
| 3 | 7.2 | Varsayılan argümanlı parametreden sonrakilerin de varsayılan argümanı olmalı | [dcl.fct.default]/4: "in this or a previous declaration"; parametre paketi istisnası. Önceki bildirimle birikme Cilt I için ayrıntı — basitleştirme olarak kabul | doğru (basitleştirme) |
| 4 | 7.2 | `f1(1, , 30);` "böyle bir yazım yok" | Sentaks hatası; kitabın terimi | biçim |
| 5 | 7.2 | Varsayılan argümanı hem bildirimde hem tanımda yazmak sentaks hatası | [dcl.fct.default]/4: "shall not be redefined by a later declaration (not even to the same value)" — aynı kapsamda | doğru |
| 6 | 7.2 | "Yeri bildirimdir; yani başlık dosyası" | Kural değil öğüt: varsayılan argüman çağrı yerinde görülen bildirimden alınır ([dcl.fct.default]/4); gerekçe söylenmiyor | eksik |
| 7 | 7.3 | "Varsayılan argüman işlev yüklemesini tetikler" | Yükleme iki bildirimden doğar, varsayılan argümandan değil ([over]/1) | düzeltilmeli |
| 8 | 7.3 | `func(5);` "çift anlamlılık hatası" | [over.match.best]/2: çağrı geçersizdir — kitabın terimi "sentaks hatası" | biçim |
| 9 | 7.3 | "Varsayılan argümanlar imzanın parçası olmadığı için iki işlev de tek argümanla çağrılabilir" | Neden-sonuç ters: imzalar farklı olduğu için iki bildirim birlikte var olabilir; ikisinin de uygun aday olmasının nedeni varsayılan argümandır ([over.match.viable]/2.3) | düzeltilmeli |
| 10 | 7.4 | Varsayılan argüman çağrı yerinde, statik türe göre seçilir; sanal işlevde tuzak | [dcl.fct.default]/10. "Çalışma zamanında değil" ifadesi argümanın değerinin de derlemede hesaplandığı izlenimini veriyor: değer her çağrıda hesaplanır ([dcl.fct.default]/9) | eksik |
| 11 | 7.4 | Varsayılan argüman eklemek/çıkarmak imzayı değiştirmez | [defns.signature] | doğru |
| 12 | 7.4 | Farklı başlıklarda farklı varsayılan argüman → farklı davranış | `inline` olmayan işlev için doğru. `inline` işlevde farklı çeviri birimlerindeki biriken varsayılan argümanlar aynı olmalıdır (cppreference "Default arguments"; ODR, [basic.def.odr]/13) | eksik |

Ayrıca: Kısım 9.8, 7.3'ün neredeyse aynı metnini (aynı 7, 9 numaralı sorunlarla) taşıyor;
Kısım 9 taramasında 7.3'ün son hâline göre düzeltilecek.

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): `void f(int, int = 2); void f(int =
1, int);` sonrasında `f();` geçerli; `void g(int=1); void g(int=1){}` sentaks hatası
(varsayılan argüman yeniden tanımlanamaz).
