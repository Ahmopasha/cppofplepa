---
cilt: "II — İleri"
kisim: "10 — `std::format`"
baslik: "10.7 Akımların yerini alıyor mu"
kaynak: "ders notları"
kutular: ["Standart Notu — C++20"]
son_kontrol: "2026-09 (C++23)"
---

## 10.7 Akımların yerini alıyor mu

Tamamen değil. `std::format` **çıktı biçimlendirmesini** devralır; akımların diğer iki
işlevi yerinde kalır.

| İş | Araç |
|---|---|
| Çıktı biçimlendirme | `std::format` / `std::print` |
| Girdi ayrıştırma | Akımlar (`>>`, `getline`) |
| Dosya ve bellek üzerinde akım soyutlaması | Akımlar |

Cilt I Kısım 26.1'deki hiyerarşi hâlâ geçerli ve `std::ostream&` parametreli işlev yazma
alışkanlığı da öyle. `std::print`'in ikinci bir biçimi, akımı doğrudan alır:

```cpp
std::print(dosya_akimi, "{}\n", x);
```

> **Standart Notu — C++20**
> **C++20 öncesi:** Biçimlendirme için ya tür güvenli olmayan `printf`, ya ayrıntılı ve
> kalıcı durum taşıyan akım manipülatörleri kullanılırdı. Kullanıcı tanımlı türler
> `printf` ile hiç çalışmazdı.
> **C++20 ile:** `std::format` kısa, tür güvenli ve genişletilebilir bir üçüncü yol
> sunar. Biçim dizgisi derleme zamanında denetlenir.
> **Neden değişti:** İki mevcut yöntemin de eksikleri yıllardır üçüncü parti
> kütüphanelerle (`fmt`) kapatılıyordu; `std::format` o kütüphanenin standartlaşmış
> hâlidir.
