---
cilt: "II — İleri"
kisim: "11 — Vocabulary Türleri"
baslik: "11.7 `std::byte`"
kaynak: "derleyen (ders notlarında yok)"
son_kontrol: "2026-09 (C++23)"
---

## 11.7 `std::byte`

Ham belleği temsil etmeye yarayan türdür. C++17 ile `<cstddef>` başlığına eklendi.

Çözdüğü problem bir adlandırma karışıklığıdır. C++'ta ham bellek geleneksel olarak
`char` veya `unsigned char` ile temsil edilir, ama o türlerin **üç ayrı işi** vardır:
metin taşımak, küçük tamsayı tutmak, ham bayt göstermek. Bildirime bakarak hangisinin
kastedildiği anlaşılmaz.

```cpp
void islem(unsigned char* veri, std::size_t n);   // metin mi, sayı mı, bayt mı?
void islem(std::byte* veri, std::size_t n);       // ham bellek
```

### Bir sınıf değil, bir `enum class`

Tanımı şudur:

```cpp
enum class byte : unsigned char {};
```

Kapsamlandırılmış bir `enum` olduğu için (bkz. Cilt I Kısım 5.3) tamsayı türlerine
örtülü olarak dönüşmez. Doğrudan sonucu, **aritmetik işlemlere kapalı olmasıdır:**

```cpp
std::byte b{42};

b + 1;          // sentaks hatası
b * 2;          // sentaks hatası
std::cout << b; // sentaks hatası — akım operatörü tanımlı değil
```

Yalnızca bit işlemleri tanımlıdır: `&`, `|`, `^`, `~`, `<<`, `>>` ve bunların bileşik
atama biçimleri.

```cpp
std::byte a{0b1100}, c{0b1010};

a & c;          // 0b1000
a | c;          // 0b1110
a << 2;         // 0b110000
```

Bu kısıtlama kasıtlıdır. Ham bellek üzerinde aritmetik yapmak neredeyse her zaman bir
hatadır; tür, o hatayı derleme zamanında yakalar.

### İlk değer verme ve dönüştürme

Küme parantezi kullanılır; kapsamlandırılmış `enum` türlerine tamsayı sabitinden doğrudan
ilk değer verme C++17 ile mümkün oldu.

```cpp
std::byte b{42};        // geçerli
std::byte c = 42;       // sentaks hatası
```

Sayıya çevirmek için `std::to_integer` kullanılır:

```cpp
int n = std::to_integer<int>(b);
std::cout << std::to_integer<int>(b);     // yazdırmak için de bu gerekir
```

Ters yön `static_cast` iledir:

```cpp
auto b2 = static_cast<std::byte>(n);
```

Her iki dönüşümün de **açıkça yazılması gerekir.** Ham bellekle sayı arasında gidip
gelmek, koda bakan kişinin görmesi gereken bir karardır.

### Örtüşme kuralının istisnası

`char`, `unsigned char` ve `std::byte`, katı örtüşme kuralının *(strict aliasing)*
istisnasıdır: bu türlerden bir gösterici, **herhangi bir nesnenin** baytlarına bakmak
için kullanılabilir.

```cpp
Myclass nesne;
auto* p = reinterpret_cast<std::byte*>(&nesne);     // tanımlı
```

Diğer türlerle aynı şeyi yapmak tanımsız davranıştır. Serileştirme, bellek kopyalama ve
donanım erişimi gibi işlerde bu istisna kullanılır.

### Ne zaman kullanmalı

Bir bayt dizisi üzerinde çalışıyor ve içeriğinin **metin de sayı da olmadığını** ifade
etmek istiyorsanız `std::byte` kullanın: tampon yönetimi, ağ paketleri, dosya biçimleri,
kriptografi.

Metin işliyorsanız `char`, küçük sayı tutuyorsanız `unsigned char` veya `std::uint8_t`
doğru tercihtir. Türün kazancı, üç işi birbirinden ayırmasıdır; hepsine `std::byte`
demek kazancı ortadan kaldırır.
