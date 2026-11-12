# Tarama — Cilt I Kısım 13 (Kasım 2026)

Kısım 13'teki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar C++20
(N4861) bölüm adlarıyla; C++23'te (N4950) farklıysa ayrıca. 13.0 normatif iddia içermiyor.
13.4, 13.5, 13.6, 13.8 ve 13.10'daki iddialar doğru; dosyalar değişmedi.

**İşlem (2026-11):** "düzeltilmeli", "eksik", "gerçekleme" ve "biçim" sonuçlu bütün iddialar
düzeltildi; metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-12_c1-13-tarama`,
beş tur; Claude hakemi xhigh). Panel ayrıca şunları düzeltti: izinli elemenin "gerçeklemeye
bağlı" sayılmaması, "aynı türden" PR-Value koşulu, `static` yerel nesneler ve parametreler,
taşıma yapılamadığında kopyalama, Rule of Zero kutusunun varsayılan kurucuyu kapsamaması,
"kaynak" ve "silinmiş" sözcüklerinin iki anlamda kullanılmaması, Cilt II 3 atfının
kapsamı (yalnızca 3.5'teki iki kural).

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 13.1 | Derleyicinin yazabileceği altı üye işlev | [special]/1. "Özel üye işlevler" terimi (sözlük, Cilt I 13.1) metinde tanıtılmıyor | doğru (biçim) |
| 2 | 13.1 | Kurucu/atama ayrımı: nesne o anda mı oluşuyor | [class.copy.ctor], [class.copy.assign] | doğru |
| 3 | 13.2 | "Siz hiçbir şey yazmazsanız derleyici altısını da yazar" | [class.copy.ctor]/10, [class.copy.assign]/7: örtülü bildirilen işlev bazı durumlarda silinmiş tanımlanır (ör. referans ya da `const` elemanlı sınıfın kopyalayan ataması) | eksik |
| 4 | 13.2 | Kopyalama işlevleri her veri elemanını bildirim sırasıyla kopyalar | [class.copy.ctor]/14: önce taban sınıflar, sonra veri elemanları. "Üye üye kopyalama" terim biçiminde değil | eksik |
| 5 | 13.2 | Varsayılan kopyalamanın "yetmediği tek bir durum" | Kaynak yönetimi başlıca durumdur; tek değildir (ör. kendi elemanını gösteren gösterici). Atıf biçimi "13.5" | eksik |
| 6 | 13.3 | Kopyalayan kurucu işlev "üç yerde" çağrılır; 2. "değer döndüren işlevin dönüşü" | C++17'den beri PR-Value döndürülünce ya da argüman PR-Value iken kopyalama yapılmaz ([dcl.init]/17.6.1, [stmt.return]); yerel nesne döndürülürken önce taşıma denenir ([class.copy.elision]/3). 13.12 ile çelişiyor. Kural: aynı türden bir L-Value'dan ilk değer verilirken. "call-by-value" İngilizce | düzeltilmeli |
| 7 | 13.4 | Kopyalayan atama işlevi; `T&` döndürür | [class.copy.assign]/2, /7 | doğru |
| 8 | 13.5 | Üye üye kopyalama kaynak yöneten sınıfta çift serbest bırakmaya, tanımsız davranışa yol açar | [expr.delete]/2 (C++20 /12) | doğru |
| 9 | 13.6 | Big-Three | Öğüt | doğru |
| 10 | 13.7 | Taşıma, "hayatının biteceği garanti" olan nesneden kaynak devralmaktır | `std::move` ile işaretlenen L-Value'nun ömrü bitmez; ölçüt nesnenin artık kullanılmayacak olmasıdır (Kısım 2.4.7) | eksik |
| 11 | 13.7 | Kod: `noexcept` | `noexcept` Cilt I'de anlatılmıyor (Cilt II 13.2); atıf yok | doğru (atıf eksik) |
| 12 | 13.7 | Kaynağı alınan nesne "sonlandırıcı işlevi güvenle çalışabilecek" duruma getirilmeli | Geçerli durumda bırakılmalı: yeniden atanabilmeli de ([lib.types.movedfrom], Kısım 2.4.7) | eksik |
| 13 | 13.7 | Taşıyan işlev yoksa kopyalayan çağrılır; yokluğunda program yalnızca yavaş çalışır | Taşıyan işlev silinmiş bildirilmişse çağrı sentaks hatasıdır ([dcl.fct.def.delete]/2); yalnızca taşınabilen türlerde (ör. `std::unique_ptr`) kopyalama da yoktur | eksik |
| 14 | 13.8 | Bir işlevi bildirmek diğerlerinin örtülü bildirimini engeller | [class.copy.ctor]/8, [class.copy.assign]/4 | doğru |
| 15 | 13.9 | Rule of Zero kutusu: `unique_ptr`, `shared_ptr` | Kitabın kuralı `std::` öneki; akıllı göstericiler Kısım 25 | biçim |
| 16 | 13.10 | `= default`, `= delete`; silinmiş işlevi çağırmak sentaks hatası | [dcl.fct.def.default], [dcl.fct.def.delete]/2 | doğru |
| 17 | 13.11 | Kopyalayan kurucuda atlanan eleman "ilk değer almamış" kalır | [class.base.init]/9: default-initialization ile ilk değer alır (Kısım 12.10 ile aynı düzeltme) | düzeltilmeli |
| 18 | 13.11 | "Derleyicinin uyarı vermediği" hatalar | Derleyici uyarısı standardın konusu değil | gerçekleme |
| 19 | 13.11 | Kendine atamada silinmiş bellekten kopyalama | Tanımsız davranıştır; metin sonucu söylemiyor. Atıf biçimi "13.7" | eksik |
| 20 | 13.12 | "Derleyici bu kopyalamayı çoğu durumda ortadan kaldırır; bir kısmında yapmak zorundadır" | [class.copy.elision]/1: yerel nesnede eleme izinlidir (gerçekleme seçer); PR-Value'da C++17'den beri kopya yoktur ([dcl.init]/17.6.1). Özne "derleyici"; C++17 bağlamı yok | eksik |
| 21 | 13.12 | `return std::move(mx);` elemeyi engeller, taşıyan kurucu çağrılır | [class.copy.elision]/1.1 (yalnızca yerel nesne ismi) | doğru |
| 22 | 13.12 | "`const` bir dönüş değeri taşınamaz; kopyalanmak zorunda kalır" | İlk değer vermede C++17'den beri kopya da taşıma da yoktur (`Myclass x = foo();`, cv yok sayılır); sorun atamadadır: `x = foo();` kopyalayan atamayı çağırır | düzeltilmeli |
| 23 | 13.12 | "Yerel nesneye referans döndürmek tanımsız davranıştır" | Döndürmek değil, döndürülen referansı kullanmak tanımsız davranıştır ([basic.life]/7) | eksik |

Not (Kısım 12 panelinden): 12B panelinin 3. turunda yazar bilgisi olarak "Kısım 13.12'de
Standart Notu — C++17 kutusu var" yazıldı; bu yanlıştı (kutu Cilt II 1.1.5'te). 12.17'deki
"C++17'den itibaren … (Kısım 13.12)" cümlesi doğru kalıyor; 13.12 bu taramayla C++17 bağlamını
söyler hâle geliyor.
