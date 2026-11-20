---
cilt: "I — Temel"
kisim: "24 — Lambda İfadeleri"
baslik: "24.3 Yakalama"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
kutular: ["Standart Notu — C++20"]
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

Yakalama listesinin başında tek başına duran `=` ya da `&` simgesine (`[=]`, `[&]`,
`[&, x]` gibi) **varsayılan yakalama** *(capture default)* denir. Varsayılan yakalamada
yalnızca gövdede gerçekten kullanılan değişkenler örtülü olarak yakalanır.

Seçim kuralı şudur:

> **Lambda, yakaladığı referansların hayatından daha uzun yaşayacaksa referansla
> yakalamayın.** Referansla yakalanan yerel bir değişken, lambda çalıştığında çoktan yok
> olmuş olabilir; sonuç sarkan referanstır.

```cpp
auto olustur()
{
    int x = 10;
    return [&x] { return x; };    // geçerli; dönen lambdayı çağırmak tanımsız davranış
}
```

Lambda, tanımlandığı ifadenin içinde hemen kullanılıyorsa referansla yakalamak güvenlidir
ve kopyalamadan ucuzdur. Saklanacak, döndürülecek veya başka bir iş parçacığına
geçirilecekse kopyalayarak yakalayın.

Sınıf üye işlevinin içinde `[=]` yazmak, veri elemanlarını **kopyalamaz**: gövdede
`static` olmayan bir üye (veri elemanı ya da üye işlev) kullanılınca nesnenin kendisi
(`*this`) referansla yakalanır ve bu üyeye o nesne üzerinden erişilir. Veri elemanı
lambdanın kopyası değil asıl nesnenin elemanı olduğu için Kısım 24.4'teki kopya kısıtı ona
uygulanmaz. Nesne yok olduktan sonra lambda çağrılırsa tanımsız davranıştır (sarkan
referans). `[*this]` ise C++17'den itibaren nesneyi kopyalar.

> **Standart Notu — C++20**
> **C++20 öncesi:** `[=]`, gövdede `static` olmayan bir üye (veri elemanı ya da üye
> işlev) kullanılınca `*this`'i örtülü olarak referansla yakalardı; `[=, this]` yazımı
> sentaks hatasıydı.
> **C++20 ile:** `*this`'in `[=]` ile örtülü olarak yakalanması hâlâ geçerlidir ama
> artık önerilmiyor (Kısım 5.2); aynı anlam için C++20'den itibaren `[=, this]` yazılır.
