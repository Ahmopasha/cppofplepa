# Tarama — Cilt I Kısım 11 (Kasım 2026)

Kısım 11'deki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar C++20
(N4861) bölüm adlarıyla; C++23'te (N4950) farklıysa ayrıca. 11.0 normatif iddia içermiyor.

**İşlem (2026-11):** "düzeltilmeli", "eksik", "gerçekleme" ve "biçim" sonuçlu bütün iddialar
düzeltildi; metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-11_c1-11-tarama`,
iki tur). Panel ayrıca şunları düzeltti: modül istisnasıyla çelişen "her durumda",
yerleştirmenin tanımın görünmesine bağlanması, "`inline` belirteci" ayrımı, "ODR'nin ikinci
yarısı" göndermesi (Kısım 2.7 ODR'yi iki kural olarak veriyor), `constexpr` `static` veri
elemanlarının C++17'de örtülü `inline` olması.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 11.1 | `inline` olmayan, kullanılan her işlevin programda tam bir tanımı olmalı (Kısım 2.7) | [basic.def.odr]/10 | doğru |
| 2 | 11.1 | İki tanım "bağlayıcı hata verir"; kod yorumu "bağlayıcı hatası" | [basic.def.odr]/10: "no diagnostic required". Kısım 0.3: bağlama adımı bildirebilir, standart istemez | gerçekleme |
| 3 | 11.1 | `inline` işlev birden çok çeviri biriminde tanımlanabilir; tanımlar aynı olmalı | [basic.def.odr]/12–13. Eksik: tanım, işlevin kullanıldığı her çeviri biriminden erişilebilir olmalı ([basic.def.odr]/12 "shall be reachable from the end of every definition domain in which it is odr-used"); tanımlar aynı değilse program hatalı, tanı istenmez | eksik |
| 4 | 11.2 | `inline`'ın bugünkü anlamı ODR istisnasıdır, "gövdenin yerleştirilmesi değil" | [dcl.inline]/2: "The inline specifier indicates to the implementation that inline substitution … is to be preferred …; An implementation is not required to perform this inline substitution". Standart yerleştirme tercihini hâlâ söylüyor | eksik |
| 5 | 11.2 | "Derleyici … yerleştirebilir; kendi karar verir" | [intro.abstract]/1 (as-if); öznenin "derleyici" olması; karar gerçeklemenin | biçim |
| 6 | 11.3 | "Üç durumda" anahtar sözcük gerekmez | `consteval` işlevler, sınıf içinde tanımlanan `friend` işlevler, `constexpr` `static` veri elemanları da örtülü `inline`'dır ([dcl.constexpr]/1, [class.friend]/7) — liste kapalı değil | eksik |
| 7 | 11.3 | Sınıf bloğunda tanımlanan üye işlevler örtülü `inline` | [class.mfct]/1: "if it is attached to the global module" — adlandırılmış modüle bağlı sınıflarda değil. Sınıflar Kısım 12'de; atıf yok | eksik |
| 8 | 11.3 | Derleyicinin ürettiği özel üye işlevler `inline` | [class.default.ctor]/1, [class.copy.ctor]/10, [class.dtor]/2 ("inline public member") | doğru |
| 9 | 11.3 | `constexpr` işlevler `inline`'lığı kapsar (Kısım 6) | [dcl.constexpr]/1; `consteval` da. Atıf Kısım 6.6 | doğru (atıf) |
| 10 | 11.4 | C++17'ye kadar `inline` yalnızca işlevler içindi | [dcl.inline] (P0386) | doğru |
| 11 | 11.4 | "Başlık dosyasında bir değişken tanımlayamazdınız" | Fazla geniş: `const` isim alanı değişkenleri iç bağlantılıdır ve başlıkta tanımlanabilir; yapılamayan, bütün çeviri birimlerinin paylaştığı tek değişkendi | eksik |
| 12 | 11.4 | "Kısım 12.14'te … görmüştük" | Kısım 12, 11'den sonra geliyor; okur `static` veri elemanlarını henüz görmedi | düzeltilmeli |
| 13 | 11.4 | `inline static int sayac = 0;` | [class.static.data]/4 | doğru |
| 14 | 11.4 | Standart Notu "Neden değişti" satırı | Gerekçe öneri belgesinden (P0386R2, N4424) doğrulanamadı; yazar kararı (2026-11-07): doğrulanamayan gerekçe satırı yazılmaz | biçim |

Kaynaklar (N4861, timsong-cpp.github.io/cppwp/n4861): [class.mfct]/1 "A member function may
be defined in its class definition, in which case it is an inline member function if it is
attached to the global module"; [dcl.inline]/2 yukarıdaki gibi.
