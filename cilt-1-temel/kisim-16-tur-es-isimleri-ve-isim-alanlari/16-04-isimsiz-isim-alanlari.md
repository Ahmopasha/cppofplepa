---
cilt: "I — Temel"
kisim: "16 — Tür Eş İsimleri ve İsim Alanları"
baslik: "16.4 İsimsiz isim alanları"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 16.4 İsimsiz isim alanları

İsim verilmeden açılan isim alanına **isimsiz isim alanı** *(unnamed namespace)* denir.
İçindeki isimler yalnızca o çeviri biriminden kullanılabilir; başka bir çeviri birimindeki
aynı isimle çakışmaz.

```cpp
namespace {
    int yardimci_sayac;
    void yardimci_islev() { /* ... */ }
    struct Yardimci { /* ... */ };
}
```

C dilinde bu iş, değişken ve işlevlere uygulanan `static` anahtar sözcüğüyle yapılır;
`static` C++'ta da bu anlamda geçerlidir, ama isimsiz isim alanı önerilen yoldur.
Üstünlüğü, değişken ve işlevlerin yanı sıra **türleri** (sınıflar, numaralandırmalar) de
kapsayabilmesidir.

Kullanım amacı, bir kaynak dosyaya ait yardımcı öğelerin dışarıya sızmasını ve bağlayıcı
düzeyinde çakışmasını engellemektir.
