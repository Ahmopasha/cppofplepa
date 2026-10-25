# Tarama — Cilt I Kısım 27 (Ekim 2026)

Kısım 27'deki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar
çalışma taslağının (eel.is/c++draft) bölüm adlarıyla verilir; paragraf numaraları C++23
metnindendir (N4950). Cilt I'in ufku C++20 olduğu için her iddia N4861'de de denetlendi;
iki metin arasında bu kısmı etkileyen fark bulunmadı. 27.0 ve 27.4 normatif iddia
içermiyor.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 27.1 | İş parçacığı, süreç içinde bağımsız çalışan yürütme akışıdır; aynı süreçtekiler aynı belleği paylaşır | [intro.multithread]/1: iş parçacığı "program içinde tek bir denetim akışı"dır; her iş parçacığı programdaki her nesneye ve işleve erişebilir. Standart "süreç" kavramını kullanmaz ama cümle onunla çelişmez | doğru |
| 2 | 27.1 | `join()` iş parçacığının bitmesini bekler; `detach()` bağı koparır, iş parçacığı arka planda devam eder | [thread.thread.member]/3 ("Blocks until the thread ... has completed"), /8 ("continues execution without the calling thread blocking") | doğru |
| 3 | 27.1 | `join` veya `detach` çağırmadan `std::thread` nesnesinin hayatının bitmesi programı sonlandırır; sonlandırıcı `std::terminate` çağırır | [thread.thread.destr]/1: yalnızca `joinable()` ise `terminate` çağrılır; taşınmış ya da varsayılan kurulmuş nesne için etkisi yoktur. Ayrıca [thread.thread.assign]/1: `joinable()` bir nesneye taşıyarak atama da `terminate` çağırır | eksik (test 1) |
| 4 | 27.1 | `std::thread` kopyalamaya kapalı, taşımaya açıktır | [thread.thread.class]: kopyalayan kurucu ve atama `= delete`, taşıyanlar `noexcept` | doğru |
| 5 | 27.2 | Data race'in tanımı üç koşuldur: iki ya da daha fazla iş parçacığı aynı bellek konumuna erişir, en az biri yazmadır, aralarında senkronizasyon yoktur | [intro.races]/21: iki *olası eşzamanlı (potentially concurrent)* *çakışan (conflicting)* eylem, **en az biri atomik değil** ve hiçbiri diğerinden önce olmuyor (*happens before*). [intro.races]/3: gevşetilmiş (*relaxed*) atomik işlemler senkronizasyon işlemi değildir, yine de data race oluşturmaz. Olası eşzamanlılık sinyal işleyici durumunu da kapsar (/21.2) | eksik (test 2) |
| 6 | 27.2 | Data race tanımsız davranıştır | [intro.races]/21: "Any such data race results in undefined behavior." | doğru |
| 7 | 27.2 | Örnek: `std::cout << sayac; // 200000 değil, tanımsız` | Tanımsız davranışta 200000 yazdırmak da olası sonuçlardandır ([intro.abstract]/5); yorumun "200000 değil" kısmı bir sonucu dışlıyor | eksik |
| 8 | 27.2 | `++sayac` üç adımdır: oku, artır, yaz | [expr.pre.incr]/1: `++x`, `x+=1`'e eşdeğerdir; [expr.ass]/6: `E1 op= E2`, `E1 = E1 op E2` gibidir, Not 2: nesneye iki kez erişilir | doğru |
| 9 | 27.2 | Derleyici data race olmadığını varsayarak optimizasyon yapabilir; değişkeni yazmaçta tutup belleğe hiç yazmayabilir; davranış ortama göre değişir | Tanımsız davranış içeren yürütmeye standart hiçbir şart koymaz ([intro.abstract]/5); yazmaç örneği izin verilen dönüşümlerden birini "-abilir" kipinde anlatıyor, standart iddiası gibi yazılmamış | doğru |
| 10 | 27.2 | Data race içeren program "çoğu zaman çalışıyor" olamaz; test ortamında doğru sonuç vermesi kodun doğru olduğunu göstermez | [intro.races]/21, [intro.abstract]/5 | doğru |
| 11 | 27.2 | Yarış koşulu ile data race bağımsızdır; data race olmadan yarış koşulu, yarış koşulu olmadan data race olabilir; senkronize olmayan erişimin sonucu doğru çıksa da program tanımsızdır | "Yarış koşulu" standart terimi değildir; data race kısmı [intro.races]/21 ile uyumlu | doğru |
| 12 | 27.2 | Data race'in ortaya çıkması "işletim sisteminin o anki yüküne, çekirdek sayısına ve derleyicinin ürettiği koda göre değişir" | Standart, iş parçacıklarının hangi sırayla ilerleyeceğini belirlemez ([intro.multithread]/1, Not 2: yürütme "genellikle" iş parçacıklarının iç içe geçmesi olarak görülebilir); işletim sistemi, çekirdek sayısı ve üretilen kod gerçekleme anlatımıdır | gerçekleme |
| 13 | 27.2 | "Derleyicilerin sunduğu `ThreadSanitizer` gibi araçlar" yalnızca o çalıştırmadaki erişimleri görür | Araç adı ve derleyicinin sunduğu araç standartta yoktur (CLAUDE.md: derleyiciye özgü ayrıntı metne girmez) | gerçekleme |
| 14 | 27.2 | Tanımdaki üç koşuldan herhangi birini kırmak yeterlidir | Kitabın tanımına göre doğru; 5 düzeltilirse "atomik erişim" ayrı bir yol olarak görünür. Stratejilerin üçüncüsü atomikleri zaten anıyor | doğru |
| 15 | 27.2 | Paylaşılan veri `const` ise bütün erişimler okuma olur, ikinci koşul sağlanmaz | [dcl.type.cv]/4 ve örneği: `const` nesnenin `mutable` elemanı değiştirilebilir; `const` üye işlevi içinde `mutable` eleman değiştiren bir tür eşzamanlı "okumada" data race üretir. Standart kütüphane türleri için [res.on.data.races]/3 bu durumu dışlar | eksik (test 3) |
| 16 | 27.3 | `std::lock_guard` kurucusunda kilidi alır, sonlandırıcısında bırakır; hata gönderilse bile kilit bırakılır | [thread.lock.guard]/2 (`m.lock()`), /6 (`pm.unlock()`); yığın geri sarımı otomatik nesneleri yok eder. Yakalanmayan hatada geri sarımın yapılıp yapılmayacağı gerçeklemeye bağlıdır ([except.terminate]/2) ama program zaten sonlanır | doğru |
| 17 | 27.3 | `lock()`/`unlock()` doğrudan çağrılır ve arada `return` ya da hata olursa kilit bırakılmaz ve "program kilitlenir" | Başka bir iş parçacığının `lock()` çağrısı süresiz bekler, ama sonuç her zaman kilitlenme değildir: aynı iş parçacığının `std::mutex`'i yeniden kilitlemesi ön koşul ihlalidir ([thread.mutex.requirements.mutex.general]: "the calling thread does not own the mutex"); kilit sahibi iş parçacığının bitmesi ya da sahipli `mutex`'in yok edilmesi tanımsız davranıştır ([thread.mutex.class]/5) | eksik |
| 18 | 27.3 | "Her zaman `lock_guard` veya `unique_lock` kullanın" | Cilt I'in ufku olan C++20'de `std::scoped_lock` (C++17, [thread.lock.scoped]) da vardır; Cilt II 15.3 ise `lock_guard` yerine `scoped_lock`'u önerir. İki cilt arasında tutarsızlık | eksik |

