---
cilt: "II — İleri"
kisim: "14 — Deyimler ve Kalıplar"
baslik: "14.5 Kaynak ve ömür deyimleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 14.5 Kaynak ve ömür deyimleri

### Scope Guard

Kapsam bittiğinde çalışacak bir temizlik işi kaydeder. RAII'nin genelleştirilmiş hâlidir;
her kaynak için ayrı bir sınıf yazmak yerine tek bir sınıf kullanılır.

```cpp
template<typename F>
class ScopeGuard {
    F temizle;
    bool aktif{true};
public:
    explicit ScopeGuard(F f) : temizle{std::move(f)} { }
    ~ScopeGuard() { if (aktif) temizle(); }
    void iptal() noexcept { aktif = false; }

    ScopeGuard(const ScopeGuard&) = delete;
    ScopeGuard& operator=(const ScopeGuard&) = delete;
};
```

```cpp
FILE* f = std::fopen("veri.txt", "r");
ScopeGuard kapat{[&] { std::fclose(f); }};
```

`iptal()` işlevi, işlem başarılı olduğunda geri almayı durdurmaya yarar; işlem
tabanlı kodda kullanılır.

### Nifty Counter

Farklı çeviri birimlerindeki statik ömürlü nesnelerin hayata gelme sırası belirtilmemiştir
(bkz. Cilt I Kısım 12.14). Bir global nesnenin, ona bağımlı başka bir çeviri biriminden
önce hayata gelmesini garantilemek için kullanılır.

Başlık dosyasına bir sayaç nesnesi konur; her çeviri birimi kendi kopyasını oluşturur.
Sayaç sıfırdan bire çıktığında asıl nesne `placement new` ile oluşturulur, birden sıfıra
düştüğünde sonlandırıcı işlevi elle çağrılır.

`std::cout` ve diğer akım nesneleri bu mekanizmayla kurulmuştur; `<iostream>` başlığını
dahil eden her çeviri birimi bir sayaç taşır.
