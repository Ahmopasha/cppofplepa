---
cilt: "II — İleri"
kisim: "15 — Eşzamanlılık"
baslik: "15.1 Bellek modeli"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 15.1 Bellek modeli

Standart, gerçeklemeden yalnızca **soyut makinenin** *(abstract machine)*
**gözlemlenebilir davranışını** *(observable behavior)* taklit etmesini ister: `volatile`
erişimler, dosyalara yazılan veri ve etkileşimli giriş-çıkış, soyut makinenin olası
yürütmelerinden biriyle aynı olmalıdır. Soyut makine, standardın programın anlamını tarif
ederken kullandığı kuramsal makinedir; aynı program ve girdi için birden çok olası
yürütmesi olabilir. Olası yürütmelerden biri tanımsız davranış içeriyorsa standart, o
programı o girdiyle çalıştıran gerçeklemeden hiçbir şey istemez. Gözlemlenebilir davranışı
koruduğu sürece gerçekleme komutları yeniden sıralayabilir, değişkenleri yazmaca alabilir,
işlemleri eleyebilir. Kural, programın kaç iş parçacığı kullandığından bağımsızdır.

Çok iş parçacıklı programlarda bu özgürlük sorun çıkarabilir: bir iş parçacığının yaptığı
yeniden sıralama, başka bir iş parçacığının okuduğu değerlerde görülebilir. Bunun başlıca
iki yolu data race (tanımsız davranış; bkz. Cilt I, Kısım 27.2) ve `seq_cst` dışındaki
atomik sıralamalardır (Kısım 15.8).

C++11, bu belirsizliği kurallaştıran bir **bellek modeli** *(memory model)* tanımladı.
Model iki soruya cevap verir: bir iş parçacığının yazdığı değeri diğeri ne zaman görür, ve
işlemlerin hangi sırayla gerçekleştiği konusunda ne varsayılabilir. Aşağıdaki koşulu
sağlayan programlarda standart, yeniden sıralamanın görülmeyeceğini garanti eder.

Atomik işlemlerin varsayılan sıralaması `seq_cst`'dir: bütün `seq_cst` işlemleri için tek
bir toplam sıra vardır. Data race içermeyen, senkronizasyon için yalnızca `mutex`'leri ve
atomik işlemleri kullanan ve bütün atomik işlemlerinde bu varsayılan sıralamayı kullanan
bir program **sıralı tutarlılık** *(sequential consistency)* gösterir: iş parçacıklarının
işlemleri basitçe iç içe geçirilmiş gibi davranır; her iş parçacığının işlemleri bu iç içe
geçişte kendi sırasıyla yer alır.

Bu en güçlü ve en anlaşılır garantidir. Standart maliyet hakkında bir şey söylemez; ama
gerçeklemelerde `seq_cst` dışındaki sıralamalardan genellikle daha pahalıdır. Bu
seçenekler Kısım 15.8'in konusu.
