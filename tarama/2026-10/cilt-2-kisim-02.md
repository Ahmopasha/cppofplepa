# Tarama — Cilt II Kısım 2 (Ekim 2026)

Kısım 2'deki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar
C++23 metninin (N4950, timsong-cpp.github.io/cppwp/n4950) bölüm adlarıyla verilir;
çalışma taslağında da aynı bölümlerdir. Testler `araclar/kod_denetimi.py` ile derlendi ve
çalıştırıldı.

**İşlem (2026-10):** "düzeltilmeli", "eksik" ve "gerçekleme" sonuçlu bütün iddialar
düzeltildi; metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-10-30_c2-02-tarama`,
beş tur). "Derleyici uyarı vermez" cümleleri "kod geçerlidir; standart, gerçeklemenin bunu
bildirmesini istemez" kalıbıyla yazıldı. Panel ayrıca şunları ekletti: bildirilmemiş işlev
çağrısının sonucunu kalan yüklemelerin belirlediği ve X-Value/PR-Value ayrımı (2.1, 2.8);
kopyalanamayan üyeli sınıfta sonlandırıcının sentaks hatasına yol açması (2.2); `vector`
kuralının `reserve` ve tek öğeyi sona eklemeyle sınırlanması ([vector.modifiers]; 2.6);
`std::deque` taşıyan kurucusunun `noexcept` olmasının garanti edilmediği (2.6); 2.8
örneğine sonlandırıcı. Açık kalan: 2.7'nin giriş cümlesi ikinci senaryoyu (`return
std::move(x)`) da "kopyalayan işleve düşer" diye anlatıyor; o senaryoda taşıyan kurucu
seçilir, kaybedilen eliminasyondur. Kısım 3 panelinde düzeltildi.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 2.1 | Altı özel üye işlev vardır; her biri bildirilmemiş, örtülü bildirilmiş (defaulted/deleted) ya da kullanıcı bildirmiş (provided/defaulted/deleted) olabilir | [special]/1; [class.copy.ctor]/6, /8, /10; [dcl.fct.def.default]/5 | doğru |
| 2 | 2.1 | Bildirilmemiş bir işlevi "çağırmak sentaks hatası verir" | Aynı paragrafın sonunda söylendiği gibi başka bir yükleme seçilebilir: taşıyan kurucu bildirilmemişse R-Value argümanla kopyalayan kurucu seçilir, hata yoktur ([class.copy.ctor]/8, [over.match]). Hata yalnızca uygun başka yükleme yoksa çıkar | eksik |
| 3 | 2.1 | Silinmiş işlev yükleme çözümlemesine katılır ve seçilirse hata verir | [class.copy.ctor]/10, [class.copy.assign] (not): silinmiş olarak tanımlanan **defaulted** taşıyan kurucu ve taşıyan atama yükleme çözümlemesinde yok sayılır; kural yalnızca açıkça `= delete` edilmiş ya da başka nedenle silinmiş işlevler için geçerlidir | eksik (test 1) |
| 4 | 2.2 | Tablonun bütün satırları (varsayılan kurucunun her kurucu bildiriminde, taşıyan işlevlerin kopyalayan işlevlerden/sonlandırıcıdan/diğer taşıyan işlevden biri bildirildiğinde bildirilmemesi; kopyalayan işlevlerin taşıyan işlev bildirildiğinde silinmesi; sonlandırıcı ve diğer kopyalayan işlevin bildirilmesinde örtülü kopyalayan işlevin *deprecated* olması) | [class.default.ctor]/1; [class.copy.ctor]/6, /8; [class.copy.assign]/2, /4 | doğru |
| 5 | 2.2 | Sonlandırıcı yazmak taşımayı kaldırır, sınıf kopyalanmaya başlar; "derleyici uyarısı vermez" | Kural doğru ([class.copy.ctor]/8). Standart tanı istemez; uyarı verilip verilmemesi gerçeklemenin tercihidir (Annex D'deki *deprecated* örtülü kopyalama için uyarı veren gerçeklemeler vardır) | gerçekleme |
| 6 | 2.2 | Taşıyan işlev yazmak kopyalayanları siler; herhangi bir kurucu varsayılan kurucuyu kaldırır | [class.copy.ctor]/6, [class.copy.assign]/2, [class.default.ctor]/1 | doğru |
| 7 | 2.3 | Kopyalayan işlevleri bildirmek taşıyanları bildirilmemiş yapar; `std::mutex` ne kopyalanabilir ne taşınabilir | [class.copy.ctor]/8, [class.copy.assign]/4; [thread.mutex.class]: `mutex(const mutex&) = delete;` `mutex& operator=(const mutex&) = delete;` | doğru |
| 8 | 2.3 | Taşıyan işlevleri bildirmek kopyalayanları siler; `std::unique_ptr` ve `std::thread` taşınabilir ama kopyalanamaz | [class.copy.ctor]/6; [unique.ptr.single.general], [thread.thread.class] | doğru |
| 9 | 2.4 | `= default` ilk bildirimdeyse işlev user-provided değildir ve trivial olabilir; sınıf dışındaysa user-provided'dır ve trivial değildir | [dcl.fct.def.default]/5: "user-declared and not explicitly defaulted or deleted on its first declaration"; [class.default.ctor]/3, [class.copy.ctor]/11 | doğru |
| 10 | 2.4 | Örnekteki fark (varsayılan kurucu) `std::is_trivially_copyable` sorgusuna yansır | [class.prop]/1: trivially copyable olmak kopyalayan/taşıyan işlevlere ve sonlandırıcıya bağlıdır, varsayılan kurucuya bağlı değildir. Örnekteki `B` trivially copyable'dır; değişen `is_trivially_default_constructible` (ve [class.prop]/2'deki *trivial class*) sonucudur | düzeltilmeli (test 2) |
| 11 | 2.5 | Standart kütüphane türleri için garanti "geçerli ama değeri belirsiz" | [lib.types.movedfrom]/1: "Unless otherwise specified, such moved-from objects shall be placed in a valid but unspecified state." Bazı türler için durum belirtilmiştir: ör. [unique.ptr.single.ctor] taşıyan kurucuda `u.get() == nullptr` son koşulu | eksik |
| 12 | 2.5 | Taşınmış nesneyle "mevcut değerine dayanan hiçbir işlem yapamazsınız" | [defns.valid]: nesnenin değişmezleri korunur ve işlemler türü için belirtildiği gibi davranır; tanımın örneğinde `x.empty()` koşulsuz, `x.front()` yalnızca `x.empty()` `false` döndürdüyse çağrılabilir. Ön koşulu olmayan işlemler (`size()`, `empty()`, `clear()`) çağrılabilir ve sonuçlarına güvenilebilir; yalnızca ön koşulu değere bağlı işlemler (`front()`, `pop_back()`) önce denetim ister | eksik |
| 13 | 2.5 | `std::remove` sonrasında aralığın sonundaki elemanlar geçerli ama belirsiz durumdadır | [alg.remove] (not): "Each element in the range [ret, last) ... has a valid but unspecified state" | doğru |
| 14 | 2.6 | `vector` kapasiteyi artırırken güçlü garantiyi korur | [vector.capacity] `reserve`: "If an exception is thrown other than by the move constructor of a non-Cpp17CopyInsertable type, there are no effects."; [vector.modifiers] aynı koşul | eksik (bkz. 15) |
| 15 | 2.6 | `vector` taşıyan kurucuyu yalnızca `noexcept` ise kullanır, değilse kopyalar; örnekteki `Yazi` için "noexcept olmazsa vector bunu kullanmaz" | [vector.capacity], [vector.modifiers]: tür *Cpp17CopyInsertable* değilse hata gönderebilen taşıyan kurucu da kullanılır ve hata hâlinde etkiler belirtilmemiştir. Örnekteki `Yazi` yalnızca taşıyan kurucu bildirdiği için kopyalayan kurucusu silinmiştir ([class.copy.ctor]/6); `vector` bu sınıfta `noexcept` olmayan taşıyan kurucuyu da kullanır | düzeltilmeli (test 3) |
| 16 | 2.6 | `noexcept` yazmazsanız taşıma "kullandırılmaz", "kazanç tamamen kaybolur"; taşıyan işlev zaten kaynak ayırmaz | Kayıp yalnızca güçlü garanti isteyen yerlerdedir (`vector`'ün yer değiştirmesi vb.); `return`, atama ve `std::swap` taşıyan işlevi `noexcept`'ten bağımsız kullanır. Örtülü bildirilen ya da ilk bildirimde `= default` yapılan işlevin özel durum belirtimi örtülüdür ([except.spec]/7, /9): üyelerinkiler `noexcept` ise kendisi de öyledir. "Kaynak ayırmaz" genellemesi standart kütüphanede de tutmaz: [deque.overview]'de `deque(deque&&);` `noexcept` değildir | eksik (test 4) |
| 17 | 2.7 | `const T` dönüş değeri `T&&` parametresine bağlanamaz; atamada kopyalayan atama seçilir | [dcl.init.ref]/5 (cv niteleyicisi düşürülemez), [over.ics.ref] | doğru |
| 18 | 2.7 | İki senaryoda da "derleyici uyarı vermez" | Standart tanı istemez; uyarı gerçeklemeye bağlıdır (`return std::move(x)` için varsayılan olarak uyarı veren gerçeklemeler vardır) | gerçekleme |
| 19 | 2.7 | `return std::move(mx)` eliminasyonu engeller, taşıyan kurucu çağrılır | [class.copy.elision]/1.1: eliminasyon için `return` işleneni otomatik ömürlü, `volatile` olmayan bir nesnenin **adı** olmalıdır | doğru |
| 20 | 2.8 | Copy-and-swap güçlü garanti sağlar; kendine atama denetimi gerekmez | `swap` `noexcept` olduğunda kopya çağrı noktasında yapılır; `*this`'e dokunulmadan önce biter ([expr.call]: parametrelerin ilk değer verilmesi işlev gövdesinden önce yapılır) | doğru |
| 21 | 2.8 | Tek işlev hem kopyalayan hem taşıyan atama görevi görür; "R-Value ise taşınarak gelir" | [class.copy.assign]/1: `operator=(Yazi)` bir **kopyalayan atama işlevidir**; kullanıcı bildirdiği için taşıyan kurucu örtülü bildirilmez ([class.copy.ctor]/8). Örnekteki `Yazi`'ye X-Value (`std::move(b)`) verildiğinde parametre kopyalanarak oluşur; taşınması için taşıyan kurucu ayrıca yazılmalıdır | eksik (test 5) |

**Normatif olmayan not.** 2.7'deki *pessimistic move* adı yaygın kullanımda *pessimizing
move*'dur; terim sözlüğüyle karşılaştırılmalı.

## Önerilen düzeltmeler

- **2 (2.1):** "Çağırmak sentaks hatası verir" yerine "çağrı ancak başka uygun bir yükleme yoksa hata verir" denmeli; taşıyan işlevler bildirilmemişse R-Value'nun kopyalayan işleve gittiği burada da söylenmeli.
- **3 (2.1):** Silinmiş işlevin çözümlemeye katıldığı söylendikten sonra, silinmiş olarak tanımlanan *defaulted* taşıyan kurucu ve atamanın yük çözümlemesinde yok sayıldığı istisnası eklenmeli.
- **5, 18 (2.2, 2.7):** "Derleyici uyarı vermez" cümleleri "standart tanı istemez" biçiminde yazılmalı ya da çıkarılmalı.
- **10 (2.4):** Örnek varsayılan kurucu olduğu için sorgu `std::is_trivially_default_constructible` olmalı; `is_trivially_copyable`'ın ancak kopyalayan/taşıyan işlev ya da sonlandırıcı sınıf dışında `= default` yapıldığında etkilendiği belirtilmeli.
- **11 (2.5):** "Aksi belirtilmedikçe" kaydı eklenmeli ve `unique_ptr`'ın taşındıktan sonra boş olmasının garanti edildiği örnek verilmeli.
- **12 (2.5):** "Mevcut değerine dayanan hiçbir işlem" yerine "ön koşulu nesnenin değerine bağlı işlemler (`front()`, `pop_back()`) önce denetim ister; ön koşulsuz işlemler (`size()`, `clear()`) serbesttir" denmeli.
- **14–15 (2.6):** Kural "tür kopyalanabiliyorsa `vector` yalnızca `noexcept` taşıyan kurucuyu kullanır; kopyalanamıyorsa hata gönderebilen taşıyan kurucuyu da kullanır ve o durumda güçlü garanti yoktur" diye yazılmalı; örnekteki `Yazi`'ye kopyalayan kurucu eklenmeli ya da yorum değiştirilmeli.
- **16 (2.6):** Kaybın yalnızca güçlü garanti isteyen işlemlerde olduğu, örtülü/ilk bildirimde `= default` taşıyan işlevlerin `noexcept`'liğinin otomatik çıkarıldığı söylenmeli; "kaynak ayırmaz" genellemesi yumuşatılmalı.
- **21 (2.8):** `operator=(Yazi)`'nin kopyalayan atama işlevi sayıldığı ve taşıyan kurucuyu baskıladığı belirtilmeli; deyimin R-Value'yu taşıyabilmesi için örneğe taşıyan (ve kopyalayan) kurucu eklenmeli.

## Test 1 — iddia 3: silinmiş olarak tanımlanan defaulted taşıyan kurucu yok sayılır

```cpp
#include <cstdio>
#include <utility>

