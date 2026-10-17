---
cilt: "II — İleri"
kisim: "3 — Kopyalama Eliminasyonu"
baslik: "3.1 Ne zaman söz konusudur"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 3.1 Ne zaman söz konusudur

Kopyalama eliminasyonu, dilin kurallarına göre bir kopyalama veya taşıma yapılması
gereken yerde bu işlemin **hiç yapılmamasıdır.** Nesne, kopyalanacağı yerde doğrudan
oluşturulur.

Dört bağlamda görülür:

- Bir nesne hayata getirilirken
- `return` deyimlerinde
- `throw` ifadelerinde
- Hatanın yakalandığı `catch` bloğunda

**Hayata gelmiş iki nesne arasındaki atamada söz konusu değildir.** Atamada taşıma
işlevlerini kullanmak maliyeti düşürür, ama ortada zaten iki nesne olduğu için elimine
edilecek bir şey yoktur. Bu ayrım sürekli karıştırılır.

<!-- kod-baglam
Myclass foo();
-->
```cpp
Myclass a = foo();      // eliminasyon mümkün
Myclass b;
b = foo();              // eliminasyon YOK, taşıyan atama çağrılır
```
