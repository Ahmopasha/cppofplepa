# Tarama — Cilt I Kısım 16 (Kasım 2026)

Kısım 16'daki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış), **biçim** (terim
tanıtımı, `std::` öneki, atıf). Kaynaklar C++20 (N4861) bölüm adlarıyla. 16.0 normatif
iddia içermiyor.

**İşlem (2026-11):** "düzeltilmeli", "eksik", "gerçekleme" ve "biçim" sonuçlu bütün iddialar
düzeltildi; metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-13_c1-16-tarama`,
üç hakem, iki hakem turu; durma kuralı tur 2'de sağlandı; Claude hakemi xhigh). Panel ayrıca
şunları düzeltti: `friend` işlevler yüzünden "sınıf içindeki isimler" → "sınıf üyeleri",
C++17 çoklu `using` bildirimi, başlık dosyası öğüdünün kapsamı, işlev göstericisi ve dizi
örneği, Kısım 22 ve 23.2/23.7 ileri atıfları, `using` direktifi yolu, `friend` cümlesinin
gerekçe yerine olanak olarak yazılması, "çoğu bakımdan" ([namespace.def]/7).

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 16.1 | `typedef` ile `using` (C++11) aynı işi yapar | [dcl.typedef]/2: alias-declaration ile verilen isim `typedef` ile verilmiş gibidir. "Tür eş ismi" terimi tanıtılmıyor, sözlükte yok | doğru; biçim (terim) |
| 2 | 16.1 | "`typedef` şablon parametresi alamaz, `using` alır"; Cilt II Kısım 4 | [temp.alias]/1. Bir sınıf şablonunun içindeki `typedef` şablon parametresini kullanabilir; doğrusu `typedef` ile şablon yazılamaz. Atıf Cilt II 4.10 | eksik; biçim (atıf) |
| 3 | 16.1 | Tür eş ismi yeni tür oluşturmaz; yüklemede ayırt edici değil | [dcl.typedef]/1–2; test: `void f(ulong); void f(unsigned long)` aynı işlev | doğru |
| 4 | 16.2 | İsim alanları iç içe; C++17 kısa yazım `a::b::c` | [namespace.def]/9 | doğru |
| 5 | 16.2 | Aynı isim alanı birden çok yerde açılabilir, parçalar birleşir | [namespace.def] (extension) | doğru |
| 6 | 16.2 | İsim alanına eş isim verilebilir | [namespace.alias] | doğru; biçim (terim) |
| 7 | 16.2 | "Hiçbir isim alanı içinde olmayan isimler global isim alanındadır" | [basic.scope.namespace]/4: çeviri biriminin en dış bildirim bölgesi. Blok ya da sınıf içindeki isimler de hiçbir isim alanında değildir ama global isim alanında değildir. "İsim alanı" ve "global isim alanı" kitapta tanıtılmıyor (1.10, 2.2 kullanıyor) | eksik; biçim (terim) |
| 8 | 16.3 | `using` bildirimi tek bir ismi kapsama taşır | [namespace.udecl]/1 (ismin bütün bildirimleri, ör. yüklenmiş işlevler) | doğru (basitleştirme); biçim (terim) |
| 9 | 16.3 | `using` direktifi bütün isimleri görünür kılar | [namespace.udir]/2: isimler, direktifi ve isim alanını içeren en yakın isim alanında bildirilmiş gibi görünür | doğru (basitleştirme); biçim (terim) |
| 10 | 16.3 | Başlık dosyasında `using namespace` kullanmayın | Öğüt | doğru |
| 11 | 16.4 | İsimsiz isim alanındaki isimler yalnızca o çeviri biriminden erişilebilir | [basic.link]/4: isimsiz isim alanı ve içindekiler iç bağlantılıdır. Terim tanıtılmıyor | doğru (basitleştirme); biçim (terim) |
| 12 | 16.4 | C'deki `static`'in "C++'taki doğru karşılığı" | `static` C++'ta da geçerlidir ([basic.link]/3.1); isimsiz isim alanı öğüttür | eksik |
| 13 | 16.4 | Üstünlüğü, "değişkenlerin yanı sıra türleri de" kapsaması | `static` işlevlere de uygulanır; sınıf ve numaralandırma türleri yalnızca isimsiz isim alanıyla iç bağlantı alır ([basic.link]/4) | eksik |
| 14 | 16.5 | `sort(v.begin(), v.end())` ADL ile derlenir, çünkü `v.begin()` `std::vector<int>::iterator` döndürür | [vector.overview]: `iterator` gerçeklemeye bağlı bir tür; gösterici olabilir ([iterator.requirements.general]/2). [basic.lookup.argdep]/2.4: `int*` için ilişkili isim alanı yok, ADL `std`'ye bakmaz. Test: `int a[3]; sort(a, a + 3);` sentaks hatası | gerçekleme |
| 15 | 16.5 | Kural: nitelenmemiş işlev çağrısında isim argüman türlerinin isim alanlarında da aranır | [basic.lookup.argdep]/1–2. Bölümün kendi örneği `s1 + s2` bir operatör ifadesi: ADL oraya [over.match.oper]/3.2 ile uygulanır; kural yalnızca işlev çağrısı diyor. ADL'in yapılmadığı durumlar ([basic.lookup.argdep]/3) anlatılmıyor (Aşama 3 envanteri) | eksik |
| 16 | 16.5 | "ADL'in varlık sebebi, operatör yüklemelerinin nitelenerek çağrılamamasıdır" | `std::operator+(a, b)` geçerli bir çağrıdır (test). Nitelenemeyen, operatör ifadesidir (`a + b`); Kısım 14.4'ün son hâli: "ADL, operatörlerin `a + b` biçiminde, nitelenmeden yazılabilmesini sağlar" | düzeltilmeli |
| 17 | 16.5 | `friend` işlevler ADL ile bulunur | [basic.lookup.argdep]/4.3; Kısım 12.16, 14.4 | doğru |
| 18 | 16.5 | ADL yükleme çözümlemesinin birinci aşamasının parçası | Kısım 9.3 | doğru |
| 19 | 16.5 | "ADL'in ayrıntıları ve şablonlarla etkileşimi: Cilt II, Kısım 4" | Cilt II Kısım 4'te ADL geçmiyor (4.9 iki aşamalı arama ADL'den söz etmiyor); ADL'i kullanan deyim Cilt II 14.4'te | düzeltilmeli (atıf) |
| 20 | 16.5 | `operator+` ve `sort` `std` içinde | Metinde `std::` öneki yok | biçim (`std::`) |
| 21 | 16.6 | `inline` isim alanının üyeleri dıştakine aitmiş gibi kullanılır; sürümleme | [namespace.def]/7 | doğru; biçim (terim) |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): bölümdeki kod örnekleri geçerli;
`std::operator+(s1, s2)`, `getline(std::cin, s1)` ve `swap(s1, s2)` geçerli;
`int a[3]{}; sort(a, a + 3);` sentaks hatası ("use of undeclared identifier"); blok
kapsamında `void f(int);` bildirimi varken `f(s)` çağrısında ADL yapılmıyor.

Notlar:
- Aşama 3 kapsam envanteri: ADL'in ayrıntıları (ilişkili isim alanları ve sınıflar; ADL'in
  yapılmadığı durumlar, [basic.lookup.argdep]/2–3) kitapta anlatılmıyor.
- Cilt II Kısım 4 taraması için: 4.9, bağımlı nitelenmemiş işlev çağrılarında örnekleme
  noktasında ADL yapıldığını söylemiyor.
