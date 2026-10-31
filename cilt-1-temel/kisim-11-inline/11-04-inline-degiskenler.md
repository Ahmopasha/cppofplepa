---
cilt: "I — Temel"
kisim: "11 — `inline`"
baslik: "11.4 `inline` değişkenler"
kaynak: "ders notları"
kutular: ["Standart Notu — C++17"]
son_kontrol: "2026-09 (C++20)"
---

## 11.4 `inline` değişkenler

C++17'ye kadar `inline` yalnızca işlevler içindi. Değişkenler için aynı problem
çözümsüzdü: başlık dosyasında bir değişken tanımlayamazdınız.

C++17 bunu değiştirdi:

```cpp
// ayarlar.h
inline int genel_sayac = 0;
```

En çok işe yaradığı yer sınıfların `static` veri elemanlarıdır. Kısım 12.14'te,
`static` veri elemanının sınıf içinde bildirilip kaynak dosyada tanımlandığını görmüştük.
`inline` ile bu ikinci adım ortadan kalkar:

```cpp
class Myclass {
public:
    inline static int sayac = 0;    // tek satır, ayrı tanım gerekmez
};
```

> **Standart Notu — C++17**
> **C++17 öncesi:** `inline` yalnızca işlevlere uygulanabilir. `static` veri elemanları
> sınıf içinde bildirilir, bir kaynak dosyada ayrıca tanımlanır. Bu ayrım, yalnızca
> başlık dosyasından oluşan kütüphaneler yazmayı zorlaştırır.
> **C++17 ile:** `inline` değişkenlere de uygulanabilir. `static` veri elemanı sınıf
> içinde tanımlanabilir; ayrı tanım gerekmez.
> **Neden değişti:** Yalnızca başlık dosyasından oluşan kütüphaneler yaygınlaştı ve
> değişkenler için ODR istisnası olmaması bu tarzın önündeki son engeldi.
