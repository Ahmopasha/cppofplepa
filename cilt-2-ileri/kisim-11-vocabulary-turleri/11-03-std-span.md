---
cilt: "II — İleri"
kisim: "11 — Vocabulary Türleri"
baslik: "11.3 `std::span`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 11.3 `std::span`

`string_view`'ün karakter dizilerine yaptığını, herhangi bir **bitişik diziye** yapar.
C++20 ile geldi.

```cpp
#include <span>

void topla(std::span<const int> veri);

std::vector<int> v{1, 2, 3};
int a[]{1, 2, 3};
std::array<int, 3> arr{1, 2, 3};

topla(v);       // hepsi çalışır
topla(a);
topla(arr);
```

Çözdüğü problem, C'den miras kalan `(gösterici, uzunluk)` ikilisidir. O ikili, ikisinin
tutarlılığını programcıya bırakır; `span` ikisini tek nesnede birleştirir ve dizi
boyutunu otomatik çıkarır.

İki biçimi vardır. **Dinamik uzunluklu** `std::span<T>` uzunluğu çalışma zamanında tutar.
**Sabit uzunluklu** `std::span<T, N>` uzunluğu tür bilgisine gömer ve sıfır çalışma
zamanı maliyeti getirir.

`string_view`'deki ömür uyarısı burada da aynen geçerlidir.
