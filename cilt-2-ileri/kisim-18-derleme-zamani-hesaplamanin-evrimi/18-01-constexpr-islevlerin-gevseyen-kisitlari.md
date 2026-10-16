---
cilt: "II — İleri"
kisim: "18 — Derleme Zamanı Hesaplamanın Evrimi"
baslik: "18.1 `constexpr` işlevlerin gevşeyen kısıtları"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 18.1 `constexpr` işlevlerin gevşeyen kısıtları

Cilt I Kısım 6.6'da `constexpr` işlevlerin derleme zamanında yürütülen koduna sınır
konduğu söylenmiş, bu sınırların standarttan standarda gevşediği buraya bırakılmıştı.

**C++11.** Gövde tek bir `return` deyiminden ibaret olmak zorundaydı. Döngü, yerel
değişken, `if` deyimi yazılamazdı. Koşullu hesaplama yalnızca üçlü operatörle,
tekrarlama yalnızca özyinelemeyle yapılabiliyordu.

```cpp
constexpr int faktoriyel(int n)          // C++11'de tek yol
{
    return n <= 1 ? 1 : n * faktoriyel(n - 1);
}
```

**C++14.** Yerel değişkenler, döngüler, `if` ve `switch` deyimleri, birden fazla `return`
serbest bırakıldı. `constexpr` işlevler sıradan işlevler gibi yazılabilir hâle geldi.

```cpp
constexpr int faktoriyel(int n)          // C++14
{
    int sonuc = 1;
    for (int i = 2; i <= n; ++i)
        sonuc *= i;
    return sonuc;
}
```

**C++17.** `if constexpr` gövdede kullanılabilir hâle geldi (bkz. Kısım 5.4) ve lambda
ifadeleri örtülü olarak `constexpr` oldu.

**C++20.** En büyük adım burada atıldı. `try`/`catch` blokları, sanal işlev çağrıları,
`union` üyesi değiştirme, `constexpr` sonlandırıcı işlevler ve — en önemlisi —
**geçici dinamik bellek ayırma** serbest bırakıldı.

Geçici olması şu demektir: derleme zamanında ayrılan bellek, yine derleme zamanında
serbest bırakılmak zorundadır. Bu sayede `std::vector` ve `std::string` derleme zamanında
kullanılabilir hâle geldi.

**C++23.** Gövdeye yazılabilecekler yeniden genişledi. `static` ve `thread_local`
değişkenler, türü **literal tür** *(literal type)* olmayan yerel değişkenler ve `goto`
artık gövdede yer alabilir; **derleme zamanında yürütülen yolda bu satırlara
gelinmemelidir**; gelinirse o çağrı sabit ifade olmaz. Sabit ifadelerde kullanılabilen
`static` ve `thread_local` değişkenler (ör. `static constexpr`) ise bu kuralın dışındadır;
derleme zamanında da kullanılabilir:

```cpp
constexpr char onaltilik(int n)          // C++23
{
    static constexpr char basamak[] = "0123456789abcdef";
    return basamak[n];
}

static_assert(onaltilik(11) == 'b');   // derleme zamanında
```

Ayrıca hiçbir argümanla derleme zamanında çalıştırılamayan bir `constexpr` işlev
(ör. gövdesinde koşulsuz olarak `constexpr` olmayan bir işlevi çağıran) C++23 öncesinde
derleyicinin bildirmek zorunda olmadığı bir hata *(ill-formed, no diagnostic required)*
idi; artık geçerlidir. Sabit ifade gerektiren bir yerde çağrılırsa sentaks hatası olur.
Parametre ve dönüş türlerinin literal tür olma zorunluluğu da kalktı.

Değişmeyen tek kural şudur: **`constexpr` işlev, derleme zamanında çalışmak zorunda
değildir.** Argümanları sabit ifade değilse çalışma zamanında çalışır. Anahtar sözcük
bir garanti değil, bir imkân bildirir.
