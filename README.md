# C++ Başvuru Kitabı

Necati Ergin'in C++ ve İleri C++ kurslarındaki ders notlarından derlenmiş, iki ciltlik
Türkçe başvuru kitabının kaynak deposu. Kitap burada **her alt başlık ayrı bir Markdown
dosyası** olacak biçimde tutulur; ciltler ve PDF bu dosyalardan derlenir.

**Kitabı okumak için:** PDF, Leanpub'da ücretsizdir: <https://leanpub.com/cppofplepa>.
Her sürümün PDF'i ayrıca bu deponun [Releases](https://github.com/Ahmopasha/cppofplepa/releases)
sayfasında bulunur.
Kitap, [free-programming-books](https://github.com/EbookFoundation/free-programming-books/blob/main/books/free-programming-books-tr.md#cpp)
listesinin Türkçe C++ bölümünde de yer alır.

---

## İzin ve kullanım

> Bu çalışma Necati Ergin'in C++ ve İleri C++ kurslarındaki ders notlarından, **kendisinin
> izniyle** derlenmiştir. Serbestçe okunabilir ve paylaşılabilir. Ticari kullanım ve
> türev çalışmalar için hocaya danışılmalıdır.

**Lisans.** Kitap metni [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.tr)
ile, `araclar/` altındaki derleme araçları MIT lisansıyla yayımlanmıştır. Ayrıntılar
`LICENSE` dosyasında.

Kitaptaki kod örneklerinin büyük kısmı derslerde yazılan ya da hocanın GitHub sayfasında
paylaştığı örneklerdir. Terimlerin Türkçe karşılıkları da onun kullandığı karşılıklardır.

Derleyen: Ahmet Kandemir Pehlivanlı

---

## Kitap nasıl bölünmüş

İki cilt **kümülatif okunmak** üzere yazıldı. Bağlayıcı kural şu: Cilt I, Cilt II'nin
geri almak zorunda kalacağı hiçbir şey söylemez. Basitleştirme vardır, yanıltma yoktur.

**Cilt I — Temel** (28 kısım). Yeni mezun bir C++ geliştiricisinin ilk yılında bilmesi
gerekenler. Her konu, o aracı doğru kullanabilmeye yetecek kadar anlatılır.

**Cilt II — İleri** (18 kısım). Kıdemli bir geliştiricinin bilmesi gerekenler: araçların
iç yapısı, tasarım gerekçeleri ve kütüphane yazarken gereken teknikler.

---

## Depo düzeni

```
cilt-1-temel/                        Cilt I
  00-on-metin.md                     cildin başlığı, künyesi ve tanıtımı
  kisim-02-temel-kavramlar/          her kısım bir klasör
    02-00-kisim-basligi.md           kısım başlığı (ve varsa kısım girişi)
    02-01-bildirim-ve-tanim.md       alt başlık 2.1
    02-04-00-l-value-ve-r-value.md   alt-alt başlıkları ayrı tutulan alt başlık 2.4
    02-04-01-bu-konuyu-neden-...md   alt-alt başlık 2.4.1
    02-04-99-cilt-ii-ye-gecis.md     2.4'ün sonundaki "Cilt II'ye geçiş" kutusu
    ...
  kisim-09-islev-yuklemesi-.../
    09-99-cilt-ii-ye-gecis.md        kısmın sonundaki "Cilt II'ye geçiş" kutusu
cilt-2-ileri/                        Cilt II, aynı düzen
gecisler/                            kısımlar ve ciltler arasındaki geçiş paragrafları
araclar/derle.py                     derleme betiği
araclar/kod_denetimi.py              kod örneklerinin denetimi
araclar/pdf/baslik.tex               PDF biçimlendirmesi
terim_sozlugu.md                     Türkçe karşılıkların dizini
BAKIM.md                             güncellik kontrolü ve yazım kuralları
DEGISIKLIKLER.md                     sürümler arası değişiklikler
```

**Dosya adındaki sayılar sırayı belirler**, ardından gelen metin yalnızca okuyana
yöneliktir. `00` bir birimin başını, `99` sonunu gösterir:

| Ad kalıbı | İçerik |
|---|---|
| `NN-00-kisim-basligi.md` | Kısım N'nin başlığı ve varsa girişi |
| `NN-MM-ad.md` | Alt başlık N.M |
| `NN-MM-00-ad.md` | Alt-alt başlıkları ayrı dosyalarda duran alt başlık N.M'nin kendisi |
| `NN-MM-KK-ad.md` | Alt-alt başlık N.M.K |
| `NN-MM-99-...md`, `NN-99-...md` | Alt başlığın ya da kısmın kapanış kutusu |

Her dosyanın başında, GitHub'ın tablo olarak gösterdiği kısa bir üst bilgi bulunur:
hangi cilde ve kısma ait olduğu, kaynağı, içerdiği Standart Notu
kutuları ve **en son ne zaman, hangi standarda göre kontrol edildiği.** Bakımın nasıl
yapılacağı `BAKIM.md`'de.

---

## Derleme

Depo kökünden:

```
python3 araclar/derle.py            iki cilt, birleşik kitap, Leanpub içindekiler listesi
python3 araclar/derle.py --pdf      yukarıdakiler ve PDF
python3 araclar/derle.py --gecissiz geçiş paragrafları olmadan
python3 araclar/derle.py --kod      ayrıca kod örneklerini derle (Clang; rapor cikti/kod_denetimi.md)
```

Çıktılar `cikti/` klasörüne yazılır:

| Dosya | Ne |
|---|---|
| `CILT_I.md`, `CILT_II.md` | İki cilt, tek dosya hâlinde |
| `kitap_birlesik.md` | İki cildin PDF için birleştirilmiş kaynağı |
| `CPP_Kitabi.pdf` | Kitabın PDF hâli (`--pdf` ile) |
| `leanpub_icindekiler.html` | Leanpub'ın içindekiler alanına yapıştırılacak liste |
| `bakim_durumu.md` | Dosyaların son kontrol tarihleri ve kutu içeren dosyalar |

Betik derlerken denetim de yapar: dosya adlarıyla başlık numaralarının uyuşmasını, metin
içindeki **"Kısım N.M" atıflarının var olan bir başlığa gitmesini** ve üst bilgideki kutu
listesinin metinle tutarlılığını. Sorunları `UYARI` / `HATA` satırlarıyla bildirir.
GitHub aynı denetimi her gönderimde kendiliğinden çalıştırır
(`.github/workflows/denetim.yml`); bir sorun varsa gönderimin yanında kırmızı işaret
görünür. Bir iş daha vardır: `kod-denetimi.yml` kod örneklerini GCC ve Clang ile derleyip
raporunu işin özetine koyar; sorunlu blok varsa iş başarısız olur.

Gerekenler: Python 3.8 veya üstü (Windows'ta `python3` yerine `py` yazın). PDF için
ayrıca [pandoc](https://pandoc.org), bir TeX dağıtımı (TeX Live ya da MiKTeX; `xelatex`
kullanılır) ve DejaVu yazı tipleri.

---

## Kaynak

| Kurs | Dönem | Ders |
|---|---|---|
| C++ | Eylül 2020 – Şubat 2021 | 42 / 42 |
| İleri C++ | Haziran 2023 – Ocak 2024 | 44 / 44 |

Bölüm sıralaması olarak hocanın kendi müfredat sıralaması kullanıldı
([`necatiergin/kurs_programlari`](https://github.com/necatiergin/kurs_programlari)).

---

## Notlardan kitaba

Ders notları tarihe göre sıralı düz metindi. Bir konu birkaç derse yayıldığında `(devam)`
ile sürüyordu; aynı konu iki not setinde farklı derinlikte iki kez anlatılmıştı.

**Konu bazlı yeniden yapılandırma.** Ders sırası bırakılıp konu sırasına geçildi. Bir
konuyu anlatan pasajlar tek bölümde toplandı; o konuyu yalnızca kullanan pasajlar kendi
yerlerinde bırakılıp bölüme atıf verildi.

**Çakışmaların çözülmesi.** İki not farklı şey söylediğinde kaynağı araştırıldı. Dilin
davranışının gerçekten değiştiği yerlerde eski ve yeni anlatım birlikte korundu; kitapta
on dört **Standart Notu** kutusu var.

---

## Provenans

Kitabın **dört alt başlığı** iki not setinde de bulunmuyordu; bunlar dışarıdan yazıldı ve
örnekleri bu çalışmaya aittir:

| Başlık | Yeri |
|---|---|
| Devreden kurucu işlevler | Cilt I 12.12 |
| Data race | Cilt I 27.2 |
| `std::byte` | Cilt II 11.7 |
| Mixin sınıflar | Cilt II 14.8 |

`gecisler/` klasöründeki geçiş paragrafları, ön metinler ve "Cilt II'ye geçiş" kutuları da
derleyene aittir. Bu dosyaların üst bilgisinde `kaynak: "derleyen"` yazar. Kitabın geri
kalanı ders notlarına dayanmaktadır.

Notların yeniden yapılandırılması ve metnin yazımı Claude ile birlikte yürütüldü. Yapının
kurulması, cilt ayrımının ölçütü ve hangi notun nereye gideceği kararları çalışmanın
sahibine aittir.

---

## Hata bildirimi

Yanlış, eksik ya da güncelliğini yitirmiş bulduğunuz yerler için bir **issue**
açabilirsiniz. İlgili dosyanın yolunu ya da cilt ve başlık numarasını belirtmeniz
yeterli.

Düzeltmeler sürüm numarası artırılarak yayımlanır; değişiklikler `DEGISIKLIKLER.md`'de.
