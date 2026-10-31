---
cilt: "I — Temel"
kisim: "11 — `inline`"
baslik: "11.2 Ne demek değil"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 11.2 Ne demek değil

`inline`'ın ismi yanıltıcıdır. Anahtar sözcüğün bugünkü anlamı, **ODR istisnası
tanımaktır**; işlev çağrısının yerine gövdenin yerleştirilmesi değil.

O ikinci anlam da vardır ama **bir talimat değil, bir imkândır.** Derleyici, bir işlev
çağrısının yapıldığı yerde işlevin tanımını da görüyorsa, çağrı yerine gövdeyi
yerleştirebilir. Bunu yapıp yapmayacağına kendi karar verir:

- `inline` yazmadığınız bir işlevi de yerleştirebilir
- `inline` yazdığınız bir işlevi yerleştirmeyebilir

Dolayısıyla `inline`'ı performans için yazmayın. Yazma sebebiniz, tanımı başlık dosyasına
koymak olmalıdır.
