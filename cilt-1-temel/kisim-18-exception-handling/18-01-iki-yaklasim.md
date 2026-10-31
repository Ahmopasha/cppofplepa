---
cilt: "I — Temel"
kisim: "18 — Exception Handling"
baslik: "18.1 İki yaklaşım"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 18.1 İki yaklaşım

Bir işlev, isteneni yapamadığında bunu çağırana nasıl bildirir? İki yaklaşım vardır.

**Hata kodu döndürmek.** İşlev geri dönüş değeriyle veya bir çıkış parametresiyle durumu
bildirir. Çağıran kod her çağrıdan sonra denetim yapar.

**Hata göndermek.** İşlev, sorunu tarif eden bir nesne gönderir ve programın akışı o
nesneyi karşılamaya hazır olan yere sıçrar.

İkincisinin üstünlüğü, hatanın **oluştuğu yer** ile **ele alınacağı yerin** birbirinden
uzak olabilmesidir. Hata kodu yaklaşımında aradaki her katman kodu taşımak zorundadır;
hata gönderme yaklaşımında aradaki katmanlar hiçbir şey yapmaz.

Ayrıca bazı yerlerde hata kodu döndürmek mümkün değildir: kurucu işlevlerin geri dönüş
değeri yoktur, operatör işlevlerinin geri dönüş değeri başka bir iş için ayrılmıştır.
