---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.17 Geçici nesneler"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 12.17 Geçici nesneler

**İsimlendirilmiş bir nesne asla geçici nesne değildir.** Geçici nesneler iki şekilde
oluşur: dilin kurallarıyla örtülü olarak (örneğin `const` bir referans farklı türden bir
değere bağlanırken, Kısım 2.4.5) ya da programcının açıkça yazdığı bir ifadeyle.

<!-- kod: atla -->
```cpp
Myclass{12}.func();   // programcının oluşturduğu geçici nesne
```

Geçici nesnelerin ömrü, **içinde bulundukları tam ifadenin sonunda** biter. Başlıca
istisnası Kısım 8.3'teki *life extension*'dır.

`Myclass{12}` ya da referans döndürmeyen bir işlevin çağrısı gibi ifadeler PR-Value (Kısım
2.4.3) kategorisindedir; PR-Value'lar `const` olmayan L-Value referanslarına bağlanamaz.
C++17'den beri bir PR-Value, ancak gerektiğinde bir geçici nesneye dönüşür (Cilt II, Kısım
1.1.5).

Bir defaya mahsus kullanılacak bir nesne için isim uydurmak yerine geçici nesne kullanmak
kodu kısaltır; C++17'den itibaren bir nesneye `=` ile aynı türden bir PR-Value'dan ilk
değer verildiğinde (`Myclass m = Myclass{12};`) ne geçici nesne ne de kopya oluşur (Kısım
13.12).
