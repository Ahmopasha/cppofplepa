---
cilt: "II — İleri"
kisim: "17 — Nesne Ömrü ve Bellek Yönetimi"
baslik: "17.8 Hizalama"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 17.8 Hizalama

Her türün, nesnelerinin bellekte hangi adreslerde durabileceğini belirleyen bir
**hizalama** *(alignment)* değeri vardır. Adres, bu değerin katı olmak zorundadır.

`alignof` operatörü bir türün hizalamasını verir:

```cpp
alignof(char);        // 1
alignof(int);         // genellikle 4
alignof(double);      // genellikle 8
```

Bir sınıfın hizalaması, en büyük hizalamalı veri elemanının hizalamasıdır. Derleyici,
elemanlar arasına gerektiğinde **dolgu** *(padding)* ekler; bu yüzden `sizeof`, elemanların
boyutları toplamından büyük olabilir.

`alignas` niteleyicisi, hizalamayı artırmak için kullanılır:

```cpp
alignas(16) int dizi[4];              // 16 baytlık sınıra hizalı
alignas(std::max_align_t) char t[64]; // her tür için uygun hizalama
```

Yalnızca **artırabilirsiniz**; türün doğal hizalamasından küçük bir değer vermek sentaks
hatasıdır.

İki kullanım alanı vardır.

**Ham tampon üzerinde nesne oluşturmak.** 17.3'teki `placement new` örneğinde tampon
`alignas(Myclass)` ile nitelenmişti; onsuz, nesne için uygun olmayan bir adrese
yerleştirme yapılabilir ve sonuç tanımsız davranıştır.

```cpp
alignas(Myclass) unsigned char tampon[sizeof(Myclass)];
Myclass* p = new (tampon) Myclass{10};
```

**Yanlış paylaşımdan kaçınmak.** Eşzamanlı kodda, farklı iş parçacıklarının sık yazdığı
iki değişken aynı önbellek satırına düşerse, mantıksal olarak bağımsız oldukları hâlde
birbirlerini yavaşlatırlar. Buna *false sharing* denir.

```cpp
struct Sayaclar {
    alignas(std::hardware_destructive_interference_size) std::atomic<int> a;
    alignas(std::hardware_destructive_interference_size) std::atomic<int> b;
};
```

`std::hardware_destructive_interference_size`, C++17 ile eklenen ve önbellek satırı
boyutunu bildiren sabittir.
