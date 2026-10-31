---
cilt: "I — Temel"
kisim: "18 — Exception Handling"
baslik: "18.3 Değerle gönder, referansla yakala"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 18.3 Değerle gönder, referansla yakala

Bu bölümün en çok tekrarlanması gereken kuralı:

> **`throw by value, catch by reference`.**

**Gönderirken geçici nesne kullanın**, bir isimlendirilmiş nesne gönderip ömrünü
düşünmeyin:

```cpp
throw std::runtime_error{"mesaj"};      // doğru
```

**Yakalarken `const` referans kullanın**, sınıf türünün kendisini değil:

<!-- kod: atla -->
```cpp
catch (const std::exception& ex)        // doğru
catch (std::exception ex)               // yanlış
```

İkinci yazımın iki sorunu vardır. Nesne kopyalanır; kopyalayan kurucu işlev de hata
gönderebilir ve durum kötüleşir. Daha önemlisi, kalıtım hiyerarşisinden gelen bir hata
nesnesi **dilimlenir** (bkz. Kısım 17.9) ve elinizde taban sınıf kısmı kalır; sanal
işlevler artık doğru sürümü çağırmaz.
