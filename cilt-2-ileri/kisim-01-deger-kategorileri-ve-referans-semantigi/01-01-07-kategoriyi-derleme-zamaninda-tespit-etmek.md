---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.1.7 Kategoriyi derleme zamanında tespit etmek"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

### 1.1.7 Kategoriyi derleme zamanında tespit etmek

`decltype((e))` kategoriye özgü bir tür ürettiğine göre, kısmi özelleştirmeyle bunu
yakalayabiliriz:

```cpp
#include <iostream>

template<typename T>
constexpr const char* p = "PR-Value";

template<typename T>
constexpr const char* p<T&> = "L-Value";

template<typename T>
constexpr const char* p<T&&> = "X-Value";

#define print_val_category(e) \
    std::cout << "Value category of '" << #e << "' is " << p<decltype((e))> << '\n'
```

`#e` önişlemcinin *stringizing* operatörüdür, argümanı olduğu gibi yazıya çevirir.
`decltype((e))` içindeki iç parantez zorunludur: onsuz operand isim sayılır ve
kategori değil bildirilen tür elde edilir.

Aynı işi `if constexpr` ile de yapabiliriz:

```cpp
#include <type_traits>
#include <iostream>

template<typename T>
void func()
{
    if constexpr (std::is_rvalue_reference_v<T>)      std::cout << "X-Value\n";
    else if constexpr (std::is_lvalue_reference_v<T>) std::cout << "L-Value\n";
    else if constexpr (!std::is_reference_v<T>)       std::cout << "PR-Value\n";
}

#define EXP(e) decltype((e))

int main()
{
    func<EXP(12)>();   // PR-Value
    int x = 43;
    func<EXP(x)>();    // L-Value
}
```
