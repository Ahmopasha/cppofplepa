---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.5 Tanımsız davranış ve akrabaları"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 2.5 Tanımsız davranış ve akrabaları

Standart, bazı durumlarda derleyiciye ne yapması gerektiğini söylemez. Bunun üç ayrı
derecesi vardır ve karıştırılmamaları gerekir.

**Tanımsız davranış** *(undefined behaviour)*. Standart hiçbir şey garanti etmez. Program
çökebilir, yanlış sonuç verebilir, doğru çalışıyormuş gibi görünebilir. Derleyicinin sizi
uyarma zorunluluğu yoktur; dahası, tanımsız davranışın gerçekleşmeyeceğini varsayarak
optimizasyon yapma hakkı vardır.

```cpp
int a[5];
a[10] = 1;              // tanımsız davranış

char* p = "merhaba";
p[0] = 'M';             // tanımsız davranış: yazı sabiti değiştirilemez

int x;
std::cout << x;         // tanımsız davranış: x ilk değer almamış
```

**Belirtilmemiş davranış** *(unspecified behaviour)*. Derleyici birkaç geçerli seçenek
arasından birini seçer. Hangisini seçtiğini **belgelemek zorunda değildir** ve aynı
derleyici farklı yerlerde farklı seçim yapabilir.

```cpp
int f1();
int f2();

int x = f1() + 5 * f2();
```

`f1` mi önce çağrılır `f2` mi, garanti edilmez. İşlevlerin yan etkisi varsa sonuç
derleyiciye göre değişir. (Çarpmanın önceliği ayrı bir konudur; o garantilidir.)

**Gerçeklemeye bağlı davranış** *(implementation-defined)*. Derleyici yine seçim yapar,
ama seçimini **belgelemek zorundadır.**

```cpp
sizeof(int)     // 4 mü 8 mi: gerçeklemeye bağlı, ama belgelenmiş
```

Farkı tek tabloda:

| | Standart garanti veriyor mu | Derleyici belgelemek zorunda mı |
|---|---|---|
| Tanımsız | hayır, hiçbir şey | — |
| Belirtilmemiş | geçerli seçenekler kümesi var | hayır |
| Gerçeklemeye bağlı | geçerli seçenekler kümesi var | **evet** |

> **Tanımsız davranış içeren bir program "bazen çalışıyor" olamaz.** Test ortamında doğru
> sonuç vermesi, kodun doğru olduğunu göstermez. Bu, C++'ta hata ayıklamanın en zor
> tarafıdır ve tanımsız davranıştan kaçınmayı bir alışkanlık hâline getirmenin sebebidir.
