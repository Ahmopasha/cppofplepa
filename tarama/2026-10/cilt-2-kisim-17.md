# Tarama — Cilt II Kısım 17 (Ekim 2026)

Kısım 17'deki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar
çalışma taslağının (eel.is/c++draft) bölüm adlarıyla verilir; C++23 metninde aynı
bölümlerdir. 17.6 ve 17.9 Ekim 2026'da panelden geçtiği için bu turda taranmadı.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 17.1 | `operator new`'ün `malloc`'tan farkı yoktur, değiştirilebilir olması dışında | [new.delete.single]: başarısızlıkta `bad_alloc` gönderir ve önce new handler'ı çağırır; [c.malloc]: `malloc` başarısızlıkta boş gösterici döndürür | düzeltilmeli |
| 2 | 17.1 | `delete` ifadesi sonlandırıcıdan sonra `operator delete(void*)` çağırır | [expr.delete]/9.6: global işlevlerde boyutlu biçimin seçilip seçilmeyeceği belirtilmemiştir | eksik |
| 3 | 17.2 | Sınıf düzeyindeki işlevler örtülü olarak `static`'tir | [class.free]/1 | doğru |
| 4 | 17.2 | Yalnızca `operator new` yüklenirse, kurucu işlev hata gönderdiğinde bellek serbest bırakılamaz | [expr.new]/27–28: ad önce sınıf kapsamında, bulunamazsa global kapsamda aranır ve bulunan işlev çağrılır; yani global `operator delete` çağrılır. Örnekteki `malloc` belleği için bu, eşleşmeyen ayırma/bırakma demektir | düzeltilmeli (test 1) |
| 5 | 17.2 | Dizi biçimleri ayrı yüklenmelidir | [class.free] | doğru |
| 6 | 17.2 | C++14, boyut bilgisini alan (sınıf düzeyindeki) sonlandırma biçimini ekledi | C++11 [class.free]/5 ve örneği iki parametreli `operator delete(void*, std::size_t)` üyesini zaten tanımlar; C++14 (N3778) yalnızca **global** boyutlu biçimi ekledi | düzeltilmeli |
| 7 | 17.2 | Boyutlu biçim varsa tercih edilir | [expr.delete]/9.4: işlevler sınıf kapsamındaysa boyutsuz olan seçilir; boyutlu biçim yalnızca tek başınaysa kullanılır | düzeltilmeli (test 2) |
| 8 | 17.3 | `placement new` sonrası `delete` yazılamaz; sonlandırıcı elle çağrılır | [expr.delete]/2 (`delete`'in operandı bir *new ifadesinin* ayırdığı nesne olmalı) | doğru |
| 9 | 17.4 | `operator new` başarısızlıkta new handler'ı çağırır, döngü; handler üç şeyden birini yapmalı; `set_new_handler` öncekini döndürür | [new.delete.single], [new.handler], [set.new.handler] | doğru |
| 10 | 17.5 | Statik ilk değer verme derleme zamanında olur; değer çalıştırılabilir dosyaya yazılır | [basic.start.static]: sabit ilk değer verme, her dinamik ilk değer vermeden önce yapılır; "derleme zamanı" ve "dosyaya yazılır" gerçekleme anlatımıdır | gerçekleme |
| 11 | 17.5 | Dinamik ilk değer verme `main` çağrılmadan önce yapılır | [basic.start.dynamic]/5: `main`'in ilk deyiminden önce mi yapılacağı, yoksa ertelenebileceği **gerçeklemeye bağlıdır** | düzeltilmeli |
| 12 | 17.5 | Aynı çeviri birimindeki nesneler bildirim sırasıyla hayata gelir | [basic.start.dynamic]/1, /3: sıralı *(ordered)* değişkenler tanım sırasıyla; şablon statik veri elemanları sırasız *(unordered)*, `inline` değişkenler kısmen sıralıdır | eksik |
| 13 | 17.5 | Farklı çeviri birimlerindeki sıra belirtilmemiştir | [basic.start.dynamic]/3 | doğru |
| 14 | 17.5 | Yerel `static` nesnenin ilk değeri C++11'den beri iş parçacığı güvenlidir; "derleyici gerekli kilitlemeyi kendisi ekler" | [stmt.dcl]/3: eşzamanlı çağrı, ilk değer verme bitene kadar bekler. İlk yarı doğru; kilit anlatımı gerçeklemedir | gerçekleme |
| 15 | 17.5 | Sonlanma sırası hayata gelme sırasının tersidir | [basic.start.term]/3 | doğru |
| 16 | 17.7 | Ayırıcının asgari arayüzü `allocate`, `deallocate` ve `value_type`'tır | [allocator.requirements.general]: `a1 == a2` karşılaştırması ve başka bir türe yeniden bağlanmış ayırıcıdan dönüştüren kurucu (`X u(b)`) da zorunludur; `allocator_traits` bunları tamamlamaz | eksik |
| 17 | 17.7 | Durumsuz bir ayırıcı kabın boyutunu artırmaz | Standart bunu garanti etmez; boş taban sınıf optimizasyonu gerçeklemenin tercihidir | gerçekleme |
| 18 | 17.8 | Adres, türün hizalamasının katı olmalıdır | [basic.align]/1 | doğru |
| 19 | 17.8 | `alignof(int)` "genellikle 4", `alignof(double)` "genellikle 8" | [basic.align]: temel türlerin hizalaması gerçeklemeye bağlıdır | gerçekleme |
| 20 | 17.8 | Bir sınıfın hizalaması en büyük hizalamalı veri elemanınınkidir | Standart böyle bir eşitlik koymaz; sınıfın hizalaması en az elemanlarınınki kadar katıdır | eksik |
| 21 | 17.8 | `alignas` ile doğal hizalamadan küçük değer vermek sentaks hatasıdır | [dcl.align]/5 | doğru |
| 22 | 17.8 | `alignas(std::max_align_t)` her tür için uygun hizalamadır | [support.types.layout]: `max_align_t`'nin hizalaması her **skaler** türünkü kadar büyüktür; aşırı hizalı türleri kapsamaz | eksik |
| 23 | 17.8 | `std::hardware_destructive_interference_size` C++17 ile geldi | P0154R1, [hardware.interference] | doğru |

## Test 1 — iddia 4: yalnızca `operator new` yüklendiğinde global `operator delete` çağrılır

```cpp
#include <cstdio>
#include <cstdlib>
#include <new>

int global_delete_cagrisi = 0;

void operator delete(void* p) noexcept { ++global_delete_cagrisi; std::free(p); }
void operator delete(void* p, std::size_t) noexcept { ++global_delete_cagrisi; std::free(p); }

struct Myclass {
    static void* operator new(std::size_t n) { return std::malloc(n); }
    Myclass() { throw 1; }
};

int main()
{
    int once = global_delete_cagrisi;
    try { new Myclass; } catch (int) { }
    std::printf("%d\n", global_delete_cagrisi - once);    // 1: global operator delete çağrıldı
}
```

## Test 2 — iddia 7: sınıf kapsamında iki biçim varsa boyutsuz olan seçilir

```cpp
#include <cstdio>
#include <new>

struct Myclass {
    static void operator delete(void* p) noexcept
    {
        std::puts("boyutsuz");
        ::operator delete(p);
    }
    static void operator delete(void* p, std::size_t) noexcept
    {
        std::puts("boyutlu");
        ::operator delete(p);
    }
};

int main()
{
    delete new Myclass;     // boyutsuz
}
```
