---
cilt: "I — Temel"
kisim: "3 — İlk Değer Verme"
baslik: "3.7 Daraltıcı dönüşüm"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 3.7 Daraltıcı dönüşüm

Küme parantezinin en önemli üstünlüğü budur. **Daraltıcı dönüşümlere**
*(narrowing conversion)* **izin vermez.**

```cpp
int a = 3.14;      // geçerli, a = 3 — bilgi sessizce kayboldu
int b{3.14};       // sentaks hatası
int c(3.14);       // geçerli, c = 3

/*
 * char'ın değer aralığı gerçeklemeye bağlıdır; aşağıdaki yorumlar
 * char'ın 1000'i tutamadığı (ör. 8 bitlik) gerçeklemeler içindir.
 * Bu dönüşüm tanımsız davranış değildir.
 */
char ch = 1000;    // geçerli, ama ch'nin değeri 1000 olmaz
char ch2{1000};    // sentaks hatası
```

Daraltıcı dönüşüm, standardın tek tek saydığı dönüşümlerden biridir; başlıcaları
şunlardır: gerçek sayıdan tamsayıya; geniş bir gerçek sayı türünden dar olana
(`long double`'dan `double`'a, `double`'dan `float`'a); tamsayıdan gerçek sayıya; hedef
türün kaynak türün bütün değerlerini tutamadığı tamsayı dönüşümleri. Gerçek sayıdan
tamsayıya dönüşüm her zaman daraltıcıdır. Listedeki diğer üç dönüşümde kaynak bir sabit
ifadeyse (Kısım 6.5) dönüşüm, değere bağlı olarak daraltıcı sayılmayabilir: gerçek sayılar
arasında değerin tam gösterilemese de hedef türün aralığında olması yeterlidir;
tamsayılarda ve tamsayıdan gerçek sayıya dönüşümde değerin hedef türde tam gösterilmesi
gerekir. `char c3{65};` ve `float f{0.1};` geçerlidir. Küme parantezi bu hataları derleme
zamanına taşır.
