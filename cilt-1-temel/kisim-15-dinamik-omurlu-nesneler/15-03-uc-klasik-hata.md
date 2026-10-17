---
cilt: "I — Temel"
kisim: "15 — Dinamik Ömürlü Nesneler"
baslik: "15.3 Üç klasik hata"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 15.3 Üç klasik hata

**Bellek sızıntısı.** `delete` çağrılmadan gösterici kaybedilir. Bellek, program bitene
kadar geri gelmez.

**Çifte serbest bırakma.** Aynı adres iki kez `delete` edilir. Tanımsız davranıştır.

**Sarkan gösterici.** `delete` edilmiş bir adresin üzerinden erişim yapılır.

<!-- kod-baglam
Myclass* p = new Myclass;
-->
```cpp
delete p;
p->func();      // tanımsız davranış
p = nullptr;    // delete'ten sonra bunu yapmak alışkanlık hâline getirilmeli
```

Üçü de derleyicinin yakalayamadığı, çalışma zamanında ortaya çıkan ve bazen hiç ortaya
çıkmayan hatalardır.
