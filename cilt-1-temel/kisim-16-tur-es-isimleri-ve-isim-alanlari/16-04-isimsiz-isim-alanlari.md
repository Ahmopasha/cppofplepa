---
cilt: "I — Temel"
kisim: "16 — Tür Eş İsimleri ve İsim Alanları"
baslik: "16.4 İsimsiz isim alanları"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 16.4 İsimsiz isim alanları

İsim verilmeden açılan isim alanındaki isimler, yalnızca o çeviri biriminden erişilebilir
hâle gelir.

```cpp
namespace {
    int yardimci_sayac;
    void yardimci_islev() { /* ... */ }
}
```

Bu, C dilinde `static` anahtar sözcüğüyle yapılan işin C++'taki doğru karşılığıdır.
`static`'ten üstünlüğü, değişkenlerin yanı sıra **türleri** de kapsayabilmesidir.

Kullanım amacı, bir kaynak dosyaya ait yardımcı öğelerin dışarıya sızmasını ve bağlayıcı
düzeyinde çakışmasını engellemektir.
