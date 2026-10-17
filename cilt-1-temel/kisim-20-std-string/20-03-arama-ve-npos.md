---
cilt: "I — Temel"
kisim: "20 — `std::string`"
baslik: "20.3 Arama ve `npos`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 20.3 Arama ve `npos`

`find` ailesi, aranan şeyin indisini döndürür. Bulamazsa `std::string::npos` döndürür.

```cpp
auto i = s.find("abc");

if (i != std::string::npos) {
    // bulundu
}
```

`npos`, `std::string::size_type` türünden temsil edilebilen en büyük değerdir.
**İşaretsiz bir türdür**; `-1` ile karşılaştırmayın, `int` değişkene atamayın.

<!-- kod: atla -->
```cpp
int i = s.find("abc");     // yanlış — npos int'e sığmaz
auto i = s.find("abc");    // doğru
```

Diğer arama işlevleri: `rfind`, `find_first_of`, `find_last_of`, `find_first_not_of`,
`find_last_not_of`.
