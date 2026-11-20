# Tarama — Cilt I Kısım 23 (Kasım 2026)

Kısım 23'teki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış), **biçim** (terim
tanıtımı, atıf). Kaynaklar C++20 (N4861) bölüm adlarıyla. 23.0 normatif iddia içermiyor;
23.3, 23.5 ve 23.7'deki iddialar doğru.

**İşlem (2026-11):** "eksik" ve "biçim" sonuçlu bütün iddialar düzeltildi; metinler AI hakem
panelinden geçti (`~/ai-panel/calismalar/2026-11-19_c1-23-tarama`, üç hakem, iki hakem turu;
durma kuralı tur 2'de sağlandı; uzunluk sınırı 600). Panel ayrıca şunları düzeltti: bitişik
iteratörün C++17'de tanımlanıp C++20'de ayrı kategori olması, `std::vector<bool>`'un bitişik
olmaması, girdi/çıktı tanımı, "sıralı" sözcüğünün iki anlamının ayrılması, yeniden yer
ayırmanın ekleme sırasında olması, silmede çoğul kural, kuralların referans ve göstericileri
de kapsaması. Tablo hücrelerindeki `std::` öneki ve 23.7'deki algoritma adlarının öneki
uygulama adımında eklendi (biçim). Son turda uygulanan maddeler hakem turunda sınanmadı.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 23.1 | Kaplar, algoritmalar, iteratörler; `std::sort` `vector` ve `deque` ile çalışır | — | doğru; biçim (terim: "kap", "iteratör" sözlükte Cilt I 23.1–23.2, İngilizceleri verilmiyor) |
| 2 | 23.2 | `end()` bir elemanı göstermez; `*v.end()` tanımsız davranış | [iterator.requirements.general]/7 | doğru |
| 3 | 23.2 | Kategori tablosu: girdi/çıktı, ileri, çift yönlü, rastgele erişimli (`vector`, `deque`, `array`) | [iterator.requirements.general]/2, /4: bir kategori daha var, bitişik iteratör (C++17'den beri, N4659 [iterator.requirements.general]/6; C++20'de `std::contiguous_iterator`). `vector`, `array`, `string` iteratörleri bitişik, `deque` değil (test). Cilt II 7.6 ve 8.2 `contiguous_iterator`'ı "Cilt I 23.2'deki kategorilerin karşılığı" sayıyor | eksik |
| 4 | 23.2 | `std::sort` rastgele erişim ister, `std::list` ile kullanılamaz | [sort]; test (sentaks hatası) | doğru |
| 5 | 23.2 | `iterator_traits`: "Cilt II, Kısım 4" | Cilt II 4.11 | biçim (atıf) |
| 6 | 23.3 | `std::vector<bool>` vekil nesnesine `auto&` bağlanamaz, `auto&&` çalışır | [vector.bool]; test | doğru |
| 7 | 23.4 | Üç grup: sıralı, birleşik, sırasız birleşik kaplar; kap uyumlandırıcıları | [sequences], [associative], [unord], [container.adaptors.general]/2. Grup adları ve "kap uyumlandırıcısı" terim biçimiyle tanıtılmıyor (sözlükte "container adaptor" Cilt I 23.4); "sıralı kaplar" (sequence) ile birleşik kapların "elemanları sıralı tutar"ı (sorted) aynı sözcüğü iki anlamda kullanıyor; "karma tablosu" tanıtılmıyor | biçim (terim) |
| 8 | 23.4 | Birleşik kaplarda arama logaritmik; sırasızlarda ortalama sabit | [associative.reqmts]/8 tablo, /11; [unord.req]/11 tablo ("Average case O(1), worst case O(b.size())") | doğru |
| 9 | 23.4 | `map`'te `[]` anahtar yoksa oluşturur | [map.access]/1 (`try_emplace`); test | doğru |
| 10 | 23.4 | `vector` bitişik; önbellek davranışı daha iyi | [vector.overview]/2 (contiguous container). Önbellek bir donanım gözlemi, öğüt olarak yazılmış | doğru |
| 11 | 23.5 | `emplace_back` doğrudan oluşturur, argümanları mükemmel gönderimle iletir | [sequence.reqmts], Cilt II 1.2.5 | doğru |
| 12 | 23.6 | `v{1, 2, 3}`; `push_back(4)` sonrası `*it` "tanımsız davranış" | [vector.modifiers]/1: yalnızca yeniden yer ayrılırsa bütün iteratörler geçersiz; ayrılmazsa ekleme noktasından öncekiler geçerli. `capacity()` standartta belirtilmez (test: `reserve(10)` sonrası `*it` geçerli) | eksik |
| 13 | 23.6 | "`vector`'de yeniden yer ayırma her şeyi geçersizleştirir; `list` ve `map`'te yalnızca silinen elemanın iteratörü geçersizleşir" | [vector.modifiers]/1, /3: yer ayırma olmasa da ekleme ve silme, o konumdaki ve sonrasındaki iteratörleri geçersiz kılar; [list.modifiers]/1, /3, [associative.reqmts]/9: ekleme hiçbirini geçersiz kılmaz | eksik |
| 14 | 23.7 | `std::remove` mantıksal sonu döndürür, sondakilerin değerine güvenilmez; `std::erase` C++20 | [alg.remove]/4, /7 (valid but unspecified); [vector.erasure]/1; test (`-std=c++17`'de yok) | doğru |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): bölümdeki kod örnekleri geçerli;
`std::vector<bool>` ile `for (auto& x : vb)` sentaks hatası, `auto&&` geçerli;
`std::contiguous_iterator` `vector`, `array`, `string` için doğru, `deque` için yanlış;
`deque` rastgele erişimli, `map` çift yönlü; `std::sort` `std::list` ile sentaks hatası;
`std::vector<int> v{1, 2, 3}` için `capacity()` 3, `reserve(10)` sonrası `push_back`
`begin()`'i geçersiz kılmıyor; `std::erase` `-std=c++17`'de yok; `m["yok"]` boyutu 1 yapıyor.
