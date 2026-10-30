---
cilt: "II — İleri"
kisim: "3 — Kopyalama Eliminasyonu"
baslik: "3.1 Ne zaman söz konusudur"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 3.1 Ne zaman söz konusudur

Kopyalama eliminasyonu, dilin kurallarına göre bir kopyalama veya taşıma yapılması
gereken yerde bu işlemin **hiç yapılmamasıdır.** Nesne, kopyalanacağı yerde doğrudan
oluşturulur.

Standart, kopyalayan ya da taşıyan kurmanın elenmesine dört bağlamda, belirli koşullarla
izin verir:

- `return` deyimlerinde
- `throw` ifadelerinde
- Hatanın yakalandığı `catch` bildiriminde, yakalayıcı nesnenin hata nesnesinden
  kurulmasında
- Bir eşyordamın parametrelerinin kopyalanmasında (bkz. Kısım 9)

Sabit ifade gerektiren bağlamlarda ve **sabit ilk değer vermede**
*(constant initialization)* (bkz. Kısım 17.5) bu izin yoktur. Bunlardan ayrı olarak, aynı
sınıf türünden (cv nitelemesi dışında) bir PR-Value bir nesneye ilk değer verdiğinde
ortada elenecek bir kopya yoktur; C++17'den beri PR-Value nesneyi doğrudan kurar (Kısım
3.3).

**Hayata gelmiş iki nesne arasındaki atamada söz konusu değildir.** Atamada taşıma
işlevlerini kullanmak maliyeti düşürür, ama ortada zaten iki nesne olduğu için elenecek
bir şey yoktur. Bu ayrım sürekli karıştırılır.

<!-- kod-baglam
Myclass foo();
-->
```cpp
Myclass a = foo();      // a doğrudan kurulur (Kısım 3.3)
Myclass b;
b = foo();              // eliminasyon YOK, taşıyan atama çağrılır
```
