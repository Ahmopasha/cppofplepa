---
cilt: "I — Temel"
kisim: "6 — Sabitler"
baslik: "6.5 `constexpr` değişkenler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 6.5 `constexpr` değişkenler

`const`, değerin **değişmeyeceğini** söyler. `constexpr` ise değerin **derleme zamanında
biliniyor olduğunu** söyler. İkisi aynı şey değildir.

```cpp
int oku();

const int a = 10;         // derleme zamanında biliniyor
const int b = oku();      // çalışma zamanında belli oluyor — geçerli
constexpr int c = 10;     // derleme zamanında biliniyor
constexpr int d = oku();  // sentaks hatası
```

Derleme zamanında bilinen değer gerektiren yerler vardır: dizi boyutları, `case`
etiketleri, şablon argümanları, `static_assert` koşulları. `constexpr` bu yerlerde
kullanılabilecek bir değer tanımladığınızı garantiler.

C dilinde `const int` bir değişken, sabit ifade gerektiren noktalarda kullanılamaz.
C++'ta, sabit ifadeyle ilk değer verilmişse kullanılabilir. `constexpr` bu imkânı
niyetinizi açıkça yazarak sağlar.

Namespace kapsamındaki `const` değişkenler C++'ta örtülü olarak iç bağlantılıdır; bu
sayede başlık dosyasında tanımlanabilirler.
