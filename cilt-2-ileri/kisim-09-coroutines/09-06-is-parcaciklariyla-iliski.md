---
cilt: "II — İleri"
kisim: "9 — Coroutines"
baslik: "9.6 İş parçacıklarıyla ilişki"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 9.6 İş parçacıklarıyla ilişki

Eşyordam ile iş parçacığı farklı şeylerdir. Eşyordam tek başına eşzamanlılık sağlamaz;
yalnızca akışı bölmenin bir yoludur.

Ama ikisi birlikte kullanılabilir ve asıl güçlü yanı buradadır: **bir iş parçacığında
askıya alınan eşyordam, başka bir iş parçacığında devam ettirilebilir.** `await_suspend`
işlevine verilen tutamak, herhangi bir iş parçacığına aktarılabilir.

Eşzamansız giriş–çıkış kütüphaneleri bu mekanizmayı kullanır: eşyordam bir kaynağı
beklerken askıya alınır, iş parçacığı serbest kalıp başka iş yapar, kaynak hazır
olduğunda eşyordam uygun bir iş parçacığında devam eder.

Blokla­yan bekleme ile karşılaştırması şudur: `std::future::get` (bkz. Kısım 15.5) iş
parçacığını bloklar; `co_await` bloklamaz, yalnızca eşyordamı askıya alır.
