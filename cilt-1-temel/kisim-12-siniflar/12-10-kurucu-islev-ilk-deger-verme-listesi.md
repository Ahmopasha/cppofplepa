---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.10 Kurucu işlev ilk değer verme listesi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
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

**Veri elemanları, sınıf tanımındaki bildirim sırasına göre hayata gelir.** Listedeki
yazım sırası hiçbir şeyi değiştirmez. İkisi farklıysa derleyici genellikle uyarır.

**Listede yer almayan ve gövdede de değer atanmayan veri elemanı, ilk değer almamış
kalır.** Yerleşik türlerde bu çöp değer demektir.

**Referans ve `const` veri elemanları yalnızca bu listede ilk değer alabilir.** Gövdede
atama yapmak mümkün değildir, çünkü gövdeye gelindiğinde onlar çoktan hayata gelmiştir.

C++11'den itibaren `()` yerine `{}` kullanılabilir ve tercih edilmelidir; daraltıcı
dönüşümleri engeller.
