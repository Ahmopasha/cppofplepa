---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.5 Tanımsız davranış ve akrabaları"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 2.5 Tanımsız davranış ve akrabaları

Standart, bazı durumlarda gerçeklemeye ne yapması gerektiğini söylemez. Bunun üç ayrı
derecesi vardır ve karıştırılmamaları gerekir.

**Tanımsız davranış** *(undefined behavior)*. Standart hiçbir şey garanti etmez. Program
çökebilir, yanlış sonuç verebilir, doğru çalışıyormuş gibi görünebilir. Standart,
gerçeklemenin sizi uyarmasını istemez; dahası gerçekleme, tanımsız davranışın
gerçekleşmeyeceğini varsayarak optimizasyon yapabilir.

```cpp
int a[5];
a[10] = 1;              // tanımsız davranış

int i = INT_MAX;
++i;                    // tanımsız davranış: işaretli tamsayı taşması

int x;
std::cout << x;         // tanımsız davranış: x ilk değer almamış
```

**Belirtilmemiş davranış** *(unspecified behavior)*. Gerçekleme birkaç geçerli seçenek
arasından birini seçer. Hangisini seçtiğini **belgelemek zorunda değildir** ve aynı
programın farklı yerlerinde farklı seçim yapabilir.

```cpp
int f1();
int f2();

int x = f1() + 5 * f2();
```

`f1` mi önce çağrılır `f2` mi, garanti edilmez. İşlevlerin yan etkisi varsa sonuç, aynı
gerçeklemede bile, değişebilir. (Çarpmanın önceliği ayrı bir konudur; o garantilidir.)

**Gerçeklemeye bağlı davranış** *(implementation-defined behavior)*. Gerçekleme yine seçim
yapar, ama seçimini **belgelemek zorundadır.**

```cpp
sizeof(int)     // kaç bayt olduğu gerçeklemeye bağlı, ama belgelenmiş
```cpp
sizeof(int)     // 4 mü 8 mi: gerçeklemeye bağlı, ama belgelenmiş
```

Farkı tek tabloda:

| | Standart garanti veriyor mu | Gerçekleme belgelemek zorunda mı |
|---|---|---|
| Tanımsız | hayır, hiçbir şey | — |
| Belirtilmemiş | geçerli seçenekler kümesi var | hayır |
| Gerçeklemeye bağlı | geçerli seçenekler kümesi var | **evet** |

> **Tanımsız davranış içeren bir program "bazen çalışıyor" olamaz.** Test ortamında doğru
> sonuç vermesi, kodun doğru olduğunu göstermez. Bu, C++'ta hata ayıklamanın en zor
> tarafıdır ve tanımsız davranıştan kaçınmayı bir alışkanlık hâline getirmenin sebebidir.
