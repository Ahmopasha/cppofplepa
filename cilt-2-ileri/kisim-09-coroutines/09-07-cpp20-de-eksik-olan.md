---
cilt: "II — İleri"
kisim: "9 — Coroutines"
baslik: "9.7 C++20'de eksik olan"
kaynak: "ders notları"
kutular: ["Standart Notu — C++20"]
son_kontrol: "2026-09 (C++23)"
---

## 9.7 C++20'de eksik olan

C++20 eşyordam **mekanizmasını** dile ekledi ama kullanıma hazır **tür** eklemedi.
Yani `promise_type` sözleşmesini sağlayan sınıfları kendiniz yazmanız gerekir.

Bu, dilin en çok eleştirilen kararlarından biridir; eşyordam yazmak, dilin geri
kalanına göre orantısız miktarda altyapı kodu gerektirir.

C++23 bir üreteç türü ekledi:

```cpp
#include <generator>

std::generator<int> sayilar()
{
    co_yield 1;
    co_yield 2;
}

for (int x : sayilar())
    std::cout << x;
```

`std::generator` bir aralıktır; Kısım 8'deki görünümlerle zincirlenebilir. Eşzamansız
işler için gereken `task` benzeri türler ise hâlâ standart dışıdır; üçüncü parti
kütüphanelerden alınır.

> **Standart Notu — C++20**
> **C++20 öncesi:** Askıya alınabilen işlev yoktu. Üreteç yazmak için ya bütün değerleri
> önceden bir kaba doldurmak, ya durumu elle taşıyan bir iteratör sınıfı yazmak
> gerekiyordu. Eşzamansız kod, geri çağırma zincirleriyle yazılıyordu.
> **C++20 ile:** `co_await`, `co_yield` ve `co_return` ile akış bölünebilir; eşzamansız
> kod, sıradan sıralı kod gibi yazılabilir.
> **Neden değişti:** Geri çağırma zincirleri okunabilirliği bozuyordu; kontrol akışı
> kaynak kodunda görünmez hâle geliyordu.
