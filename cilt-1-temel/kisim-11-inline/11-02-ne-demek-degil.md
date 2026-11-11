---
cilt: "I — Temel"
kisim: "11 — `inline`"
baslik: "11.2 Ne demek değil"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 11.2 Ne demek değil

`inline`'ın ismi yanıltıcıdır. Standart, `inline`'ın gerçeklemeye "çağrı yerine işlevin
gövdesini yerleştirmek tercih edilir" dediğini söyler, ama gerçeklemeyi bu
**satır içi yerleştirme** *(inline substitution)* işlemini yapmaya zorlamaz. Anahtar
sözcüğün yerleştirme yapılsa da yapılmasa da geçerli olan sonucu ise
**ODR istisnası tanımasıdır** (Kısım 2.7).

Gövdenin yerleştirilmesi **bir talimat değil, bir imkândır.** Gerçekleme, çağrı yerine
gövdeyi yerleştirebilir. Bunu yapıp yapmayacağına kendi karar verir:

- `inline` yazmadığınız bir işlevi de yerleştirebilir
- `inline` yazdığınız bir işlevi yerleştirmeyebilir

Dolayısıyla `inline`'ı performans için yazmayın. Yazma sebebiniz, tanımı başlık dosyasına
koymak olmalıdır.
