---
cilt: "I — Temel"
kisim: "18 — Exception Handling"
baslik: "18.6 Asıl cevap: RAII"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 18.6 Asıl cevap: RAII

Yukarıdaki sorunun çözümü, her `new`'in yanına `try`/`catch` yazmak değildir. Çözüm,
kaynağı bir nesnenin sonlandırıcı işlevine bağlamaktır.

**RAII** *(Resource Acquisition Is Initialization)*: kaynak, bir nesnenin kurucu
işlevinde edinilir ve sonlandırıcı işlevinde bırakılır. Nesnenin ömrü bittiğinde — normal
yoldan da, yığın geri sarılarak da — kaynak serbest kalır.

```cpp
void f()
{
    auto p = std::make_unique<Myclass>();
    g();                        // hata gelse de p'nin belleği serbest kalır
}
```

Bu, Kısım 13.9'daki Rule of Zero ile aynı fikrin başka bir yüzüdür. `std::string`,
`std::vector` ve akıllı göstericiler zaten RAII uygular; siz de kaynak yönetirken aynısını
yapmalısınız.

> **C++'ta hata yönetiminin temeli `try`/`catch` değil, RAII'dir.** `try`/`catch`,
> hataya *müdahale edeceğiniz* yerde kullanılır; kaynak temizliği için değil.
