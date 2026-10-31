---
cilt: "I — Temel"
kisim: "23 — STL"
baslik: "23.4 Kaplar"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 23.4 Kaplar

Üç ana grup vardır.

### Sıralı kaplar

| Kap | Yapısı | Güçlü olduğu yer |
|---|---|---|
| `vector` | Dinamik dizi | Sona ekleme, indisle erişim |
| `deque` | Parçalı dinamik dizi | Başa ve sona ekleme |
| `list` | Çift yönlü bağlı liste | Ortadan ekleme/silme |
| `forward_list` | Tek yönlü bağlı liste | Bellek kısıtlı durumlar |
| `array` | Sabit boyutlu dizi | Boyutu derleme zamanında bilinen veriler |

> **Varsayılan tercihiniz `vector` olsun.** Bellekte bitişik durduğu için önbellek
> davranışı diğerlerinden çok daha iyidir. `list`'in "ortadan ekleme hızlıdır" avantajı,
> pratikte o konuma ulaşmak için gereken dolaşma yüzünden çoğu zaman kaybolur.

### Birleşik kaplar

Elemanları sıralı tutar; arama logaritmik zamandadır.

| Kap | Tutar |
|---|---|
| `set` | Benzersiz anahtarlar |
| `multiset` | Tekrarlı anahtarlar |
| `map` | Benzersiz anahtar–değer çiftleri |
| `multimap` | Tekrarlı anahtar–değer çiftleri |

```cpp
std::map<std::string, int> yas;
yas["ahmet"] = 30;
yas.insert({"mehmet", 25});

if (auto it = yas.find("ahmet"); it != yas.end())
    std::cout << it->second;
```

`map` üzerinde `[]` operatörü, anahtar yoksa **onu oluşturur.** Yalnızca okumak
istiyorsanız `find` veya `at` kullanın.

### Sırasız birleşik kaplar

Aynı dört kabın karma tablosuna dayanan sürümleridir: `unordered_set`, `unordered_map`,
`unordered_multiset`, `unordered_multimap`.

Arama ortalama sabit zamandadır ama elemanlar sıralı değildir. Sıraya ihtiyacınız yoksa
ve anahtarlarınız karma işlevi olan türlerdense bunları tercih edin.

### Kap uyumlandırıcıları

Mevcut kapların arayüzünü kısıtlayarak farklı bir soyutlama sunarlar: `stack`, `queue`,
`priority_queue`. Kendi başlarına kap değildirler; içeride bir kap kullanırlar.
