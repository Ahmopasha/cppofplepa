# Tarama — Cilt I Kısım 21 (Kasım 2026)

Kısım 21'deki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış), **biçim** (terim
tanıtımı, atıf). Kaynaklar C++20 (N4861) bölüm adlarıyla. 21.0 normatif iddia içermiyor;
21.5'teki iddialar doğru.

**İşlem (2026-11):** "düzeltilmeli", "eksik" ve "biçim" sonuçlu bütün iddialar düzeltildi;
metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-19_c1-21-tarama`, üç hakem,
üç hakem turu; tur 3 kararı kabul; Claude hakemi xhigh). Panel ayrıca şunları düzeltti:
"doğrudan kopyalar" yargısının kopyalama ve taşıma işlevleriyle sınırlanması (varsayılan
kurucu ve sonlandırıcı işlev yerleşik türden elemanları kopyalamaz), silinme koşulunun
"silinmiş ya da erişilemez" olması, kod örneğinde sentaks hatasının gösterilmesi,
"sonlandırma" yerine "sonlandırıcı işlev". Kısım başlığı yazar kararıyla "Composition".

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 21.0, 21.2 | Kısım başlığı "Bileşik Nesneler", 21.2 "bileşik nesne" (composition anlamında) | Sözlük ve Kısım 3.10, Cilt II 16.6 "bileşik tür"ü aggregate için kullanıyor; 3.10'un başlığı "Bileşik nesnelere ilk değer verme". Kitabın geri kalanı composition'ı İngilizce kullanıyor (17.1, 17.10, Cilt II 6.7, 6.8, 14.8). Yazar kararı: İngilizce kalır, başlık "Composition", sözlükte çevrilmeyenlere | biçim (terim) |
| 2 | 21.1 | Başka sınıf türünden veri elemanı barındırma: composition, has-a | Kısım 17.1 | doğru |
| 3 | 21.2 | Sıra: taban sınıf, veri elemanları bildirim sırasıyla, gövde; hayat biterken tersi | [class.base.init]/13 (sanal tabanlar Cilt II'ye bırakılmış basitleştirme), [class.dtor]/14 | doğru |
| 4 | 21.2 | İlk değer verme listesindeki yazım sırasının etkisi yok | [class.base.init]/13.2–13.3 | doğru |
| 5 | 21.3 | Derleyicinin yazdığı altı işlev her eleman için elemanın işlevini çağırır ve "doğru sonuç verir"; `std::unique_ptr` elemanlı `Kayit` için "kopyalama, taşıma ve yıkım doğru çalışır" | [class.copy.ctor]/10.1, [class.copy.assign]/7.4: kopyalanamayan eleman varsa örtülü kopyalama işlevleri silinmiş sayılır; [unique.ptr.single]: kopyalama işlevleri `= delete`. `Kayit b = a;` sentaks hatası (test) | düzeltilmeli |
| 6 | 21.4 | Kodda "veri'nin geri kalan 40 işlevi" | `std::map`'in üye işlev sayısı yükleme ve sayım biçimine bağlı; doğrulanabilir bir sayı değil | eksik |
| 7 | 21.4 | "Kalıtımda taban sınıfın bütün `public` arayüzü devralınır" | [class.access.base]/1: yalnızca `public` kalıtımda taban sınıfın `public` üyeleri türemiş sınıfta `public` kalır; `private` kalıtımda `private` olur (Cilt II 6.7) | eksik |
| 8 | 21.4 | `private` kalıtımın composition'a tercih edildiği üç durum: Cilt II 6.7 | Cilt II 6.7 iki durumu sayar, üçüncüsünü 6.8'e bırakır | doğru |
| 9 | 21.5 | `private` bölümdeki içsel tür dışarıdan kullanılamaz | [class.access]/1.2, /5 (örnek `A::B y; // access error`); test | doğru |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): bölümdeki kod örnekleri geçerli;
`Kayit` için `std::is_copy_constructible_v` ve `std::is_copy_assignable_v` yanlış,
taşıma ve varsayılan kurucu işlev doğru; `Kayit b = a;` sentaks hatası (örtülü silinmiş
kopyalayan kurucu işlev); hayata gelme sırası B, M1, M2, gövde, sonlanma tersi (ilk değer
verme listesi ters yazıldığında da); `L::N` (`private` içsel tür) dışarıda sentaks hatası.
