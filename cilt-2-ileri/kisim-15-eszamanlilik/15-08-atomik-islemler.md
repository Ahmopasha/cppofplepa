---
cilt: "II — İleri"
kisim: "15 — Eşzamanlılık"
baslik: "15.8 Atomik işlemler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
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

`is_lock_free()` üye işlevi, işlemin gerçekten donanım desteğiyle mi yoksa arka planda
bir kilitle mi yapıldığını bildirir. Büyük türlerde kilit kullanılabilir; o durumda
atomik kullanmanın kazancı kalmaz.

`std::atomic_flag`, **her zaman kilitsiz olma garantisi veren** tek türdür. Yalnızca
`test_and_set` ve `clear` işlemlerini sunar; ilkel bir kilit kurmaya yeter.

### Bellek sıralaması

Her atomik işlem, bir `std::memory_order` değeri alabilir. Varsayılan
`memory_order_seq_cst`, yani 15.1'deki sıralı tutarlılıktır.

| Sıralama | Ne garantiler |
|---|---|
| `seq_cst` | Küresel tek sıra; en güçlü, en pahalı |
| `acquire` / `release` | Bir çift arasında sıralama; yaygın ve yeterli |
| `relaxed` | Yalnızca atomiklik; sıralama garantisi yok |

> **Varsayılanı değiştirmeyin.** Gevşetilmiş sıralamalar yalnızca ölçümle kanıtlanmış bir
> darboğaz varsa ve modelin tamamı anlaşılmışsa kullanılır. Yanlış kullanımı, test
> ortamında hiç ortaya çıkmayan hatalar üretir.

Sayaç artırma gibi bağımsız işlemlerde `relaxed` güvenlidir; bayrak ve kilit kurulumunda
`acquire`/`release` gerekir.
