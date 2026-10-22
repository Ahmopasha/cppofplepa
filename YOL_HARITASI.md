# Yol haritası

Kitabın bakımı ve geliştirilmesi için sıradaki işler. Sıra, getiriye göre: önce doğruluk,
sonra otomatik denetim, sonra okurun kullanımı, en son yeni içerik. Bir aşama bitince ilgili
maddeler işaretlenir; plan değişirse bu dosya güncellenir.

Bu planın dayanağı Ekim 2026'da yapılan bir değerlendirmedir. Somut tespitler depodan,
GitHub'dan ve Leanpub sayfasından doğrulandı.

---

## Aşama 0 — Hemen yapılacaklar

- [x] **Cilt I 23.7:** "`std::remove`, silinecek elemanları sona iter" yanlış. `remove`
  korunan elemanları başa taşır; yeni mantıksal son ile eski son arasının içeriği
  belirsizdir. Düzeltme panelden geçer.
- [x] **Cilt II 16.4:** Standart Notu, "tek bir `operator<=>` bildirimi altısını birden
  üretir" diyor. Bu yalnızca `= default` için doğru; elle yazılan `<=>` `==` üretmez. Ana
  metinle uyumlu hâle getirilir. Düzeltme panelden geçer.
- [x] **README:** Başa Leanpub bağlantısı (<https://leanpub.com/cppofplepa>).
- [x] **GitHub depo açıklaması:** "226 sayfa" Leanpub'daki 235 ile tutmuyordu; sayfa
  sayısı açıklamadan çıkarıldı.
- [x] **GitHub konu etiketleri ve Website alanı:** `cpp`, `cpp20`, `cpp23`, `turkish`,
  `book`; Website: <https://leanpub.com/cppofplepa>.
- [x] **Leanpub tanıtımı:** GitHub bağlantısı sondaki noktayı adrese katıyor
  (`…/cppofplepa.`); düzeltilir.
- [x] **BAKIM.md, standart ufku:** "Kusur raporları hariç" notu eklenir. Kusur raporları
  (DR) eski standartlara da uygulanır ve derleyiciler onları eski `-std` kiplerine işler;
  ufkun ötesinde kabul edilmiş bir DR kitabın ufkunu da ilgilendirebilir (örnek: Sürüm
  1.1'deki CWG 1696 düzeltmesi).
- [x] **BAKIM.md, sürüm yayımlamak:** "Tanıtım metinlerindeki sayıları (sayfa, kısım,
  kutu) güncelle" adımı eklenir. `derle.py` bu sayıları `bakim_durumu.md`'ye yazdırabilir.

`v1.0` etiketi verilmez: Sürüm 1.0'ın birebir karşılığı olan bir commit yok, depo kitabın
alt başlıklara bölünmesinden sonra açıldı. Bu geçmişi DEGISIKLIKLER.md anlatıyor.

---

## Aşama 1 — Kod denetimi

Kitabın en çok hata barındıran ve en hızlı eskiyen kısmı kod örnekleridir. Şu anki denetim
yapısaldır (başlık numaraları, atıflar, kutu listeleri); kodu derlemez.

- [x] **Örneklerin işaretlenmesi.** Bloğun türünü (parça, tam program, bilerek hata
  veren satır, tanımsız davranış) araç kendisi bulur: parçaları bir işlev gövdesine
  koyar, aynı dosyadaki önceki bloğu ve `araclar/kod_baglami.hpp`'deki yer tutucu adları
  bağlam olarak kullanır, hata satırlarını ve "tanımsız" yorumlarını okur. Okurun
  görmeyeceği HTML yorumu yalnızca bunun yetmediği 82 blokta var (`kod: atla`,
  `kod-baglam`, `kod: c`; bkz. BAKIM.md, "Kod örnekleri").
- [x] **`derle.py --kod`.** `araclar/kod_denetimi.py` her bloğu ayrı bir dosyaya çıkarır;
  Cilt I'i `-std=c++20`, Cilt II'yi `-std=c++23` ile, `-pedantic-errors` bayrağıyla
  derler. Yerelde Clang, GitHub Actions'ta GCC 14 ve Clang 18 kullanılır.
  `-pedantic-errors` olmadan derleyiciler birçok geçersiz yapıyı yalnızca uyarıyla
  geçirir (Sürüm 1.1'de düzeltilen `char* p = "merhaba";` bunun örneğiydi).
- [x] **Bilerek hata veren satırların doğrulanması.** `// sentaks hatası` ile işaretli
  satırlar çıkarılınca kalan kodun sorunsuz derlendiği, satırlar tek tek geri konunca her
  birinin tam o satırda hata verdiği denetlenir. Satır hem ad alanı düzeyinde hem işlev
  gövdesinde sınanır; böylece test yanlış nedenle (ör. yanlış yerleşim ya da eksik bir
  bildirim) geçmez. Derleyicinin mesajı raporda kitabın açıklamasının yanında durur.
- [x] **C ve C++ farkı örnekleri.** Kısım 1'deki "C'de geçerli, C++'ta değil" örnekleri
  hem C17 hem C++ derleyicisinde sınanır.
- [x] **Sanitizer.** `main()` içeren örnekler `-fsanitize=address,undefined` (iş
  parçacığı kullananlar `-fsanitize=thread`) ile çalıştırılır: "tanımsız" denen örnek
  gerçekten öyle mi, "doğru" denen örnek gizlice tanımsız mı.
- [x] **Kademeli devreye alma.** İlk raporda 504 bloğun 10'u sorunluydu; hepsi kitap
  metnindeki hatalardı ve panelden geçerek düzeltildi (Cilt I 9.2, 12.7, 12.12, 14.4;
  Cilt II 1.1.4, 1.2.6, 13.3, 16.1, 16.5). Sorunlu blok kalmayınca `kod-denetimi.yml`
  `--kati` ile çalışmaya başladı (2026-10-22).
- [x] ~~**Derleyici Notu testleri.**~~ Kaldırıldı (2026-10-21). Kitap artık derleyici
  davranışını değil yalnızca standardı anlatıyor; iki Derleyici Notu kutusu kaldırıldı,
  testleri ve aylık iş akışı da onlarla birlikte gitti (bkz. BAKIM.md, "Derleyici farkı").

---

## Aşama 2 — Sürekli teknik doğruluk taraması

- [ ] **Ritim.** Her ay, `son_kontrol` tarihi en eski olan yaklaşık 8 kısım taranır; 46
  kısım altı ayda bir dolaşılır. İlk turda riskli konulardan başlanır: nesne ömrü,
  referanslar, taşıma, `constexpr`, ranges, eşzamanlılık.
- [ ] **Yöntem.** Yapay zekâya "bu bölüm doğru mu?" diye sorulmaz; dosyadaki her normatif
  iddia ("tanımsız davranıştır", "geçersizdir", "C++17'den beri") bir tabloya dökülür,
  her birine standarttaki bölüm adı ve iddiayı sınayan kısa bir kod eklenir. Kodlar
  Aşama 1'deki denetimden geçer. Kanıtı olmayan ya da derleyiciyle çelişen iddialar
  incelenir.
- [ ] **Kümülatif ilke sorusu.** Cilt I dosyalarında: "Bu dosyadaki hangi cümle C++23'te ya
  da Cilt II'deki anlatım karşısında yanlış kalır?"
- [ ] **Bulguların işlenmesi.** Esaslı her düzeltme AI hakem panelinden (`cpp-kitap`
  ölçütü) geçer. Hakemlerin internet erişimi olmadığı için standart iddiaları birincil
  kaynaktan (önerge, cppreference) ve kod derlenerek panelin dışında doğrulanır. Gözden
  geçirme, metni yazan oturumdan bağımsız bir oturumda yapılır.
- [ ] **Depo köküne `CLAUDE.md`.** BAKIM.md'yi gösterir; üstüne yalnızca yapay zekâya özgü
  kuralları ekler: kanıtsız iddia yok, her normatif iddiaya bir test kodu, derlenmeyen
  kod "derlendi" diye yazılmaz.
- [ ] **Terim uyarısı.** `derle.py`, terim sözlüğünde tercih edilmeyen karşılıkları uyarı
  olarak bildirir. İlk adım: kitapta 8 dosyada geçen 11 "fonksiyon" (616 "işlev"in
  yanında; biri `02-04-06-fonksiyon-parametresini-nasil-secersiniz.md` dosya adında).

---

## Aşama 3 — Kapsam tablosu ve Sürüm 1.2 içeriği

- [ ] **`kapsam.md`.** Dört sütun: hocanın kurs programı, ders notları, kitaptaki dosya,
  durum (anlatılıyor / kısmen / yok / bilinçli olarak dışarıda).
- [ ] **Önce notlarda olup kitapta olmayan konular.** Kaynağı ders notları olduğu için
  provenans değişmez. Notlardaki geçiş sayılarıyla (satır):

  | Konu | C++ notları | İleri C++ notları | Kitapta |
  |---|---|---|---|
  | `std::chrono` | 60 | 91 | yalnızca 16.5'te geçiyor |
  | `std::regex` | 112 | 86 | yok |
  | `<random>` | 59 | 27 | yok |
  | Attribute'lar (`[[nodiscard]]` …) | 32 | 40 | yok |
  | `decltype(auto)` | — | 41 | yalnızca 0.2 tablosunda |
  | Semaforlar, `std::call_once` | — | 21 / 14 | yok |

  Bilerek dışarıda bırakılan konu varsa tabloda öyle işaretlenir.
- [ ] **Sonra yalnızca hocanın güncel programında olanlar.** `std::expected`,
  `std::mdspan`, `std::flat_map`/`flat_set`, `std::stacktrace`, `if consteval`, çok
  boyutlu `operator[]`. Bunlar "derleyen (ders notlarında yok)" kaynağıyla yazılır ve
  README'deki provenans tablosuna eklenir. Notlara dayanmayan pay büyüyeceği için
  Aşama 1 bunlardan önce bitmiş olmalıdır.
- [ ] **Yöntem.** Her yeni alt başlık notlardan çıkarılır, kod örnekleri derlenir ve
  `cpp-kitap` ölçütüyle panelden geçer (Sürüm 1.1'deki Cilt II 17.9 gibi).

---

## Aşama 4 — Okur tarafı

| Öncelik | İş | Not |
|---|---|---|
| Yüksek | Terim sözlüğünü PDF'e eklemek (iki dilli dizin) | Sözlük depoda var ama `derle.py` kitaba katmıyor. Okur çoğu zaman İngilizce terimle ("copy elision") arar |
| Yüksek | GitHub Issue formu | BAKIM.md'deki altı değişiklik türü açılır liste olarak; dosya yolu ya da başlık numarası alanı |
| Orta | Karar ve başvuru tabloları | "Hangi kabı seçmeli?", "değer mi, referans mı, gösterici mi?", iteratör geçersizleşmesi, özel üye işlevler, tür çıkarımı |
| Orta | EPUB | Leanpub şu an yalnızca PDF sunuyor; `derle.py --epub` |
| Orta | Web sürümü (MkDocs Material ya da mdBook, GitHub Pages) | Her alt başlık zaten ayrı dosya; arama ve kalıcı adres gelir. Her sayfaya dosya yolunu dolduran "bu sayfada hata bildir" bağlantısı |
| Sonra | Kısım sonu soruları ("derlenir mi, tanımsız davranış mı?") | Aşama 1 bitmeden başlanmaz; cevaplar da derlenerek doğrulanır |
| Sonra | Diyagramlar | Değer kategorileri, `vptr` yerleşimi, `vector` kapasite büyümesi |
| Sürekli | Görünürlük | Türkçe C++ toplulukları ve LinkedIn'de duyuru; hocaya kitabı öğrencileriyle paylaşmak isteyip istemeyeceğini sormak |

Atıfların kalıcılığı da bu aşamada ele alınabilir: alt başlıklara numaradan bağımsız
kimlikler vermek, araya başlık eklenince bir atfın var olan ama yanlış bir başlığa gitmesini
önler (BAKIM.md, "Numaralandırma").

---

## Aşama 5 — Düzenli bakım takvimi

| Ne zaman | Ne |
|---|---|
| Her değişiklikte | `python3 araclar/derle.py --kati`; ilgili kod örneklerinin derlenmesi; değişen dosyaya atıf yapan yerlerin okunması; esaslı metinler için panel |
| Ayda bir | 8 kısımlık doğruluk taraması; okur bildirimleri; hocanın `KURS_PROGRAMLARI` deposundaki iki programın takibi (değiştiğinde issue açan zamanlanmış bir iş) |
| Her sürümde | Sürüm satırı, DEGISIKLIKLER.md, `vX.Y` etiketi, PDF'li GitHub Release, Leanpub yüklemesi, tanıtım metinlerindeki sayıların eşleşmesi, PDF'in gözle kontrolü |
| Üç ayda bir | Kapsam tablosu, kaynak bağlantıları, panelin modelleri (`./panel.sh preflight`) |

---

## Çalışma ilkeleri

- Kitabın kuralları BAKIM.md'dedir; bu dosya yalnızca sırayı ve kapsamı tutar.
- Standart ufku değişmez: Cilt I C++20, Cilt II C++23 (kusur raporları hariç).
- Panele yalnızca esaslı metin gider; tek kelimelik düzeltmeler, tablo satırları ve tarih
  alanları gitmez.
- Panel brief'lerindeki alıntılar güncel tutulur; eski bir alıntı hakemleri yanlış bulguya
  götürür.
- Uzunluk sınırları cömert konur; onaylanan eklemeler metni uzatır.
