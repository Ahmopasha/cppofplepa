---
cilt: "II — İleri"
kisim: "2 — Taşıma Semantiği ve Bildirim Kuralları"
baslik: "2.5 Kaynağı devralınmış nesnenin durumu"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 2.5 Kaynağı devralınmış nesnenin durumu

Standart kütüphane türleri için verilen garanti: **geçerli ama değeri belirsiz.**

Bunun pratik karşılığı üç maddedir. Nesnenin sonlandırıcı işlevi güvenle çalışır.
Nesneye yeni bir değer atayabilirsiniz. Mevcut değerine dayanan hiçbir işlem
yapamazsınız.

```cpp
std::string s(10000, 'A');
auto t = std::move(s);

s.size();          // tanımlı ama değeri garanti edilmiyor
s = "yeni";        // geçerli
std::cout << s;    // artık okunabilir
```

Kendi sınıfınızı yazarken aynı garantiyi vermeniz beklenir. "Kaynağı bırak" adımını
atlamak yalnızca çift serbest bırakma sorunu değil, bu sözleşmenin de ihlalidir.

Üçüncü parti kütüphaneler bu garantiyi vermek zorunda değildir.