## Önerilen düzeltmeler

- **3:** "Bir iş parçacığını temsil eden (`joinable()`) bir `std::thread` nesnesinin hayatı `join` ya da `detach` çağrılmadan biterse sonlandırıcı `std::terminate` çağırır; böyle bir nesneye taşıyarak atama yapmak da aynı sonucu doğurur."
- **5:** Üçüncü koşul "erişimlerden en az biri atomik değil ve aralarında bir önce olma (*happens before*) ilişkisi kurulmamış" biçiminde yazılmalı; senkronizasyonun da atomikliğin de data race'i önlediği ayrı ayrı belirtilmeli.
- **7:** Yorum "`// 200000 olacağı garanti değil: tanımsız davranış`" gibi bir ifadeye çevrilmeli.
- **12:** Cümle "Hangi araya girmenin gerçekleşeceğini standart belirlemez; aynı program her çalıştırmada farklı davranabilir" gibi gerçekleme anlatımından arındırılmalı.
- **13:** Araç adı çıkarılıp "çalışma anında erişimleri izleyen denetim araçları" gibi genel bir ifade kullanılmalı.
- **15:** "`mutable` elemanı olmayan ve `const` üye işlevlerinde gizli değişiklik yapmayan" kaydı eklenmeli; standart kütüphane türlerinin bu konuda güvenli olduğu ([res.on.data.races]) belirtilebilir.
- **17:** "Program kilitlenir" yerine "kilidi bekleyen iş parçacıkları süresiz bekler; aynı iş parçacığının yeniden kilitlemesi, kilit tutarken bitmesi ya da `mutex`'in yok edilmesi tanımsız davranıştır" yazılmalı.
- **18:** Öneri "`std::lock_guard`, `std::scoped_lock` ya da `std::unique_lock`" olarak genişletilmeli ya da Cilt II 15.3'ün önerisiyle uyumlu hâle getirilmeli.

## Test 1 — iddia 3: taşınmış `std::thread` nesnesinin yok edilmesi programı sonlandırmaz

```cpp
#include <cstdio>
#include <thread>
#include <utility>

void is() { }

int main()
{
    std::thread t1{is};
    std::thread t2{std::move(t1)};      // t1 artık bir iş parçacığını temsil etmiyor
    t2.join();
    std::printf("%d\n", t1.joinable()); // 0: t1'in sonlandırıcısı terminate çağırmaz
}
```

## Test 2 — iddia 5: senkronizasyon kurmayan atomik erişimler data race oluşturmaz

```cpp
#include <atomic>
#include <cstdio>
#include <thread>

std::atomic<int> sayac{0};

void artir()
{
    for (int i = 0; i < 100000; ++i)
        sayac.fetch_add(1, std::memory_order_relaxed);  // senkronizasyon işlemi değil
}

int main()
{
    std::thread t1{artir};
    std::thread t2{artir};
    t1.join();
    t2.join();
    std::printf("%d\n", sayac.load());  // 200000
}
```

## Test 3 — iddia 15: `const` nesnenin `mutable` elemanı değiştirilebilir

```cpp
#include <cstdio>

struct Onbellek {
    mutable int sorgu_sayisi = 0;
    int deger() const { ++sorgu_sayisi; return 42; }   // const işlevde yazma
};

const Onbellek ortak{};

int main()
{
    ortak.deger();
    ortak.deger();
    std::printf("%d\n", ortak.sorgu_sayisi);    // 2: const nesneye "okuma" yazma yaptı
}
```
