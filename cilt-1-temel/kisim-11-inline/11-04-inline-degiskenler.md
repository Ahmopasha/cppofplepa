---
cilt: "I — Temel"
kisim: "11 — `inline`"
baslik: "11.4 `inline` değişkenler"
kaynak: "ders notları"
kutular: ["Standart Notu — C++17"]
son_kontrol: "2026-11 (C++20)"
---

## 11.4 `inline` değişkenler

C++17'ye kadar `inline` belirteci yalnızca işlevler içindi. Değişkenler için doğrudan bir
çözüm yoktu: başlık dosyasında, işlev dışında tanımlanan sıradan bir değişkeni bütün
çeviri birimlerinin paylaştığı tek değişken olarak tanımlayamazdınız. Bildirim başlığa
`extern` ile, tanım ise bir kaynak dosyaya konurdu.

C++17 bunu değiştirdi:

```cpp
// ayarlar.h
inline int genel_sayac = 0;
```

`inline` değişken de birden çok çeviri biriminde tanımlanabilir ve bütün çeviri birimleri
aynı değişkeni kullanır; Kısım 11.1'deki iki koşul burada da geçerlidir.

En çok işe yaradığı yer sınıfların `static` veri elemanlarıdır. Kısım 12.14'te göreceğiniz
gibi, `static` veri elemanı sınıf içinde bildirilir ve bir kaynak dosyada ayrıca
tanımlanır. `inline` ile bu ikinci adım ortadan kalkar:

```cpp
class Myclass {
public:
    inline static int sayac = 0;    // tek satır, ayrı tanım gerekmez
};
```

> **Standart Notu — C++17**
> **C++17 öncesi:** `inline` belirteci yalnızca işlevlere uygulanabilir. `static` veri
> elemanları sınıf içinde bildirilir, bir kaynak dosyada ayrıca tanımlanır.
> **C++17 ile:** `inline` belirteci değişkenlere de uygulanabilir. `inline` ile
> bildirilen `static` veri elemanı sınıf içinde tanımlanabilir; ayrı tanım gerekmez.
> `constexpr` `static` veri elemanları da örtülü olarak `inline`'dır.
