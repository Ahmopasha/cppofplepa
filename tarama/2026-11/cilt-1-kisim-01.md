# Tarama — Cilt I Kısım 1 (Kasım 2026)

Kısım 1'deki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). C++ kaynakları C++20
(N4861) bölüm adlarıyla verilir. Kısım C ile karşılaştırma yaptığı için C iddiaları C17'ye (C11
N1570 madde numaraları; kod denetimi `-std=c17`) göre sınandı, kaynak olarak cppreference'ın
C sayfaları da kullanıldı. C23 birkaç farkı kapatmıştır.

**İşlem (2026-11):** "düzeltilmeli", "eksik" ve "gerçekleme" sonuçlu bütün iddialar düzeltildi;
metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-01_c1-01-tarama`, dört tur, iki
hakem: Gemini kotası doluydu). Panel ayrıca şunları düzeltti: `<=>` ve yüklenmiş operatörler;
ön ekli, çok karakterli ve temel karakter kümesi dışındaki karakter sabitleri; `nullptr`'ın örtülü
dönüşümü; `std` hükmünün makroları kapsamaması; örtülü işlev bildiriminin tanımı; C dil
bağlantısı; terim tanıtımları ve atıflar. Kısım 2.4.4'e atama ve koşul operatörü Kısım 2
taramasında eklenecek.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 1.1 | Birçok geçerli C programı C++'ta derlenmez | [diff.iso] | doğru |
| 2 | 1.1 | C bilmeyen bölümü atlayabilir; geri kalan bölümler bu bölümü varsaymaz | `nullptr`'ın tek anlatımı 1.5'te; Kısım 3.3 ve 8.2 onu açıklamasız kullanır | eksik |
| 3 | 1.1–1.9 | "C'de ..." anlatımları sürüm belirtmez | C23: `bool` anahtar sözcük, `f()` parametresiz, `nullptr`, sabit temel türlü `enum` | eksik |
| 4 | 1.2 | C'de `bool`, `int` üzerine kurulu bir makrodur | C11 7.18: `bool` makrosu `_Bool`'a genişler; 6.2.5: `_Bool` ayrı bir işaretsiz tamsayı türüdür | düzeltilmeli |
| 5 | 1.2 | Karşılaştırma ve mantık operatörleri C'de `int`, C++'ta `bool` döndürür | C11 6.5.8–6.5.14; [expr.rel], [expr.log.and] | doğru |
| 6 | 1.2 | `sizeof(1 == 1)` C'de 4, C++'ta 1 | `sizeof(int)` ve `sizeof(bool)` gerçeklemeye bağlıdır ([expr.sizeof]/1) | gerçekleme |
| 7 | 1.2 | Karakter sabiti C'de `int`, C++'ta `char`; `sizeof('A')` C'de 4 | C11 6.4.4.4/10; [lex.ccon]; `sizeof(char)` 1'dir, `sizeof(int)` gerçeklemeye bağlıdır | gerçekleme |
| 8 | 1.2 | Yazı sabiti C++'ta `const char[N]`, C'de `char[N]` | [lex.string], C11 6.4.5/6 | doğru |
| 9 | 1.3 | "`const T*` türünden `T*` türüne örtülü dönüşüm yoktur" bir C–C++ farkıdır | C11 6.5.16.1/1: C'de de kısıt ihlalidir (Kısım 6.2 düzeltildi) | düzeltilmeli |
| 10 | 1.3 | C++'ta `const` değişkene ilk değer vermek zorunludur | Kısım 6.1'in daraltılmış anlatımıyla: `const` bir değişken tanımlarken; bazı sınıf türleri ayrıdır | eksik |
| 11 | 1.3 | `const` tamsayı, sabit ifade gerektiren yerlerde kullanılabilir | [expr.const]: sabit ifadeyle ilk değer almışsa (Kısım 6.5) | eksik |
| 12 | 1.4 | C'de `void*` nesne göstericisine örtülü dönüşür, C++'ta dönüşmez | C11 6.3.2.3/1; [conv.ptr] | doğru |
| 13 | 1.4 | `malloc`, C kodunun derlenmemesinin "en sık sebebi"dir | Doğrulanamaz | gerçekleme |
| 14 | 1.5 | C'de `NULL` `0` veya `(void*)0` olarak tanımlıdır | C11 7.19/3, 6.3.2.3/3: gerçeklemeye bağlı boş gösterici sabiti | eksik |
| 15 | 1.5 | C++'ta `NULL` yalnızca `0`'dır | [support.types.nullptr]: "implementation-defined null pointer constant"; dipnot: "Possible definitions include 0 and 0L, but not (void*)0." | düzeltilmeli |
| 16 | 1.5 | `func(NULL)` belirsizlik yaratır | Sonuç `NULL`'ın tanımına bağlıdır: `0` ise `func(int)` seçilir, `0L` ise belirsizdir (test 1) | eksik |
| 17 | 1.5 | `nullptr` yalnızca göstericilere dönüşür | [conv.ptr], [conv.mem], [conv.bool]: üye göstericilerine ve doğrudan ilk değer vermede `bool`'a da dönüşür; tamsayıya dönüşmez | eksik (test 2) |
| 18 | 1.6 | C'de boş parantez parametreleri belirtmez ve her türlü çağrıya izin verir | C11 6.7.6.3/14; 6.5.2.2/6: sayı ya da tür uyuşmazsa tanımsız davranış. C23'te `(void)` ile aynıdır | eksik |
| 19 | 1.6 | C'de örtülü bildirim "C99'a kadar" mümkündür | C99 ile kalktı; yani C90'a kadar | eksik |
| 20 | 1.7 | `++x`, `--x` ve virgül C'de R-Value, C++'ta L-Value üretebilir | cppreference; [expr.pre.incr], [expr.comma]. Atama ve koşul işleci için de geçerlidir | eksik |
| 21 | 1.8 | C'de temel tür `int` olmak zorundadır | C11 6.7.2.2/4: `char`, işaretli ya da işaretsiz bir tamsayı türüyle uyumludur; seçim gerçeklemeye bağlıdır. Numaralandırıcılar `int`'tir | düzeltilmeli |
| 22 | 1.8 | C'de aritmetik türden `enum`'a dönüşüm serbest, C++'ta örtülü dönüşüm yok | C11 6.5.16.1; [conv.integral], [dcl.enum] | doğru |
| 23 | 1.8 | C++'ta temel türü "derleyici seçer" | [dcl.enum]/7: gerçeklemeye bağlı; /5: kapsamlı `enum`'da belirtilmezse `int` | eksik |
| 24 | 1.9 | Etiketler C'de ayrı isim uzayındadır, anahtar sözcük gerekir; C++'ta tür ismi doğrudan kullanılır | C11 6.2.3; [class.name] | doğru |
| 25 | 1.10 | `<cstdio>` gibi başlıklar isimleri `std`'ye yerleştirir | [headers]/5: `std` içindedir; önce küresel kapsamda bildirilip bildirilmediği belirtilmemiştir | eksik |
| 26 | 1.3, 1.7, 1.8, 1.10 | "Kısım 6'da ayrıntılandırıldı", "2.4.4'te verilmişti" gibi geçmiş zamanlı atıflar | Hedefler sonraki kısımlardadır; atıf yönü yanlış | düzeltilmeli |

**Sayım:** 26 iddia — 6 doğru, 5 düzeltilmeli, 12 eksik, 3 gerçekleme.

## Test 1 — iddia 16: `func(0)` belirsiz değildir, `func(0L)` belirsizdir

```cpp
void func(int);
void func(char*);

void sina()
{
    func(0);     // func(int)
    func(0L);    // sentaks hatası
}
```

## Test 2 — iddia 17: `nullptr`'ın dönüşümleri

```cpp
struct S { int m; };

int S::* uye = nullptr;
bool b{nullptr};
int i = nullptr;       // sentaks hatası
```
