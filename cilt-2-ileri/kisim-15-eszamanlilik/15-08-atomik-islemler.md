---
cilt: "II — İleri"
kisim: "15 — Eşzamanlılık"
baslik: "15.8 Atomik işlemler"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 15.8 Atomik işlemler

Cilt I Kısım 27.2'de anlatılan data race'ten kaçınmanın kilitsiz yoludur. Atomik bir
işlem bölünemez; yarım görülemez.

```cpp
#include <atomic>

std::atomic<int> sayac{0};

void artir() { ++sayac; }        // kilit gerekmez
```

`std::atomic<T>` bir sınıf şablonudur. Temel işlemleri: `load`, `store`, `exchange`,
`compare_exchange_weak` ve `compare_exchange_strong`.

`is_lock_free()` üye işlevi, nesnenin atomik işlemlerinin **kilitsiz** *(lock-free)* olup
olmadığını bildirir. `is_always_lock_free` (C++17) ise türün işlemlerinin her zaman
kilitsiz olup olmadığını derleme zamanında bildirir; değeri `true` ise `is_lock_free()` de
`true` döner. Kilitsiz olmayan işlemler bloklayabilir. İşlemleri kilitsiz olmayan bir
atomik tür de data race'i önler; standart performans hakkında bir şey söylemez.

C++20'ye kadar **her zaman kilitsiz olma garantisi veren** tek tür `std::atomic_flag`'ti.
C++20'den beri **barındırılan** *(hosted)* gerçeklemelerde `std::atomic_signed_lock_free`
ve `std::atomic_unsigned_lock_free` tür eş adları da her zaman kilitsizdir.
`atomic_flag`'in işlemleri `test_and_set` ve `clear`'dı; C++20 `test`, `wait`,
`notify_one` ve `notify_all`'ı ekledi. İlkel bir kilit kurmaya yeter.

### Bellek sıralaması

Atomik işlemlerin üye işlev biçimleri bir `std::memory_order` değeri alabilir; işleç
biçimleri (`=`, `++`, `T`'ye dönüşüm) her zaman varsayılanı kullanır. Varsayılan
`std::memory_order::seq_cst`'dir (Kısım 15.1).

| Sıralama | Ne garantiler |
|---|---|
| `seq_cst` | Bütün `seq_cst` işlemleri için tek bir toplam sıra; en güçlü |
| `acquire` / `release` / `acq_rel` | `release` işlemiyle, onun yazdığı değeri okuyan `acquire` işlemi arasında sıralama; `acq_rel` okuyup yazan işlemlerde ikisini birden yapar; yaygın ve yeterli |
| `relaxed` | Yalnızca atomiklik; başka verilere sıralama getirmez, ama aynı atomik nesne üzerindeki değişikliklerin tek bir sırası yine vardır |

Altıncı değer `consume`'dur; standart bir notta onun yerine `acquire` kullanılmasını
önerir.

> **Varsayılanı değiştirmeyin.** Gevşetilmiş sıralamalar yalnızca ölçümle kanıtlanmış bir
> darboğaz varsa ve modelin tamamı anlaşılmışsa kullanılır. Yanlış kullanımı, test
> ortamında hiç ortaya çıkmayan hatalar üretir.

Sayaç artırma gibi bağımsız işlemlerde `relaxed` güvenlidir; bayrak ve kilit kurulumunda
`acquire`/`release` gerekir.
