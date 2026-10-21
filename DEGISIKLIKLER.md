# Değişiklik kaydı

## Yayımlanmamış

### Düzeltmeler

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
- Kitap artık derleyici davranışını değil yalnızca C++ standardını anlatıyor. İki Derleyici
  Notu kutusu kaldırıldı:
  - Cilt II 1.1.7: MSVC'nin `std::move(foo)` için X-Value bildirdiği söyleniyordu; güncel
    MSVC doğru sonucu veriyor. Kutunun taşıdığı dil kuralı Cilt II 1.1.3'e istisna olarak
    taşındı: `T` bir işlev türüyse `T&&` döndüren çağrı L-Value üretir. 1.1.7'nin son
    örneğine eksik `<iostream>` eklendi; standart `exp` adını gölgeleyen makro `EXP` oldu.
  - Cilt II 17.6: Clang'ın davranışını anlatan kutu kaldırıldı; standardın hükmü (CWG
    1696) ana metinde duruyor.

### Bakım

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
  eklendi.
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
