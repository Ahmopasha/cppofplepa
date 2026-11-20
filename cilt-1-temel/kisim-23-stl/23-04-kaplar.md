---
cilt: "I — Temel"
kisim: "23 — STL"
baslik: "23.4 Kaplar"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 23.4 Kaplar

Üç ana grup vardır: **sıralı kaplar** *(sequence containers)*, **birleşik kaplar**
*(associative containers)* ve **sırasız birleşik kaplar**
*(unordered associative containers)*. Sıralı kaplarda elemanlar konuldukları düzende
durur; birleşik kaplar elemanları anahtarlarına göre dizer, sırasız birleşik kaplar
dizmez.

### Sıralı kaplar

| Kap | Yapısı | Güçlü olduğu yer |
|---|---|---|
| `std::vector` | Dinamik dizi | Sona ekleme, indisle erişim |
| `std::deque` | Parçalı dinamik dizi | Başa ve sona ekleme |
| `std::list` | Çift yönlü bağlı liste | Ortadan ekleme/silme |
| `std::forward_list` | Tek yönlü bağlı liste | Bellek kısıtlı durumlar |
| `std::array` | Sabit boyutlu dizi | Boyutu derleme zamanında bilinen veriler |

> **Varsayılan tercihiniz `std::vector` olsun.** Bellekte bitişik durduğu için önbellek
> davranışı diğerlerinden çok daha iyidir. `std::list`'in "ortadan ekleme hızlıdır"
> avantajı, pratikte o konuma ulaşmak için gereken dolaşma yüzünden çoğu zaman kaybolur.

### Birleşik kaplar

Elemanları anahtarlarına göre, varsayılan olarak küçükten büyüğe dizili tutar; arama
logaritmik zamandadır.

| Kap | Tutar |
|---|---|
| `std::set` | Benzersiz anahtarlar |
| `std::multiset` | Tekrarlı anahtarlar |
| `std::map` | Benzersiz anahtar–değer çiftleri |
| `std::multimap` | Tekrarlı anahtar–değer çiftleri |

```cpp
std::map<std::string, int> yas;
yas["ahmet"] = 30;
yas.insert({"mehmet", 25});

if (auto it = yas.find("ahmet"); it != yas.end())
    std::cout << it->second;
```

`std::map` üzerinde `[]` operatörü, anahtar yoksa **onu oluşturur.** Yalnızca okumak
istiyorsanız `find` veya `at` kullanın.

### Sırasız birleşik kaplar

Aynı dört kabın **karma tablosuna** *(hash table)* dayanan sürümleridir:
`std::unordered_set`, `std::unordered_map`, `std::unordered_multiset`,
`std::unordered_multimap`. Bir elemanın yeri, anahtara uygulanan **karma işlevinin**
*(hash function)* sonucuna göre belirlenir.

Arama ortalama sabit zamandadır ama elemanlar sıralı değildir. Sıraya ihtiyacınız yoksa ve
anahtarlarınız karma işlevi olan türlerdense bunları tercih edin.

### Kap uyumlandırıcıları

**Kap uyumlandırıcıları** *(container adaptors)*, mevcut kapların arayüzünü kısıtlayarak
farklı bir soyutlama sunar: `std::stack`, `std::queue`, `std::priority_queue`. Kendi
başlarına kap değildirler; içeride bir kap kullanırlar.
