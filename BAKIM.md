# Bakım rehberi

Bu belge iki şeyi anlatır: bir alt başlığın güncelliğinin nasıl kontrol edileceğini ve
kitap yazılırken uyulan kuralları. İkincisi, yapılacak her değişikliğin kitabın geri
kalanıyla uyumlu kalması içindir.

---

## Bir dosyayı kontrol etmek

1. Dosyanın üst bilgisindeki `son_kontrol` alanına bakın. `2026-09 (C++23)`, dosyanın
   Eylül 2026'da, C++23'e kadarki standartlar gözetilerek gözden geçirildiğini söyler.
2. Metni dilin ve derleyicilerin güncel durumuyla karşılaştırın. Önce `kutular` alanında
   **Standart Notu** ya da **Derleyici Notu** geçen dosyalara bakın; bunlar standart veya
   derleyici değiştiğinde ilk eskiyen yerlerdir. Listenin tamamı, her derlemede
   `cikti/bakim_durumu.md` içinde yeniden üretilir.
3. Değişiklik gerekmiyorsa yalnızca `son_kontrol` alanını güncelleyin:
   `son_kontrol: "2027-03 (C++26)"`.
4. Değişiklik gerekiyorsa aşağıdaki kurallara göre yapın, `son_kontrol`'ü güncelleyin ve
   `DEGISIKLIKLER.md`'ye bir satır ekleyin.
5. `python3 araclar/derle.py` ile derleyin ve çıkan uyarıları giderin.

Bir dosyayı değiştirdiğinizde, ona atıf yapan dosyalara da bakın. Atıflar "Kısım 12.13"
biçimindedir; dosyanın numarasını depoda aratmak, onu anan yerleri bulmanın en kısa
yoludur.

---

## Üst bilgi alanları

| Alan | Anlamı |
|---|---|
| `cilt` | `I — Temel` ya da `II — İleri` |
| `kisim` | Dosyanın ait olduğu kısım |
| `baslik` | Dosyadaki başlık |
| `kaynak` | `ders notları`, `derleyen (ders notlarında yok)` ya da `derleyen` (ön metin, geçiş, kapanış kutusu) |
| `kutular` | Dosyadaki Standart Notu ve Derleyici Notu kutuları; yoksa alan yazılmaz |
| `son_kontrol` | En son kontrolün ayı ve gözetilen en yeni standart |

Üst bilgi derlenen kitaba girmez; yalnızca depoda görünür. `kutular` alanını kutu
ekleyip çıkardığınızda elle güncelleyin; unutursanız derleme betiği uyarır.

---

## Değişikliğin türüne göre ne yapılır

Kitap yazılırken iki not seti arasındaki çakışmalar altı türe ayrılmıştı. Aynı ayrım,
bakımda karşılaşılan değişiklikler için de geçerlidir:

| Tür | Örnek | Ne yapılır |
|---|---|---|
| Standart değişikliği | C++26 bir kuralı değiştirdi | Eski ve yeni davranış birlikte korunur; **Standart Notu** kutusu açılır |
| Derinlik farkı | Bir konu başka bir kaynakta daha ayrıntılı | Kutu açılmaz; eksik ayrıntı ilgili cilde eklenir |
| Hata | Metinde yanlış bir bilgi ya da atıf | Düzeltilir, `DEGISIKLIKLER.md`'ye yazılır |
| Derleyici farkı | Bir derleyici standarttan farklı davranıyor | **Derleyici Notu** kutusu açılır; derleyici düzeldiğinde kutu güncellenir ya da kaldırılır |
| Terim farkı | Aynı kavram için iki terim | Standart terim birincildir; diğeri ilk geçtiği yerde parantez içinde verilir; `terim_sozlugu.md` güncellenir |
| Bağlam farkı | Aynı konu iki yerde anlatılıyor | Tek yerde anlatılır, diğer yer oraya atıf yapar |

En sık yapılan hata, derinlik farkını standart değişikliği sanmaktır: bir anlatımın eski
olması dilin değiştiği anlamına gelmez. Kutu açmadan önce değişikliğin hangi standartla
geldiğini doğrulayın.

### Standart Notu kutusu

Davranış bir standartla değiştiyse ya da eski yöntem mevcut kod tabanlarında hâlâ
yaygınsa açılır:

```
> **Standart Notu — C++17**
> **C++17 öncesi:** Derleme zamanında dallanmak için tag dispatching, `enable_if` ile
> SFINAE, veya sınıf şablonu özelleştirmesi kullanılırdı.
> **C++17 ile:** `if constexpr` ile doğrudan yazılır.
> **Neden değişti:** Derleme zamanı dallanma, şablon kodunun en yaygın ihtiyacıydı ve
> mevcut çözümlerin hiçbiri okunabilir değildi.
```

### Derleyici Notu kutusu

```
> **Derleyici Notu**
> Fonksiyonlar hangi referans türüne dönüştürülürse dönüştürülsün her zaman L-Value
> kalır. Buna rağmen MSVC, `std::move(foo)` gibi bir ifade için X-Value bildirmektedir.
> Doğru sonucu görmek için GCC ile doğrulayın.
```

---

## Yazım ilkeleri

