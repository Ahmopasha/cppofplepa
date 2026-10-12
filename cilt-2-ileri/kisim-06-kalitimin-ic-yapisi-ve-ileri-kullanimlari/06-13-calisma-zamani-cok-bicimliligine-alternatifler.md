---
cilt: "II — İleri"
kisim: "6 — Kalıtımın İç Yapısı ve İleri Kullanımları"
baslik: "6.13 Çalışma zamanı çok biçimliliğine alternatifler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 6.13 Çalışma zamanı çok biçimliliğine alternatifler

Kısım 6.1'deki maliyet önem kazandığında ya da tür kümesi derleme zamanında biliniyorsa
üç alternatif vardır.

**CRTP.** Türemiş sınıf, taban sınıf şablonuna kendisini şablon argümanı olarak geçirir.
Çok biçimlilik derleme zamanında çözülür; `vptr` yoktur, çağrılar `inline` edilebilir.

```cpp
template<typename Der>
class Taban {
public:
    void arayuz() { static_cast<Der*>(this)->impl(); }
};

class Somut : public Taban<Somut> {
public:
    void impl();
};
```

Bedeli, ortak bir taban tür kalmamasıdır; `Taban<A>` ile `Taban<B>` ilgisiz türlerdir,
dolayısıyla hepsini tek bir kapta tutamazsınız.

**`std::variant`.** Tür kümesi kapalı ve önceden biliniyorsa, kalıtım yerine
`std::variant` ile modelleyip `std::visit` ile dağıtım yapabilirsiniz. Dinamik bellek
kullanılmaz.

**Type erasure.** Ortak bir taban sınıf gerektirmeden çok biçimli davranış elde etmenin
yoludur; `std::function` bunun standart kütüphanedeki örneğidir.

Bu üçü Kısım 14'te ayrıntılı olarak ele alınıyor.
