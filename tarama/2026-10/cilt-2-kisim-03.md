# Tarama — Cilt II Kısım 3 (Ekim 2026)

Kısım 3'teki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar
C++23 metninin (N4950, timsong-cpp.github.io/cppwp/n4950) bölüm adlarıyla verilir;
çalışma taslağında da aynı bölümlerdir. Testler `araclar/kod_denetimi.py` ile derlendi ve
çalıştırıldı.

**İşlem (2026-10):** "düzeltilmeli", "eksik" ve "gerçekleme" sonuçlu bütün iddialar
düzeltildi; metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-10-30_c2-03-tarama`,
dört tur). Panel ayrıca şunları düzeltti: 3.3'ün ilk paragrafı 1.1.5'e uyduruldu (iddia 5);
`throw` için kopyalayan kurucu şartı ([except.throw]/5; test 3 değişti); 3.4'te kurucu
seçimi (`const` yerel nesne, Kısım 2.1'deki yok sayılan taşıyan kurucu) ve C++23 / C++20 /
C++11–17 örtülü taşıma kuralı (C++17'de ek koşul: N4659 [class.copy.elision]/3); C++17
öncesi yıkım sırası; "uygun" *(eligible)* tanımı; 3.6'daki öğüdün kopyalayan/taşıyan kurucu
çağrılarıyla sınırlanması. Kısım 2.7'nin giriş cümlesi de bu panelde düzeltildi.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 3.1 | Eliminasyon dört bağlamda görülür: nesne hayata getirilirken, `return`, `throw`, `catch` | [class.copy.elision]/1: izinli eliminasyon `return` (1.1), `throw` (1.2), **eşyordam parametresinin kopyası** (1.3) ve yakalayıcının *exception-declaration*'ı (1.4) için tanımlanır; ayrıca sabit ifade gerektiren bağlamda ve sabit ilk değer vermede eliminasyon yapılamaz. "Nesne hayata getirilirken" maddesi C++17'den beri eliminasyon değil, PR-Value'nun doğrudan hedefi oluşturmasıdır ([dcl.init.general]/16.6.1) | eksik |
| 2 | 3.1 | Hayata gelmiş iki nesne arasındaki atamada eliminasyon yoktur | [class.copy.elision]/1 yalnızca kopyalayan/taşıyan **kurma** işlemini eler; `b = foo()`'da PR-Value atama işlevinin referans parametresine bağlanmak için somutlaşır ([class.temporary]/2) | doğru |
| 3 | 3.2 | Zorunlu olmayan eliminasyonda kopyalayan/taşıyan kurucu çağrılabilir olmalıdır; zorunluda gerekmez | [stmt.return]/2: dönüş nesnesi işlenenden *copy-initialization* ile kurulur, kurucu seçimi eliminasyondan bağımsız yapılır; [dcl.init.general]/16.6.1: aynı sınıftan PR-Value hedefi doğrudan kurar | doğru |
| 4 | 3.2 | Zorunlu olmayan eliminasyon "derleyici optimizasyonu"dur, "öncesinden beri" vardır | [class.copy.elision]/1: "an implementation is allowed to omit"; zorunlu biçim C++17'de P0135R1 ile geldi | doğru |
| 5 | 3.3 | C++17 ile PR-Value nesne değil, nesneyi ilk değerle donatma reçetesidir; somutlaşma olmazsa nesne yoktur | [basic.lval]/1.2, [class.temporary]/2. **Sonradan düzeltildi:** "somutlaşma olmazsa nesne yoktur" kısmı yanlış; PR-Value aynı türden hedefi doğrudan kurar ve o nesne vardır (Cilt II 1.1.5 paneli, Ekim 2026) | eksik |
| 6 | 3.3 | Zorunlu eliminasyon "iki yerde görülür" (`return Myclass{...}` ve değer parametresine geçici nesne) | [dcl.init.general]/16.6.1 genel kuraldır: aynı sınıftan her PR-Value hedefini doğrudan kurar. `Myclass m = foo();` (3.7 tablosunda da var), `Myclass m = Myclass{};`, `throw Myclass{};` ([except.throw]/3), `new Myclass(Myclass{})` aynı kuraldandır. `throw`'da kopyalayan kurucu yine silinmemiş ve erişilebilir olmalıdır ([except.throw]/5) | eksik (test 3) |
| 7 | 3.3 | `return Myclass{31};` için kopyalayan/taşıyan kurucu silinmiş olsa da kod derlenir | [stmt.return]/2 (not 2), [dcl.init.general]/16.6.1 | doğru |
| 8 | 3.3 | Geri dönüşte ve değer parametresine geçişte "yalnızca bir nesne oluşur" | [class.temporary]/3: türün bütün uygun kopyalayan/taşıyan kurucuları trivial, sonlandırıcısı trivial ya da silinmişse gerçekleme parametre ya da dönüş nesnesi için ek bir geçici nesne oluşturabilir (yazmaçla aktarım için). Kural yalnızca bu türlerde gevşer | eksik |
| 9 | 3.4 | NRVO zorunlu değildir | [class.copy.elision]/1.1 ("is allowed to omit") | doğru |
| 10 | 3.4 | NRVO "derleyiciye ve optimizasyon seviyesine bağlıdır" | Standart yalnızca eliminasyona izin verir; yapılıp yapılmayacağını belirtmez. Derleyici ve optimizasyon seviyesi gerçekleme anlatımıdır | gerçekleme |
| 11 | 3.4 | Kopyalayan veya taşıyan kurucu çağrılabilir olmalıdır; "ikisi de `delete` edilmişse" kod derlenmez; sıra "NRVO yoksa taşınır, taşıma yoksa kopyalanır" | [expr.prim.id.unqual]/3–4: `return` işlenenindeki yerel nesne adı *move-eligible*'dır ve ifade bir X-Value'dur; kurucu bu X-Value için yükleme çözümlemesiyle seçilir. Taşıyan kurucu **açıkça silinmişse** o seçilir ve kod, kopyalayan kurucu erişilebilir olsa da geçersizdir. "Taşıma yoksa kopyalanır" ancak taşıyan kurucu bildirilmemişse (ya da silinmiş olarak tanımlanan defaulted ise) doğrudur | eksik (test 1) |
| 12 | 3.4 | `return mx;`, `return std::move(mx);` ile aynı taşımayı zaten yapar | [expr.prim.id.unqual]/4.1, [class.copy.elision]/3 | doğru |
| 13 | 3.5 | `return std::move(mx);` işlenen ad olmadığı için NRVO'yu engeller, taşıyan kurucu çağrılır | [class.copy.elision]/1.1 | doğru |
| 14 | 3.5, 3.7 | `const T` geri dönüş türü eliminasyonu engeller; 3.7: "`const Myclass foo();` — eliminasyon yok, kopyalama" | [dcl.init.general]/16.6.1 ve [class.copy.elision]/1.1 cv niteleyicisini yok sayar ("the cv-unqualified version of the source type", "ignoring cv-qualification"): `Myclass m = foo();` zorunlu eliminasyondur, `foo` içindeki `return mx;` NRVO'ya uygundur. `const` yalnızca dönüş değerinin `T&&`'ye bağlanmasını (taşıyan atama/kurucu) engeller | düzeltilmeli (test 2) |
| 15 | 3.5 | Koşullu dönüşte NRVO uygulanamaz, çünkü "derleyici hangi nesnenin ... oluşturulacağını derleme zamanında bilemez" | Sonuç doğru, gerekçe değil: [class.copy.elision]/1.1'e göre `b ? a : c` bir ad değildir. Aynı ifade örtülü taşımaya da uygun değildir ([expr.prim.id.unqual]/4), L-Value olduğu için **kopyalanır**. `if (b) return a; return c;` yazımında her iki dönüş için NRVO standartça izinlidir | eksik (test 4) |
| 16 | 3.5 | Değerle alınan parametre için NRVO yoktur, örtülü taşıma vardır; gerekçe: "parametre yerel bir nesne olmadığı için" | Sonuç doğru: [class.copy.elision]/1.1 parametreleri açıkça dışlar, [expr.prim.id.unqual]/4.1 parametreyi *move-eligible* sayar. Parametre de otomatik ömürlüdür; dışlanma bir istisna kuralıdır | eksik |
| 17 | 3.5 | Veri elemanı döndürülürken ne NRVO ne örtülü taşıma uygulanır | [expr.prim.id.unqual]/4: *implicitly movable entity* otomatik ömürlü bir değişkendir; veri elemanı değildir | doğru |
| 18 | 3.6 | Eliminasyonda kurucunun gövdesindeki yan etkiler de gerçekleşmez | [class.copy.elision]/1: kurucu ya da sonlandırıcının yan etkisi olsa bile eleme izinlidir | doğru |
| 19 | 3.6 | Kopya sayısı "derleyiciye ve optimizasyon seviyesine göre değişir"; NRVO bağlamında artıp artmayacağı belirsizdir; zorunlu bağlamda artmaz | İkinci ve üçüncü kısım doğrudur ([class.copy.elision]/1, [dcl.init.general]/16.6.1). Birinci kısım gerçekleme anlatımıdır: standart, izinli eliminasyonun yapılıp yapılmadığını belirtmez | gerçekleme |
| 20 | 3.7 | Tablonun diğer satırları (`return Myclass{...}`, `func(Myclass{})`, `Myclass m = foo()` zorunlu; `return mx` NRVO; `return b ? a : c` ve `return std::move(mx)` eliminasyonsuz; atamada söz konusu değil) | Yukarıdaki kaynaklar; satır 14 hariç | doğru |

## Önerilen düzeltmeler

- **1 (3.1):** Bağlam listesine eşyordam parametresinin kopyası eklenmeli; "nesne hayata getirilirken" maddesinin C++17'den beri eliminasyon değil PR-Value kuralı olduğu söylenmeli; sabit ifade bağlamında izinli eliminasyonun yapılamadığı belirtilmeli.
- **6 (3.3):** "İki yerde görülür" yerine "aynı sınıftan bir PR-Value bir nesneye ilk değer verdiğinde görülür; en sık iki yeri şunlardır" denmeli.
- **8 (3.3):** Trivial kopyalanan türlerde gerçeklemenin ek geçici nesne oluşturabileceği ([class.temporary]/3) bir cümleyle eklenmeli.
- **10, 19 (3.4, 3.6):** "Derleyiciye ve optimizasyon seviyesine bağlıdır" yerine "standart yapılıp yapılmayacağını belirtmez" denmeli.
- **11 (3.4):** "İkisi de silinmişse" yerine "işlenen X-Value sayılarak seçilen kurucu çağrılabilir olmalıdır; taşıyan kurucu açıkça silinmişse kopyalayan kurucu olsa da kod derlenmez" denmeli.
- **14 (3.5, 3.7):** `const T` dönüş türü eliminasyonu engelleyenler listesinden çıkarılmalı ("taşımayı engelleyen" olarak anılmalı); 3.7 tablosundaki satır "`m = foo();` (atama) — taşıma yerine kopyalayan atama" biçiminde yeniden yazılmalı.
- **15 (3.5):** Gerekçe "işlenen bir ad değildir" olarak değiştirilmeli; koşullu ifadenin taşınmadığı, kopyalandığı eklenmeli; `if`/`return` yazımında NRVO'nun izinli olduğu not edilmeli.
- **16 (3.5):** "Yerel bir nesne olmadığı için" yerine "standart parametreleri NRVO'dan açıkça dışladığı için" denmeli.

## Test 1 — iddia 11: taşıyan kurucu açıkça silinmişse `return mx;` derlenmez

```cpp
struct Myclass {
    Myclass() = default;
    Myclass(const Myclass&) = default;
    Myclass(Myclass&&) = delete;
};