**Kümülatif ilke.** Cilt I, Cilt II'nin geri almak zorunda kalacağı hiçbir şey söylemez.
Basitleştirme vardır, yanıltma yoktur. Cilt I'e eklenen her cümle bu ölçüte göre
yazılır.

**Bir konu tek yerde anlatılır.** Aynı cilt içinde de geçerlidir. Konuyu anlatan yer
bellidir; onu kullanan diğer yerler oraya atıf yapar.

**Okuyucu o noktaya kadar neyi biliyor?** Bir bölüm, kendisinden önce gelen bölümlerde
anlatılmamış bir kavrama dayanamaz; dayanması gerekiyorsa ileriye atıf verir.

**Bölünemeyen kalem.** Bazı konuların kuralı yeni mezun için, gerekçesi kıdemli için
gereklidir. O durumda kural Cilt I'de, gerekçesi Cilt II'de yer alır ve ikisi birbirine
atıf yapar. Örnek: aralık tabanlı `for` döngüsünde `auto&&` kuralı Cilt I 23.3'te,
nedeni Cilt II 1.2.7'de.

**Ders tarihleri ve künyeleri metne girmez.** Kitap bir ders kaydı değil, bir başvuru
kaynağıdır.

**Terimler.** Yeni bir terim ilk geçtiği yerde `**Türkçe karşılık** *(İngilizce terim)*`
biçiminde tanıtılır ve `terim_sozlugu.md`'ye eklenir. Sözlüğün sonundaki üç soru,
karşılık seçerken sorulacak sorulardır.

**Satır uzunluğu.** Metin satırları yaklaşık 90 karakterde kırılır. Zorunlu değildir;
Markdown satır içi kırılmaları birleştirir.

---

## Numaralandırma

Dosya adındaki numara ile dosyanın ilk satırındaki başlık numarası aynı olmalıdır
(`12-13-...md` → `## 12.13 ...`). Betik ikisinin uyuşmadığı her dosyada derlemeyi
durdurur.

**Sona alt başlık eklemek** kolaydır: bir sonraki numarayla yeni dosya açılır.

**Araya alt başlık eklemek** sonraki bütün alt başlıkların numarasını kaydırır: dosya
adları, başlık satırları ve metin içindeki atıflar birlikte değişmelidir. Betik var
olmayan bir başlığa giden atıfları yakalar; ama numarası kaydığı için artık **başka**
bir başlığı gösteren atıfları yakalayamaz. Bu yüzden numara kaydırmadan önce, kayacak
numaraların geçtiği yerleri depoda aratın.

**Yeni kısım eklemek** için `kisim-NN-ad/` klasörü, içinde `NN-00-kisim-basligi.md`
dosyası açılır ve `gecisler/` altına iki komşu kısımla ilgili geçiş dosyası eklenir.

---

## Geçiş paragrafları

`gecisler/` klasöründeki her dosya iki kısmı birbirine bağlar ve bağlandığı kısmın
başlığının hemen altına, varsa kısım girişinden önce yerleşir. `kisim-08-09.md`,
Kısım 9'un başına girer ve Kısım 8'den geçişi kurar. İki cilt arasındaki geçiş iki
dosyadır: `cilt-1-kapanis.md` Cilt I'in sonuna ayrı bir bölüm olarak, `cilt-2-acilis.md`
Cilt II'nin ön metninin sonuna eklenir.

Bir geçiş paragrafı komşu iki kısmın içeriğine dayanır. Bir kısmın ilk ya da son alt
başlığı değiştiğinde, o kısma giren ve o kısımdan çıkan geçişleri yeniden okuyun.
`cilt-2-acilis.md`'deki tablo, Cilt II kısımlarının Cilt I'deki karşılıklarını
gösterir; kısım eklendiğinde ya da kaldırıldığında güncellenmelidir.

Geçişler kitabın kendi metnini tekrar etmez: kısmın ilk alt başlığının ilk cümlesiyle
aynı şeyi söyleyen bir geçiş, o cümleyi gereksiz kılar.

---

## Sürüm yayımlamak

1. İki ön metin dosyasındaki (`cilt-1-temel/00-on-metin.md`, `cilt-2-ileri/00-on-metin.md`)
   `Derleyen: ... · Sürüm ... · ...` satırını güncelleyin. PDF'in kapağı bu satırdan
   üretilir; iki dosya farklıysa betik uyarır.
2. `DEGISIKLIKLER.md`'de "Yayımlanmamış" başlığını sürüm numarasıyla değiştirin.
3. `python3 araclar/derle.py --pdf` ile derleyin; uyarı kalmadığından emin olun.
4. Leanpub'a `cikti/CPP_Kitabi.pdf`'i yükleyin; içindekiler alanına
   `cikti/leanpub_icindekiler.html`'in içeriğini yapıştırın.

---

## Açık konular

**Cilt I 25.5'teki atıf.** "Özel silici tanımlama, kontrol bloğunun ayrıntıları ve
`enable_shared_from_this`" için Cilt II Kısım 14'e atıf veriliyor, ama bu konular
Cilt II'nin hiçbir yerinde anlatılmıyor. Ya Cilt II'ye bu konuları anlatan bir alt başlık
eklenmeli ya da cümle kaldırılmalı.

**C++26 taraması yapılmadı.** Bütün dosyalar C++23'e göre işaretli. C++26'nın kitaptaki
konulara dokunan değişiklikleri henüz işlenmedi.
