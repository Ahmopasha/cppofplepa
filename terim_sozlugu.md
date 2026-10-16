# Terim Sözlüğü

C++ Kitap Projesi · ek belge

Kitapta kullanılan Türkçe karşılıkların dizini. Metinde bir terim ilk geçtiğinde
`**Türkçe karşılık** *(İngilizce terim)*` biçiminde tanıtılır; sonraki kullanımlarda
yalnızca Türkçe karşılık geçer.

---

## 1. Terim seçme ilkeleri

**Standart terim birincildir, ders terimi parantez içinde verilir.** İki terim yaygın
kullanımdaysa, standart metnindeki tercih edilir; dersleri izlemiş okuyucu için diğeri
ilk geçişte eş anlamlı olarak tanıtılır.

Uygulandığı yer: `forwarding reference` birincil, `universal reference` eş anlamlı
(Cilt II 1.2.1). Notlarda ikincisi 30, birincisi 3 kez geçmesine rağmen standart terim
seçildi.

**Yerleşmiş kısaltmalar çevrilmez.** RAII, RTTI, ADL, CTAD, ODR, SFINAE, STL, NVI, CRTP,
UDL, EBO kısaltma olarak bırakıldı; açılımları ilk geçişte verildi.

**Anahtar sözcükler çevrilmez.** `const`, `constexpr`, `mutable`, `inline`, `virtual`,
`friend`, `override`, `final` ve benzerleri kod yazımıyla, tırnak içinde geçer.

**Betimlemeler çevrilmez ama sözlüğe de girmez.** Notlardaki `opaque` gibi, standart
terimi olmayan nitelemeler yerinde bırakıldı (Cilt II 9.2). Bunlar terim değil, anlatım
öğesidir.

**Notlardaki yazım hataları normalize edildi.** `inheritence` → `inheritance`,
`Referance` → `reference`, `Ellision` → `elision`, `Mandotary` → `mandatory`,
`Assigningment` → `assignment`, `Funciton` → `function`, `Kalıyım` → `kalıtım`.

---

## 2. İngilizce → Türkçe

### Temel kavramlar

| İngilizce | Türkçe | İlk geçtiği yer |
|---|---|---|
| declaration | bildirim | Cilt I 2.1 |
| definition | tanım | Cilt I 2.1 |
| scope | kapsam | Cilt I 2.2 |
| name lookup | isim arama | Cilt I 2.3 |
| shadowing | gölgelenme | Cilt I 2.2 |
| undefined behaviour | tanımsız davranış | Cilt I 2.5 |
| unspecified behaviour | belirtilmemiş davranış | Cilt I 2.5 |
| implementation-defined | gerçeklemeye bağlı davranış | Cilt I 2.5 |
| translation unit | çeviri birimi | Cilt I 0.3 |
| complete / incomplete type | tamamlanmış / tamamlanmamış tür | Cilt I 2.6 |
| padding | dolgu | Cilt II 17.8 |
| alignment | hizalama | Cilt II 17.8 |
| strict aliasing | katı örtüşme kuralı | Cilt II 11.7 |
| deprecated | artık önerilmiyor | Cilt I 5.2 |
| literal type | literal tür | Cilt II 18.1 |
| defect report | kusur raporu | Cilt II 17.6 |

### Değer kategorileri ve referanslar

| İngilizce | Türkçe | İlk geçtiği yer |
|---|---|---|
| value category | değer kategorisi | Cilt I 2.4.1 |
| L-Value / R-Value / PR-Value / X-Value / GL-Value | çevrilmedi, olduğu gibi kullanılır | Cilt I 2.4.2 |
| reference collapsing | referans çökmesi | Cilt II 1.2.2 |
| forwarding reference *(universal reference)* | çevrilmedi | Cilt II 1.2.1 |
| perfect forwarding | mükemmel gönderim | Cilt II 1.2.5 |
| life extension | ömrün uzatılması | Cilt I 8.3 |
| dangling reference | sarkan referans | Cilt I 8.3 |
| materialization | çevrilmedi | Cilt II 1.1.5 |
| result object | çevrilmedi | Cilt II 1.1.5 |

### Sınıflar ve kalıtım

