---
cilt: "II — İleri"
kisim: "13 — İleri Hata Yönetimi"
baslik: "13.5 İşlev try blokları"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 13.5 İşlev try blokları

Kurucu işlevin **ilk değer verme listesinde** oluşan hatayı yakalamanın tek yoludur.
Sıradan bir `try` bloğu gövdenin içindedir ve listeyi kapsamaz.

```cpp
class Myclass {
    std::vector<int> v;
public:
    Myclass(std::size_t n)
    try : v(n)                 // liste try'ın içinde
    {
        // gövde
    }
    catch (const std::bad_alloc&) {
        // v'nin ilk değer alması başarısız oldu
    }
};
```

Bir kısıtı vardır ve önemlidir: **kurucu işlevin `catch` bloğu hatayı yutamaz.** Blok
normal biterse hata otomatik olarak yeniden gönderilir. Sebep, nesnenin hayata
gelmemiş olmasıdır; hata yutulursa çağıran kodun elinde geçersiz bir nesne kalırdı
(bkz. Cilt I Kısım 18.9).

Bu yüzden kullanım alanı dardır: hatayı **dönüştürmek** veya günlüğe yazmak için
uygundur, düzeltmek için değil.
