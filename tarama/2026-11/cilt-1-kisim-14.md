# Tarama — Cilt I Kısım 14 (Kasım 2026)

Kısım 14'teki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar C++20
(N4861) bölüm adlarıyla; C++23'te (N4950) farklıysa ayrıca. 14.0 normatif iddia içermiyor.
14.7'deki iddialar doğru; dosya değişmedi.

**İşlem (2026-11):** "düzeltilmeli", "eksik" ve "biçim" sonuçlu bütün iddialar düzeltildi;
metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-12_c1-14-tarama`, dört tur;
Claude hakemi xhigh; uzunluk sınırı tur 3'te 550 → 600, brief v2). 14.3'e Standart Notu —
C++20 açıldı. Panel ayrıca şunları düzeltti: kutuda yer değiştirmenin yalnızca `==`/`!=` için
olması ve `5 != k` örneği, eşleşen `operator!=` koşulu (N4861'de yok, N4950'de var; P2468R2,
yazar kararıyla "C++23'ten itibaren" yazıldı), `bool operator==`, 14.5'te "yeniden
yazılabilir" ve yükleme çözümlemesi, `operator new[]`/`delete[]`, C++23 `static` operatörler.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 14.1 | Operatör yüklemesi "yalnızca aritmetik anlamı gerçekten olan türler için doğrudur" | Bölümün kendi örneği `<<` akım operatörü aritmetik değil; ölçüt operatörün tür için doğal anlam taşıması | eksik |
| 2 | 14.2 | Yüklenemeyen operatörler: `.`, `.*`, `::`, `?:`, `sizeof`, `typeid`, `alignof`, `noexcept` | [over.oper]/3 | doğru |
| 3 | 14.2 | Yeni operatör uydurulamaz; öncelik, birleşme, operand sayısı değişmez | [over.oper]/1, /5 | doğru |
| 4 | 14.2 | En az bir operand kullanıcı tanımlı tür olmalı | [over.oper]/6: sınıf ya da numaralandırma türü (14.7 bunu kullanıyor); `operator new`/`delete` istisnası | doğru (basitleştirme) |
| 5 | 14.2 | Operatör işlevi ya isim alanı kapsamında ya `static` olmayan üye; "üçüncü seçenek yok" | [class.free]/1: `operator new` ve `operator delete` üye olarak yazılırsa örtülü `static`'tir. (C++23'te `static operator()` ve `operator[]` de eklendi) | eksik |
| 6 | 14.2 | `=`, `[]`, `()`, `->` üye olmak zorunda | [over.ass], [over.call], [over.sub], [over.ref] | doğru |
| 7 | 14.3 | Üye işlevde "sol operand `this`" | Sol operand `*this`'tir (nesne); `this` göstericidir (Kısım 12.6) | düzeltilmeli |
| 8 | 14.3 | Üye işlevde sol operand dönüşüme uğrayamaz; `k + 5` çalışır, `5 + k` çalışmaz | [over.match.oper]/3. Örnek, gösterilmeyen bir `int`'ten dönüştüren kurucuya dayanıyor (14.4'teki `Kesir(int, int)` bunu sağlamıyor) | eksik |
| 9 | 14.3 | Karşılaştırma operatörlerinde de global tercih edilir (simetri) | [over.match.oper]/3.4 (C++20): `==` ve `!=` için ters çevrilmiş adaylar da denenir; üye `operator==` ile `5 == k` geçerli. Davranış C++20 ile değişti (ölçüt 4); Cilt II 16.4 | eksik |
| 10 | 14.4 | Sınıf içinde tanımlanan `friend` işlev "global bir işlevdir" | Sınıfın bulunduğu isim alanının işlevidir ([class.friend]/7) | eksik |
| 11 | 14.4 | İsmi yalnızca ADL ile bulunur, `Kesir::` ile nitelenemez | [basic.lookup.argdep]/4; Kısım 12.16 ile aynı | doğru |
| 12 | 14.4 | "16.5'te … demiştik"; alıntı "operatör yüklemesi nitelenmeden çağrılmak zorundadır" | Kısım 16, 14'ten sonra geliyor (yanlış yön). Alıntı 16.5'in ifadesiyle de örtüşmüyor; nitelenmiş çağrı (`std::operator+(a, b)`) aslında geçerlidir | düzeltilmeli |
| 13 | 14.5 | Aritmetik operatörler global, `const` referans alır, değer döndürür; `+=` üye | Öğüt | doğru |
| 14 | 14.5 | "`==` ve `<` yazmak çoğu zaman yeterlidir; diğerleri bunlardan türetilir" | C++20 öncesinde diğerleri kendiliğinden türetilmez, yazılması gerekir; C++20'de yalnızca `!=` `==`'den otomatik türetilir, sıralama operatörleri `<=>`'den. Atıf "Cilt II, Kısım 16" → 16.4 | düzeltilmeli |
| 15 | 14.5 | İndisleme üye, iki sürüm; akım operatörleri global | [over.sub] | doğru |
| 16 | 14.6 | Sonek biçimi kukla `int` parametre alır | [over.inc]/1 | doğru |
| 17 | 14.6 | Önek referans, sonek değer döndürür ("farklıdır") | Gelenektir, kural değil: yerleşik operatörleri taklit eder ([over.inc] dönüş türünü belirlemez) | eksik |
| 18 | 14.7 | Kapsamlandırılmamış `enum` `|` ile tamsayıya dönüşür; `enum class` için operatör yüklenir | [conv.prom]/3, [over.oper]/6 | doğru |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): `struct K { K(int=0); bool
operator==(const K&) const; };` ile `5 == k` ve `k != 5` geçerli; `K operator+(const K&)
const;` ile `5 + k` sentaks hatası.

Not (Kısım 16 taraması için): 16.5'teki "ADL'in varlık sebebi, operatör yüklemelerinin
nitelenerek çağrılamamasıdır" ifadesi yanlış — nitelenmiş çağrı geçerlidir; ADL'in amacı
nitelenmeden yazılabilmesidir.
