# Tarama — Cilt I Kısım 6 (Ekim 2026)

Kısım 6'daki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). C++ kaynakları
bölüm adlarıyla verilir; paragraf numaraları C++23 metnine (N4950) göredir, C++20 (N4861)
farklıysa ayrıca yazılır. C dilindeki iddialar C11 metniyle (N1570) karşılaştırıldı. 6.6
Ekim 2026'da panelden geçmişti; bu turda yeniden tarandı. Cilt I C++20'yi anlattığı hâlde
her cümle C++23'te de doğru kalmalıdır (kümülatif ilke); bu açıdan ayrıca işaret gerektiren
cümle bulunmadı: 18. satırdaki eksiklik C++20'de de C++23'te de geçerlidir (P2788R0, C++20'ye
kusur raporu olarak uygulandı).

**İşlem (2026-10):** "düzeltilmeli", "eksik" ve "gerçekleme" sonuçlu bütün iddialar
düzeltildi; metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-10-31_c1-06-tarama`,
iki tur). Panel ayrıca şunları düzeltti: 6.1'de zorunluluk yeniden "`const` bir değişken
tanımlarken" biçimine döndü, sınıf türü istisnası "bazı sınıf türleri" oldu (test 1'in
karşıtı: `struct Nokta { int x; }; const Nokta n;` sentaks hatasıdır); C'de "bildirilebilir"
yerine "tanımlanabilir" yazıldı; 6.2'ye doğrudan değiştirme örneği ve C'deki tanımsız davranış
eklendi; 6.5'teki istisnalara daha önceki bildirim eklendi, modül istisnası "bazı
değişkenler" oldu; 6.6'da `consteval` eklendi ve başlık "Sabit ifadede neler yapılamaz?" oldu.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 6.1 | `const` değişkenlere ilk değer vermek zorunludur; `const int y;` sentaks hatasıdır | [dcl.init.general]/8: `const` nitelikli bir nesnenin varsayılan ilk değer almasını gerektiren program, tür *const-default-constructible* bir sınıf türü (ya da dizisi) değilse geçersizdir. Kullanıcı tanımlı varsayılan kurucusu olan bir sınıf türünden `const` nesne ilk değersiz tanımlanabilir; `extern const int y;` ise tanım değil bildirimdir. `int` için iddia doğrudur | eksik (test 1) |
| 2 | 6.1 | C'de ilk değer almamış `const` değişken bildirilebilir | C11 6.7.3 ve 6.7.9 böyle bir kısıt koymaz. C++ Ek C ([diff.basic], `const` bağlantı maddesi) yalnızca C++'ın açık ilk değeri "teşvik ettiğini" söyler; doğrudan bir karşılaştırma maddesi yok | doğru |
| 3 | 6.1 | `const` bir nesneyi dönüşümle değiştirmeye çalışmak tanımsız davranıştır; derleyici değerin değişmeyeceğini varsayabilir | [dcl.type.cv]/4 (örneğindeki `mutable` istisnasıyla); ikinci yarı tanımsız davranışın sonucudur | doğru |
| 4 | 6.2 | C'de `const T*` → `T*` dönüşümü serbesttir; örnekteki `int* p = cp;` "C'de derlenir" | C11 6.5.16.1/1 (kısıt): sol işlenenin gösterdiği tür sağdakinin bütün niteleyicilerine sahip olmalıdır; 6.7.9/11: ilk değer vermede aynı kısıtlar geçerlidir; 5.1.1.3/1: kısıt ihlali tanı mesajı gerektirir. Yani C'de de bu dönüşüm geçersizdir; C derleyicilerinin bunu yalnızca uyarıyla geçmesi gerçeklemenin tercihidir | düzeltilmeli |
| 5 | 6.2 | C++'ta `const T*` türünden `T*` türüne örtülü dönüşüm yoktur | [conv.qual]/3: dönüşüm yalnızca niteleyici birleşimi hedef türün kendisiyse yapılır | doğru |
| 6 | 6.2 | `const T&` → `T&` dönüşümü yoktur; `const` nesne `const` olmayan referansa bağlanamaz | [dcl.init.ref]/4–5 (5.2: `const` nitelikli olmayan türe lvalue referansı bağlanamazsa program geçersizdir) | doğru |
| 7 | 6.2 | Yazı sabitlerinin türü C++'ta `const char[N]`, C'de `char[N]`'dir | [lex.string], Tablo 12 ("array of n const char"); C11 6.4.5/6 (elemanlar `char` türündendir) | doğru |
| 8 | 6.2 | C++'ta yazı sabitini değiştirmeye çalışan kod derlenmez | `const_cast` ile değiştirme girişimi derlenir; davranışı tanımsızdır ([lex.string], Not 4; C11 6.4.5/7'de de tanımsızdır). Doğrudan atama derlenmez | eksik (test 2) |
| 9 | 6.2 | `char* p = "merhaba";` C++'ta sentaks hatasıdır | [lex.string] Tablo 12 + [conv.qual]/3 (dizi → `const char*`, oradan `char*`'a dönüşüm yok) | doğru |
| 10 | 6.3 | `const int* p1` gösterilen nesneyi, `int* const p2` göstericinin kendisini `const` yapar | [dcl.ptr]/1 | doğru |
| 11 | 6.3 | Okuma kuralı: `const` hemen solundakini, solunda bir şey yoksa sağındakini niteler | Anımsatıcıdır; [dcl.ptr]/1 (`*`'tan sonraki niteleyici göstericiyi niteler) ve [dcl.type.general] (bildirim belirleyicilerinin sırası serbesttir) ile uyumlu | doğru |
| 12 | 6.3 | `const` göstericiye ilk değer vermek zorunludur ve sonradan başka nesneye yönlendirilemez | [dcl.init.general]/8 (skaler `const` nesnenin varsayılan ilk değeri geçersiz); [expr.ass]/1 (sol işlenen değiştirilebilir lvalue olmalı) | doğru |
| 13 | 6.4 | Okuma amaçlı bağlantılar `const` olmalıdır; `const` eklememek zinciri büyütür | Tasarım önerisi, normatif iddia değil. Altındaki kural doğru: `const` olmayan üye işlev `const` nesne üzerinden çağrılamaz ([over.match.funcs]) | doğru |
| 14 | 6.5 | `const int b = oku();` geçerli; `constexpr int d = oku();` sentaks hatası | [dcl.constexpr]/6 (C++20: /10): `constexpr` değişkenin ilk değer ifadesi sabit ifade olmalıdır | doğru |
| 15 | 6.5 | Dizi boyutu, `case` etiketi, şablon argümanı ve `static_assert` koşulu derleme zamanında bilinen değer gerektirir | [dcl.array]/1, [stmt.label], [temp.arg.nontype], [dcl.pre] (hepsi sabit ifade ister) | doğru |
| 16 | 6.5 | C'de `const int` bir değişken sabit ifade gerektiren yerlerde kullanılamaz | C11 6.6/6: tamsayı sabit ifadesinin işlenenleri arasında değişken yoktur. 6.6/10 gerçeklemenin başka biçimleri kabul etmesine izin verir; taşınabilir C için iddia doğrudur | doğru |
| 17 | 6.5 | C++'ta sabit ifadeyle ilk değer verilmiş `const int` sabit ifade gerektiren yerde kullanılabilir | [expr.const]/3–4: yalnızca `constexpr` değişkenler ile `volatile` olmayan `const` **tamsayı ya da numaralandırma** türünden (ve referans türünden) değişkenler. `const int` için doğru; okur `const double`'a genellememelidir | doğru |
| 18 | 6.5 | Namespace kapsamındaki `const` değişkenler örtülü olarak iç bağlantılıdır | [basic.link]/3.2: yalnızca şablon olmayan, `volatile` olmayan değişkenler; `extern` ya da `inline` bildirilenler ve önceki bildirimi iç bağlantılı olmayanlar hariç. C++20 metninde (N4861) dışa aktarılanlar (`export`), P2788R0 sonrasında (C++20'ye kusur raporu; N4950) modül arayüz biriminin kapsamında bildirilenler de hariçtir | eksik |
| 19 | 6.6 | Argümanlar derleme zamanında biliniyorsa sonuç derleme zamanında hesaplanabilir; `constexpr int a = kare(5);` derleme zamanında hesaplanır | [expr.const] (`constexpr` değişkenin ilk değeri açıkça sabit değerlendirilen *(manifestly constant-evaluated)* bir ifadedir); "hesaplanabilir" ihtiyatı yerinde | doğru |
| 20 | 6.6 | `constexpr` işlevler örtülü olarak `inline`'dır | [dcl.constexpr]/1 | doğru |
| 21 | 6.6 | Derleyici, `constexpr` olmayan bir işlevin gövdesini derleme zamanında çalıştırmaz | [expr.const]/5.3 (C++20: /5.2): `constexpr` olmayan bir işlevin çağrısı çekirdek sabit ifade *(core constant expression)* değildir. Standart derleyicinin ne yürüttüğünü söylemez; "as-if" kuralı ([intro.abstract]/1) gereği gerçekleme sabit ifade olmayan bir çağrıyı da çeviri sırasında hesaplayabilir | gerçekleme |
| 22 | 6.6 | Derleme zamanında giriş-çıkış gibi çalışma zamanına ait işler yapılamaz | [expr.const]/5.3 (G/Ç işlevleri `constexpr` değildir) | doğru |
| 23 | 6.6 | C++20'den itibaren dinamik bellek ayrılabilir, ama aynı hesaplama bitmeden geri verilmelidir | P0784R7; [expr.const]/5.18–5.21. C++23'te de aynı | doğru |
| 24 | 6.6 | `constexpr`, "her zaman derleme zamanında çalış" değil "gerekirse çalışabil" demektir | [dcl.constexpr], [expr.const] (sabit değerlendirme yalnızca gerektiren bağlamda zorunlu) | doğru |

**Özet:** 24 iddia — 19 doğru, 1 düzeltilmeli, 3 eksik, 1 gerçekleme.

## Önerilen düzeltmeler

- **İddia 1 (6.1):** "`const` değişkenlere ilk değer vermek zorunludur" cümlesi, temel türler
  için geçerli olduğu ve kullanıcı tanımlı varsayılan kurucusu olan sınıf türlerinin istisna
  olduğu belirtilerek daraltılmalı (ya da "temel türden `const` değişkenlere" denmeli).
- **İddia 4 (6.2):** "C dilinde bu dönüşüm serbesttir" cümlesi ve örnekteki "C'de derlenir"
  yorumu kaldırılmalı; C'de de bu dönüşüm kısıt ihlali olduğundan madde "C++'a özgü fark"
  başlığından çıkarılmalı ya da yalnızca C++ kuralı olarak anlatılmalı (derleyicilerin C'de
  uyarıyla geçmesi gerçekleme davranışıdır, kitaba girmez).
- **İddia 8 (6.2):** "yazı sabitini değiştirmeye çalışan kod derlenmez" cümlesine "doğrudan
  değiştirme; `const_cast` ile denenirse kod derlenir ama davranış tanımsızdır" eklenmeli.
- **İddia 18 (6.5):** "örtülü olarak iç bağlantılıdır" cümlesine "`volatile`, `extern` ya da
  `inline` değilse ve bir modül arayüzünde bildirilmemişse" kaydı eklenmeli.
- **İddia 21 (6.6):** "Derleyici ... çalıştırmaz" yerine "`constexpr` olmayan bir işlevin
  çağrısı sabit ifadede yer alamaz" gibi standardın diliyle bir cümle yazılmalı.

## Test 1 — iddia 1: kullanıcı tanımlı varsayılan kurucusu olan `const` nesne ilk değersiz tanımlanabilir

```cpp
struct Sayac {
    Sayac() { }
    int n = 0;
};

const Sayac sayac_nesnesi;       // geçerli: varsayılan kurucu kullanıcı tanımlı
extern const int bildirilen;     // geçerli: tanım değil, bildirim
const int ilk_degersiz;          // sentaks hatası
```

## Test 2 — iddia 8: yazı sabitini değiştirme girişimi `const_cast` ile derlenir

```cpp
void yazi_degistir()
{
    char* p = const_cast<char*>("merhaba");   // derlenir
    p[0] = 'M';                               // derlenir; çalıştırılırsa davranış tanımsız
}
```