struct Uye {
    Uye() = default;
    Uye(const Uye&) { std::puts("kopya"); }
    Uye(Uye&&) = delete;
};

struct Sinif {
    Uye u;
    Sinif() = default;
    Sinif(const Sinif&) = default;
    Sinif(Sinif&&) = default;       // Uye(Uye&&) silinmiş: bu kurucu silinmiş olarak tanımlanır
};

int main()
{
    Sinif a;
    Sinif b = std::move(a);         // silinmiş taşıyan kurucu yok sayılır, kopyalayan seçilir: "kopya"
}
```

## Test 2 — iddia 10: sınıf dışında `= default` edilen varsayılan kurucu trivially copyable'ı etkilemez

```cpp
#include <type_traits>

class A { public: A() = default; };

class B { public: B(); };
B::B() = default;

static_assert(std::is_trivially_default_constructible_v<A>);
static_assert(!std::is_trivially_default_constructible_v<B>);
static_assert(std::is_trivially_copyable_v<A>);
static_assert(std::is_trivially_copyable_v<B>);    // fark bu sorguya yansımaz

int main() { }
```

## Test 3 — iddia 15: kopyalanamayan türde `vector`, `noexcept` olmayan taşıyan kurucuyu kullanır

```cpp
#include <cstdio>
#include <type_traits>
#include <vector>

