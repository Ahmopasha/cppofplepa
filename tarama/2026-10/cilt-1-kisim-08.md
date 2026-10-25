# Tarama — Cilt I Kısım 8 (Ekim 2026)

Kısım 8'deki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış). Cilt I'in ufku
C++20 olduğu için kaynaklar C++20 metninin (N4861, timsong-cpp.github.io/cppwp/n4861)
bölüm adları ve paragraf numaralarıyla verilir; eski kiplere de uygulanan kusur raporları
ayrıca belirtilir. Tasarım tavsiyeleri (8.5'teki `const T&`/`T&` seçimi, 8.7'deki seçim
kuralı) normatif olmadığı için tabloya alınmadı. Testler `araclar/kod_denetimi.py` ile
`-std=c++20` altında derlendi ve çalıştırıldı.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 8.1 | Referans yeni bir nesne oluşturmaz, mevcut nesneye bir ad daha verir | [dcl.init.ref]/5.3 ve 5.4.2: referans bir PR-Value'ya ya da türü uymayan bir ifadeye bağlanırken geçici nesne oluşturulur (kitabın kendi 8.3 ve 8.4 örnekleri) | eksik |
| 2 | 8.1, 8.7 | Referans bir nesne değil, bir isimdir | [basic.pre]/3: nesne ve referans ayrı varlık *(entity)* türleridir, yani referansın nesne olmadığı doğrudur. Ama referans bir isim de değildir: isim, bir varlığı belirten tanıtıcının kullanımıdır ([basic.pre]/4); işlev çağrısının sonucu ya da referans veri elemanı gibi kendi adı olmayan referanslar vardır. [dcl.ref]/4: referansın yer kaplayıp kaplamadığı belirtilmemiştir | eksik |
| 3 | 8.2, 8.7 | Referansa ilk değer vermek zorunludur | [dcl.ref]/5: `extern` belirteçli bildirim, sınıf tanımı içindeki veri elemanı bildirimi, parametre ve geri dönüş türü bildirimi ilk değer vermeden yazılabilir | eksik (test 1) |
| 4 | 8.2 | `int& r;` sentaks hatasıdır | [dcl.ref]/5 (blok kapsamındaki tanımda istisnalardan hiçbiri yok) | doğru |
| 5 | 8.2 | Referans bağlandıktan sonra başka nesneye bağlanamaz; atama bağlandığı nesneye yapılır | [dcl.init.ref]/2 ve notu | doğru |
| 6 | 8.2, 8.7 | "Geçersiz referans diye bir şey yoktur"; referans hiçbir şeye bağlanmamış olamaz; bu, iki kuralın sonucudur | [dcl.ref]/5: referansın geçerli bir nesneye ilk değer alması bir *şarttır*, iki kuralın sonucu değildir; boş referans yalnızca iyi tanımlı bir programda olamaz. Referans, bağlandığı nesnenin ömrü bittikten sonra da var olabilir (sarkan referans; kitabın kendi 8.3 ve 8.6 metinleri). Kullanılması tanımsız davranıştır: [expr.type]/1, CWG 2933 (Kasım 2024'te kusur raporu olarak kabul edildi, C++98'e kadar geriye uygulanır) | düzeltilmeli (test 2) |
| 7 | 8.3 | `const int& r = 100;` için geçici nesne oluşturulur ve referans ona bağlanır | [dcl.init.ref]/5.3.1: PR-Value'ya geçici nesne somutlaştırma dönüşümü uygulanır | doğru |
| 8 | 8.3 | Geçici nesnenin hayatı içinde bulunduğu ifadenin sonunda biter | [class.temporary]/4: geçici nesneyi (sözcüksel olarak) içeren **tam ifadenin** *(full-expression)* sonunda; alt ifadenin sonunda değil. /5 iki istisna daha sayar (dizi elemanlarının kurulmasındaki varsayılan argümanlar) | eksik |
| 9 | 8.3 | Geçici nesne bir **`const` referansa** bağlandığında ömrü referansın ömrü kadar uzar | [class.temporary]/6: her referans türü için geçerlidir (`T&&` dahil); ayrıca bağlanan glvalue'nun /6.1–6.8'de sayılan ifadelerden biriyle (somutlaştırma, parantez, `.` ile üye erişimi, dizi indisleme, belirli dönüşümler, üçlü ve virgül operatörü) elde edilmiş olması gerekir | eksik (test 3) |
| 10 | 8.3 | Bu uzatmanın iki istisnası vardır | [class.temporary]/6.9–6.12 dört istisna sayar: işlev çağrısında referans parametre, parantezli ifade listesiyle ilk değer alan kümenin *(aggregate)* referans elemanı, `return` deyimi, *new-initializer*. Ayrıca [class.base.init]/8: *mem-initializer*'da referans veri elemanını doğrudan bir geçici nesneye bağlamak sentaks hatasıdır | eksik (test 3) |
| 11 | 8.3 | Uzatma işlevden döndürülen referans için geçerli değildir | [class.temporary]/6.11 | doğru |
| 12 | 8.3 | Referans veri elemanı kurucu işlevin referans parametresinden ilk değer alıyorsa uzatma yoktur; geçici nesne kurucu çağrısını içeren tam ifadenin sonunda yok olur | [class.temporary]/6.9: geçici nesne parametreye bağlanır ve çağrıyı içeren tam ifadenin sonuna kadar yaşar; veri elemanı ise bir isim ifadesine (parametre) bağlandığı için /6'daki listeye girmez | doğru |
| 13 | 8.4 | Referansın türü ile bağlanacak nesnenin türü aynı olmak zorundadır | [dcl.init.ref]/4–5: türün *referansla uyumlu* *(reference-compatible)* olması yeter; `const`/`volatile` ekleme ve türemiş sınıftan taban sınıfa bağlama doğrudan bağlamadır | eksik (test 4) |
| 14 | 8.4 | `double& dr = ival;` sentaks hatası; `const double& cdr = ival;` geçerli ve bir `double` geçici nesnesi üretilir | [dcl.init.ref]/5.2 (örnekteki `double& rd3 = i; // error` satırı), /5.4.2 | doğru |
| 15 | 8.4 | `const int cx; int& r = cx;` sentaks hatasıdır | [dcl.init.ref]/5.1 uygulanmaz (`int`, `const int` ile referansla uyumlu değil), /5.2 | doğru |
| 16 | 8.6 | İşlev referans döndürdüğünde çağrı ifadesi L-Value olur | [expr.call]/14: yalnızca L-Value referans (ya da işleve R-Value referans) döndüren çağrı L-Value'dur; nesne türüne R-Value referans döndüren çağrı X-Value'dur. Okur `T&&`'yi Kısım 2.4'ten tanıyor | eksik (test 5) |
| 17 | 8.6 | Yerel nesneye referans döndürmek için "derleyici genellikle uyarı verir ama sentaks hatası değildir" | "Sentaks hatası değildir" C++20 için doğrudur ([stmt.return], [dcl.init.ref]); uyarı derleyici davranışıdır | gerçekleme |
| 18 | 8.6 | Sarkan referansı kullanmak tanımsız davranıştır | [expr.type]/1, CWG 2933 (bkz. iddia 6) | doğru |
| 19 | 8.6 | Parametre olarak gelen bir nesnenin elemanı ve sınıfın veri elemanı "işlev çağrısından daha uzun yaşar" koşulunu sağlar | Değerle alınan parametrenin ömrünün işlev dönerken mi, tam ifadenin sonunda mı bittiği gerçeklemeye bağlıdır ([expr.call]/7); referans parametreye bağlanan geçici argüman çağrıyı içeren tam ifadenin sonunda yok olur ([class.temporary]/6.9) ve dönen referans o noktadan sonra sarkar. Aynısı geçici bir nesnenin veri elemanı için de geçerlidir | eksik (test 6) |
| 20 | 8.7 | `T& &` ve `T&[N]` geçersizdir | [dcl.ref]/5: referansa referans, referans dizisi ve referansa gösterici olamaz | doğru |
| 21 | 8.8 | Diziye ve işleve referans; dizinin boyutu türün parçasıdır, referans bağlarken göstericiye dönüşüm olmaz | [dcl.init.ref]/1 örneği (`int (&ra)[3] = a;`, `int (&rg)(int) = g;`), /5.1 notu (dizi-gösterici dönüşümü uygulanmaz), [dcl.array] | doğru |
| 22 | 8.9 | Şablon bağlamında yazılan `T&&` "R-Value referansı değil", üçüncü bir referans türüdür | [temp.deduct.call]/3: *forwarding reference*, cv niteleyicisiz bir şablon parametresine **R-Value referanstır**; farkı yalnızca çıkarım kuralındadır (L-Value argümanda `T` L-Value referans olarak çıkarılır, çökme `T&`'ye götürür). [dcl.ref]/2: dilde iki referans türü vardır. "Şablon bağlamında" da geniştir: `T`'nin o çağrıdan çıkarılması gerekir (Cilt II 1.2.6) | düzeltilmeli (test 7) |

## Önerilen düzeltmeler

- **İddia 1:** "Yeni bir nesne oluşturmaz" cümlesi, var olan bir nesneye bağlanan referansla sınırlanmalı; geçici nesne durumu için 8.3'e gönderme yapılmalı.
- **İddia 2:** "Referans bir nesne değil, bir isimdir" yerine "referans bir nesne değildir; bağlandığı nesneyi belirtir" gibi bir ifade kullanılmalı (8.7 tablosundaki "hayır, isimdir" de buna göre).
- **İddia 3:** "Zorunludur" kuralına, `extern` bildirimi, veri elemanı (kurucuda ilk değer alır) ve parametre istisnaları dipnot ya da tek cümleyle eklenmeli.
- **İddia 6:** "Geçersiz referans diye bir şey yoktur" yerine "boş *(null)* referans diye bir şey yoktur" denmeli; referansın sarkabileceği (8.3, 8.6) ve bunun kuralların sonucu değil, programcıya düşen bir şart olduğu söylenmeli; "denetim satırından kurtulursunuz" cümlesi boş gösterici denetimiyle sınırlanmalı.
- **İddia 8:** "İfadenin sonunda" yerine "tam ifadenin sonunda" yazılmalı (terim gerekiyorsa sözlüğe eklenerek).
- **İddia 9:** Uzatmanın `const` olmayan R-Value referanslar için de geçerli olduğu ve referansın geçici nesneye doğrudan bağlanması gerektiği belirtilmeli.
- **İddia 10:** "İki önemli istisnası vardır" yerine "en sık karşılaşılan iki istisnası" denmeli ya da `new` ifadesi ve doğrudan *mem-initializer* bağlaması (sentaks hatası) da sayılmalı.
- **İddia 13:** "Aynı olmak zorundadır" yerine "türler uyumlu olmalıdır: aynı tür, daha çok `const`/`volatile` nitelenmiş tür ya da taban sınıf" denmeli.
- **İddia 16:** "Referans döndürdüğünde" yerine "L-Value referans döndürdüğünde" yazılmalı; `T&&` döndüren çağrının X-Value olduğu Cilt II 1.1.3'e gönderilebilir.
- **İddia 17:** "Derleyici genellikle uyarı verir" ifadesi çıkarılmalı; "sentaks hatası değildir" bırakılabilir.
- **İddia 19:** Listedeki "parametre olarak gelen bir nesnenin elemanı" ifadesi "referansla alınan ve çağıranda yaşamaya devam eden nesnenin elemanı" diye daraltılmalı; geçici argüman ve geçici nesnenin veri elemanı durumunda dönen referansın tam ifadeden sonra sarktığı belirtilmeli.
- **İddia 22:** "R-Value referansı değil" yerine "yazılışı da türü de R-Value referanstır, ama `T` çıkarılırken özel bir kural uygulandığı için L-Value'lara da bağlanabilir" denmeli; "şablon bağlamında" yerine "`T` çağrıdan çıkarıldığında" yazılmalı.

## Test 1 — iddia 3: ilk değer vermeden yazılabilen referans bildirimleri

```cpp
extern int& dis_ref;            // extern bildirimi: ilk değer yok, geçerli

struct Tutucu {
    int& m;                     // veri elemanı: ilk değerini kurucu verir
    explicit Tutucu(int& a) : m(a) { }
};

void degistir(int& p);          // parametre: ilk değerini çağrı verir

int deger = 1;
int& dis_ref = deger;           // tanım ayrı yerde

int main()
{
    Tutucu t{deger};
    t.m = 2;
    return dis_ref == 2 ? 0 : 1;
}
```

## Test 2 — iddia 6: referans, nesnesi yok olduktan sonra da var olabilir

```cpp
#include <cstdio>

int main()
{
    int* p = new int{10};
    int& r = *p;                // r geçerli bir nesneye bağlandı
    delete p;                   // nesne yok oldu; r sarkan referans olarak kaldı
    std::puts("r var ama kullanılmıyor");
}
```

## Test 3 — iddia 9 ve 10: `T&&` de ömrü uzatır; `new` ifadesi uzatmaz

```cpp
#include <cstdio>

struct Izci {
    ~Izci() { std::puts("~Izci"); }
};

struct Kume {
    const Izci& m;
};

int main()
{
    Izci&& r = Izci{};          // const olmayan R-Value referans: ömür uzar
    Kume* p = new Kume{Izci{}}; // new-initializer: geçici Izci bu satırın sonunda yok olur
    std::puts("main sonu");     // çıktı: "~Izci", "main sonu", "~Izci"
    delete p;
}
```

## Test 4 — iddia 13: tür aynı olmadan doğrudan bağlama

```cpp
struct Taban { };
struct Turemis : Taban { };

int main()
{
    Turemis d;
    Taban& rb = d;              // türemiş sınıftan taban sınıfa: doğrudan bağlama
    int i = 0;
    const volatile int& rcv = i;  // daha çok nitelenmiş tür: doğrudan bağlama
    return (&rb == &d && &rcv == &i) ? 0 : 1;   // geçici nesne yok, aynı nesneler
}
```

## Test 5 — iddia 16: `T&&` döndüren çağrı X-Value'dur

```cpp
#include <type_traits>
#include <utility>

int sayi = 0;
int&& tasi_sayi() { return std::move(sayi); }

static_assert(std::is_same_v<decltype((tasi_sayi())), int&&>);   // X-Value

int main()
{
    tasi_sayi() = 5;            // sentaks hatası — atamanın solunda L-Value gerekir
}
```

## Test 6 — iddia 19: geçici argümanın elemanına dönen referans tam ifadeden sonra sarkar

```cpp
#include <cstdio>

struct Kutu {
    int x = 1;
    ~Kutu() { std::puts("~Kutu"); }
};

const int& icerik(const Kutu& k) { return k.x; }

int main()
{
    const int& r = icerik(Kutu{});  // geçici Kutu bu tam ifadenin sonunda yok olur
    std::puts("r artık sarkıyor");  // "~Kutu" bundan önce yazılır; r kullanılmıyor
}
```

## Test 7 — iddia 22: çıkarım yapılmazsa `T&&` düz R-Value referanstır

```cpp
template<typename T>
void g(T&& x) { }

int main()
{
    int n = 0;
    g(n);                       // T = int&, parametre int& (çökme)
    g<int>(n);                  // sentaks hatası — T = int iken parametre int&&, L-Value bağlanmaz
}
```