| İngilizce | Türkçe | İlk geçtiği yer |
|---|---|---|
| data member | veri elemanı | Cilt I 12.2 |
| member function | üye işlev | Cilt I 12.2 |
| type member / nested type | tür üyesi / içsel tür | Cilt I 12.2, 12.18 |
| constructor | kurucu işlev | Cilt I 12.8 |
| destructor | sonlandırıcı işlev | Cilt I 12.9 |
| target constructor | hedef kurucu işlev | Cilt I 12.12 |
| special member functions | özel üye işlevler | Cilt I 13.1 |
| shallow / deep copy | sığ / derin kopyalama | Cilt I 13.5 |
| object slicing | nesne dilimlenmesi | Cilt I 17.9 |
| upcasting | çevrilmedi | Cilt I 17.4 |
| diamond formation | elmas formasyonu | Cilt II 6.11 |
| virtual inheritance | sanal kalıtım | Cilt II 6.11 |
| covariant return type | çevrilmedi | Cilt II 6.4 |
| aggregate | bileşik tür | Cilt I 3.10 |

### İşlevler ve şablonlar

| İngilizce | Türkçe | İlk geçtiği yer |
|---|---|---|
| function overloading | işlev yüklemesi | Cilt I 9.1 |
| overload resolution | yükleme çözümlemesi | Cilt I 9.3 |
| exact match | tam uyum | Cilt I 9.6 |
| promotion | yükseltme | Cilt I 9.6 |
| name mangling | çevrilmedi | Cilt I 9.9 |
| instantiation | örnekleme | Cilt II 4.2 |
| specialization | özelleştirme *(iki anlamlı, bkz. Cilt II 4.2)* | Cilt II 4.3 |
| parameter pack | parametre paketi | Cilt II 4.5 |
| pack expansion | paket açma | Cilt II 4.5 |
| fold expression | katlama ifadesi | Cilt II 4.6 |
| deduction guide | çevrilmedi | Cilt II 4.7 |
| dependent / non-dependent name | bağımlı / bağımsız isim | Cilt II 4.9 |
| alias template | eş isim şablonu | Cilt II 4.10 |
| variable template | değişken şablonu | Cilt II 4.10 |
| immediate context | doğrudan bağlam | Cilt II 4.8 |
| non-deduced context | çıkarılmayan bağlam | Cilt II 5.7 |
| concept | kavram | Cilt II 7.1 |
| subsumption | kısıt sıralaması | Cilt II 7.7 |

### Kaynak yönetimi ve hata yönetimi

| İngilizce | Türkçe | İlk geçtiği yer |
|---|---|---|
| stack unwinding | yığının geri sarılması | Cilt I 18.5 |
| basic / strong guarantee | temel / güçlü garanti | Cilt II 13.1 |
| moved-from state | kaynağı devralınmış nesne durumu | Cilt II 2.5 |
| copy elision | kopyalama eliminasyonu | Cilt II 3.1 |
| pessimistic move | çevrilmedi | Cilt II 2.7 |
| control block | kontrol bloğu | Cilt I 25.3 |
| custom deleter | özel silici | Cilt II 17.9 |

### STL ve kütüphane

| İngilizce | Türkçe | İlk geçtiği yer |
|---|---|---|
| container | kap | Cilt I 23.1 |
| container adaptor | kap uyumlandırıcısı | Cilt I 23.4 |
| iterator | iteratör | Cilt I 23.2 |
| sentinel | çevrilmedi | Cilt II 8.3 |
| range | aralık | Cilt II 8.2 |
| view | görünüm | Cilt II 8.4 |
| range adaptor / factory | aralık uyumlandırıcısı / fabrikası | Cilt II 8.6 |
| projection | izdüşüm | Cilt II 8.9 |
| borrowed range | ödünç aralık | Cilt II 8.10 |
| lazy evaluation | tembel değerlendirme | Cilt II 8.5 |
| proxy | vekil nesne | Cilt I 23.3 |
| vocabulary types | çevrilmedi | Cilt II 11.1 |
| formatted / unformatted I/O | biçimli / biçimsiz giriş-çıkış | Cilt I 26.2 |

### Lambda ve çağrılabilirler

