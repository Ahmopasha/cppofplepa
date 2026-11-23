# Tarama — Cilt I Kısım 26 (Kasım 2026)

Kısım 26'daki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış), **biçim** (terim
tanıtımı, atıf). Kaynaklar C++20 (N4861) bölüm adlarıyla. 26.0 normatif iddia içermiyor;
26.6'daki iddialar doğru. "Akım" *(stream)*, "tampon" *(buffer)*, "manipülatör"
*(manipulator)* ve "yazı akımı" *(string stream)* terimleri tanıtılmıyor ve sözlükte yok
(biçim). Kütüphane adları metinde kimi yerde `std::` öneksiz (`getline`, `setw`, `endl`;
şemadaki adlar şema içi).

**İşlem (2026-11):** "düzeltilmeli", "eksik", "gerçekleme" ve "biçim" sonuçlu bütün iddialar
düzeltildi; metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-21_c1-26-tarama`,
üç hakem, beş hakem turu; tur sınırında bitti; uzunluk 500 brief v2). Panel ayrıca şunları
düzeltti: `eofbit` cümlesinin yönü (kurulu olmaması sonraki okumanın başarısını göstermez),
`badbit` satırının çıktıyı da kapsaması, `std::setw`'in uygulandığı işlemlerin `>>` ile
`std::string` ve `char` dizisi okumasıyla sınırlanması (sayı okuması kullanmaz), "alan
genişliği" teriminin tanıtılması. Son turda uygulanan bir madde (`char` dizisi) hakem
turunda sınanmadı; test kodla doğrulandı.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 26.1 | "Akım sınıfları bir kalıtım hiyerarşisidir ve hepsi sınıf şablonudur" | [ios.base] sinopsis: `class ios_base {` — şablon değil; şemanın tepesinde duruyor | düzeltilmeli |
| 2 | 26.1 | `std::ostream` `basic_ostream<char>`'ın eş ismi; `std::cout` bu türden | [iosfwd.syn]; [iostream.syn] `extern ostream cout;` | doğru |
| 3 | 26.1 | "Dört standart akım nesnesi vardır: `std::cin`, `std::cout` (çıkış, tamponlu), `std::cerr` (hata, tamponsuz), `std::clog` (hata, tamponlu)" | [iostream.syn]: sekiz nesne (`wcin`, `wcout`, `wcerr`, `wclog` dahil). [narrow.stream.objects]/3: `cout` `stdout`'a bağlı bir tampona yazar, tamponlama söylenmez (C'nin `stdout` kuralına bağlı); /5: `cerr`'de `unitbuf` kurulu (her çıkıştan sonra boşaltılır) ve `cerr.tie()` `&cout`; /6: `clog` için ikisi de yok. Test | eksik; gerçekleme |
| 4 | 26.1 | `std::ostream&` parametreli işlev dosya ve yazı akımlarıyla da çalışır | [ofstream], [ostringstream] `basic_ostream`'den türer; test (bölüm kodu) | doğru |
| 5 | 26.2 | `<<` ve `>>` biçimli işlem; zincirleme akımı referansla döndürmekten | [istream.formatted], [ostream.formatted]; Kısım 14.5 | doğru |
| 6 | 26.2 | "`>>` operatörü boşluk karakterlerini atlar ve boşluğa kadar okur" | [istream.sentry]/2: `skipws` kuruluysa (varsayılan) baştaki boşluklar atlanır. "Boşluğa kadar" yalnızca `std::string` için doğru; sayı okurken sayının parçası olamayan ilk karakterde durur ([facet.num.get.virtuals]) | eksik |
| 7 | 26.2 | `>>` sonrası kalan satır sonu `getline`'a boş satır okutur; "`std::cin.ignore()` ile temizlenir" | [istream.unformatted]/25: `ignore(streamsize n = 1, int_type delim = eof)` — varsayılanla tek karakter atar. Test: girdi "5␠␠⏎merhaba" iken `ignore()` sonrası `getline` "␠" okuyor. Satırın kalanını atmak için `ignore(std::numeric_limits<std::streamsize>::max(), '\n')` | eksik |
| 8 | 26.3 | "Her akım, dört durum bitini taşır" (`goodbit` dahil) | [ios.iostate]/2: "goodbit, the value zero" — bit değil, hiçbir bitin kurulu olmamasıdır; bitler üç: `badbit`, `eofbit`, `failbit` | düzeltilmeli |
| 9 | 26.3 | Tablo: `failbit` "Biçimsel hata; okuma başarısız oldu", `eofbit` "Dosya sonuna gelindi" | [ios.iostate] Tablo 118: `failbit` çıkış işleminin başarısızlığını da kapsar; `eofbit` girdi dizisinin sonu (yalnızca dosya değil) | eksik |
| 10 | 26.3 | `bool` bağlamı: `failbit` ya da `badbit` kuruluysa yanlış | [iostate.flags]/1 (`!fail()`), /9 | doğru |
| 11 | 26.3 | `eof()` döngüsünde "son eleman iki kez işlenir"; "`eofbit`, okuma başarısız olduktan sonra kurulur" | [istream.sentry]/2: boşluk atlarken girdi biterse `failbit | eofbit`, değer değişmez. Girdi son sayıdan sonra boşlukla (satır sonu) bitiyorsa son eleman iki kez işlenir (test: "1 2 3⏎" → 4 tur); bitmiyorsa `eofbit` başarılı son okumada kurulur ve döngü doğru biter (test: "1 2 3" → 3 tur). `eofbit` başarısız okumaya bağlı değil, girdinin sonuna varılmasına bağlı ([ios.iostate] Tablo 118) | eksik |
| 12 | 26.3 | Hatadan sonra `clear()` olmadan okuma çalışmaz | [istream.sentry]/2: `good()` değilse `failbit` | doğru |
| 13 | 26.4 | "Akımın davranışını değiştiren nesnelerdir. Çoğu `<iomanip>` başlığındadır." | [ios.syn]: `boolalpha`, `hex`, `fixed` vb. 24 manipülatör `<ios>`'ta; [iomanip.syn]: 11 (`setw`, `setfill`, `setprecision` …); [ostream.syn]: `endl`, `flush` …; [istream.syn]: `ws`. Örnekteki `std::fixed`, `std::hex`, `std::boolalpha` `<ios>`'ta. `std::hex` gibi çoğu bir işlevdir (test: `std::is_class_v<decltype(std::hex)>` yanlış) | düzeltilmeli |
| 14 | 26.4 | Çoğu manipülatör kalıcı; `setw` yalnızca bir sonraki işleme uygulanır | [ostream.inserters.character]/1, /4: `width(0)`; [facet.num.put.virtuals]; test | doğru |
| 15 | 26.4 | `endl` satır sonu yazar ve tamponu boşaltır | [ostream.manip]/2 | doğru |
| 16 | 26.5 | Sonlandırıcı işlev dosyayı kapatır; RAII (Kısım 18.6); açma kipleri; açılmamış akıma yazmak sessizce başarısız | [filebuf.cons]/5 (`close()`); [ofstream.cons]/2 (`setstate(failbit)`); [iostate.flags] `exceptions()` varsayılanı `goodbit` | doğru |
| 17 | 26.7 | `operator<<` "global işlev olmak zorundadır" | Kitapta "global" üye olmayan işlev anlamında (Kısım 14.3 başlığı, 14.5); [over.oper] | doğru |
| 18 | 26.8 | C++20 `std::format`; ayrıntı Cilt II 10 | [format]; Cilt II 10 | doğru |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): bölümdeki kod örnekleri geçerli;
`std::ios_base::goodbit == 0`; `std::cerr.flags() & std::ios_base::unitbuf` sıfır değil,
`std::clog` için sıfır; `std::cerr.tie() == &std::cout`; `!std::cin.eof()` döngüsü "1 2 3⏎"
girdisinde dört tur (son değer iki kez), "1 2 3" girdisinde üç tur; `std::cin >> x;
std::cin.ignore(); std::getline(...)` "5␠␠⏎merhaba" girdisinde "␠" okuyor, "5⏎merhaba"
girdisinde "merhaba"; `std::is_class_v<decltype(std::hex)>` yanlış.
