# Tarama — Cilt I Kısım 19 (Kasım 2026)

Kısım 19'daki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış), **biçim** (terim
tanıtımı, atıf). Kaynaklar C++20 (N4861) bölüm adlarıyla. 19.0 normatif iddia içermiyor;
19.2'deki iddialar doğru.

**İşlem (2026-11):** "eksik", "gerçekleme" ve "biçim" sonuçlu bütün iddialar düzeltildi;
metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-17_c1-19-tarama`, üç hakem,
üç hakem turu; tur 3 kararı kabul; Claude hakemi xhigh). Panel ayrıca şunları düzeltti:
çalışma zamanı denetiminin yalnızca aşağı dönüşümde olması, çok biçimli olması gerekenin
taban sınıf olması (test: sanal işlevsiz `Sekil`, sanal işlevli `Daire` ile `typeid(*s)`
`Sekil` veriyor, `dynamic_cast<Daire*>(s)` sentaks hatası), terim sırası, statik tür
tanımı, Kısım 17.10 atfı.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 19.1 | RTTI, nesnenin "dinamik türünü" sorgular | [defns.dynamic.type], [defns.static.type]. "Dinamik tür" ve "statik tür" kitapta tanıtılmıyor (17.10 "statik tür"ü tanıtmadan kullanıyor), sözlükte yok | doğru; biçim (terim) |
| 2 | 19.1 | "Her ikisi de sınıfın çok biçimli olmasını gerektirir" | [expr.typeid]/3: çok biçimli olmayan ifadede `typeid` statik türü verir (test). [expr.dynamic.cast]/4–5: çok biçimlilik yalnızca aşağı dönüşümde gerekir (Kısım 10.5 bunu söylüyor). Gerektiren, dinamik türü sorgulamaktır | eksik |
| 3 | 19.1 | "En az bir sanal işlevi bulunmalıdır" | [class.virtual]/1: sanal işlev bildiren ya da devralan sınıf; Kısım 17.6'daki tanım | doğru; biçim (atıf) |
| 4 | 19.1 | "Nesnenin dinamik türü … `vptr` üzerinden okunur" | Standart, dinamik türün nasıl bulunacağını belirtmez; `vptr` yaygın bir gerçekleme yoludur (Cilt II 6.1) | gerçekleme |
| 5 | 19.2 | Başarısızlık: göstericide `nullptr`, referansta `std::bad_cast` | [expr.dynamic.cast]/9 | doğru |
| 6 | 19.2 | `static_cast` ile aşağı dönüşüm denetimsiz; tür yanlışsa tanımsız davranış | [expr.static.cast]/11 | doğru |
| 7 | 19.3 | `typeid(*s)` dinamik, `typeid(s)` statik tür | [expr.typeid]/2–3 | doğru |
| 8 | 19.3 | `name()` gerçeklemeye bağlı; "Derleyiciler farklı biçimler üretir" | [type.info]/8. Kitap derleyici davranışından söz etmez; "gerçeklemeden gerçeklemeye" yeterli | doğru; biçim |
| 9 | 19.3 | `typeid` tam eşleşme, `dynamic_cast` türemişleri de kabul eder | [type.info]/3, [expr.dynamic.cast]/8 | doğru |
| 10 | 19.4 | "`dynamic_cast` çalışma zamanında hiyerarşide arama yapar ve sanal çağrıdan pahalıdır" | Standart maliyet hakkında bir şey söylemez; arama ve pahalılık gerçekleme ayrıntısı. Kısım 10.5 "maliyeti"ni 19'a gönderiyor | gerçekleme |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): bölümdeki kod örnekleri geçerli;
çok biçimli olmayan tabanda `dynamic_cast<D*>(b)` sentaks hatası, yukarı dönüşüm geçerli;
çok biçimli olmayan `B& b = d;` için `typeid(b) == typeid(B)`; çok biçimli tabanda
`typeid(b) == typeid(D)`; `typeid(int)` geçerli; boş göstericiden `typeid(*p)`
`std::bad_typeid` gönderiyor.

Not (Cilt II Kısım 6 taraması için): 6.1 sanal tabloyu "derleyici üretir" diye kural gibi
anlatıyor; standart bunu belirtmez (gerçekleme).
