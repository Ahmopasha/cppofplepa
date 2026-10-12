---
cilt: "II — İleri"
kisim: "15 — Eşzamanlılık"
baslik: "15.10 Ayırıcı darboğazı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 15.10 Ayırıcı darboğazı

Genel amaçlı bellek ayırıcı, bütün iş parçacıkları tarafından paylaşılır ve kendi içinde
senkronizasyon yapar. Çok sayıda küçük nesne ayıran eşzamanlı programlarda bu, ölçeklemeyi
sınırlayan bir darboğaza dönüşür; iş parçacığı sayısını artırmak hızı artırmaz.

Çözüm, iş parçacığına özel havuzlar kullanan bir ayırıcı yazmaktır. Kapların ayırma
biçimini değiştirmenin yolu olan `std::allocator` arayüzü Kısım 17.7'de anlatıldı.
