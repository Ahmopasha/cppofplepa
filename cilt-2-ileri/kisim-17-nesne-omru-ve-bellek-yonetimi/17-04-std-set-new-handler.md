---
cilt: "II — İleri"
kisim: "17 — Nesne Ömrü ve Bellek Yönetimi"
baslik: "17.4 `std::set_new_handler`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 17.4 `std::set_new_handler`

`operator new` bellek ayıramadığında, hata göndermeden önce kurulu bir işlevi çağırır.
Bu işleve *new handler* denir.

```cpp
#include <new>

void bellek_yetmedi()
{
    std::cerr << "bellek yetersiz\n";
    std::abort();
}

int main()
{
    std::set_new_handler(bellek_yetmedi);
}
```

Mekanizma bir **döngüdür**: ayırma başarısız olursa handler çağrılır, sonra ayırma tekrar
denenir. Handler hiçbir şey yapmazsa döngü sonsuza gider.

Bu yüzden bir handler şu üçünden birini yapmak zorundadır: kullanılabilir bellek
sağlamak (önceden ayrılmış bir rezervi serbest bırakmak gibi), `std::bad_alloc`
göndermek, ya da programı sonlandırmak.

`std::set_new_handler`, önceki handler'ı döndürür; geçici olarak değiştirip geri koymak
bu sayede mümkündür.
