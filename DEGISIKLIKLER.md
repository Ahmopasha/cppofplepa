# Değişiklik kaydı

## Yayımlanmamış

### Düzeltmeler

- Cilt I ve geçişlerinin `son_kontrol` etiketi cildin ufkuna uyduruldu: `(C++23)` yerine
  `(C++20)`; tarihler değişmedi. `BAKIM.md`'ye etiketin anlamı eklendi.
- Cilt I Kısım 6 (Aşama 2 taraması; iddia tablosu `tarama/2026-10/cilt-1-kisim-06.md`):
  - 6.1: `extern const` bildirimi ve varsayılan kurucusuyla ilk değer alan sınıf türleri
    ayrıldı; C'de `const` değişkenin ilk değersiz tanımlanabildiği yazıldı.
  - 6.2: "C'de bu dönüşüm serbesttir" ve "C'de derlenir" yanlıştı; C'de de kısıt ihlalidir.
    Başlık "`const`luğu koruyan iki kural" oldu. Yazı sabitini doğrudan değiştirme sentaks
    hatasıyla sınırlandı; `const_cast` ve C'deki tanımsız davranış eklendi.
  - 6.5: Örtülü iç bağlantı kuralının istisnaları eklendi.
  - 6.6: "Derleyici ... çalıştırmaz" anlatımı standardın diliyle yazıldı; `consteval` eklendi.
