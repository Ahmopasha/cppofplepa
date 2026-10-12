---
cilt: "II — İleri"
kisim: "13 — İleri Hata Yönetimi"
baslik: "13.1 Garanti seviyeleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 13.1 Garanti seviyeleri

Cilt I Kısım 18'de hatanın nasıl gönderilip yakalandığı anlatılmıştı. Bu bölümün konusu,
bir işlevin hata durumunda **ne vaat ettiğidir.**

Dört seviye vardır ve zayıftan güçlüye sıralanır.

**Garanti yok.** Hata durumunda kaynak sızabilir, nesne tutarsız kalabilir. Kabul
edilebilir değildir; bu düzeydeki kod düzeltilmelidir.

**Temel garanti** *(basic guarantee)*. Kaynak sızıntısı yoktur ve programın durumu
geçerlidir. Ama hangi duruma geçildiği belirtilmemiştir; nesne değişmiş olabilir.

**Güçlü garanti** *(strong guarantee)*. Temel garantinin üzerine şunu ekler: hata
oluşursa program, işlem hiç başlamamış gibi **eski durumuna döner.** İşlem ya tamamen
yapılır ya hiç yapılmaz.

**`noexcept` garantisi.** İşlev hiç hata göndermez.

Cilt II Kısım 2.6'daki `vector` örneği bu sıralamanın somut uygulamasıydı: `vector`,
yeniden yer ayırırken güçlü garanti vermek zorunda olduğu için, taşıyan kurucu işlevi
yalnızca `noexcept` ise kullanır.

Güçlü garanti bedava değildir; genellikle geçici bir kopya oluşturup başarı hâlinde
takas etmeyi gerektirir. Cilt II Kısım 2.8'deki copy-and-swap deyimi tam olarak bu
düzeni kurar.

> Her işlev için **hangi garantiyi verdiğinizi belgeleyin.** Belgelenmemiş bir garanti,
> çağıran kod tarafından varsayılamaz.
