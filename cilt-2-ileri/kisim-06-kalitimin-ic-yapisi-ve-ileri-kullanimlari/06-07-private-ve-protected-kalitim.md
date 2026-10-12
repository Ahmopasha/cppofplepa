---
cilt: "II — İleri"
kisim: "6 — Kalıtımın İç Yapısı ve İleri Kullanımları"
baslik: "6.7 `private` ve `protected` kalıtım"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 6.7 `private` ve `protected` kalıtım

`public` kalıtım is-a ilişkisi kurar. `private` kalıtım kurmaz; taban sınıfın
**implementasyonunu** devralır, arayüzünü değil.

`private` kalıtımda:

- Taban sınıfın `public` ve `protected` öğeleri türemiş sınıfta `private` olur.
- Dışarıdan bakan kod ilişkiyi göremez.
- Türemiş sınıf türünden nesne, taban sınıf türüne örtülü olarak dönüşmez.

Bu, composition'ın yaptığı işin aynısıdır. Dolayısıyla varsayılan tercih composition
olmalıdır. `private` kalıtımın composition'a üstün geldiği iki durum vardır: taban
sınıfın `protected` öğelerine erişmeniz gerekiyorsa, ya da taban sınıfın bir sanal
işlevini geçersiz kılmanız gerekiyorsa.

Bir üçüncü durum daha vardır ve o Kısım 6.8'in konusudur.

`protected` kalıtım, `private` kalıtımla neredeyse aynıdır. Tek farkı, taban sınıfın
ilgili öğelerinin türemiş sınıfta `protected` kalması, dolayısıyla bir alt kuşağa da
görünür olmasıdır.
