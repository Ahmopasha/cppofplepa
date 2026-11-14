# Tarama — Cilt I Kısım 17 (Kasım 2026)

Kısım 17'deki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış), **biçim** (terim
tanıtımı, atıf). Kaynaklar C++20 (N4861) bölüm adlarıyla. 17.0 normatif iddia içermiyor;
17.3 ve 17.10'daki iddialar doğru, dosyalar değişmedi.

**İşlem (2026-11):** "düzeltilmeli", "eksik" ve "biçim" sonuçlu bütün iddialar düzeltildi;
metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-13_c1-17-tarama`, üç hakem,
iki hakem turu; durma kuralı tur 2'de sağlandı; Claude hakemi xhigh). Panel ayrıca şunları
düzeltti: kalıtımın "arayüz" yerine "üyeler" ile tanımı, geçersiz kılmada `const`
niteleyicisi, "gizler" → "gölgeler" (17.5 başlığı da), sanal sonlandırıcı kuralının silme
koşuluna bağlanması ve sızıntı cümlesinin çıkarılması, `protected` kalıtımda erişim
ölçütü, `using` ile yükleme, çok biçimli sınıf tanımı (10.2'nin atfı için), üye işlev
içindeki `this` çağrısı, çok katmanlı soyutluk. Yazar kararıyla reddedilen: C++20
destroying `operator delete` istisnası (kitapta anlatılmıyor; Aşama 3 envanteri).

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 17.1 | "Kalıtım", "taban sınıf", "türemiş sınıf" | Üç terim kitapta hiç tanıtılmıyor (2.4.5'ten beri kullanılıyor), sözlükte yok; yazar kararı: 17.1'de tanıtılır | biçim (terim) |
| 2 | 17.1 | "Her türemiş sınıf nesnesi, aynı zamanda bir taban sınıf nesnesidir" (is-a) | Yalnızca `public` kalıtımda (17.2'nin kendi ifadesi; Cilt II 6.7). Metin kalıtım biçimini söylemeden genelliyor | eksik |
| 3 | 17.1 | Taban sınıf tamamlanmış tür olmalı | [class.derived]/2; test: `struct B; struct D : B {};` sentaks hatası | doğru |
| 4 | 17.2 | Üç kalıtım biçimi; diğer ikisi "Cilt II'de" | Cilt II 6.7 | doğru; biçim (atıf) |
| 5 | 17.2 | Varsayılan: `class` → `private`, `struct` → `public` | [class.access.base]/2 | doğru |
| 6 | 17.3 | Kurma sırası: taban, veri elemanları bildirim sırasıyla, gövde; sonlanma tersi | [class.base.init]/13; [class.dtor]/14 (kurucuların tamamlanma sırasının tersi) | doğru (sanal taban basitleştirmesi) |
| 7 | 17.3 | Taban sınıfın varsayılan kurucusu yoksa ve listede çağrılmazsa sentaks hatası | [class.base.init]/13; test | doğru |
| 8 | 17.4 | Örtülü dönüşüm "`public` kalıtımda güvenlidir" | [conv.ptr]/3: taban sınıf erişilemiyor ya da çift anlamlıysa dönüşüm sentaks hatası. `private` kalıtımda dönüşüm "güvensiz" değil, sınıf dışında yapılamaz (test). "Çok biçimlilik" burada tanıtılmadan kullanılıyor | eksik; biçim (atıf) |
| 9 | 17.5 | Türemiş sınıftaki isim tabandakini gizler; arama ilk bulduğu kapsamda durur | [class.member.lookup]/4–5; test | doğru |
| 10 | 17.5 | "birbirinin `overload`'ı olmaz" | Kitabın terimi "işlev yüklemesi" (sözlük, Cilt I 9.1); `overload` anahtar sözcük değil, kod yazıtipinde olmamalı | biçim (terim) |
| 11 | 17.5 | `using Base::func;` ile taşıma; imzalar aynıysa türemişteki seçilir | [namespace.udecl]/14 | doğru |
| 12 | 17.5 | `private` üye için `using` bildirimi sentaks hatası | [namespace.udecl]/17: getirilen bildirimlerin hepsi erişilebilir olmalı; test | doğru |
| 13 | 17.6 | "Sanal işlev", "geçersiz kılmak", "çok biçimlilik" | Kitapta tanıtılmıyor; 10.2 "çok biçimli"yi Kısım 17.6'ya atıfla kullanıyor | biçim (terim) |
| 14 | 17.6 | Dinamik bağlama için "işlevi `virtual` bildirmek yeterlidir" | Çağrı gösterici ya da referans üzerinden ve nitelenmeden yapılmalı: nesne üzerinden çağrıda statik ve dinamik tür aynı; nitelenmiş çağrı sanal mekanizmayı kapatır ([class.virtual]/16). 17.9, Cilt II 6.2 | eksik |
| 15 | 17.6 | `override` yazılırsa derleyici geçersiz kılmayı doğrular | [class.virtual]/5: geçersiz kılmıyorsa sentaks hatası; test | doğru |
| 16 | 17.6 | "Bir işlev bir kez `virtual` olduysa hiyerarşinin geri kalanında öyle kalır" | [class.virtual]/1–2: sanal bir işlevi geçersiz kılan işlev (aynı isim, parametre listesi, cv ve referans niteleyicisi) sanaldır. Aynı isimli ama farklı parametreli işlev sanal olmaz (17.5'teki gizleme) | eksik |
| 17 | 17.7 | Sanal olmayan sonlandırıcıyla taban göstericisinden `delete` tanımsız davranış | [expr.delete]/3 | doğru |
| 18 | 17.7 | "Kaynak sızıntısına yol açan gerçek bir hatadır ve derleyici sizi uyarmaz" | Sonuç tanımsız davranıştır; "kaynak sızıntısı" olası sonuçlardan biri. Standart tanı istemez; "uyarmaz" derleyici davranışı | eksik |
| 19 | 17.8 | Saf sanal işlev: "işlevi bildirip tanımlamamak istersiniz" | [class.abstract]/2: saf sanal işlev tanımlanabilir; yalnızca nitelenmiş isimle çağrılırsa tanımı gerekir (test). Doğrusu: tanımlamak zorunda kalmadan bildirmek. "Saf sanal işlev", "soyut sınıf", "somut sınıf" İngilizcesiz tanıtılıyor | eksik; biçim (terim) |
| 20 | 17.8 | En az bir saf sanal işlev → soyut; nesne oluşturulamaz; türemiş hepsini geçersiz kılmazsa soyut kalır | [class.abstract]/2–4 | doğru |
| 21 | 17.9 | `Sekil s = d;` dilimlenme örneği | Bir önceki bölüm (17.8) `Sekil`'i soyut tanımladı; o `Sekil` ile `Sekil s = d;` sentaks hatasıdır (test, [class.abstract]/3). Örnek 17.6'daki soyut olmayan `Sekil`'e dayanıyor ama bunu söylemiyor | eksik (örnek) |
| 22 | 17.10 | Kurucu/sonlandırıcıda sanal çağrı türemişe gitmez | [class.cdtor]/4 | doğru |
| 23 | 17.10 | Varsayılan argüman statik türe göre seçilir | [dcl.fct.default]/10 | doğru |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): bölümdeki kod örnekleri geçerli;
`class D : B {}` için sınıf dışında `B* p = &d;` sentaks hatası, `D`'nin üye işlevinde
geçerli; `private` üye için `using B::f;` sentaks hatası; soyut `S` ile `S s = d;` sentaks
hatası, `const S& r = d;` geçerli; tanımlı saf sanal işlev `S::c()` ile çağrılabiliyor;
geçersiz kılmayan `override` sentaks hatası; tamamlanmamış taban sentaks hatası.

Notlar:
- 17.1 ve 17.10 "composition" terimini İngilizce kullanıyor; Kısım 21 taramasında
  "bileşik" terim çakışmasıyla birlikte kullanıcıya sorulacak.
- "Static binding" / "dynamic binding" İngilizce bırakılmış; Türkçe karşılık yazar kararına
  bırakıldı.
