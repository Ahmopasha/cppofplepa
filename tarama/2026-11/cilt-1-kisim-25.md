# Tarama — Cilt I Kısım 25 (Kasım 2026)

Kısım 25'teki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış), **biçim** (terim
tanıtımı, atıf). Kaynaklar C++20 (N4861) bölüm adlarıyla. 25.0 normatif iddia içermiyor.
Kısım genelinde kütüphane adları (`unique_ptr`, `make_unique`, `shared_ptr`,
`make_shared`, `weak_ptr`, `enable_shared_from_this`) `std::` öneki olmadan yazılmış (biçim).

**İşlem (2026-11):** "düzeltilmeli", "eksik", "gerçekleme" ve "biçim" sonuçlu bütün iddialar
düzeltildi; metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-20_c1-25-tarama`,
üç hakem, iki hakem turu; durma kuralı tur 2'de sağlandı; uzunluk 400 → 440 brief v2). 25.2'ye
Standart Notu — C++17 kutusu eklendi. Panel ayrıca şunları düzeltti: "gerçeklemeye bağlı"
yerine "standart belirtmez" (implementation-defined ile karışmasın), "silici" teriminin
tanıtılması, "iki sahibi olamaz" genellemesinin kopyalamayla sınırlanması (25.5 ile
çelişiyordu), `std::make_unique`'in C++14'te geldiği, kalın kuralın [expr.delete]/2
koşuluna getirilmesi, çifte silme yorumunun zamanı. Son turda uygulanan iki madde hakem
turunda sınanmadı.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 25.1 | "Kısım 18.6'da bunun gerekçesini görmüştük: yığın geri sarılırken yalnızca sonlandırıcı işlevi olan nesneler temizlenir" | Gerekçe Kısım 18.5'te (yığının geri sarılması); 18.5'e göre geri sarılmada otomatik ömürlü nesneler yok edilir ([except.ctor]/2) | biçim (atıf); eksik |
| 2 | 25.1 | `BasitAkilli` "bu fikrin tam hâlidir" (öncesi) | Sınıfın örtülü kopyalama işlevleri var ([class.copy.ctor]/6); kopyalanırsa iki nesne aynı göstericiyi siler: [expr.delete]/2 tanımsız davranış. Metin bunu söylemiyor | eksik |
| 3 | 25.2 | Tek sahip; kopyalanamaz, taşınabilir; taşımadan sonra `p` boş | [unique.ptr]/1, /4; [unique.ptr.single.ctor]/20 (`u.get() == nullptr`); test | doğru |
| 4 | 25.2 | "Kopyalanamaz oluşu, Cilt II Kısım 2.2'deki bildirim tablosunun doğrudan sonucudur: taşıyan işlevleri bildirmek kopyalayan işlevleri siler" | [unique.ptr.single] sinopsis: "// disable copy from lvalue", `unique_ptr(const unique_ptr&) = delete;`, `unique_ptr& operator=(const unique_ptr&) = delete;` — standart kopyalama işlevlerini açıkça siler | düzeltilmeli |
| 5 | 25.2 | `std::make_unique<int[]>(100)` | [unique.ptr.create]; test | doğru |
| 6 | 25.2 | `make_unique` "`new` ile kurucu işlev arasında hata oluşması ihtimalini ortadan kaldırır" | Kurucu işlev hata gönderirse bellek zaten geri verilir ([expr.new]/25). Kastedilen sızıntı (`f(std::unique_ptr<T>(new T), g())`) C++17 öncesine ait: N4140 [intro.execution]/15 argüman değerlendirmeleri sırasız; C++17'den itibaren her parametrenin ilk değer verilmesi ötekilerle belirsiz sıralı (N4659 [expr.call]/5, N4861 [expr.call]/8), araya girme yok | düzeltilmeli |
| 7 | 25.3 | Sayaç sıfıra düşünce nesne yok edilir; `use_count()` 2 | [util.smartptr.shared.dest]/1; test | doğru |
| 8 | 25.3 | "Sayaç için ayrı bir **kontrol bloğu** tutulur … `make_shared` … nesneyi ve kontrol bloğunu tek seferde ayırdığı için" | "Control block" standartta geçmiyor; [util.smartptr.shared.create]/7 not: "internal bookkeeping structures such as reference counts"; /7.1: "Implementations should perform no more than one memory allocation" (öneri, zorunluluk değil). Maliyet karşılaştırması standartta yok. Terim tanıtımında İngilizce yok | gerçekleme; biçim (terim) |
| 9 | 25.4 | "İki `shared_ptr` birbirini gösterirse sayaçlar hiç sıfıra düşmez"; "döngüsel başvuru" | Birbirini gösteren `shared_ptr`'lar değil, birbirini `shared_ptr` üyeleriyle gösteren nesneler (test: iki nesnenin sonlandırıcı işlevi çalışmıyor). Terim İngilizcesiz | eksik; biçim (terim) |
| 10 | 25.4 | `weak_ptr` sahiplenmez, sayacı artırmaz; `lock()` boş döner | [util.smartptr.weak]/1; [util.smartptr.weak.obs]/3; test (`use_count()` 2 kalıyor) | doğru |
| 11 | 25.5 | "Varsayılan silicide maliyeti çıplak göstericiyle aynıdır" | [unique.ptr]/1–3: gösterici ve silici saklar, sayaç yok; boyut ve maliyet standartta belirtilmez | gerçekleme |
| 12 | 25.5 | Aynı çıplak adres iki `shared_ptr`'a: "// çifte yıkım" | Kod geçerli; ikinci silme tanımsız davranış ([expr.delete]/2, [basic.stc.dynamic.deallocation]) | eksik |
| 13 | 25.5 | "Yığında duran bir nesneyi `delete` etmek tanımsız davranıştır" | [expr.delete]/2 ("created by a previous new-expression … If not, the behavior is undefined"). "Yığın" bir gerçekleme kavramı; kitabın terimi otomatik ömürlü (Kısım 15.1) | doğru; biçim (terim) |
| 14 | 25.5 | Kaplarda akıllı gösterici; Kısım 17.9 dilimlenme; Cilt II 17.9 atfı | Kısım 17.9 (nesne dilimlenmesi), Cilt II 17.9 | doğru |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): bölümdeki kod örnekleri geçerli;
`std::is_copy_constructible_v<std::unique_ptr<Myclass>>` yanlış, taşıma doğru;
`auto q = p;` (`std::unique_ptr`) sentaks hatası; taşımadan sonra `p == nullptr`;
`use_count()` 2, `std::weak_ptr` eklenince yine 2; birbirini `std::shared_ptr` üyeleriyle
gösteren iki nesnenin sonlandırıcı işlevi kapsam sonunda çalışmıyor.

Not (Cilt II Kısım 17.9 için; o kısım ilk turda işlendi): kontrol bloğunu standart gibi
anlatıyor ("Blokta iki sayaç vardır"; "`make_shared` … tek bir bellek bloğunda ayırır");
standart bunları belirtmiyor ([util.smartptr.shared.create]/7). "Cilt I Kısım 25.5'teki
maliyet eşitliği" ve "Cilt I Kısım 25.3'te … ayrı bir kontrol bloğunda tuttuğu
söylenmişti" atıfları bu taramanın sonucuna göre uyumlandırılmalı.
