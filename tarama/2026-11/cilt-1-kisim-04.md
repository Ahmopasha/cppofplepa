# Tarama — Cilt I Kısım 4 (Kasım 2026)

Kısım 4'teki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar C++20
(N4861) bölüm adlarıyla; C++23'te (N4950) farklıysa ayrıca. 4.0 normatif iddia içermiyor.
4.1'deki iddialar doğru; dosya değişmedi.

**İşlem (2026-11):** "düzeltilmeli", "eksik" ve "gerçekleme" sonuçlu bütün iddialar ile atıf ve
terim eksikleri düzeltildi; metinler AI hakem panelinden geçti
(`~/ai-panel/calismalar/2026-11-06_c1-04-tarama`, beş tur). Panel ayrıca şunları düzeltti:
`const` sınıf türünden R-Value'ya `auto&` bağlanması, `const auto&`'ın işleve bağlanması,
göstericinin kendi `const`unun düşmesi, `return`'süz işlevde `void` ve özyineleme kuralı,
başlıkta `inline` tanım. Geri dönüş türü çıkarımının kuralları ve `decltype` Cilt I'de
anlatılmıyor; Aşama 3 kapsam envanterine bırakıldı.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 4.1 | `auto` türü ilk değer veren ifadeden çıkarır; `auto s = "merhaba";` `const char*` | [dcl.type.auto.deduct]/2–4, [temp.deduct.call]/2 (dizi göstericiye dönüşür) | doğru |
| 2 | 4.1 | İlk değer vermeden `auto` değişken tanımlanamaz | [dcl.spec.auto]/4 (C++20 [dcl.spec.auto.general]) | doğru |
| 3 | 4.1 | C'deki `auto` ile ilgisi yoktur; C++11 anlamı değiştirdi | C17 6.7.1 (saklama sınıfı); C++11 N2546 | doğru |
| 4 | 4.2 | `auto x = expr;` referanslığı ve üst düzey `const`luğu düşürür | [temp.deduct.call]/2–3. "Üst düzey `const`" kitapta ilk kez burada geçiyor, tanıtılmıyor; alt düzey `const`un korunduğu söylenmiyor | eksik |
| 5 | 4.2 | Sonuç bağımsız bir kopyadır | [dcl.init] | doğru |
| 6 | 4.2 | `auto&`'ta "referanslık korunur" | `auto&` her zaman L-Value referans üretir; ifadenin referanslığından bağımsızdır. `auto& y = 10;` sentaks hatasıdır ([dcl.init.ref]/5) — metin bunu söylemiyor | eksik |
| 7 | 4.2 | `auto&` `const`luğu korur; `const auto&` her zaman `const` referans | [temp.deduct.call]/3 | doğru |
| 8 | 4.2 | `auto&&` her şeye bağlanır; aralık tabanlı `for`'da güvenli tercih | [temp.deduct.call]/3 (forwarding reference). Kısım 8.9 ve 23.3'e atıf yok ("bkz. Kısım 23") | doğru (atıf eksik) |
| 9 | 4.3 | `auto x = expr;` dizi ve işlev ismini göstericiye dönüştürür; `auto&` dönüştürmez | [temp.deduct.call]/2. "Çürüme" *(decay)* terimi tanıtılmıyor, sözlükte yok | doğru (terim eksik) |
| 10 | 4.4 | Lambda türü yazılamaz; şablonlarda `auto` | [expr.prim.lambda.closure]/1. Lambda (Kısım 24) ve şablonlara (Kısım 22) atıf yok | doğru (atıf eksik) |
| 11 | 4.4 | `v.size()` `std::size_t` döndürür | [vector.overview]: `size_type` gerçeklemeye bağlı işaretsiz tamsayı türüdür ([container.reqmts]); `std::allocator` ile pratikte `std::size_t` | gerçekleme |
| 12 | 4.4 | `int boyut2 = v.size();` "uyarı verebilir" | Derleyicinin tanısı standardın konusu değil; dönüşüm geçerlidir, değer sığmayabilir | gerçekleme |
| 13 | 4.4 | "açıkça `int` yazmak hatalıdır" | Kod geçerlidir; "hatalı" kitapta sentaks hatası anlamında da kullanılıyor | düzeltilmeli |
| 14 | 4.5 | `auto a2{10};` `int`; `auto a3 = {10};` `std::initializer_list<int>`; `auto a4{10, 20};` sentaks hatası | [dcl.type.auto.deduct]/2 (N3922) | doğru |
| 15 | 4.5 | "Kural: `auto` ile eşittir yazımını kullanın" | `auto a3 = {10};` de eşittirlidir; kural kendi örneğiyle çelişiyor (3.9 artık "eşittir ve tek değer" diyor) | eksik |
| 16 | 4.5 | Standart Notu: "çok elemanlı olan `auto` ile sentaks hatasıdır" | Yalnızca eşittirsiz yazımda; `auto x = {1, 2};` geçerlidir | eksik |
| 17 | 4.6 | Sondan yazılan geri dönüş türünde `auto` tür çıkarmaz; parametre isimlerine başvurulabilir | [dcl.fct]/2, [basic.scope.pdecl] | doğru |
| 18 | 4.6 | Faydası parametrelere bağlı türde | Bunu gösteren örnek yok; `decltype` Cilt I'de anlatılmıyor (Cilt II 1.1.4) — örnek anlatılanı göstermiyor | eksik |
| 19 | 4.6 | C++14'ten itibaren geri dönüş türü çıkarılabilir; tanım çağrıldığı yerde görünür olmalı, başlık/kaynak ayrımında kullanılamaz | [dcl.spec.auto]/11 (C++20 [dcl.spec.auto.general]/11): tür çıkarılmadan işlev kullanılırsa program geçersizdir. Kısıt "aynı çeviri biriminde, çağrıdan önce" | doğru (kesinleştirilebilir) |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): `const int* pc; auto x5 = pc;`
`const int*`; `const auto& z = 10;` geçerli, `auto& y4 = 10;` sentaks hatası;
`auto i4 = {10, 20};` geçerli; `decltype(v.size())` `std::vector<int>::size_type`.
