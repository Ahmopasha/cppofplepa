---
cilt: "I — Temel"
kisim: "26 — Giriş–Çıkış Akımları"
baslik: "26.2 Biçimli giriş–çıkış"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 26.2 Biçimli giriş–çıkış

`<<` ve `>>` operatörleri **biçimli** *(formatted)* işlem yapar: veriyi metne çevirir
veya metinden çözer.

```cpp
int x;
std::cin >> x;              // metinden sayıya
std::cout << x << '\n';     // sayıdan metne
```

Zincirleme kullanım, operatörlerin akımı referansla döndürmesi sayesinde çalışır
(bkz. Kısım 14.5).

`>>` operatörü baştaki boşluk karakterlerini (boşluk, sekme, satır sonu gibi) varsayılan
olarak atlar, sonra okunan türe göre okur: `std::string` için bir sonraki boşluk
karakterine kadar, sayı için sayının parçası olamayan ilk karaktere kadar. Satırın
tamamını `std::getline` okur:

```cpp
std::string satir;
std::getline(std::cin, satir);
```

`>>` ile `std::getline` karışık kullanılırsa, `>>` sonrası satırın okunmamış kalanı akımda
kalır ve `std::getline` onu okur; yalnızca satır sonu kaldıysa sonuç boş satırdır.
`std::cin.ignore()` yalnızca bir karakter atar; satır sonundan önce başka karakter
kaldıysa yetmez; satırın kalanını atmak için iki argüman verilir: ilki atılacak karakter
sayısına sınır koymaz, ikincisi satır sonunu da atıp durur:

```cpp
#include <limits>

std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
```