int tasima = 0;

class Yazi {
public:
    Yazi() = default;
    Yazi(Yazi&&) { ++tasima; }      // noexcept değil
};

static_assert(!std::is_copy_constructible_v<Yazi>);

int main()
{
    std::vector<Yazi> v;
    v.emplace_back();
    int once = tasima;
    for (int i = 0; i < 100; ++i)
        v.emplace_back();           // yer değiştirmeler taşıyan kurucuyla yapılır
    std::printf("%d\n", tasima > once);    // 1
}
```

## Test 4 — iddia 16: örtülü ve ilk bildirimde `= default` taşıyan kurucu kendiliğinden `noexcept`'tir

```cpp
#include <string>
#include <type_traits>

struct Ortulu {
    std::string s;
};

struct Varsayilan {
    std::string s;
    Varsayilan(Varsayilan&&) = default;      // noexcept yazılmadı
};

static_assert(std::is_nothrow_move_constructible_v<Ortulu>);
static_assert(std::is_nothrow_move_constructible_v<Varsayilan>);

int main() { }
```

## Test 5 — iddia 21: `operator=(T)` kopyalayan atamadır; taşıyan kurucu olmadan R-Value kopyalanır

```cpp
#include <cstdio>
#include <type_traits>
#include <utility>

struct Parca {
    Parca() = default;
    Parca(const Parca&) { std::puts("kopya"); }
    Parca(Parca&&) noexcept { std::puts("tasima"); }
    Parca& operator=(const Parca&) = default;
};

class Yazi {
    Parca p;
public:
    Yazi() = default;
    void swap(Yazi& other) noexcept { std::swap(p, other.p); }
    Yazi& operator=(Yazi other) noexcept { swap(other); return *this; }    // kopyalayan atama
};

static_assert(std::is_copy_assignable_v<Yazi>);

int main()
{
    Yazi a, b;
    a = std::move(b);       // ilk satır "kopya": Yazi'nin taşıyan kurucusu bildirilmemiş
}
```
