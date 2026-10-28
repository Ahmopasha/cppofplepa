# Tarama — Cilt II Kısım 15 (Ekim 2026)

Kısım 15'teki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar
çalışma taslağının (eel.is/c++draft) bölüm adlarıyla verilir; paragraf numaraları C++23
metnindendir (N4950). Sürüm iddiaları ilgili standart metninde (N4140 = C++14, N4659 =
C++17, N4861 = C++20) türün varlığına bakılarak denetlendi. 15.0 normatif iddia
içermiyor.

**İşlem (2026-10):** "düzeltilmeli", "eksik" ve "gerçekleme" sonuçlu bütün iddialar
düzeltildi; metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-10-28_c2-15-tarama`,
dört tur). İki ayrılık: iddia 30'daki `[[nodiscard]]` bilgisi metne alınmadı (güncel taslakta
`std::async` bildiriminde yok); "Ek gözlemler"deki "`seq`'ten farklı olarak" yanlıştır,
[execpol.seq]/2'ye göre `seq`'te de `std::terminate` çağrılır. `std::pmr` atfı kitapta
anlatılmadığı için eklenmedi. Panel ayrıca şunları ekletti: tanımsız davranış sınırı ve soyut
makine tanımı (15.1), yalancı uyanmanın yüklemsiz `wait` ile sınırlanması (15.4),
`set_exception`'ın hatayı sakladığı (15.5), ilkesiz ya da çok ilkeli çağrıda da sonlandırıcının
beklemesi (15.6), öğe erişim işlevi kapsamı ve "algoritmaların çoğu" (15.9), data race
kuralının global ayırma işlevleriyle sınırlanması (15.10).

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 15.1 | Tek iş parçacıklı programlarda derleyicinin tek yükümlülüğü gözlemlenebilir davranışın kaynak koddaki gibi olmasıdır | [intro.abstract]/1: gerçekleme soyut makinenin yalnızca gözlemlenebilir davranışını taklit etmek zorundadır; bu kural iş parçacığı sayısından bağımsızdır. [intro.abstract]/5–6: gözlemlenebilir davranış `volatile` erişimler, dosyaya yazılan veri ve etkileşimli giriş-çıkışla sınırlıdır ve soyut makinenin **olası yürütmelerinden biriyle** aynı olmalıdır | eksik |
| 2 | 15.1 | Çok iş parçacıklı programlarda bir iş parçacığının yeniden sıralaması başka bir iş parçacığınca gözlemlenebilir | [intro.races] Not 21: data race içermeyen ve yalnızca `mutex` ile `seq_cst` atomik kullanan programlar, iş parçacıklarının basitçe iç içe geçmesi gibi davranır. Yeniden sıralama ancak data race (tanımsız) ya da `seq_cst` dışındaki sıralamalarla görülebilir | eksik |
| 3 | 15.1 | Bellek modelini C++11 tanımladı | N2429 "Concurrency memory model (final revision)"; C++11 [intro.multithread] | doğru |
| 4 | 15.1 | Varsayılan davranış sıralı tutarlılıktır: bütün atomik işlemler tek bir küresel sırada gerçekleşmiş gibi görünür ve her iş parçacığı kendi işlemlerini kaynak koddaki sırada yapar | [atomics.order]/4: tek toplam sıra S yalnızca **`seq_cst` işlemleri ve çitleri** kapsar. [atomics.order] Not 5: sıralı tutarlılık yalnızca data race içermeyen ve **yalnızca** `seq_cst` atomik kullanan programlar için sağlanır; `seq_cst` işlemleri çoğu durumda aynı iş parçacığının diğer atomik işlemlerine göre yeniden sıralanabilir | eksik |
| 5 | 15.1, 15.8 | Sıralı tutarlılık en güçlü garantidir, "en pahalı olanı da odur" | Güç kısmı [atomics.order]/4 ile doğru; maliyet hakkında standart bir şey söylemez | gerçekleme |
| 6 | 15.2 | `std::jthread` C++20'de eklendi | N4861 [thread.jthread.class] (C++17 metninde yok) | doğru |
| 7 | 15.2 | `std::jthread`'in sonlandırıcısı önce durma ister, sonra `join` eder | [thread.jthread.cons]/11: "If `joinable()` is true, calls `request_stop()` and then `join()`." | doğru |
| 8 | 15.2 | İş işlevi `std::stop_token` parametresi alırsa durma isteği bunun üzerinden iletilir | [thread.jthread.cons]/5: ifade geçerliyse işlev `get_stop_token()` ilk argüman olarak verilerek çağrılır | doğru |
| 9 | 15.2 | `join`/`detach` çağrılmadan nesnenin hayatı biterse program sonlanır (Cilt I 27.1'e gönderme) | [thread.thread.destr]/1: yalnızca `joinable()` ise; bkz. Cilt I Kısım 27 taraması, iddia 3 | eksik |
| 10 | 15.3 | Standart kütüphane dört `mutex` türü sunar | [thread.mutex]: `mutex`, `recursive_mutex`, `timed_mutex`, `recursive_timed_mutex`, `shared_mutex`, `shared_timed_mutex` — altı tür | düzeltilmeli (test 1) |
| 11 | 15.3 | `std::shared_mutex` C++17'de geldi | N4508 "Shared Mutex"; N4659 [thread.sharedmutex.class] (C++14'te yalnızca `shared_timed_mutex`, N3891) | doğru |
| 12 | 15.3 | `shared_mutex` okuyucuların aynı anda girmesine izin verir; yazıcı tek başına kilitler | [thread.sharedmutex.requirements.general]/1–2: özel (*exclusive*) ve paylaşımlı (*shared*) sahiplik kipleri | doğru |
| 13 | 15.3 | `lock_guard` taşınamaz, ertelenemez | [thread.lock.guard]: kopyalama silinmiş, taşıyan üye yok; kurucular yalnızca kilitleyen ve `adopt_lock_t` alan biçimlerdir | doğru |
| 14 | 15.3 | `unique_lock` taşınabilir, ertelenebilir, `condition_variable` ile çalışır | [thread.lock.unique] (`defer_lock_t` kurucusu, taşıyan üyeler); [thread.condition.condvar]: `wait` `unique_lock<mutex>&` alır | doğru |
| 15 | 15.3 | `scoped_lock` birden fazla kilidi kilitlenme riski olmadan alır (C++17); sıra fark etmez | P0156R2 "Variadic lock_guard"; [thread.lock.scoped]; [thread.lock.algorithm]/5: çağrı dizisi kilitlenmeye yol açmaz, algoritma belirtilmemiştir | doğru |
| 16 | 15.3 | `shared_lock` C++14'te geldi | N3659 "Shared Locking Revision 2"; N4140 [thread.lock.shared] | doğru |
| 17 | 15.3 | Kilit sarmalayıcıları dörde ayrılır | [thread.lock]: `lock_guard`, `scoped_lock`, `unique_lock`, `shared_lock` | doğru |
| 18 | 15.4 | `wait` kilidi geçici olarak bırakır, uyanınca yeniden alır; bu yüzden `unique_lock` gerekir | [thread.condition.condvar]/8.1–8.2; `condition_variable` yalnızca `unique_lock<mutex>` alır (`condition_variable_any` başka kilitlenebilir türlerle de çalışır) | doğru |
| 19 | 15.4 | Yüklemsiz `wait` yalancı uyanmada hatalı devam eder; yüklemli biçim uyandığında koşulu yeniden denetler | [thread.condition.condvar]/8.3: `wait` "spuriously" de dönebilir — doğru. Ama /13: yüklemli biçim `while (!pred()) wait(lock);` eşdeğeridir; koşulu **beklemeden önce** de denetler, böylece bekleme başlamadan yapılmış bildirimin kaçırılmasını da önler. Yüklemsiz biçim döngü içinde doğru kullanılabilir | eksik (test 2) |
| 20 | 15.4 | Koşulu değiştiren kod kilit altında olmalıdır, aksi hâlde bildirim kaçırılabilir | cppreference, `std::condition_variable`: paylaşılan değişken atomik olsa bile bekleyen iş parçacığına doğru yayımlanması için `mutex` tutulurken değiştirilmelidir; atomik değilse kilitsiz değişiklik zaten data race'tir ([intro.races]/21) | doğru |
| 21 | 15.4 | `notify_one` bir bekleyeni, `notify_all` hepsini uyandırır | [thread.condition.condvar]/5–6 | doğru |
| 22 | 15.5 | `get()` değer gelene kadar bloklar ve yalnızca bir kez çağrılabilir; birden çok okuyucu için `shared_future` | [futures.unique.future]: `get` önce `wait()` çağırır, sonra `valid() == false` olur; /3: geçersiz nesnede `get` tanımsız davranıştır. [futures.shared.future]/1 | doğru |
| 23 | 15.5 | Hata `set_exception` ile gönderilir, `get()`'te yeniden fırlatılır | [futures.promise] (`set_exception`); [futures.unique.future] (`get`: saklanan hatayı fırlatır) | doğru |
| 24 | 15.5 | Bu, `exception_ptr` mekanizmasının uygulamasıdır; "iş parçacığı sınırını aşan tek hata taşıma yolu budur" | `exception_ptr` herhangi bir paylaşılan değişkenle de taşınabilir (`current_exception`/`rethrow_exception`, [propagation]); yakalanan hata nesnesi değer olarak kopyalanarak da taşınabilir. `future` da `exception_ptr` da tek yol değildir | düzeltilmeli (test 3) |
| 25 | 15.6 | Çalıştırma ilkesi iki değer alır | [future.syn]: `enum class launch { async, deferred, implementation-defined }` — gerçekleme ek değer tanımlayabilir; değerler bit maskesidir, `async \| deferred` ilkesiz çağrının anlamıdır ([futures.async]/3) | eksik |
| 26 | 15.6 | `launch::async`: yeni iş parçacığında hemen başlar | [futures.async]/3.1: işlev "**sanki** bir `thread` nesnesinin temsil ettiği yeni bir yürütme akışında" çağrılır; ne zaman başlayacağı belirtilmez | eksik |
| 27 | 15.6 | `launch::deferred`: `get()` çağrılana kadar hiç çalışmaz, sonra çağıran iş parçacığında çalışır | [futures.async]/3.2: ilk **zaman aşımsız bekleme işlevi** (`get` ya da `wait`) işlevi çağıran iş parçacığında çalıştırır; [futures.unique.future]/22–23: `wait_for` çalıştırmaz, `future_status::deferred` döndürür | eksik (test 4) |
| 28 | 15.6 | İlke yazılmazsa seçim gerçeklemeye bırakılır; "derleyici ikisinden birini seçebilir" | [futures.async]/3: ilkesiz çağrı `launch::async \| launch::deferred` ile aynıdır, gerçekleme herhangi birini seçebilir — doğru. Seçimi derleyici değil gerçekleme yapar; önerilen uygulama seçimin çalışma anında, eşzamanlılık olanağına göre yapılmasıdır (/3.2, "Recommended practice") | eksik |
| 29 | 15.6 | `std::async` ile elde edilen `future`'ın sonlandırıcısı bloklar | [futures.state]/5.3: durum `async` ile yaratılmışsa, henüz hazır değilse ve son başvuru buysa bloklayabilir; [futures.async]/4.2 bunu `launch::async` seçildiğinde fiilen zorunlu kılar. `launch::deferred` seçildiyse sonlandırıcı beklemez ve işlev hiç çağrılmaz ([futures.async] Not 1). Örnek `launch::async`'i açıkça yazdığı için örnek doğru | eksik (test 5) |
| 30 | 15.6 | Dönüş değeri tutulmazsa geçici nesne hemen yok olur ve satır iş bitene kadar bekler | `launch::async` ile 29'daki kural; ayrıca C++20'den beri `async` `[[nodiscard]]`'dır ([futures.async], N4861 ve N4950 bildirimleri) | doğru |
| 31 | 15.7 | `packaged_task` bir çağrılabilir nesneyi sarmalar ve sonucunu `future` ile sunar; ne zaman çalışacağına çağıran karar verir | [futures.task]/1–2 | doğru |
| 32 | 15.8 | Atomik işlem bölünemez; yarım görülemez | [atomics.order] Not 2: her atomik erişim aynı nesneye yapılan diğer atomik erişimlere göre bölünemez (*indivisible*) olmalıdır | doğru |
| 33 | 15.8 | Temel işlemler: `load`, `store`, `exchange`, `compare_exchange_weak`, `compare_exchange_strong` | [atomics.types.operations] | doğru |
| 34 | 15.8 | `is_lock_free()`, işlemin donanım desteğiyle mi yoksa arka planda bir kilitle mi yapıldığını bildirir; büyük türlerde kilit kullanılırsa atomiğin kazancı kalmaz | [atomics.lockfree]/3, [atomics.types.operations]/5: nesnenin işlemlerinin kilitsiz (*lock-free*) olup olmadığını bildirir; kilitsizlik ilerleme garantisiyle tanımlanır ([atomics.lockfree]/4, [intro.progress]). "Donanım", "arka planda kilit" ve "kazanç kalmaz" gerçekleme anlatımıdır; kilitli gerçeklenen atomik de data race'i önler | gerçekleme |
| 35 | 15.8 | `std::atomic_flag` her zaman kilitsiz olma garantisi veren tek türdür | C++20'den beri barındırılan (*hosted*) gerçeklemede `atomic_signed_lock_free` ve `atomic_unsigned_lock_free` da `is_always_lock_free`'dir ([atomics.alias]/2, P1135R6); [atomics.lockfree]/2: en az bir işaretli tamsayı özelleşmesi daima kilitsizdir. (cppreference'ın `atomic_flag` sayfası da eski ifadeyi taşıyor; standart esastır) | düzeltilmeli (test 6) |
| 36 | 15.8 | `atomic_flag` yalnızca `test_and_set` ve `clear` işlemlerini sunar | [atomics.flag]: C++20'den beri `test`, `wait`, `notify_one`, `notify_all` da vardır (P1135R6) | düzeltilmeli (test 6) |
| 37 | 15.8 | Her atomik işlem bir `std::memory_order` alabilir | İşleç biçimleri almaz ve daima `seq_cst`'tir: `operator=` `store(desired)`'a, `operator T` `load()`'a eşdeğerdir ([atomics.types.operations]) | eksik |
| 38 | 15.8 | Varsayılan `memory_order_seq_cst`'tir | [atomics.types.operations]: varsayılan argüman `memory_order::seq_cst` | doğru |
| 39 | 15.8 | Tablo: `seq_cst` "küresel tek sıra" | 4 ile aynı: S yalnızca `seq_cst` işlemleri üzerinde tanımlıdır | eksik |
| 40 | 15.8 | Tablo: `acquire`/`release` bir çift arasında sıralama kurar | [atomics.order]/2: bırakma işlemi, bırakma dizisindeki değeri okuyan edinme işlemiyle senkronize olur | doğru |
| 41 | 15.8 | Tablo: `relaxed` yalnızca atomiklik verir, "sıralama garantisi yok" | [atomics.order]/1.1: başka belleği sıralamaz — doğru; ama her atomik nesnenin değişiklik sırası ve tutarlılık (*coherence*) kuralları ([intro.races]/4, /15–18) `relaxed` işlemlere de uygulanır | eksik |
| 42 | 15.8 | Tabloda üç sıralama var | [atomics.order]: `memory_order` altı değer alır: `relaxed`, `consume`, `acquire`, `release`, `acq_rel`, `seq_cst` (`consume` için Not 1 `acquire`'ı önerir) | eksik |
| 43 | 15.8 | Sayaç gibi bağımsız işlemlerde `relaxed` güvenlidir; bayrak ve kilit kurulumunda `acquire`/`release` gerekir | Sayaç değeri `join` sonrasında okunursa doğru ([thread.thread.member]/4; Cilt I Kısım 27 taraması, test 2); bayrakta en az `acquire`/`release` gerekir, `seq_cst` de yeter | doğru |
| 44 | 15.9 | C++17 algoritmalara çalıştırma ilkesi parametresi ekledi | N4659 [execpol]; P0024R2 | doğru |
| 45 | 15.9 | Kilit, iş parçacığı ve bölme işini kütüphane üstlenir; `par` paraleldir | [execpol.par]/1: yürütme "paralelleştirilebilir" (*may be parallelized*) — izin verir, zorunlu kılmaz; [algorithms.parallel.exec]/6: çağrılar çağıran iş parçacığında da çalışabilir | eksik |
| 46 | 15.9 | Dört ilke vardır: `seq`, `par`, `par_unseq`, `unseq` (C++20) | P1001R2; N4861 [execpol.unseq] (N4659'da yok). [execpol.type]/2: gerçekleme standart dışı ilke de tanımlayabilir | doğru |
| 47 | 15.9 | Geçirilen çağrılabilir nesneler data race üretmemeli | [algorithms.parallel.exec]/6, Not 6 ve Örnek 1; data race zaten tanımsızdır ([intro.races]/21) | doğru |
| 48 | 15.9 | `par_unseq` durumunda kilit bile alınmamalıdır; vektörleşme işlemleri birbirine geçirir | [algorithms.parallel.exec]/7: `par_unseq`'te vektörleşmeye uygun olmayan (*vectorization-unsafe*, [algorithms.parallel.defns]/4) kütüphane işlevini çağırmak tanımsız davranıştır — doğru; /5: aynı kural `unseq` için de geçerlidir | eksik |
| 49 | 15.9 | Küçük kaplarda iş parçacığı kurma maliyeti kazancı aşar | Maliyet ve iş parçacığı kurulması gerçeklemeye bağlıdır; standart iş parçacığı kurulmasını bile garanti etmez (45) | gerçekleme |
| 50 | 15.10 | Genel amaçlı ayırıcı bütün iş parçacıklarınca paylaşılır, kendi içinde senkronizasyon yapar; çok küçük ayırmada darboğaz olur | [new.delete.dataraces]: ayırma/bırakma işlevleri yalnızca data race oluşturmamalı ve belirli bir depolama birimi için tek toplam sırada olmalıdır; iç yapı (paylaşılan havuz, kilit) ve ölçekleme gerçeklemeye bağlıdır | gerçekleme |
| 51 | 15.10 | Çözüm iş parçacığına özel havuz kullanan bir ayırıcı yazmaktır; kapların ayırma biçimini değiştirmenin yolu `std::allocator` arayüzüdür | Özel ayırıcı `std::allocator`'ın değil ayırıcı gereksinimlerinin ([allocator.requirements]) arayüzünü sağlar; C++17'den beri `std::pmr::unsynchronized_pool_resource` ([mem.res.pool.overview]) standart bir havuz kaynağıdır | eksik |

## Önerilen düzeltmeler

- **1:** "Derleyici" yerine "gerçekleme", "kaynak koddaki gibi" yerine "soyut makinenin olası yürütmelerinden biriyle aynı" denmeli ve kuralın çok iş parçacıklı programlarda da geçerli olduğu söylenmeli.
- **2:** "Bu yeniden sıralamalar ancak data race (tanımsız davranış) ya da gevşetilmiş atomik sıralamalar yoluyla gözlemlenebilir" kaydı eklenmeli.
- **4, 39:** "Bütün `seq_cst` atomik işlemleri tek bir toplam sırada görünür; data race içermeyen ve yalnızca `seq_cst` kullanan bir program, iş parçacıklarının işlemleri iç içe geçirilmiş gibi davranır" biçiminde daraltılmalı.
- **5:** "En pahalı" ifadesi çıkarılmalı ya da "gerçeklemelerde genellikle daha maliyetli" gibi standart dışı bir gözlem olarak işaretlenmeli.
- **9:** Cilt I 27.1'deki düzeltmeyle uyumlu olarak "bir iş parçacığını temsil eden nesnenin" kaydı eklenmeli.
- **10:** "Altı `mutex` türü" denmeli; tabloya `recursive_timed_mutex` ve `shared_timed_mutex` (C++14) eklenmeli.
- **19:** Yüklemli biçimin `while (!pred()) wait(lock);` eşdeğeri olduğu, koşulu beklemeden önce de denetlediği ve böylece erken gelen bildirimi de karşıladığı yazılmalı.
- **24:** "Tek yol" iddiası çıkarılmalı; örneğin "hatayı iş parçacıkları arasında taşımanın hazır yoludur" denmeli; iş parçacığı işlevinden kaçan hatanın `std::terminate` çağırdığı ([thread.thread.constr]/5) eklenebilir.
- **25:** "Standart iki değer tanımlar; değerler birleştirilebilir ve gerçekleme ek değer tanımlayabilir" denmeli.
- **26:** "Sanki yeni bir iş parçacığında çalışır" denmeli; "hemen" çıkarılmalı.
- **27:** "`get()` ya da `wait()` çağrılana kadar çalışmaz; `wait_for`/`wait_until` onu çalıştırmaz" denmeli.
- **28:** "Derleyici" yerine "gerçekleme" yazılmalı; seçimin çalışma anında da yapılabileceği eklenmeli.
- **29:** "`launch::async` ile başlatılmış ve henüz bitmemiş işin son `future`'ı yok edilirken iş beklenir; `launch::deferred`'da beklenmez" diye daraltılmalı; `async`'in C++20'den beri `[[nodiscard]]` olduğu eklenebilir.
- **34:** "`is_lock_free()`, bu türün işlemlerinin kilitsiz olup olmadığını bildirir; derleme anında `is_always_lock_free` (C++17) kullanılabilir" denmeli; "kazancı kalmaz" yerine "kilitsizlik ve performans garantisi kalmaz, data race güvenliği kalır" yazılmalı.
- **35:** "C++20'den önce tek türdü; C++20'den beri barındırılan gerçeklemelerde `std::atomic_signed_lock_free` ve `std::atomic_unsigned_lock_free` da her zaman kilitsizdir" denmeli.
- **36:** C++20 ile eklenen `test`, `wait`, `notify_one`, `notify_all` işlevleri anılmalı.
- **37:** "Üye işlevler bir `std::memory_order` alabilir; işleç biçimleri daima `seq_cst` kullanır" denmeli.
- **41:** "Başka verilere sıralama getirmez; aynı atomik nesne üzerindeki değişikliklerin tek bir sırası yine vardır" denmeli.
- **42:** Tabloya `acq_rel` eklenmeli; `consume`'un var olduğu ama `acquire`'ın önerildiği bir dipnotla belirtilmeli.
- **45:** "`par` paralel yürütmeye izin verir; gerçekleme algoritmayı çağıran iş parçacığında da yürütebilir" denmeli.
- **48:** Kural `unseq` için de söylenmeli.
- **49:** Gerçekleme gözlemi olarak işaretlenmeli ("küçük kaplarda paralel yürütmenin ek maliyeti kazancı aşabilir").
- **50:** "Standart, ayırma işlevlerinin data race üretmemesini şart koşar; bunu nasıl sağladıkları gerçeklemeye bağlıdır ve birçok gerçeklemede eşzamanlı küçük ayırmalar ölçeklemeyi sınırlayabilir" gibi gerçekleme olarak işaretlenmeli.
- **51:** "Ayırıcı gereksinimleri (Kısım 17.7)" denmeli; `std::pmr` havuz kaynaklarına gönderme eklenebilir.

## Ek gözlemler (düzyazı iddiası değil)

- **15.5 örneği** yalnızca `<future>`'ı içeriyor ama `std::jthread` kullanıyor; standart `<future>`'ın `<thread>`'i içermesini garanti etmez. Kod denetimi başlıkları kendisi eklediği için bu sorun görünmüyor; okurun derlediği kodda `#include <thread>` gerekir.
- **15.9** paralel algoritmaların hata davranışından söz etmiyor: `par`, `par_unseq` ve `unseq` ilkelerinde öğe erişim işlevinden hata kaçarsa `std::terminate` çağrılır ([execpol.par]/2, [execpol.parunseq]/2, [execpol.unseq]/2); `seq`'ten farklı olarak hata çağırana ulaşmaz. 15.5'teki hata taşıma anlatımına bir cümle olarak eklenebilir.

