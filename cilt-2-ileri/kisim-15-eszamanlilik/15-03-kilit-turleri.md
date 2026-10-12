---
cilt: "II — İleri"
kisim: "15 — Eşzamanlılık"
baslik: "15.3 Kilit türleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 15.3 Kilit türleri

Standart kütüphane dört `mutex` türü sunar:

| Tür | Ne zaman |
|---|---|
| `std::mutex` | Varsayılan |
| `std::recursive_mutex` | Aynı iş parçacığı aynı kilidi birden fazla alabilmeli |
| `std::timed_mutex` | Kilit için zaman aşımı gerekiyor |
| `std::shared_mutex` | Çok okuyan, az yazan (C++17) |

`std::shared_mutex`, okuyucuların **aynı anda** girmesine izin verir; yazıcı geldiğinde
tek başına kilitlenir.

```cpp
std::shared_mutex m;

void oku()  { std::shared_lock kilit{m};       /* birden fazla okuyucu */ }
void yaz()  { std::unique_lock kilit{m};       /* tek yazıcı */ }
```

Kilit sarmalayıcıları da dörde ayrılır:

| Sarmalayıcı | Özelliği |
|---|---|
| `std::lock_guard` | En basit; taşınamaz, ertelenemez |
| `std::unique_lock` | Taşınabilir, ertelenebilir, `condition_variable` ile çalışır |
| `std::scoped_lock` | **Birden fazla** kilidi kilitlenme riski olmadan alır (C++17) |
| `std::shared_lock` | `shared_mutex` ile paylaşımlı erişim (C++14) |

İki kilidi ayrı ayrı almak **ölümcül kilitlenmeye** *(deadlock)* yol açabilir: iki iş
parçacığı ikisini ters sırada alırsa ikisi de bekler. `std::scoped_lock` bunu, kilitleri
belirli bir algoritmayla alarak önler.

```cpp
std::scoped_lock kilit{m1, m2};     // sıra fark etmez, kilitlenme olmaz
```

> **C++17'den itibaren `std::lock_guard` yerine `std::scoped_lock` kullanın.** Tek kilitle
> de çalışır ve çok kilitli duruma geçtiğinizde kodu değiştirmenize gerek kalmaz.
