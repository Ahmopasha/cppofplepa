---
cilt: "I — Temel"
kisim: "26 — Giriş–Çıkış Akımları"
baslik: "26.2 Biçimli giriş–çıkış"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
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

`>>` operatörü **boşluk karakterlerini atlar** ve boşluğa kadar okur. Satırın tamamını
okumak için `std::getline` kullanılır:

```cpp
std::string satir;
std::getline(std::cin, satir);
```

`>>` ile `getline` karışık kullanılırsa, `>>` sonrası akımda kalan satır sonu karakteri
`getline`'ın boş satır okumasına yol açar. `std::cin.ignore()` ile temizlenir.
