# Tarama — Cilt I Kısım 24 (Kasım 2026)

Kısım 24'teki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış), **biçim** (terim
tanıtımı, atıf). Kaynaklar C++20 (N4861) bölüm adlarıyla. 24.0 normatif iddia içermiyor.

**İşlem (2026-11):** "eksik", "gerçekleme" ve "biçim" sonuçlu bütün iddialar düzeltildi;
metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-20_c1-24-tarama`, üç hakem,
üç hakem turu; durma kuralı tur 3'te sağlandı; uzunluk 360 → 440 brief v2–v3). Yazar
kararıyla iki Standart Notu kutusu açıldı (24.2 C++23, 24.3 C++20). Panel ayrıca şunları
düzeltti: varsayılan yakalamanın tek başına duran `=`/`&` simgesine bağlanması ve örtülü
yakalamayla sınırlanması, `*this` yakalamasını tetikleyenin `static` olmayan üye (veri
elemanı ya da üye işlev) olması, `[=]` altında elemana yazılabilmesi, tanımsız davranışın
dönen lambdanın çağrısına bağlanması, `operator()` ile çağrı operatörünün bağlanması.
Son turda uygulanan maddeler hakem turunda sınanmadı.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 24.1 | Lambda ifadesi isimsiz bir sınıf ve o türden bir nesne üretir; `operator()` lambdanın gövdesidir | [expr.prim.lambda.closure]/1 ("unique, unnamed non-union class type"), /4. "Kapanış türü" 24.4 ve 24.5'te kullanılıyor ama tanıtılmıyor (sözlükte Cilt II 12.1) | doğru; biçim (terim) |
| 2 | 24.1 | "`f`'in türünü yazamazsınız" | Türün adı yok ([expr.prim.lambda.closure]/1), ama türe `decltype(f)` ile başvurulabilir (test). Kısım 4.4 "adıyla yazılamayan türler" diyor | eksik |
| 3 | 24.2 | "Parametre listesi ve geri dönüş türü isteğe bağlıdır" | [expr.prim.lambda] dilbilgisi: isteğe bağlı olan *lambda-declarator*'ın tamamı; geri dönüş türü ya da `mutable` yazılacaksa `( … )` zorunlu; yoksa `()` yazılmış sayılır (/4). Test: `[] -> int { return 1; }` ve `[a] mutable {}` C++20'de sentaks hatası. C++23'te kısıt kalktı (N4950 [expr.prim.lambda.general] dilbilgisi, P1102R2) | eksik |
| 4 | 24.2 | Geri dönüş türü yazılmazsa `return`'den çıkarılır | [expr.prim.lambda]/4: geri dönüş türü `auto`, [dcl.spec.auto]'ya göre `return` deyimlerinden çıkarılır (Kısım 4.6: `return` yoksa `void`). Kitabın terimi "`return` deyimi" (4.6, 8.2) | doğru; biçim (terim) |
| 5 | 24.3 | Yakalama biçimleri (`[a]`, `[&a]`, `[=]`, `[&]`, `[=, &b]`, `[&, a]`) | [expr.prim.lambda.capture] dilbilgisi, /2 | doğru |
| 6 | 24.3 | "`[=]` ve `[&]` yazımlarına varsayılan yakalama denir" | [expr.prim.lambda.capture] dilbilgisi: *capture-default*. Terim İngilizcesiyle tanıtılmıyor, sözlükte yok | biçim (terim) |
| 7 | 24.3 | Yalnızca gövdede kullanılan değişkenler yakalanır | [expr.prim.lambda.capture]/7 (yalnızca gövdede başvurulan yerel varlıklar). Test: `const int n = 5; [=]{ return n; }` boş kapanış türü (`n` odr-kullanılmıyor) | doğru |
| 8 | 24.3 | `return [&x] { return x; };    // HATA: x yok olacak` | Kod geçerli (test: derleniyor); hata, döndürülen lambdanın çağrılmasında: [expr.prim.lambda.capture]/13 ve /16 not (ömrü bitmiş varlık; "likely to result in undefined behavior"), [basic.life]. "HATA" yorumu sentaks hatası gibi okunuyor | eksik |
| 9 | 24.3 | Üye işlevde `[=]` veri elemanlarını kopyalamaz, `this` göstericisini kopyalar | [expr.prim.lambda.capture]/10.1, /12: `*this` referansla yakalanır (standart "gösterici kopyalanır" demiyor). C++20'de `[=]` ile `this`'in örtülü yakalanması artık önerilmiyor: /7, [depr.capture.this] (önerilen karşılık `[=, this]`). Test: `[=, this]` `-std=c++17`'de sentaks hatası, C++20'de geçerli | eksik |
| 10 | 24.3 | `[*this]` C++17'den itibaren | P0018R3; test (`-std=c++14` sentaks hatası) | doğru |
| 11 | 24.4 | `[a] { ++a; }` sentaks hatası; çağrı operatörü `const`, `mutable` kaldırır | [expr.prim.lambda.closure]/4; test | doğru |
| 12 | 24.4 | Referansla yakalamada `mutable` gerekmez, "çünkü `const`luk referansın kendisini niteler" | [expr.prim.lambda.capture]/12: referansla yakalamada kapanış türünde veri elemanı bildirilip bildirilmediği belirtilmemiş; /13: gövdedeki ad, yakalanan referansın bağlı olduğu varlığı gösterir. Gerekçe bir gerçekleme modeline dayanıyor | gerçekleme |
| 13 | 24.4, 24.5 | Cilt II 12.1–12.2 ve Kısım 12 atıfları; 24.5'teki konu listesi | Cilt II 12.1–12.6 | doğru |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): bölümdeki kod örnekleri geçerli;
`[a] { ++a; }` sentaks hatası; `[] -> int { return 1; }` ve `[a] mutable { … }` C++20'de
sentaks hatası, `-std=c++23`'te geçerli; `[=]` ile `this`'in örtülü yakalanması
`-Wdeprecated` ile uyarı veriyor, `[=, this]` C++20'de geçerli, C++17'de sentaks hatası;
`[*this]` C++14'te sentaks hatası, C++17'de geçerli; `const int n` `[=]` ile yakalanmıyor
(`std::is_empty_v`); `decltype(f) g = f;` geçerli; `[&x]` döndüren işlev derleniyor.

Not (Cilt II Kısım 12 taraması için): 12.1 ve 12.2 referansla yakalamayı "referans veri
elemanı" diye kural gibi anlatıyor ([expr.prim.lambda.capture]/12: belirtilmemiş);
`[=]` ile `this`'in örtülü yakalanmasının C++20'de artık önerilmediği söylenmiyor; 12.1'in
"kapanış türü" tanıtımı Cilt I 24.1'e geçerse yinelenir.

Not (Kısım 4 için, önemsiz): 4.4'teki madde listesi tek paragrafa kaynamış.