## Test 1 — iddia 10: standart kütüphanede altı `mutex` türü vardır

```cpp
#include <mutex>
#include <shared_mutex>

std::mutex m1;
std::recursive_mutex m2;
std::timed_mutex m3;
std::recursive_timed_mutex m4;
std::shared_mutex m5;
std::shared_timed_mutex m6;
```

## Test 2 — iddia 19: yüklemli `wait` koşulu beklemeden önce de denetler

```cpp
#include <condition_variable>
#include <cstdio>
#include <mutex>

int main()
{
    std::mutex m;
    std::condition_variable cv;
    bool hazir = true;                          // bildirim hiç gelmeyecek

    std::unique_lock kilit{m};
    cv.wait(kilit, [&] { return hazir; });      // while (!hazir) cv.wait(kilit); — beklemez
    std::puts("beklemeden döndü");
}
```

## Test 3 — iddia 24: hata, `future` olmadan da iş parçacıkları arasında taşınır

```cpp
#include <cstdio>
#include <exception>
#include <stdexcept>
#include <thread>

int main()
{
    std::exception_ptr hata;
    std::runtime_error kopya{""};

    std::thread t{[&] {
        try { throw std::runtime_error{"uretici"}; }
        catch (const std::runtime_error& e) {
            hata = std::current_exception();    // exception_ptr, sıradan bir değişkende
            kopya = e;                          // ya da hata nesnesinin kopyası
        }
    }};
    t.join();                                   // join, yazmaları okumadan önceye sıralar

    try { std::rethrow_exception(hata); }
    catch (const std::runtime_error& e) { std::puts(e.what()); }   // uretici
    std::puts(kopya.what());                                        // uretici
}
```

