# Tarama — Cilt I Kısım 10 (Kasım 2026)

Kısım 10'daki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar C++20
(N4861) bölüm adlarıyla; C++23'te (N4950) farklıysa ayrıca. 10.0 normatif iddia içermiyor.
10.1'deki iddialar doğru; dosya değişmedi.

**İşlem (2026-11):** "düzeltilmeli", "eksik", "gerçekleme" ve "biçim" sonuçlu bütün iddialar
ile atıf eksikleri düzeltildi; metinler AI hakem panelinden geçti
(`~/ai-panel/calismalar/2026-11-10_c1-10-tarama`, dört tur). Panel ayrıca şunları düzeltti:
gerçeklemeye bağlılığın yalnızca gösterici ile tamsayı arasında olması ve gidiş-dönüş güvencesi,
erişim kuralının türe bağlanması, aynı adres güvencesinin nesne göstericileriyle sınırlanması,
C tarzı dönüşümün beş adımlı sırası, "aşağı dönüşüm" terimi.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 10.1 | C tarzı dönüşüm `const`luk kaldırır, ilgisiz göstericileri çevirir, sayısal dönüşüm yapar | [expr.cast]/4 | doğru |
| 2 | 10.1 | Dört operatör; yanlış dönüşüm sentaks hatası verir | [expr.static.cast], [expr.const.cast], [expr.reinterpret.cast], [expr.dynamic.cast] | doğru |
| 3 | 10.2 | `static_cast`: örtülü yapılabilen ve ilişkili türler arası dönüşümler; `void*` → `T*`; `enum class` → `int` | [expr.static.cast]/4, /10, /13. `enum class` Kısım 5.3'te; atıf yok | doğru (atıf eksik) |
| 4 | 10.2 | Kod: `malloc(100)` | `<cstdlib>` ile küresel `malloc`'un bildirilip bildirilmediği belirtilmemiştir (Kısım 1.10); kitabın kuralıyla `std::malloc` | biçim |
| 5 | 10.2 | Taban → türemiş göstericiye `static_cast` denetim yapmaz | [expr.static.cast]/11: nesne gerçekten o türemiş türden değilse davranış tanımsızdır — metin sonucu söylemiyor; kalıtım Kısım 17'de | eksik |
| 6 | 10.3 | `const_cast` yalnızca `const` ve `volatile` ekler/kaldırır | [expr.const.cast]/3 | doğru |
| 7 | 10.3 | Gerçekten `const` nesneyi değiştirmek tanımsız davranış | [dcl.type.cv]/4 | doğru |
| 8 | 10.3 | "`const` bir bağlantı üzerinden erişildiği" | "Bağlantı" kitapta dil bağlantısı (linkage) için kullanılıyor (Kısım 1.10, 9.9); burada gösterici ya da referans kastediliyor | düzeltilmeli |
| 9 | 10.4 | `reinterpret_cast` ilgisiz gösterici türleri arasında dönüşüm yapar | [expr.reinterpret.cast]/4–7, /11: gösterici ile tamsayı arası ve referanslar da | eksik |
| 10 | 10.4 | "Bit örüntüsüne dokunmaz", derleyiciye "buraya şu türden bakacağım" der | [expr.reinterpret.cast]/4: göstericiden tamsayıya eşleme gerçeklemeye bağlıdır; nesne göstericileri için /7 `static_cast<T*>(static_cast<void*>(p))` ile aynıdır. Bit düzeyi davranış standardın söylediği değil | gerçekleme |
| 11 | 10.4 | "Çoğu kullanımı tanımsız davranışa yakındır" | "Yakın" standardın bir kategorisi değil. Dönüşümün sonucu çoğunlukla gerçeklemeye bağlıdır; dönüştürülmüş gösterici üzerinden nesneye erişmek `char`, `unsigned char`, `std::byte` istisnaları dışında tanımsız davranıştır ([basic.lval]/11) | düzeltilmeli |
| 12 | 10.5 | `dynamic_cast` çok biçimli hiyerarşide çalışma zamanında denetler; göstericide `nullptr`, referansta `std::bad_cast` | [expr.dynamic.cast]/8–9. Çok biçimlilik Kısım 17.6'da; atıf yok | doğru (atıf eksik) |
| 13 | 10.5 | "Sınıfın en az bir sanal işlevi olmalıdır; yoksa sentaks hatası" | [expr.dynamic.cast]/5–6: yalnızca aşağı ve yan dönüşümde, kaynak türü çok biçimli olmalı; yukarı dönüşüm her sınıfta geçerli | eksik |
| 14 | 10.6 | Tablo | [expr.*.cast] | doğru |
| 15 | 10.6 | "Derleyici sırayla `const_cast`, `static_cast`, `reinterpret_cast` ve birleşimlerini dener" | [expr.cast]/4: sıra standardın kuralıdır (const_cast; static_cast; static_cast + const_cast; reinterpret_cast; reinterpret_cast + const_cast) | biçim |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): `struct B{}; struct D:B{};`
için `dynamic_cast<B*>(&d)` geçerli, `dynamic_cast<D*>(&bb)` sentaks hatası ('B' is not
polymorphic).
