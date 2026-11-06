# Tarama — Cilt I Kısım 5 (Kasım 2026)

Kısım 5'teki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar C++20
(N4861) bölüm adlarıyla; C++23'te (N4950) farklıysa ayrıca; C için C17. 5.0 normatif iddia
içermiyor.

**İşlem (2026-11):** "düzeltilmeli", "eksik", "gerçekleme" ve "biçim" sonuçlu bütün iddialar
düzeltildi; metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-06_c1-05-tarama`,
üç tur). Panel ayrıca şunları düzeltti: numaralandırıcıların türünde kapanış parantezi kaydı,
artık önerilmeyen kullanımın gerçek sayıları da kapsaması, niteleme kuralında kendi kapsam.
5.4'teki Standart Notu kutusu ölçüt 4'e göre (davranış değişmedi) düz metne alındı.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 5.1 | `enum` "sınırlı sayıda isimlendirilmiş değerden oluşan" bir tür tanımlar | [dcl.enum]/8: türün değerleri numaralandırıcılarla sınırlı değildir (`static_cast<Renk>(2)` gibi değerler de geçerlidir) | eksik |
| 2 | 5.1 | Değerler sıfırdan başlar, birer artar; değer verilen sabitten devam eder | [dcl.enum]/2 | doğru |
| 3 | 5.1 | `enum` türleri "hem kullanıcı tanımlı türlerdir hem de tamsayı türleridir" | [basic.fundamental]/11, [basic.compound]/1: numaralandırma türü tamsayı türü değildir, ayrı bir bileşik türdür (`std::is_integral_v<Renk>` yanlış); kapsamlandırılmamış olan tamsayıya örtülü dönüşür ([conv.prom]/3) | düzeltilmeli |
| 4 | 5.2 | Kapsamlandırılmamış `enum`'un sabitleri dış kapsama sızar | [dcl.enum]/11, [basic.scope.enum] | doğru |
| 5 | 5.2 | Tamsayıdan `enum`'a örtülü dönüşüm sentaks hatası, ters yönü serbest | [conv.prom]/3, [dcl.enum]/10 | doğru |
| 6 | 5.2 | Kod yorumu "derlenir" | Kitabın terimi "geçerli" | biçim |
| 7 | 5.2 | Farklı `enum`'ların karşılaştırılması C++20'den beri artık önerilmiyor; "derleyiciler uyarı verir" | [depr.arith.conv.enum]/1 (P1120). Derleyicinin tanısı standardın konusu değil; standart yalnızca kullanımı artık önerilmiyor sayar ([depr]/2) | gerçekleme |
| 8 | 5.2 | "Temel tür üzerinde denetiminiz yoktur" | C++11'den beri kapsamlandırılmamış `enum`'un da temel türü belirtilebilir (5.3 bunu söylüyor) — sorun yalnızca belirtilmediğinde var | düzeltilmeli |
| 9 | 5.2 | "Hangi tamsayı türüyle temsil edileceğine derleyici karar verir" | [dcl.enum]/7: temel tür gerçeklemeye bağlıdır | gerçekleme |
| 10 | 5.2 | Temel tür belirtilmeyince ileri bildirim "belirsizleşir" | [dcl.enum]/2–3: temel türü belirtilmemiş kapsamlandırılmamış `enum` ileri bildirilemez (`enum E;` sentaks hatası) | eksik |
| 11 | 5.2 | "C dilinde temel tür `int` olmak zorundadır" | C17 6.7.2.2/4: "The choice of type is implementation-defined" — numaralandırıcıların türü `int`'tir, temel tür değil. Kısım 1.8 de doğrusunu söylüyor | düzeltilmeli |
| 12 | 5.3 | `enum class` C++11; `enum struct` aynı anlamda | [dcl.enum]/2 | doğru |
| 13 | 5.3 | Örtülü dönüşüm yok; `static_cast` ile dönüşüm | [conv.prom]/3, [expr.static.cast]/10. `static_cast`'ın anlatıldığı Kısım 10.2'ye atıf yok | doğru (atıf eksik) |
| 14 | 5.3 | Temel tür belirtilebilir, belirtilmezse `int` | [dcl.enum]/5 | doğru |
| 15 | 5.3 | "Üç sorun da çözülür" | Üçüncü sorunun bir yarısı ileri bildirimdi; `enum class`'ın ileri bildirilebildiği söylenmiyor ve gösterilmiyor | eksik |
| 16 | 5.3 | Kapsamlandırılmamış `enum`'a da C++11 ile temel tür belirtilebilir | [dcl.enum]/2 (N2347) | doğru |
| 17 | 5.4 | `using enum` C++20; sabitler o kapsama getirilir | [enum.udecl] (P1099) | doğru |
| 18 | 5.4 | Standart Notu: C++20 öncesinde "tek çözüm" `constexpr` eş isimdi | Başka yollar da vardı (kapsamlandırılmamış `enum`'u bir isim alanına koymak); `constexpr` Kısım 6'da anlatılıyor, atıf yok | eksik |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): `std::is_integral_v<Renk>` yanlış;
`decltype(Kirmizi)` `Renk`; `enum class Sc;` ve `enum U : int;` geçerli, `enum E;` sentaks
hatası; `static_cast<Renk>(3)` geçerli; `Kirmizi == Elma` geçerli (artık önerilmiyor).
