---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.10 Kurucu işlev ilk değer verme listesi"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 12.10 Kurucu işlev ilk değer verme listesi

Veri elemanlarına ilk değer vermenin doğru yolu, kurucu işlevin gövdesi değil **ilk değer
verme listesidir.**

```cpp
class Myclass {
    int x;
    std::string s;
public:
    Myclass(int a, const std::string& b) : x{a}, s{b} { }
};
```

Üç kural:

**Veri elemanları, sınıf tanımındaki bildirim sırasına göre ilk değer alır.** Listedeki
yazım sırası bu sırayı değiştirmez.

**Listede yer almayan bir veri elemanı, sınıf içi ilk değeri (Kısım 12.11) varsa onunla, yoksa default-initialization ile (Kısım 3.2) ilk değer alır.**
Yerleşik türlerde default-initialization değer vermez; örneğin otomatik ömürlü bir nesnede
eleman belirsiz (çöp) değer tutabilir; gövdede yapılan atama ilk değer verme sayılmaz.

**Referans veri elemanları gövdede bağlanamaz, `const` veri elemanlarına gövdede değer atanamaz;**
referanslar ve kendiliğinden değer almayan türden (örneğin yerleşik türden) `const`
elemanlar ilk değerlerini bu listeden ya da sınıf içi ilk değerden almak zorundadır.
Gövdeye gelindiğinde onlar çoktan ilk değer almıştır.

C++11'den itibaren `()` yerine `{}` kullanılabilir ve tercih edilmelidir; daraltıcı
dönüşümleri engeller (Kısım 3.7); istisnaları: Kısım 3.9.
