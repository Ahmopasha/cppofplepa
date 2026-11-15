# Tarama — Cilt I Kısım 18 (Kasım 2026)

Kısım 18'deki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış), **biçim** (terim
tanıtımı, atıf). Kaynaklar C++20 (N4861) bölüm adlarıyla. 18.0 ve 18.99 normatif iddia
içermiyor; 18.2 ve 18.6'daki iddialar doğru.

**İşlem (2026-11):** "düzeltilmeli", "eksik" ve "biçim" sonuçlu bütün iddialar düzeltildi;
metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-14_c1-18-tarama`, üç hakem,
üç hakem turu; durma kuralı tur 3'te sağlandı; Claude hakemi xhigh; uzunluk sınırı tur 3'te
520 → 580, brief v2). 18.8'e Standart Notu — C++11 açıldı (kaynak: N3337 [class.dtor]/3,
[except.spec]/12, cppreference; N3204'e ulaşılamadığı için gerekçe satırı yok). Panel
ayrıca şunları düzeltti: kütüphane hatalarının `Throws:` ile sınırı ve kullanıcı türleri,
C++17'de geçici nesnenin doğrudan hata nesnesi olması, `noexcept(false)` atfı, "hata"
sözcüğünün genel anlamı, "hata nesnesi" tanımı, iç içe `try`, devreden kurucunun gövdesi.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 18.1 | "Hata" (exception), "hata göndermek" (throw), "yakalamak" (catch) | Kitap bu karşılıkları 12.12'den beri kullanıyor; hiçbir yerde tanıtılmıyor, sözlükte yok | biçim (terim) |
| 2 | 18.1 | Kurucunun dönüş değeri yok; operatör işlevlerinin dönüş değeri başka işe ayrılmış | [class.ctor] | doğru |
| 3 | 18.2 | `catch` blokları sırayla denenir, ilk uyan çalışır | [except.handle]/4 | doğru |
| 4 | 18.2 | `catch (...)` yalnızca en sonda | [except.handle]/5: son işleyici olmalı; test: önde yazılırsa sentaks hatası | doğru |
| 5 | 18.3 | "Bir isimlendirilmiş nesne gönderip ömrünü düşünmeyin" | [except.throw]/3: `throw` işleneninden ayrı bir hata nesnesi oluşturur (kopyalayarak ya da taşıyarak); isimlendirilmiş nesnenin ömrü sorun değildir (test). Gerekçe yanlış | eksik |
| 6 | 18.3 | Değerle yakalamada "kopyalayan kurucu işlev de hata gönderebilir" | [exception]/2: `std::exception`'dan türeyen her standart sınıfın kopyalayan kurucusu hata göndermez (test: `is_nothrow_copy_constructible`). Bölümün örneği `std::exception`; iddia yalnızca kullanıcının kendi sınıfları için geçerli | eksik |
| 7 | 18.3 | Değerle yakalamada dilimlenme | Kısım 17.9 | doğru |
| 8 | 18.4 | "Standart kütüphane, gönderdiği bütün hata nesnelerini `std::exception`'dan türeyen sınıflardan üretir" | [res.on.exception.handling]/1, /4: `Throws:` ile belirtilen türler ya da onlardan türeyenler; gerçeklemenin ek hataları için yalnızca öneri ("should"). Kütüphane, kullanıcı türünün işlemlerinden gelen hatayı da geçirir | eksik |
| 9 | 18.4 | Hiyerarşi şeması | [std.exceptions]: `domain_error` ve `underflow_error` da var; `bad_alloc` (Kısım 15.4) gibi doğrudan `std::exception`'dan türeyenler de. Şema tamammış gibi duruyor | eksik |
| 10 | 18.4 | `what()` sanal | [exception] | doğru |
| 11 | 18.4 | "İlkel türleri (`int`, `const char*`)" göndermeyin | Kitabın terimi "yerleşik tür" (Kısım 16.5 vb.) | biçim (terim) |
| 12 | 18.5 | Hata gönderildiğinde akış uygun `catch`'e sıçrar; terk edilen bloklardaki otomatik nesnelerin sonlandırıcıları çalışır | [except.ctor]/2: `try` bloğuna girildikten sonra kurulan nesneler. [except.handle]/9: uygun işleyici yoksa `std::terminate`; geri sarılıp sarılmayacağı gerçeklemeye bağlı | eksik |
| 13 | 18.5 | "Buna *stack unwinding* denir" | Sözlükte karşılık "yığının geri sarılması" (Cilt I 18.5) ve bölüm başlığı bu; metinde Türkçe terim tanıtılmıyor | biçim (terim) |
| 14 | 18.6 | RAII; Rule of Zero (Kısım 13.9) | — | doğru |
| 15 | 18.7 | "Parametresiz `throw;` yazımı yalnızca `catch` bloğu içinde geçerlidir" | [expr.throw]/4: her yerde geçerlidir; işlenen hata yokken çalışırsa `std::terminate`. `catch`'ten çağrılan bir işlevde de işlenen hatayı yeniden gönderir (test) | düzeltilmeli |
| 16 | 18.7 | `throw;` yakalanan nesnenin kendisini yeniden gönderir; `throw ex;` kopyalar | [expr.throw]/3 | doğru |
| 17 | 18.8 | Geri sarma sırasında sonlandırıcı hata gönderirse `std::terminate` | [except.terminate]/1.4 | doğru |
| 18 | 18.8 | Sonlandırıcılar C++11'den itibaren örtülü `noexcept` | [except.spec]/8: bir alt nesnenin sonlandırıcısı hata gönderebilir değilse; `noexcept(false)` ile değiştirilebilir (test) | eksik |
| 19 | 18.8 | Gövdedeki hatayı "yakalayıp yutmanız gerekir" | Gerekçesi verilmiyor: `noexcept` işlevden hata çıkarsa `std::terminate` ([except.spec]/5) | eksik |
| 20 | 18.8 | "Cilt II, Kısım 2.6'da anlatıldı" | Cilt II sonra gelir; geçmiş zaman yanlış yön | düzeltilmeli (atıf) |
| 21 | 18.9 | Kurucu hata gönderirse sonlandırıcı çağrılmaz; hayata gelmiş veri elemanlarınınki çağrılır | [except.ctor]/3: taban sınıf alt nesneleri de (test). /4: devreden kurucunun gövdesinden çıkılırsa sonlandırıcı çağrılır (Kısım 12.12 bunu söylüyor ve 18.9'a atıf veriyor) | eksik |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): bölümdeki kod örnekleri geçerli;
`void f() { throw; }` geçerli, işlenen hata yokken çağrılınca program `std::terminate` ile
sonlanıyor; `catch` içinden çağrılan işlevde `throw;` yakalanan `int`'i yeniden gönderiyor;
`catch (...)` önde sentaks hatası; `std::exception` ve `std::runtime_error` için
`is_nothrow_copy_constructible` doğru; `noexcept(false)` sonlandırıcılı üyesi olan sınıfın
sonlandırıcısı `noexcept` değil; kurucu hata gönderince taban sınıfın sonlandırıcısı
çalışıyor; devreden kurucunun gövdesinden hata çıkınca sonlandırıcı çalışıyor;
isimlendirilmiş yerel nesneyi `throw e;` ile göndermek geçerli.