| İngilizce | Türkçe | İlk geçtiği yer |
|---|---|---|
| capture | yakalama | Cilt I 24.3 |
| closure type | kapanış türü | Cilt II 12.1 |
| init capture | ilk değerli yakalama | Cilt II 12.3 |
| generic lambda | genelleştirilmiş lambda | Cilt II 12.4 |
| IIFE | hemen çağrılan lambda | Cilt II 12.5 |

### Eşzamanlılık

| İngilizce | Türkçe | İlk geçtiği yer |
|---|---|---|
| thread | iş parçacığı | Cilt I 27.1 |
| data race | çevrilmedi | Cilt I 27.2 |
| race condition | yarış koşulu | Cilt I 27.2 |
| deadlock | ölümcül kilitlenme | Cilt II 15.3 |
| busy wait | meşgul bekleme | Cilt II 15.4 |
| spurious wakeup | yalancı uyanma | Cilt II 15.4 |
| sequential consistency | sıralı tutarlılık | Cilt II 15.1 |
| false sharing | yanlış paylaşım | Cilt II 17.8 |
| coroutine | eşyordam | Cilt II 9.1 |
| awaitable | beklenebilir | Cilt II 9.5 |
| immediate function | ivedi işlev | Cilt II 18.3 |

### Deyimler

| İngilizce | Türkçe | İlk geçtiği yer |
|---|---|---|
| idiom | deyim | Cilt II 14.1 |
| policy class | ilke sınıfı | Cilt II 14.8 |
| mixin | çevrilmedi | Cilt II 14.8 |
| type erasure | çevrilmedi | Cilt II 14.3 |
| RAII | çevrilmedi, açılımı verilir | Cilt I 18.6 |

---

## 3. Çevrilmeyen terimler ve gerekçeleri

| Terim | Neden çevrilmedi |
|---|---|
| L-Value, R-Value, PR-Value, X-Value, GL-Value | Standart metnindeki kısaltmalar; Türkçeleştirmek beş kategorinin ilişkisini gizler |
| upcasting | Yerleşik; "yukarı dönüştürme" karşılığı yaygın değil |
| sentinel | Ranges bağlamında teknik bir rol adı; "nöbetçi" yanıltıcı olurdu |
| data race | Yarış koşulundan ayrılması gereken teknik bir terim; "veri yarışı" ikisini birbirine yaklaştırır |
| mixin, type erasure, deduction guide | Literatürde İngilizce dolaşıyor; çevirisi arama yapmayı zorlaştırır |
| materialization, result object | C++17 tanımına ait; standart metnine bağlı kalındı |
| pessimistic move | Kalıbın adı; betimleme değil |
| vocabulary types | Bir tür ailesinin adı, kavram değil |

---

## 4. Kayda geçen terim kararları

Karar kayıtlarında dağınık duran kararların dizini.

| Karar | Nerede kayıtlı |
|---|---|
| `forwarding reference` birincil, `universal reference` eş anlamlı | Cilt II 1.2 karar kaydı |
| `L-Value Referance` yazımı `reference` olarak normalize edildi | Prototip 1 karar kaydı |
| `specialization` iki anlamlı; açıklanarak bırakıldı, tek anlama indirgenmedi | Cilt II 4 karar kaydı |
| `opaque` betimlemesi çevrilmedi, sözlüğe alınmadı | Cilt II 9 karar kaydı |
| `requires requires` yazımı kitapta hiç kullanılmadı | Cilt II 7 karar kaydı |
| Deyim numaraları (notlardaki 1–21) kitaba taşınmadı | Cilt II 14 karar kaydı |

---

## 5. Sözlüğün bakımı

Yeni bir terim eklenirken üç soru sorulur:

1. Standart metninde bir karşılığı var mı? Varsa o birincil olur.
2. Türkçe karşılık, terimi arayan okuyucunun kaynağa ulaşmasını zorlaştırıyor mu?
   Zorlaştırıyorsa çevrilmez.
3. Aynı kavram kitapta başka bir adla geçiyor mu? Geçiyorsa biri seçilip diğeri
   düzeltilir.

Üçüncü soru için son geçişte otomatik denetim yapıldı: 61 terimin hiçbirinde çakışan
karşılık bulunmadı.
