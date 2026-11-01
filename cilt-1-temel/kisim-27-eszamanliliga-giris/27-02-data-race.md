---
cilt: "I — Temel"
kisim: "27 — Eşzamanlılığa Giriş"
baslik: "27.2 Data race"
kaynak: "derleyen (ders notlarında yok)"
son_kontrol: "2026-11 (C++20)"
---

## 27.2 Data race

Eşzamanlı programlamanın temel tehlikesi budur. Tanımı üç koşulun aynı anda sağlanmasıdır:

1. Farklı iş parçacıklarından iki erişim **aynı bellek konumuna** yapılıyor,
2. Bu iki erişimden **en az biri yazma**,
3. Bu iki erişimden **en az biri atomik değil** (sıradan okuma ve yazmalar atomik
   değildir; atomik işlemler için bkz. Cilt II, Kısım 15.8) ve aralarında
   **senkronizasyonla kurulan bir sıra yok** (bkz. Kısım 27.3).

Üçü birden sağlanıyorsa ortada bir **data race** vardır ve bu, **tanımsız davranıştır**
(bkz. Kısım 2.5).

```cpp
int sayac = 0;                        // paylaşılan

void artir() { for (int i = 0; i < 100000; ++i) ++sayac; }

int main()
{
    std::thread t1{artir};
    std::thread t2{artir};
    t1.join(); t2.join();
    std::cout << sayac;               // 200000 olacağı garanti değil: tanımsız davranış
}
```

`++sayac` tek bir işlem gibi görünür ama üç adımdır: oku, artır, yaz. İki iş parçacığı
araya girdiğinde artışlar kaybolur.

### Neden "yanlış sonuç" demek yetmiyor

Yukarıdaki programın 200000'den küçük bir sayı yazdıracağını düşünmek doğal ama eksiktir.
Data race **tanımsız davranıştır**; Kısım 2.5'te anlatıldığı gibi, standart hiçbir şey
garanti etmez.

Derleyici, data race olmadığını **varsayarak** optimizasyon yapma hakkına sahiptir.
Değişkeni bir yazmaca alıp döngü boyunca belleğe hiç yazmayabilir; bu durumda bir iş
parçacığının yaptığı artışların hiçbiri diğerine görünmez. Programın davranışı derleyiciye,
optimizasyon seviyesine ve işlemci mimarisine göre değişir.

> **Data race içeren bir program "çoğu zaman çalışıyor" olamaz.** Test ortamında doğru
> sonuç vermesi, kodun doğru olduğunu göstermez.

### Yarış koşulundan farkı

İki terim karıştırılır ama aynı şey değildirler.

**Yarış koşulu** *(race condition)*, programın doğruluğunun işlemlerin zamanlamasına
bağlı olmasıdır. Bir mantık hatasıdır.

**Data race**, yukarıdaki üç koşulun sağlanmasıdır. Bellek modeline ilişkin bir kural
ihlalidir.

İkisi bağımsızdır. Bütün erişimleri doğru kilitlediğiniz hâlde işlemlerin sırası yanlışsa
**data race olmadan yarış koşulu** yaşarsınız:

<!-- kod-baglam
struct Hesap {
    int bakiye() const;
    void cek(int);
} hesap;
-->
```cpp
if (hesap.bakiye() >= 100)        // kilitli
    hesap.cek(100);               // kilitli — ama arada başkası çekmiş olabilir
```

Burada hiçbir data race yoktur; her erişim senkronize. Yine de program yanlıştır, çünkü
denetim ile işlem arasındaki boşlukta durum değişebilir.

Tersi de mümkündür: senkronize olmayan bir erişimin mantıksal sonucu doğru çıkabilir ama
yine de data race vardır ve program tanımsız davranıştadır.

**Kural: data race her zaman hatadır; yarış koşulu bazen kabul edilebilir.**

### Neden test ederek bulunamaz

Data race'in belirtisi, başka etkenlerin yanında iş parçacıklarının hangi sırayla
ilerlediğine göre de değişebilir. Standart bu sırayı belirlemez; aynı program her
çalıştırmada farklı davranabilir.

Bir program yıllarca sorunsuz çalışıp, farklı bir makinede veya farklı bir derleyici
sürümüyle bozulabilir. Hatanın yeniden üretilmesi çoğu zaman mümkün olmaz.

Bu yüzden data race, **test edilerek değil, tasarımla** önlenir. Çalışma anında erişimleri
izleyen denetim araçları yardımcı olur ama garanti vermez; yalnızca o çalıştırmada
gerçekleşen erişimleri görürler.

### Üç kaçınma stratejisi

Tanımdaki üç koşuldan **herhangi birini** kırmak yeterlidir.

**Paylaşmayın.** Her iş parçacığı kendi verisiyle çalışsın; sonuçlar sonda birleştirilsin.
Bu, üç stratejinin en hızlısı ve en güvenlisidir.

**Değiştirmeyin.** Paylaşılan veri `const` ise ve `mutable` eleman (bkz. Kısım 12.15) gibi
yollarla gizlice yazılmıyorsa, bütün erişimler okuma olur ve ikinci koşul sağlanmaz. Sabit
veriyi kaç iş parçacığının okuduğunun önemi yoktur. Aksi belirtilmedikçe standart
kütüphane işlevleri, başka iş parçacıklarının erişebildiği nesnelerden yalnızca `const`
olmayan argümanları (üye işlevlerde `this` dahil) üzerinden eriştiklerini değiştirebilir.

**Senkronize edin.** Paylaşım da değişiklik de kaçınılmazsa, erişimleri `mutex` (bkz.
Kısım 27.3) ile sıralayın ya da atomik işlemler kullanın.

Sıralama bilinçli olarak bu şekildedir: kilit, ilk iki strateji uygulanamadığında
başvurulan son çözümdür. Kilit eklemek hem maliyet getirir hem yeni hata sınıfları açar
(ölümcül kilitlenme gibi).

Atomik işlemler ve bellek modelinin tamamı: **Cilt II, Kısım 15.**
