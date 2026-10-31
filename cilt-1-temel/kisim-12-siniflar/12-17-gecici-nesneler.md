---
cilt: "I — Temel"
kisim: "12 — Sınıflar"
baslik: "12.17 Geçici nesneler"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++20)"
---

## 12.17 Geçici nesneler

**İsimlendirilmiş bir nesne asla geçici nesne değildir.** Geçici nesneler iki şekilde
oluşur: derleyicinin kendiliğinden oluşturması, veya programcının açıkça istemesi.

<!-- kod: atla -->
```cpp
Myclass{12}      // programcının oluşturduğu geçici nesne
```

Geçici nesnelerin hayatı, **içinde bulundukları tam ifadenin sonunda** biter. İstisnası
Kısım 8.3'teki life extension'dır.

Geçici nesne oluşturan ifadeler PR-Value (Kısım 2.4.3) kategorisindedir. Bu yüzden
`const` olmayan sol taraf referanslarına bağlanamazlar.

Bir defaya mahsus kullanılacak bir nesne için isim uydurmak yerine geçici nesne
kullanmak, hem kodu kısaltır hem de derleyiciye Kısım 13.12'deki eliminasyon imkânını
verir.