## Test 4 — iddia 27: ertelenmiş işlevi `wait()` de çalıştırır, `wait_for` çalıştırmaz

```cpp
#include <chrono>
#include <cstdio>
#include <future>
#include <thread>

int main()
{
    const auto cagiran = std::this_thread::get_id();
    bool calisti = false;
    bool ayni_is_parcacigi = false;

    auto f = std::async(std::launch::deferred, [&] {
        calisti = true;
        ayni_is_parcacigi = std::this_thread::get_id() == cagiran;
        return 42;
    });

    auto durum = f.wait_for(std::chrono::seconds{0});
    std::printf("%d %d\n", durum == std::future_status::deferred, calisti);   // 1 0
    f.wait();                                                                 // get() değil
    std::printf("%d %d\n", calisti, ayni_is_parcacigi);                       // 1 1
    std::printf("%d\n", f.get());                                             // 42
}
```

## Test 5 — iddia 29: `launch::deferred` ile elde edilen `future`'ın sonlandırıcısı beklemez

```cpp
#include <cstdio>
#include <future>

int main()
{
    bool calisti = false;
    {
        auto f = std::async(std::launch::deferred, [&] { calisti = true; });
    }                                   // sonlandırıcı işlevi çalıştırmaz, beklemez
    std::printf("%d\n", calisti);       // 0
}
```

## Test 6 — iddia 35, 36: C++20'de kilitsizlik garantili tamsayı atomikleri ve yeni `atomic_flag` işlevleri

```cpp
#include <atomic>
#include <cstdio>

static_assert(std::atomic_signed_lock_free::is_always_lock_free);
static_assert(std::atomic_unsigned_lock_free::is_always_lock_free);

int main()
{
    std::atomic_flag bayrak;            // C++20'den beri temiz (clear) durumda kurulur
    bayrak.test_and_set();
    bool dolu = bayrak.test();          // C++20
    bayrak.clear();
    bayrak.notify_all();                // C++20
    bayrak.wait(true);                  // C++20; değer true olmadığı için hemen döner
    std::printf("%d %d\n", dolu, bayrak.test());    // 1 0
}
```
