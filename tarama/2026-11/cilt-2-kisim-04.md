# Tarama — Cilt II Kısım 4 (Kasım 2026)

Kısım 4'teki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış), **biçim** (terim
tanıtımı, atıf). Kaynaklar C++23 (N4950) bölüm adlarıyla. 4.0 normatif iddia içermiyor.
Terim tanıtımında İngilizce karşılık eksik: "specialization" (4.2, Türkçesi yazılmamış),
"örtülü örnekleme" (4.2), "tam özelleştirme" (4.3), "kısmi özelleştirme" (4.4), "işlev
parametre paketi" (4.5), "akım iteratörleri", "ekleme iteratörleri" (4.12) (biçim).
Kütüphane adları metinde kimi yerde `std::` öneksiz
(`iterator_traits`, `back_inserter`, `front_inserter`, `inserter`, `move_iterator`,
`invoke`; `type_traits` başlık adı `<type_traits>` biçiminde değil).

**İşlem (2026-11):** "düzeltilmeli", "eksik", "gerçekleme" ve "biçim" sonuçlu bütün iddialar
düzeltildi; metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-24_c2-04-tarama`,
üç hakem, dört hakem turu; durma kuralı tur 4'te sağlandı; uzunluk 700 → 820 brief v2).
Yazar kararıyla 4.9 ve 4.11'e Standart Notu — C++20 kutusu açıldı. Panel ayrıca şunları
düzeltti: yapısal sınıfta koşulların statik olmayan elemanlara uygulanması ve dizi
elemanlar, açık örneklemede tanımı taşınamayan işlevler (dönüş türü çıkarılan, `inline`,
`constexpr`) ve hata hükmünün sınırı, `typename`'in şablon argüman listelerinde hâlâ
zorunlu olması, `std::iterator_traits`'te `value_type`'ın işlemlerden çıkarılmaması ve
çıkış iteratörü durumu (yazarın ilk testi yanlış raporlanmıştı), ADL'nin yalnızca
ilişkili isim alanında bulması, `std::apply`'ın çağırdığı şey. Terim tanıtımları ve
`std::` önekleri uygulama adımında yapıldı (panele gitmedi).

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 4.1 | Başlık "Şablon parametrelerinin dört grubu"; dördüncü grup "Parametre paketleri"; "Cilt I'de ikisi tanıtılmıştı" | [temp.param]/1–2 dilbilgisi: üç biçim (*type-parameter*, *parameter-declaration*, şablon şablon parametresi); /17: her biri `...` ile paket olur. Cilt I 22.3 artık üç biçimi ve paketi tanıtıyor, ilk ikisini kullanıyor | düzeltilmeli |
| 2 | 4.1 | Tür olmayan parametre: "Tamsayı türleri, `enum` türleri, gösterici ve referanslar kullanılabilir; C++20'den itibaren kayan noktalı türler ve sade sınıf türleri" | [temp.param]/6–7: yapısal tür (*structural type*): skaler tür (üye göstericisi ve `std::nullptr_t` dahil), sol taraf referansı, koşulları sağlayan sabit ifadeye uygun sınıf türü (bütün taban ve elemanlar `public`, `mutable` olmayan, kendileri yapısal); yer tutucu (`auto`) türler. Test: `int&&` parametre sentaks hatası; `mutable` elemanlı sınıf yapısal değil; `int S::*`, `std::nullptr_t`, `double`, `auto` geçerli. "Sade" tanımsız | eksik |
| 3 | 4.1 | Şablon şablon parametresi örneği; `Sarmalayici<int, std::vector>` | [temp.param]/3, [temp.arg.template]; test | doğru |
| 4 | 4.2 | Örnekleme; ürüne "specialization" denir; terim iki anlamlı | [temp.spec.general]/4; sözlük: özelleştirme (iki anlamlı). Türkçe karşılık yazılmamış | doğru; biçim (terim) |
| 5 | 4.2 | Örtülü örnekleme kullanıldığı yerde; `template class Kutu<int>;` açık örnekleme tanımı | [temp.inst], [temp.explicit]/2 | doğru |
| 6 | 4.2 | "Açık örnekleme, şablon tanımını başlık dosyasından çıkarıp tek bir çeviri biriminde derlemeye yarar; derleme süresini kısaltır ama esnekliği azaltır" | [temp.explicit]/11: sınıf şablonunun açık örneklenmesi yalnızca o noktada tanımlı üyeleri örnekler; sınıfın tanımı tamamlanmış tür gereken her çeviri biriminde gerekir ([basic.def.odr]); başlıktan çıkabilen, işlev şablonlarının ve üye işlevlerin tanımlarıdır. /13: `extern template` açık örnekleme bildirimi. Derleme süresi standartta yok | eksik; gerçekleme |
| 7 | 4.3 | Tam özelleştirme; işlev özelleştirmeleri yükleme çözümlemesine katılmaz, önce şablon seçilir | [temp.over]/1: aday kümesi şablonlardan çıkarımla üretilen bildirimler ve şablon olmayan işlevler; tam özelleştirme aday değildir. Test: `f(T)`'nin `int*` özelleştirmesi varken `f(p)` `f(T*)`'i seçiyor | doğru |
| 8 | 4.4 | Kısmi özelleştirme yalnızca sınıf ve değişken şablonlarında | [temp.decls.general]/2 ("which shall be a class or variable template"); test: işlev şablonunda sentaks hatası | doğru |
| 9 | 4.4 | Cilt II 1.1.7'deki `p<T&>`, `p<T&&>` | 01-01-07 dosyası | doğru |
| 10 | 4.5 | Parametre paketi sıfır ya da daha çok argüman; `sizeof...`; paket açma deseni her eleman için yineler | [temp.variadic]/1, /2, /5, /9 | doğru |
| 11 | 4.5 | "C++17 öncesinde paketi işlemenin tek yolu özyinelemeydi" | [temp.variadic]/5: paket açma C++11'den beri ilk değer listesinde de yapılabilir (`int d[] = {0, (f(a), 0)...};`); test (`-std=c++11`). Özyineleme tek yol değildi | düzeltilmeli |
| 12 | 4.6 | Katlama ifadesi parantez içinde; dört biçim ve açılımları; boş paket: `&&` `true`, `\|\|` `false`, `,` `void()`; öteki operatörlerde sentaks hatası | [expr.prim.fold] dilbilgisi; [temp.variadic]/10, Tablo 20; test (`(... + a)` boş pakette hata) | doğru |
| 13 | 4.7 | CTAD; örtülü çıkarım kuralları; `Kutu(const char*) -> Kutu<std::string>;` | [over.match.class.deduct]/1, [temp.deduct.guide]/3; test: `Kutu k{"merhaba"}` `Kutu<std::string>` | doğru |
| 14 | 4.7 | Kutu: "**Neden değişti:** … dilin en sık şikâyet edilen tutarsızlıklarından biriydi" | P0091R3, "Summary"/"The problem": gerekçe, tür argümanlarının işlevlerdeki gibi argümanlardan çıkarılabilmesi ve `make_` işlevlerinin yapay, tutarsız ek kod olması. "En sık şikâyet edilen" önergede yok | düzeltilmeli |
| 15 | 4.8 | "Şablon argüman yerleştirmesi sırasında geçersiz bir tür oluşursa … aday listeden düşer" | [temp.deduct.general]/8: geçersiz tür **ya da ifade** | eksik |
| 16 | 4.8 | "Kural yalnızca doğrudan bağlamda geçerlidir; yani imzada" | [temp.deduct.general]/7–8: yerleştirme yerleri işlev türü (`noexcept` hariç), `explicit` belirteci ve şablon parametresi bildirimleri; bunların doğrudan bağlamı. /8 not: yerleştirmenin tetiklediği sınıf şablonu örneklemesindeki hata doğrudan bağlamda değildir. Test: imzadaki `Kotu<T>::t` içindeki hata gerçek hata. Örnekteki `std::enable_if_t` şablon parametresi bildiriminde, "imza" değil | eksik |
| 17 | 4.9 | Bağımsız isimler tanım noktasında aranır ve bağlanır | [temp.res.general]/1, Örnek 2 (`f(1)` sonradan bildirilen `f(E)`'yi görmez); test | doğru |
| 18 | 4.9 | "Bağımlı isimler … şablonun örneklendiği noktada aranır" | [temp.res.general]/1; [basic.lookup.argdep]/4: bağımlı çağrıda olağan nitelenmemiş arama tanım bağlamından; argümana bağlı arama ayrıca örnekleme bağlamından da yapılır. Test: tanımdan sonra bildirilen `k(E)` bulunuyor, `k(int)` bulunmuyor | eksik |
| 19 | 4.9 | `typename` ve `template` zorunluluğu; `<` karşılaştırma sanılır | [temp.res.general]/5, [temp.names]/3; test | doğru |
| 20 | 4.9 | "C++20, `typename`'in zorunlu olduğu yerlerin bir kısmında yazma zorunluluğunu kaldırdı" | [temp.res.general]/4–5 (yalnızca tür olabilen bağlam), P0634R3. Hangi yerler olduğu söylenmiyor; örnekteki blok kapsamı bildirimde `typename` hâlâ zorunlu (test). Test: `using deger = T::deger_turu;` C++20'de geçerli, C++17'de sentaks hatası | eksik |
| 21 | 4.10 | `typedef` şablonlaştırılamaz; Cilt I 16.1 atfı; değişken şablonu; `_v` adları `::value`'nun kısaltması | [temp.alias]; [meta.type.synop] (`inline constexpr bool is_integral_v = is_integral<T>::value;`); Cilt I 16.1 | doğru; biçim (`<type_traits>`) |
| 22 | 4.11 | "Algoritmaların bu kategoriyi sorgulayabilmesi için, her iteratörün beş tür bilgisi sunması gerekir" | C++17 (N4659 [iterator.traits]/2): beş üye tür. C++20 ile [iterator.traits]/3.1: dört üye yeter, `pointer` yoksa `void`; /3.2: dört üyeden biri eksikse ve iteratör *cpp17-input-iterator* ise eksikler hesaplanır (`value_type` yine üye `value_type`/`element_type`'tan gelir). Test: `pointer`'sız sınıfta `void`; yalnızca `value_type` üyeli iteratörde kategori ve `difference_type` hesaplanıyor | eksik |
| 23 | 4.11 | `std::iterator_traits` göstericiler için kısmi özelleştirilmiş; temsili kodda `value_type = T` | [iterator.traits]/5: `requires is_object_v<T>`, `iterator_concept = contiguous_iterator_tag`, `value_type = remove_cv_t<T>`. Test: `const int*` için `value_type` `int` | eksik |
| 24 | 4.12 | Akım, ekleme ve taşıma iteratörleri; ekleme iteratörü yazmayı ekleme çağrısına çevirir | [back.insert.iter.ops]; [stream.iterators]; [move.iterators]; test (bölüm kodu) | doğru |
| 25 | 4.12 | "Algoritmaların kaba eleman eklememesi sorununu çözer (bkz. Cilt I Kısım 23.7)" | Cilt I 23.7 algoritmaların eleman silmediğini ve kabın boyutunu değiştirmediğini söylüyor; eklemeden söz etmiyor | biçim (atıf) |
| 26 | 4.12 | Taşınan elemanlar kaynağı devralınmış durumda (Kısım 2.5) | [lib.types.movedfrom]; Cilt II 2.5 | doğru |
| 27 | 4.13 | `std::apply`, `std::invoke` tek tip çağrı | [tuple.apply]/1, [func.invoke], [func.require] (INVOKE) | doğru |
| 28 | 4.13 | "`std::apply` da zaten arka planda onu çağırır" | [tuple.apply]/1: etki, açıklama amaçlı *apply-impl* içinde INVOKE işlemiyle tanımlı; `std::invoke` çağrısı değil, onunla aynı çağırma kuralı ([func.invoke]/1 de INVOKE) | gerçekleme |

Testler (Apple clang 21, `-std=c++23 -pedantic-errors`): bölümdeki kod örnekleri geçerli;
tür olmayan parametre olarak `int S::*`, `std::nullptr_t`, `double`, yapısal sınıf, `auto`,
`int&` geçerli, `int&&` ve `mutable` elemanlı sınıf sentaks hatası; `f(T)`'nin `int*`
tam özelleştirmesi varken `f(p)` `f(T*)`'i seçiyor; işlev şablonunun kısmi özelleştirmesi
sentaks hatası; `int d[] = {0, (std::cout << a, 0)...};` paketi özyinelemesiz işliyor;
boş paketle `(... + a)` sentaks hatası, `(... && b)` `true`; `Kutu k{"merhaba"}`
`Kutu<std::string>`; imzadaki `Kotu<T>::t`'nin içindeki hata aday düşürmüyor, gerçek hata;
`g(e)` `k(char) k(E)`, `g('a')` `k(char) k(char)`; tanımdan sonra bildirilen `k(int)`
bağımlı çağrıda bulunmuyor; `using deger = T::deger_turu;` C++20'de geçerli, C++17'de
sentaks hatası; blok kapsamında `T::deger_turu x;` C++23'te de sentaks hatası;
`pointer`'sız dört üyeli iteratörde `std::iterator_traits<I>::pointer` `void`; yalnızca
`value_type` üyeli iteratörde kategori `std::forward_iterator_tag` hesaplanıyor, hiç üye
türü olmayanda `std::output_iterator_tag`; `std::iterator_traits<const int*>::value_type` `int`.
