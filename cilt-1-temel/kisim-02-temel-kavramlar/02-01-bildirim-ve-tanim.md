---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.1 Bildirim ve tanım"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 2.1 Bildirim ve tanım

**Bildirim** *(declaration)* derleyiciye bir ismi tanıtır: böyle bir varlık var, türü şu.
**Tanım** *(definition)* ise varlığın kendisini oluşturur.

Her tanım aynı zamanda bir bildirimdir; tersi doğru değildir.

```cpp
extern int x;        // bildirim: "x adında bir int var, tanımı başka yerde"
int x;               // tanım: değişken burada oluşturuluyor
int y = 10;          // tanım

void foo(int);       // bildirim
void foo(int a)      // tanım
{
    // ...
}

class Myclass;            // bildirim
class Myclass { int a; }; // tanım
```

Ayrımın pratik karşılığı şudur: bir ismi **kullanabilmek** için bildirimini görmek
yeterlidir, tanımını görmeniz gerekmez. Bu yüzden başlık dosyalarında bildirimler,
kaynak dosyalarda tanımlar bulunur.
