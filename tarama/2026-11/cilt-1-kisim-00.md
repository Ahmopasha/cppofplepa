# Tarama — Cilt I Kısım 0 (Kasım 2026)

Kısım 0'daki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Kaynaklar C++20
(N4861, timsong-cpp.github.io/cppwp/n4861) bölüm adlarıyla verilir; C++23'te de doğru
kalmalıdır. 0.0 normatif iddia içermiyor.

**İşlem (2026-11):** "eksik" ve "gerçekleme" sonuçlu bütün iddialar düzeltildi; metinler AI hakem
panelinden geçti (`~/ai-panel/calismalar/2026-11-01_c1-00-tarama`, iki tur, iki hakem: Gemini
kotası doluydu). Panel ayrıca şunları düzeltti: ODR cümlesi ("bu adım bildirebilir"); `std::vector<int>`
(`vector<bool>` bitişik değildir); "çoğunlukla" derleyici bildirir; `main`'in sonuna ulaşma;
"gerçekleme", araç terimleri ve "koşullu derleme" atfı.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 0.1 | C++ çok paradigmalı bir dildir; dil birini dayatmaz | Tanımlayıcı; standart bir paradigma iddiası taşımaz | doğru |
| 2 | 0.1 | Tasarımın "iki değişmezi" vardır ve "bütün kararları" bu ikisi açıklar | cppreference, *Zero-overhead principle*: tasarım ilkesidir, standart maddesi değildir; RTTI ve hata gönderme mekanizması bu ilkeye uymayan iki özellik olarak anılır | eksik |
| 3 | 0.1 | "Bir özellik, onu kullanmayan koda ek maliyet getirmez" | Aynı kaynak: hedeftir, güvence değildir | eksik |
| 4 | 0.1 | "Sanal işlev yazmadığınız sınıfın nesnesinde `vptr` bulunmaz" | `vptr` standartta yoktur. Sanal işlev yazılmasa da çok biçimli tabandan türemiş sınıf çok biçimlidir ([class.virtual]/1–2) | gerçekleme (test 1) |
| 5 | 0.1 | "`std::vector`, elle yönetilen bir dizi kadar hızlıdır" | [vector.overview]: bitişik depolama ve sabit zamanlı rastgele erişim karmaşıklığı; hız güvencesi yoktur | gerçekleme |
| 6 | 0.2 | C++ ISO tarafından standartlaştırılır; 2011'den beri üç yılda bir yenilenir | C++11, 14, 17, 20, 23 | doğru |
| 7 | 0.2 | Standart tablosu | C++11: `auto`, lambda, taşıma, akıllı göstericiler, `nullptr`, `enum class`; C++14: `decltype(auto)`, jenerik lambda; C++17: P0135R1, `optional`, `variant`, `string_view`, yapısal bağlama; C++20: kavramlar, ranges, eşyordamlar, modüller, `std::format` | doğru |
| 8 | 0.2 | Özelliğin geldiği standart, davranış değişikliği olan yerlerde Standart Notu ile belirtilir | `BAKIM.md`: kutu, eski yöntem yaygınsa ve C++23'e ilk girilen yerlerde de açılır | eksik |
| 9 | 0.3 | Program "üç aşamadan geçer" | [lex.phases]: dokuz çeviri aşaması; "Implementations must behave as if these separate phases occur, although in practice different phases might be folded together." | eksik |
| 10 | 0.3 | `#include` dosyanın içeriğini o satıra kopyalar | [cpp.include]: yönerge, başlığın tüm içeriğiyle değiştirilir | doğru |
| 11 | 0.3 | Önişlemci çıktısı "tek bir uzun metin dosyasıdır" | [lex.phases]/4: aşama ön işlem birimleri *(preprocessing tokens)* üzerinde çalışır; dosya üretmesi gerekmez | gerçekleme |
| 12 | 0.3 | Önişlemci çıktısına çeviri birimi denir | [lex.separate]/1: "A source file together with all the headers and source files included via the preprocessing directive #include", koşullu derlemeyle atlanan satırlar hariç | eksik |
| 13 | 0.3 | "ODR ihlallerinin çoğu bu aşamada yakalanır" | [basic.def.odr]/10: "no diagnostic required". Kaç tanesinin yakalandığı gerçeklemeye bağlıdır | gerçekleme |
| 14 | 0.3 | "Tanımlanmamış başvuru" bağlayıcı hatasıdır; bildirim var, tanım yok demektir | [lex.phases]/9 dış başvuruları çözer; mesaj metni gerçeklemeye aittir | gerçekleme |
| 15 | 0.4 | Başlığa bildirimler, sınıf tanımları, `inline` işlevler, şablonlar, `constexpr` işlevler; kaynağa diğerleri | [basic.def.odr]/10–13 ile uyumlu bir düzen önerisi | doğru |
| 16 | 0.4 | Kaynak dosyaya `static` veri elemanlarının tanımları konur | [class.static.data]: `inline` `static` veri elemanı sınıf içinde tanımlanabilir (bkz. Cilt I 12.14) | eksik |
| 17 | 0.4 | `#pragma once` "standart olmasa da bütün derleyicilerin desteklediği" yazımdır | [cpp.pragma]: etkisi gerçeklemeye bağlıdır, tanınmayan pragma yok sayılır. "Bütün derleyiciler" doğrulanamaz | gerçekleme |
| 18 | 0.5 | `main`'in dönüş türü `int` olmak zorundadır | [basic.start.main]/2: "it shall have a declared return type of type int" | doğru |
| 19 | 0.5 | `return` yazılmazsa "derleyici `return 0;` varsayar" | [basic.start.main]/5: "the effect is equivalent to a return with operand 0"; gerçekleme anlatımıyla yazılmış | gerçekleme (test 2) |
| 20 | 0.5 | `main` bu ayrıcalığa sahip tek işlevdir | [stmt.return]: `void` işlevler ve bazı eşyordamlar da `return`'süz biter; ayrıcalık değer döndüren sıradan işlevler arasında geçerlidir | eksik |

**Sayım:** 20 iddia — 6 doğru, 7 eksik, 7 gerçekleme.

## Test 1 — iddia 4: sanal işlev yazılmayan sınıf da çok biçimli olabilir

```cpp
#include <type_traits>

struct Taban { virtual void f(); };
struct Turemis : Taban { };                  // sanal işlev yazılmadı

static_assert(std::is_polymorphic_v<Turemis>);
```

## Test 2 — iddia 19: `main`'in sonuna ulaşmak `return 0` gibidir

```cpp
int main()
{
}
```
