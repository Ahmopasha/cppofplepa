---
cilt: "I — Temel"
kisim: "7 — Varsayılan Argümanlar"
baslik: "7.4 İmzanın parçası değildir"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
kutular: ["Standart Notu — C++20"]
---

## 7.4 İmzanın parçası değildir

Hangi varsayılan argümanın kullanılacağı
**çalışma zamanında değil, derleme sırasında, çağrı yerinde görülen bildirime göre**
belirlenir; değeri ise varsayılan argümanın kullanıldığı her çağrıda yeniden hesaplanır.
Sanal işlevlerde hangi varsayılan argümanın kullanılacağını nesnenin değil, çağrıda
kullanılan göstericinin ya da referansın türü belirler; bu bir tuzağa dönüşür; geçersiz
kılan işlevde farklı varsayılan argüman vermeyin (Kısım 17.10).

Varsayılan argüman imzanın parçası olmadığı için (Kısım 9.2) onu eklemek ya da çıkarmak
işlevin kendisini değiştirmez; çağrı yerinde uygulandığı için de yalnızca o bildirimi
gören çeviri birimlerindeki çağrıları etkiler. Ancak standart, varsayılan argümanı da ODR
açısından bir tanım sayar (Kısım 2.7): `inline` işlev tanımları gibi birden çok çeviri
biriminde bulunabilir, ama aynı kapsamda bulunduğu her birimde aynı olmalıdır. Bu yüzden
aynı işlevin aynı parametresine farklı çeviri birimlerinde, aynı kapsamda (ör. ikisi de
bütün işlevlerin dışında) farklı varsayılan argüman vermek programı hatalı yapar ve
standart, gerçeklemenin bunu her durumda bildirmesini istemez. `inline` bir işlevde (Kısım
11) ayrıca işlevin tanımlandığı her çeviri biriminde aynı parametrelere aynı varsayılan
argümanlar verilmiş olmalıdır; birinde verilip ötekinde verilmemesi de programı hatalı
yapar ve standart, gerçeklemenin bunu bildirmesini istemez.

> **Standart Notu — C++20**
> **C++20 öncesi:** Farklı çeviri birimlerindeki varsayılan argümanların aynı olma
> koşulu yalnızca `inline` işlevler içindi.
> **C++20 ile:** Aynı işlevin aynı parametresine farklı çeviri birimlerinde, aynı
> kapsamda farklı varsayılan argüman vermek `inline` olmayan işlevlerde de programı
> hatalı yapar; standart, gerçeklemenin bunu her durumda bildirmesini istemez.
