---
cilt: "I — Temel"
kisim: "24 — Lambda İfadeleri"
baslik: "24.3 Yakalama"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 24.3 Yakalama

Köşeli parantez, lambdanın gövdesinde kullanacağı dış değişkenleri belirler. Buna
**yakalama** *(capture)* denir.

<!-- kod: atla -->
```cpp
int a = 10, b = 20;

[]        { }              // hiçbir şey yakalanmaz
[a]       { }              // a kopyalanarak yakalanır
[&a]      { }              // a referansla yakalanır
[a, &b]   { }              // a kopya, b referans
[=]       { }              // kullanılan her şey kopyalanarak
[&]       { }              // kullanılan her şey referansla
[=, &b]   { }              // b hariç hepsi kopya
[&, a]    { }              // a hariç hepsi referans
```

`[=]` ve `[&]` yazımlarına **varsayılan yakalama** denir. Yalnızca gövdede gerçekten
kullanılan değişkenler yakalanır.

Seçim kuralı şudur:

> **Lambda, yakaladığı referansların hayatından daha uzun yaşayacaksa referansla
> yakalamayın.** Referansla yakalanan yerel bir değişken, lambda çalıştığında çoktan yok
> olmuş olabilir; sonuç sarkan referanstır.

```cpp
auto olustur()
{
    int x = 10;
    return [&x] { return x; };    // HATA: x yok olacak
}
```

Lambda, tanımlandığı ifadenin içinde hemen kullanılıyorsa referansla yakalamak güvenlidir
ve kopyalamadan ucuzdur. Saklanacak, döndürülecek veya başka bir iş parçacığına
geçirilecekse kopyalayarak yakalayın.

Sınıf üye işlevinin içinde `[=]` yazmak, veri elemanlarını **kopyalamaz**; `this`
göstericisini kopyalar. Nesne yok olursa lambda sarkar. C++17'den itibaren `[*this]`
yazarak nesnenin kopyasını yakalayabilirsiniz.
