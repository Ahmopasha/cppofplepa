---
cilt: "I — Temel"
kisim: "18 — Exception Handling"
baslik: "18.3 Değerle gönder, referansla yakala"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 18.3 Değerle gönder, referansla yakala

Bu bölümün en çok tekrarlanması gereken kuralı:

> **`throw by value, catch by reference`.**

**Gönderirken geçici nesne kullanın.** `throw`'un gönderdiği, `catch` bloğunun yakaladığı
nesneye **hata nesnesi** *(exception object)* denir; Kısım 18.1'de «hata» dediğimiz nesne
budur. İsimlendirilmiş bir nesne gönderirseniz `throw` ondan ayrı bir hata nesnesi
oluşturur; bu da geçerlidir, ama geçici nesne yazmak hem kısa hem açıktır:

```cpp
throw std::runtime_error{"mesaj"};      // doğru
```

**Yakalarken `const` referans kullanın**, sınıf türünün kendisini değil:

<!-- kod: atla -->
```cpp
catch (const std::exception& ex)        // doğru
catch (std::exception ex)               // yanlış
```

İkinci yazımda yakalanan hata nesnesi kopyalanır. Standart hata sınıflarının kopyalayan
kurucu işlevi hata göndermez, ama kendi yazdığınız bir hata sınıfınınki gönderebilir; bu
kopyalama sırasında hata çıkarsa program `std::terminate` ile sonlanır. Daha önemlisi,
türemiş sınıf türünden bir hata taban sınıf türünden bir parametreyle yakalanırsa
parametreye yalnızca taban sınıf kısmı kopyalanır, yani **dilimlenir** (Kısım 17.9); bu
parametre üzerinden yapılan sanal işlev çağrıları türemiş sınıfın sürümünü çalıştırmaz.
