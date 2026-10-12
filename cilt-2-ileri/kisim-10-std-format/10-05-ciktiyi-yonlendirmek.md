---
cilt: "II — İleri"
kisim: "10 — `std::format`"
baslik: "10.5 Çıktıyı yönlendirmek"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 10.5 Çıktıyı yönlendirmek

`std::format` her çağrıda yeni bir `std::string` oluşturur. Bunu istemediğiniz durumlar
için üç yardımcı vardır.

**`std::format_to`**, sonucu bir çıktı iteratörüne yazar (bkz. Kısım 4.12):

```cpp
std::string s;
std::format_to(std::back_inserter(s), "{} {}", 1, 2);
```

**`std::format_to_n`**, en fazla `n` karakter yazar; tampon taşmasını önler.

**`std::formatted_size`**, sonucun kaç karakter olacağını hesaplar; tamponu önceden
doğru boyutta ayırmak için kullanılır.