- Cilt II Kısım 3 (Aşama 2 taraması; iddia tablosu `tarama/2026-10/cilt-2-kisim-03.md`):
  - 3.1: Eliminasyon bağlamları standarda göre (eşyordam parametresi, sabit ifade ve sabit
    ilk değer verme istisnası); aynı türden PR-Value ile ilk değer verme ayrıca anlatıldı.
  - 3.2, 3.4, 3.6: "Derleyiciye ve optimizasyon seviyesine bağlıdır" anlatımları çıktı.
  - 3.3: İlk paragraf 1.1.5'e uyduruldu; kural genelleştirildi; `throw`'da kopyalayan
    kurucu şartı; trivial türlerde ek geçici nesne istisnası; C++17 öncesi yıkım sırası.
  - 3.4: Kurucu seçimi X-Value için yükleme çözümlemesiyle; örtülü taşımanın C++23, C++20 ve
    C++11–17 kuralı (Kısım 1.1.2'nin Standart Notu artık buraya gerçek bir atıf veriyor).
  - 3.5, 3.7: `const T` dönüş türü eliminasyonu değil taşımayı engeller; koşullu dönüş
    kopyalanır; `if`/`return` yazımında NRVO izinli; parametre istisnası.
  - 2.7: Giriş cümlesi iki senaryoyu doğru ayırıyor (ikincisinde taşıyan kurucu çağrılır).
  - Terim sözlüğüne "uygun" *(eligible)* eklendi.
- Cilt II Kısım 2 (Aşama 2 taraması; iddia tablosu `tarama/2026-10/cilt-2-kisim-02.md`):
  - 2.1: Bildirilmemiş işlev çağrısının sonucunu kalan yüklemeler belirler; silinmiş olarak
    tanımlanan örtülü ya da ilk bildiriminde `= default` taşıyan işlevlerin yok sayılması.
  - 2.2, 2.6, 2.7: "Derleyici uyarı vermez" cümleleri standarda göre yazıldı.
  - 2.4: Örnekteki fark `is_trivially_copyable`'a değil `is_trivially_default_constructible`'a
    yansır.
  - 2.5: "Aksi belirtilmedikçe" kaydı; ön koşulu olan ve olmayan işlemler ayrımı.
  - 2.6: `vector` kuralı `reserve` ve tek öğeyi sona eklemeyle, kopyalanabilen türlerle
    sınırlandı; örnekteki `Yazi`'ye kopyalayan kurucu eklendi; örtülü `noexcept`.
  - 2.8: `operator=(Yazi)` kopyalayan atama işlevidir ve taşıyan kurucuyu baskılar; örneğe
    taşıyan ve kopyalayan kurucu ile sonlandırıcı eklendi.
- Cilt I Kısım 8 (Aşama 2 taraması; iddia tablosu `tarama/2026-10/cilt-1-kisim-08.md`):
  - 8.1: Referans "bir isim" değil; bağlandığı nesneyi belirtir. Geçici bir değere bağlanan
    referans yeni bir geçici nesneye bağlanır.
  - 8.2: İlk değer zorunluluğunun istisnaları (`extern`, veri elemanı, parametre, dönüş
    türü) eklendi. "Geçersiz referans yoktur" yerine boş referans yoktur; referans sarkabilir.
  - 8.3: "İfadenin sonunda" yerine tam ifadenin sonunda; ömrün uzatılması `T&&` için de
    geçerli.
  - 8.4: Türler aynı değil uyumlu olmalı (`const` ekleme, taban sınıf); `const` düşürmek
    sentaks hatası.
  - 8.6: L-Value referans döndüren çağrı L-Value, `T&&` döndüren X-Value; derleyici uyarısı
    anlatımı çıktı; geçici argümana dönen referansın sarkması eklendi.
  - 8.9: "Üçüncü referans türü" yanlıştı; başlık "Şablonlarda `T&&`" oldu.
  - Terim sözlüğüne tam ifade ve boş referans eklendi.
- Cilt II Kısım 15 (Aşama 2 taraması; iddia tablosu `tarama/2026-10/cilt-2-kisim-15.md`):
  - 15.1: "Derleyicinin tek yükümlülüğü" yerine soyut makinenin gözlemlenebilir davranışı
    ve tanımsız davranış sınırı; sıralı tutarlılık, koşulunu sağlayan programlarla
    sınırlandı; "en pahalı" gerçekleme gözlemi oldu.
  - 15.2: `std::thread` kuralı bir iş parçacığını temsil eden nesneyle sınırlandı;
    sonuç "`std::terminate` çağrılır" diye verildi.
  - 15.3: `mutex` türleri dört değil altı.
  - 15.4: Yüklemli `wait`'in `while (!pred()) wait(lock);` eşdeğeri ve yalancı uyanma.
  - 15.5: Hata taşımanın "tek yolu" `future` değil; örneğe `<thread>` ve `<utility>`.
  - 15.6: Başlatma ilkesinin değerleri, `deferred`'ın `get`/`wait` ile çalışması,
    ilkesiz çağrıda seçimin gerçeklemede olması, sonlandırıcının yalnızca `async`
    seçildiğinde beklemesi.
  - 15.8: `is_lock_free`/`is_always_lock_free` ayrımı; `atomic_flag`'in "tek kilitsiz
    tür" olması C++20 öncesiyle sınırlandı, C++20 üyeleri eklendi; işleç biçimleri
    `memory_order` almaz; tabloya `acq_rel`, `relaxed`'in değişiklik sırası ve `consume`.
  - 15.9: `par` izindir; vektörleşme kuralı `unseq` için de geçerli; öğe erişim
    işlevinden kaçan hatada `std::terminate`.
  - 15.10: Ayırıcının iç yapısı gerçekleme gözlemi oldu; data race kuralının kapsamı
    global ayırma işlevleriyle sınırlandı; atıf ayırıcı gereksinimlerine (Kısım 17.7).
  - Terim sözlüğüne dokuz terim eklendi.
- Cilt II Kısım 1 (Aşama 2 taraması; iddia tablosu `tarama/2026-10/cilt-2-kisim-01.md`):
  - 1.1.1: "Kimlik" `&`'nin operandı olabilmekle tanımlanıyordu; X-Value'nun kimliği olduğu
    hâlde adresinin alınamadığı yazıldı.
  - 1.1.2, 1.2.5: "İsimler L-Value'dur" değişken adlarıyla sınırlandı; `return`, `co_return`
    ve `throw` istisnası (taşınmaya uygun adlar, C++23'te X-Value) ve Standart Notu — C++23
    kutusu eklendi.
  - 1.1.3: İşlev isimleri için "her zaman" çıktı, statik olmayan üye işlev istisnası
    eklendi; üçlü operatörün kategori kuralı [expr.cond]'a göre yeniden yazıldı.
  - 1.1.5: PR-Value'nun sonuç nesnesi ve materialization durumları standarda göre
    anlatıldı ("materialization olmazsa nesne yoktur" yanlıştı); Standart Notu uyduruldu.
  - 1.1.7: `decltype((e))` iç parantezinin gerekçesi düzeltildi.
  - 1.2.1: Başlık "Üçüncü referans türü" iken "`T&&`'nin şablondaki anlamı" oldu;
    forwarding reference ayrı bir referans türü değil, çıkarım kuralıdır.
  - 1.2.3, 1.2.4, 1.2.7: `T`'nin taşıdığı bilgi, `volatile` R-Value istisnası ve küme
    parantezli liste istisnası düzeltildi.
  - 1.2.5: Mükemmel gönderimin "hiçbir fark bırakmadığı" iddiası kaldırıldı; kalan farklar
    (PR-Value'nun X-Value olarak iletilmesi, `0`, küme listeleri) yazıldı.
- Cilt II Kısım 17 (Aşama 2 taramasının ilk kısmı; iddia tablosu
  `tarama/2026-10/cilt-2-kisim-17.md`):
  - 17.1: `operator new`'ün `malloc`'tan "farkı yoktur" deniyordu; new handler döngüsü,
    `bad_alloc` ve değiştirilebilirlik farkları yazıldı. `delete`'in bırakma işlevi seçimi
    standarda göre anlatıldı.
  - 17.2: Yalnızca `operator new` yüklendiğinde global `operator delete` çağrılır
    ("serbest bırakılamaz" deniyordu); sınıf düzeyindeki boyutlu `operator delete`
    C++14'ten önce de vardı; iki biçim birlikteyse boyutsuz olan seçilir. Örnekteki
    `operator new` artık `bad_alloc` gönderiyor; gerçekleme anlatan "sistem çağrısı"
    cümlesi silindi.
  - 17.5: Dinamik ilk değer vermenin `main`'den önce yapılması gerçeklemeye bağlı
    (ertelenebilir) olarak yazıldı; aynı çeviri birimindeki sıra "tanım sırası" oldu ve
    sırasız/kısmen sıralı istisnaları eklendi; "derleme zamanında dosyaya yazılır" ve
    "derleyici kilit ekler" gibi gerçekleme anlatımları standardın ifadeleriyle değişti.
  - 17.7: Ayırıcının asgari arayüzü tamamlandı (`==`, dönüştüren kurucu, kopyalama/taşıma,
    hata göndermeme); `rebind` varsayılanının koşulu yazıldı.
  - 17.8: `alignof` değerleri, sınıf hizalaması, `max_align_t` ve genişletilmiş hizalama
    standarda göre düzeltildi.
  - Terim sözlüğüne altı terim eklendi.
- Cilt I 23.7: `std::remove` için "silinecek elemanları sona iter" deniyordu. Doğrusu,
  silinmeyecek elemanları başa kaydırması; kabın boyutu değişmez ve mantıksal sondan
  itibaren elemanların değerine güvenilmez. Gerekçe için Cilt II 2.5'e atıf eklendi;
  Cilt II 2.5'e de 23.7'ye geri atıf eklendi.
- Cilt II 16.4: Hem ana metin hem Standart Notu, tek bir `operator<=>` bildiriminin altı
  operatörü birden sağladığını her durum için söylüyordu; bu yalnızca `= default` için
  geçerli. Anlatım yeniden yazma kuralına göre düzeltildi: `<=>` dört ilişkisel
  operatörü, `==` de `!=`'yi karşılar; örtülü `==` yalnızca sınıf hiçbir `operator==`
  bildirmemişse gelir; elle yazılan `<=>`'nin yanına `==` aynı ölçütle yazılmalıdır;
  `==` ile `<=>`'nin tutarlılığı programcıya kalır.
- Kod denetiminin bulduğu, örneğin kendisinin derlenmediği ya da "sentaks hatası" denen
  satırın geçerli olduğu yerler düzeltildi:
  - Cilt I 9.2: `void func(int); void func(const int);` için "sentaks hatası" deniyordu;
    ikisi aynı işlevin geçerli bildirimleridir. Örnek, hatanın ancak ikinci tanımda
    çıktığını gösterecek biçimde yeniden yazıldı. "Göstericilerde `const` imzanın
    parçasıdır" cümlesi gösterilen nesneyle sınırlandı; göstericinin kendi `const`u üst
    düzeydir ve yok sayılır.
  - Cilt I 12.7: `const Myclass cm;` derlenmiyordu (sınıfın kullanıcı tanımlı varsayılan
    kurucu işlevi yok); `const Myclass cm{};` yapıldı.
  - Cilt I 14.4 ve Cilt II 16.1: veri elemanları `private` olan `Kesir`'in kurucu işlevi
    yoktu, `Kesir{...}` derlenmiyordu; kurucu işlev eklendi.
  - Cilt II 13.3: `Der` ve `Der2` taban sınıftan türetilmemişti, `override` geçersizdi;
    kalıtım eklendi.
  - Cilt II 1.2.6: `Myclass` şablon olduğu için `void f4(Myclass&&)` derlenmiyordu;
    parametre `std::string&&` yapıldı. `f2` satırının yorumu da düzeltildi: `T`
    çıkarılır, ama parametre `T&&` biçiminde değildir.
- Kod denetiminin bulduğu son üç sorun düzeltildi:
  - Cilt I 12.12: Kurucu işlevin doğrudan ya da dolaylı olarak kendine devretmesi
    "tanımsız davranış" diye anlatılıyordu; standarda göre derleyicinin bildirmek zorunda
    olmadığı bir hatadır *(ill-formed, no diagnostic required)*. Terim sözlüğe eklendi.
  - Cilt II 1.1.4: İkinci örnekteki ilk değersiz referans bildirimleri `using` eş
    adlarına çevrildi. `decltype`'ın bildirilen türü verdiği durum parantezsiz sınıf
    üyesi erişimini de kapsayacak biçimde yazıldı; "(x) artık bir ifadedir" yorumu
    düzeltildi.
  - Cilt II 16.5: Literal operatör bildirimlerine geri dönüş türü eklendi; izin verilen
    parametre listeleri standarttaki tam listeye göre yazıldı (şablon olmayan biçimler,
    `wchar_t`/`char8_t`/`char16_t`/`char32_t`, varsayılan argüman yasağı).
- Kitap artık derleyici davranışını değil yalnızca C++ standardını anlatıyor. İki Derleyici
  Notu kutusu kaldırıldı:
  - Cilt II 1.1.7: MSVC'nin `std::move(foo)` için X-Value bildirdiği söyleniyordu; güncel
    MSVC doğru sonucu veriyor. Kutunun taşıdığı dil kuralı Cilt II 1.1.3'e istisna olarak
    taşındı: `T` bir işlev türüyse `T&&` döndüren çağrı L-Value üretir. 1.1.7'nin son
    örneğine eksik `<iostream>` eklendi; standart `exp` adını gölgeleyen makro `EXP` oldu.
  - Cilt II 17.6: Clang'ın davranışını anlatan kutu kaldırıldı; standardın hükmü (CWG
    1696) ana metinde duruyor.

### Bakım

- Kod denetiminin başarı sinyali sıkılaştırıldı (Kimi ve ChatGPT incelemeleri):
  - `derle.py --kod`, kod denetimi çalışamazsa (ör. derleyici yok) başarısız döner ve
    `--kati`'yi kod denetimine de aktarır; önceden sonuç ne olursa olsun 0 dönüyordu.
  - Çalıştırılan örneğin çıkış kodu denetlenir: tanımlı davranışlı örnek 0 ile bitmelidir;
    başka bir kod ya da sinyal bekleyen örnek `cikis-N`/`cikis-sinyal` işaretiyle belirtilir.
  - Derleyici farkı artık kendiliğinden muaf değil: çalışma zamanı bulguları hiç muaf
    tutulmaz; derleme farkı yalnızca bloğun özetine ve derleyici sürümüne bağlı gerekçeli
    bir kayıtla geçer ve kayıt aynı bloğun çalışma zamanı bulgusunu kapatmaz
    (`DERLEYICI_FARKI_ISTISNALARI`; Cilt II 17.6 ve Cilt II Kısım 18
    taramasının iki farkı kaydedildi).
  - Kod denetimi iş akışı `tarama/**` değişikliklerinde de çalışır; araç testleri
    (`araclar/testler/`) iş akışında koşar.
- Depo köküne yapay zekâ oturumları için `CLAUDE.md` eklendi.
- Terim sözlüğüne "Kullanılmayan karşılıklar" bölümü eklendi; `derle.py` bu sözcükleri
  uyarır. Kitaptaki 11 "fonksiyon" "işlev" oldu (Cilt I 2.4.1, 2.4.4, 2.4.6 başlığı,
  23.4; Cilt II 1.1.2, 1.1.5, 14.7 başlığı). *hash function* → karma işlevi sözlüğe eklendi.
- Aşama 2 taraması başladı: normatif iddia tabloları `tarama/` altında; kod denetimi
  tablolardaki test kodlarını da derler. İlk tablo Cilt II Kısım 17.
- README'ye Leanpub bağlantısı ve GitHub Releases yönlendirmesi eklendi.
- `BAKIM.md`: standart ufku kuralına kusur raporu istisnası eklendi; sürüm yayımlama
  adımlarına GitHub Release ve tanıtım metinlerindeki sayıların güncellenmesi eklendi.
- `YOL_HARITASI.md` eklendi.
- Terim sözlüğü: *candidate* → aday, *rewritten candidate* → yeniden yazılmış aday,
  *comparison category* → sıralama kategorisi.
- Kod denetimi eklendi (`araclar/kod_denetimi.py`, `derle.py --kod`): kitaptaki her kod
  bloğu Cilt I için C++20, Cilt II için C++23 ile `-pedantic-errors` bayrağıyla derlenir;
  "sentaks hatası" denen satırların tam o satırda hata verdiği doğrulanır, Kısım 1'in C ve
  C++ farkı örnekleri iki dilde sınanır, `main()` içeren örnekler sanitizer ile
  çalıştırılır. Tek başına derlenemeyen 82 bloğun önüne okurun görmediği işaretler kondu
  (bkz. BAKIM.md, "Kod örnekleri"). GitHub Actions'ta GCC ve Clang ile rapor üreten bir iş
  eklendi. Sorunlu blok kalmadığı için iş artık `--kati` ile çalışır.
- Kod denetimi, kodun hemen üstündeki çok satırlı `/* ... */` yorum bloğunu tanır; bloğun
  içindeki "sentaks hatası" gibi işaretler altındaki satıra ait sayılır.

## Sürüm 1.1 — Ekim 2026

### Yapı

- Kitap, her alt başlık ayrı bir dosya olacak biçimde bölündü (`cilt-1-temel/`,
  `cilt-2-ileri/`). Ciltler ve PDF artık `araclar/derle.py` ile bu dosyalardan derleniyor.
  Bölme kayıpsızdır: geçişsiz derleme, bu sayfada sayılan değişiklikler dışında
  Sürüm 1.0'ın metnini harfi harfine verir.
- Kısımlar arasına ve iki cilt arasına geçiş paragrafları eklendi (`gecisler/`). Cilt I
  artık "Cilt I'den Cilt II'ye" başlıklı kısa bir kapanışla bitiyor; Cilt II'nin ön
  metnine, bölümlerinin Cilt I'deki karşılıklarını gösteren bir tablo eklendi.
- Cilt II'de, bölüm dosyaları birleştirilirken kalmış üç fazla yatay çizgi kaldırıldı
  (1.1 ile 1.2 arası, Kısım 2 ve Kısım 6 sonu).

### Düzeltmeler

- Cilt I 6.6: `constexpr` kısıtlarının gevşemesi ile `consteval` ve `constinit` için
  verilen atıf Cilt II Kısım 16'yı gösteriyordu; doğrusu Kısım 18.
- Cilt I 15.5: `operator new` / `operator delete` yüklemesi, `placement new` ve
  `std::set_new_handler` için verilen atıf Cilt II Kısım 16'yı gösteriyordu; doğrusu
  Kısım 17.
- Cilt II 8.7: Kısım 14'te bulunmayan bir "pipeline operator" deyimine yapılan atıf
  kaldırıldı.
- Cilt II ön metni: "karşılığını bilindiği varsayar" → "karşılığının bilindiğini
  varsayar".
- Cilt I 2.5: Tanımsız davranış örneklerindeki `char* p = "merhaba";` satırı C++11'den
  beri sentaks hatasıydı ve 6.2 ile çelişiyordu. Yerine işaretli tamsayı taşması örneği
  kondu.
- Cilt I 6.6: `constexpr` işlevin gövdesinde dinamik bellek ayırmanın ve `static` yerel
  nesnelerin yer alamayacağı söyleniyordu. Bu, C++20 ve C++23 ile gevşeyen kurallarla ve
  Cilt II 18.1 ile çelişiyordu. Paragraf, derleme zamanında yürütülen kodun neleri
  yapamayacağını anlatacak biçimde düzeltildi.
- Cilt I 8.3 ve Cilt II 17.6: Veri elemanı olan referansa bağlanan geçici nesne, C++14
  dahil önceki standart metinlerinin kuralıyla anlatılıyordu; CWG 1696'dan beri ilk değer
  verme listesinde böyle bir bağlama sentaks hatası. İkinci istisnanın kuralı, kurucu
  işlevle ilk değer alan referans veri elemanıyla sınırlandı (küme parantezli bileşik tür
  ilk değer vermesinde, `new` ifadesi dışında, ömür uzar). 17.6'daki örneğin mekanizması
  düzeltildi, geçersiz bağlama ayrı bir örnekle gösterildi ve derleyici farkı için bir
  Derleyici Notu eklendi. 8.3'te *sarkan referans* terimi tanıtıldı.
- Cilt I 25.5: Özel silici, kontrol bloğu ve `enable_shared_from_this` için Cilt II
  Kısım 14'e verilen atıf boşa gidiyordu; artık Cilt II 17.9'a gidiyor. `unique_ptr`'ın
  maliyetinin çıplak göstericiyle aynı olduğu cümlesi varsayılan siliciyle sınırlandı.

### Eklemeler

- Cilt II 17.9 "Özel silici, kontrol bloğu ve `enable_shared_from_this`" eklendi. Cilt I
  25.5'in Cilt II'ye bıraktığı üç konuyu ders notlarına dayanarak anlatır; `shared_from_this`
  için bir Standart Notu (C++17) içerir.
- Cilt II 18.1: `constexpr` işlevlerin gevşeyen kısıtlarının kronolojisine C++23
  paragrafı eklendi (`static`/`thread_local` ve literal olmayan türden değişkenler, `goto`,
  hiç sabit değerlendirilemeyen `constexpr` işlev, literal tür şartının kalkması); Cilt I
  6.6'nın atfı buna göre güncellendi.
- Cilt I 5.2: Farklı iki `enum` türünün değerlerini karşılaştırmanın C++20'den beri artık
  önerilmediği *(deprecated)* eklendi.
- Terim sözlüğü: *control block* → kontrol bloğu, *custom deleter* → özel silici,
  *dangling reference* → sarkan referans, *deprecated* → artık önerilmiyor,
  *literal type* → literal tür, *defect report* → kusur raporu.
- Cilt II ön metnindeki tabloda Kısım 17'nin Cilt I karşılığına Kısım 25 eklendi.

### Bakım

- `BAKIM.md`'ye standart ufku kuralı eklendi: kitap Necati Ergin'in kurslarında izlenen
  standartlara bağlıdır (Cilt I C++20, Cilt II C++23). "C++26 taraması" açık konusu bu
  kararla kaldırıldı.

## Sürüm 1.0 — Eylül 2026

İlk yayım.
