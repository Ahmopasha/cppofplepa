---
cilt: "II — İleri"
kisim: "15 — Eşzamanlılık"
baslik: "15.10 Ayırıcı darboğazı"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 15.10 Ayırıcı darboğazı

Standart, kütüphanenin global bellek ayırma ve bırakma işlevlerinin (`operator new`,
`operator delete`, `malloc`, `free` gibi) ve bunların yerine kullanıcının koyduğu
`operator new`/`operator delete` sürümlerinin data race üretmemesini şart koşar; bunu
nasıl sağlayacaklarını belirlemez. Birçok gerçeklemede genel amaçlı ayırıcı bütün iş
parçacıklarınca paylaşılır ve kendi içinde senkronizasyon yapar. Çok sayıda küçük nesne
ayıran eşzamanlı programlarda bu, ölçeklemeyi sınırlayan bir darboğaza dönüşebilir; iş
parçacığı sayısını artırmak hızı artırmayabilir.

Çözümlerden biri, iş parçacığına özel havuzlar kullanan bir ayırıcı yazmaktır. Kapların
ayırma biçimini değiştiren bir ayırıcının sağlaması gereken arayüz Kısım 17.7'de
anlatılır.