Myclass bar()
{
    Myclass mx;
    return mx;      // sentaks hatası: X-Value için silinmiş taşıyan kurucu seçilir
}
```

## Test 2 — iddia 14: `const T` dönüş türü zorunlu eliminasyonu ve NRVO iznini engellemez

```cpp
#include <type_traits>

struct Myclass {
    Myclass() = default;
    Myclass(const Myclass&) = delete;
    Myclass(Myclass&&) = delete;
};

const Myclass foo() { return Myclass{}; }

int main()
{
    Myclass m = foo();      // kopyalayan/taşıyan kurucu silinmiş: zorunlu eliminasyon
    static_assert(std::is_same_v<decltype(foo()), const Myclass>);
    (void)m;
}
```

## Test 3 — iddia 6: `throw` işleneni PR-Value ise hata nesnesi doğrudan kurulur

İlk sürümdeki test, kopyalayan ve taşıyan kurucusu silinmiş bir sınıfla `throw Myclass{};`
yazıp derlendiğini gösteriyordu. [except.throw]/5'e göre kopyalayan kurucu eleme yapılsa
bile silinmemiş ve erişilebilir olmalıdır; o program geçersizdir ve derleyicinin onu kabul
etmesi standart hükmü değildir. Test buna göre değiştirildi.

```cpp
#include <cstdio>

struct Myclass {
    Myclass() = default;
    Myclass(const Myclass&) { std::puts("kopya"); }    // silinmemiş ve erişilebilir olmalı
    Myclass(Myclass&&) = delete;                        // PR-Value'da seçilmez
};

int main()
{
    try {
        throw Myclass{};    // hata nesnesi doğrudan kurulur: "kopya" yazılmaz
    }
    catch (const Myclass&) {
        std::puts("yakalandi");
    }
}
```

## Test 4 — iddia 15: koşullu ifade döndürülürken nesne taşınmaz, kopyalanır

```cpp
#include <cstdio>

struct Myclass {
    Myclass() = default;
    Myclass(const Myclass&) { std::puts("kopya"); }
    Myclass(Myclass&&) noexcept { std::puts("tasima"); }
};

Myclass baz(bool b)
{
    Myclass a, c;
    return b ? a : c;       // L-Value koşullu ifade: örtülü taşıma yok, "kopya"
}

int main()
{
    baz(true);
}
```
