# Tarama — Cilt I Kısım 15 (Kasım 2026)

Kısım 15'teki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış), **biçim** (terim
tanıtımı, `std::` öneki, atıf). Kaynaklar C++20 (N4861) bölüm adlarıyla. 15.0 normatif
iddia içermiyor.

**İşlem (2026-11):** "düzeltilmeli", "eksik" ve "biçim" sonuçlu bütün iddialar düzeltildi;
metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-13_c1-15-tarama`, üç hakem,
iki hakem turu; durma kuralı tur 2'de sağlandı; Claude hakemi xhigh). Panel ayrıca şunları
düzeltti: 3.2'ye geri atıf ve "ömür türü" terim uyumu, dinamik ömrün ölçütü, `thread_local`
ve Kısım 27 atfı, ilk değer verilmeyen elemanları okumanın tanımsız davranış olması,
`delete[]`, sıradan `new` sınırlaması, "çıplak `new`". Yazar kararıyla reddedilen: sınıfa
özgü `noexcept` `operator new`'in boş gösterici döndürebilmesi (Cilt II 17'de anlatılmıyor;
Cilt I için basitleştirme).

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 15.1 | Dört ömür kategorisi: otomatik, statik, dinamik, iş parçacığına özel | [basic.stc]/1: dört *storage duration*. Terim kitapta hiç tanıtılmıyor, sözlükte yok | doğru; biçim (terim tanıtımı) |
| 2 | 15.1 | Otomatik: bildirim noktasında başlar, kapsam bitince biter | [stmt.dcl]/2: akış bildirime her geldiğinde ilk değer alır | doğru (basitleştirme) |
| 3 | 15.1 | Statik: "program başında veya ilk kullanımda" hayata gelir | [stmt.dcl]/4: blok içindeki statik değişken akış bildirime **ilk geldiğinde** ilk değer alır, ilk kullanımda değil. [basic.start.dynamic]/5: blok dışındakilerde dinamik ilk değer verme `main`'in ilk deyiminden önce ya da ertelenerek (gerçeklemeye bağlı); Cilt II 17.5 | düzeltilmeli |
| 4 | 15.1 | Statik: program sonunda biter | [basic.start.term] | doğru |
| 5 | 15.1 | İş parçacığına özel: "iş parçacığı başlarken" hayata gelir, biterken biter | [stmt.dcl]/4: blok içindeyse akış bildirime ilk geldiğinde; [basic.start.dynamic]/7: blok dışındakilerde iş parçacığının ilk işlevinden önce ya da ertelenerek (gerçeklemeye bağlı). [basic.stc.thread]/2: iş parçacığı bitince yok edilir | eksik |
| 6 | 15.1 | Dinamik: başlangıç ve son programcıya bırakılır | [basic.stc.dynamic] | doğru |
| 7 | 15.2 | C++'ta dinamik bellek işlemleri operatör düzeyindedir | [expr.new], [expr.delete]; ayırma işlevi ayrı (Cilt II 17.1) | doğru |
| 8 | 15.2 | `new` bellek ayırır ve "kurucu işlevi çağırır" | [expr.new] (*new-initializer*), [dcl.init]: nesneye ilk değer verilir; kurucu yalnızca sınıf türünde. Hemen üstteki `new int[100]` örneğinde kurucu yok, elemanlar default-initialization ile değer almaz (Kısım 3.2) | eksik |
| 9 | 15.2 | `delete` sonlandırıcıyı çağırır ve belleği geri verir | [expr.delete]/6–7 | doğru |
| 10 | 15.2 | `malloc`/`free` yalnızca bellek işini yapar; sınıflarla kullanılmamalı | Öğüt. Metinde `std::` öneki yok | doğru; biçim (`std::`) |
| 11 | 15.2 | `new`/`delete` ve `new[]`/`delete[]` karıştırmak tanımsız davranış | [expr.delete]/2 | doğru |
| 12 | 15.2 | "`nullptr` üzerinde `delete` çağırmak" güvenli, hiçbir şey yapmaz | [expr.delete]/2, /6–7; [basic.stc.dynamic.deallocation]/4. Doğrusu: değeri boş gösterici olan bir göstericiye `delete` uygulamak. `delete nullptr;` yazımı sentaks hatasıdır (`std::nullptr_t` gösterici değil); `delete` işlev değil operatördür | eksik |
| 13 | 15.3 | Sızıntı: bellek program bitene dek geri gelmez | Standart sızıntıyı tanımsız davranış saymaz; metin de saymıyor | doğru |
| 14 | 15.3 | Çifte serbest bırakma tanımsız davranış | [basic.stc]/4: geçersiz gösterici değerinin ayırma geri verme işlevine verilmesi | doğru |
| 15 | 15.3 | Sarkan göstericiden erişim tanımsız davranış | [basic.stc]/4: geçersiz gösterici değeri üzerinden erişim | doğru |
| 16 | 15.3 | Üçü de "derleyicinin yakalayamadığı" hatalardır | Standart tanı istemez; derleyici bazı durumları yakalayabilir. "yakalamak zorunda olmadığı" | eksik |
| 17 | 15.4 | `new` ayıramazsa `std::bad_alloc` gönderir, `nullptr` döndürmez | [basic.stc.dynamic.allocation]/4: `std::bad_alloc` ile yakalanabilen türde bir hata. Hata gönderme ve `try`/`catch` Kısım 18'de; burada atıfsız kullanılıyor | doğru; biçim (atıf) |
| 18 | 15.4 | `new (std::nothrow)` hata göndermez, boş gösterici döndürür | [basic.stc.dynamic.allocation]/4, [new.delete.single] | doğru |
| 19 | 15.4 | Bellek yetmezliğinden kurtulmak çoğu uygulamada mümkün değil | Öğüt | doğru |
| 20 | 15.5 | "Sebebi Kısım 18.5'te görülmüştü" | Kısım 18, 15'ten sonra geliyor (yanlış yön) | düzeltilmeli |
| 21 | 15.5 | "Bir hata gönderildiğinde yığın geri sarılır" | [except.handle]/9: uygun `catch` bulunmazsa `std::terminate` çağrılır; geri sarılıp sarılmayacağı gerçeklemeye bağlı | eksik |
| 22 | 15.5 | "Doğru araç akıllı göstericilerdir"; örnekte `std::vector` | Örneğin ikinci satırı akıllı gösterici değil, kap (Kısım 23.4) | eksik |
| 23 | 15.5 | İleri konular Cilt II, Kısım 17'de | Cilt II 17.1–17.4 | doğru |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): bölümdeki bütün kod örnekleri
geçerli; `delete nullptr;` sentaks hatası.

Not (Kısım 25 taraması için): 25.1 "Kısım 18.6'da bunun gerekçesini görmüştük" diyor; gerekçe
(geri sarılırken çıplak belleğin sızması) 18.5'te.
