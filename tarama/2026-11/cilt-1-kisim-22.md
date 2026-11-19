# Tarama — Cilt I Kısım 22 (Kasım 2026)

Kısım 22'deki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış), **biçim** (terim
tanıtımı, atıf). Kaynaklar C++20 (N4861) bölüm adlarıyla. 22.0 normatif iddia içermiyor.

**İşlem (2026-11):** "düzeltilmeli", "eksik", "gerçekleme" ve "biçim" sonuçlu bütün iddialar
düzeltildi; metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-19_c1-22-tarama`,
üç hakem, beş hakem turu, tur sınırında bitti; uzunluk 460 → 520 brief v2; Claude hakemi
xhigh). Panel ayrıca şunları düzeltti: kuralın örtülü örneklemeyle ve sanal olmayan üye
işlevlerle sınırlanması, parametre ya da dönüş türü geçersizse örneklemenin sentaks hatası
olması (varsayılan argümanlar bildirimle örneklenmez), [temp.pre]/10 hükmünün işlev
şablonu ve üye işlev tanımlarıyla sınırlanması, sınıf şablonunun kendi tanımı için
tamamlanmış tür (Kısım 2.6), açık örneklemenin yeri ve kapsamı ([temp.explicit]/12),
"tür başına" yerine "şablon argümanı bileşimi", adsız paketler, `std::array`'in yalnızca
parametre biçimi ([array.overview]/2: aggregate), terim tanıtımları. Son turda uygulanan
özne düzeltmesi (I-018) hakem turunda sınanmadı.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 22.1 | `typename` ile `class` bu bağlamda aynıdır | [temp.param]/2 | doğru |
| 2 | 22.2 | `enbuyuk("a", "b")` için `T = const char*` | [temp.deduct.call]/2.1 (dizi → gösterici); test | doğru |
| 3 | 22.2 | Argüman türleri farklıysa çıkarım başarısız, `enbuyuk(3, 5.2)` sentaks hatası | [temp.deduct.type]/2; test | doğru |
| 4 | 22.2 | Şablon argüman çıkarımı `auto` kurallarıyla aynı temele dayanır (Kısım 4) | [dcl.type.auto.deduct]/4. Atıf Kısım 4.2'ye daraltılabilir | doğru; biçim (atıf) |
| 5 | 22.3 | "Şablon parametreleri dört gruba ayrılır" (tür, tür olmayan, şablon şablon, parametre paketi) | [temp.param]/1: üç biçim (tür parametresi, şablon şablon parametresi, tür olmayan parametre); /18: paket ayrı bir grup değil, üçünden biri `...` ile bildirilince pakettir (test: `typename...`, `int...`, `template<class> class...`) | eksik |
| 6 | 22.3 | `std::array` tür olmayan parametreyle tanımlanır | [array.overview]: `template<class T, size_t N> struct array` | doğru |
| 7 | 22.4 | C++17'den itibaren kurucu işlev argümanlarından çıkarım; "Bu mekanizmanın adı CTAD'dir" | [over.match.class.deduct]/1; test (`-std=c++14` sentaks hatası, `-std=c++17` geçerli). CTAD'in açılımı verilmiyor (sözlük §1: kısaltmanın açılımı ilk geçişte); atıf Cilt II 4 → 4.7 | doğru; biçim (terim, atıf) |
| 8 | 22.5 | "Buna *instantiation* denir" | Sözlükte "örnekleme", ilk geçiş Cilt II 4.2 yazıyor; tanıtım biçimi `**Türkçe** *(English)*` değil | biçim (terim) |
| 9 | 22.5 | "Yalnızca çağrılan üye işlevler üretilir … hiç derlenmez" | [temp.inst]/3.1: sınıf şablonu örneklenince üye işlevlerin bildirimleri örneklenir, tanımları değil; /4: tanım, var olmasını gerektiren bir bağlamda kullanılınca örneklenir (yalnızca çağrı değil); /11: sanal üye işlevlerde örneklenip örneklenmemesi belirtilmemiş. Test: `std::unique_ptr` ile geçersiz olan çağrılmamış üye işlev hata vermiyor | eksik |
| 10 | 22.5 | "Şablon tanımları başlık dosyasında olmalıdır … Kaynak dosyada tanımlarsanız bağlayıcı hatası alırsınız" | [temp.pre]/10: tanım, örtülü örneklendiği her yerden erişilebilir olmalı, ilgili özelleştirme bir çeviri biriminde açıkça örneklenmedikçe; aksi hâlde program hatalı, tanı gerekmez. "Bağlayıcı hatası" gerçeklemenin tipik tepkisi; açık örneklemeyle kaynak dosyada tanım geçerli (test; Cilt II 4.2) | gerçekleme; eksik |
| 11 | 22.5 | "Şablonlar, birden fazla çeviri biriminde tanımlanabilen üç şeyden biridir (bkz. Kısım 2.7)" | Kısım 2.7 beş tür sayıyor (sınıflar, numaralandırmalar, `inline` işlevler, `inline` değişkenler, şablonlar) | düzeltilmeli |
| 12 | 22.6 | Özelleştirme, değişken sayıda parametre, SFINAE, kavramlar, derleme zamanı hesaplama: "Cilt II, Kısım 4, 5 ve 7" | Derleme zamanı hesaplama Cilt II Kısım 18'de | biçim (atıf) |
| 13 | 22.6 | "Standart kütüphanenin tamamı şablonlardan oluşur" | Şablon olmayan sınıf ve işlevleri de vardır (ör. `std::exception`, `std::mutex`; test: şablon argümanı olmadan nesne tanımlanıyor) | düzeltilmeli |
| 14 | 22.2 | `enbuyuk("a", "b")` "muhtemelen istediğiniz bu değil" | [expr.rel]/4–5: farklı dizilerin göstericileri karşılaştırılınca sonuç belirtilmemiş. Metin bunu iddia etmiyor | doğru |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): bölümdeki kod örnekleri geçerli;
`decltype(enbuyuk("a", "b"))` `const char*`; `enbuyuk(3, 5.2)` sentaks hatası (çatışan
çıkarım `int`/`double`); `Kutu k3{42}` `Kutu<int>`, `-std=c++14`'te sentaks hatası;
`typename...`, `int...`, `template<class> class...` paketleri geçerli; `T kopya() const`
üyesi `std::unique_ptr<int>` için geçersizken çağrılmadığında `Kutu<std::unique_ptr<int>>`
geçerli; şablon tanımı yalnızca bir kaynak dosyadayken başka çeviri biriminden çağrı
bağlamada başarısız, aynı kaynak dosyaya `template int kare<int>(int);` eklenince çalışıyor.

Not (Cilt II Kısım 4 taraması için): 4.1'in başlığı ve yapısı "dört grup" (parametre
paketi ayrı grup); [temp.param]/18'e göre paket ayrı bir tür değil. Cilt I 22.3 düzeltmesiyle
uyumlandırılmalı.
