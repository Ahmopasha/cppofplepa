---
cilt: "I — Temel"
kisim: "6 — Sabitler"
baslik: "6.4 Okuma / yazma ayrımı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 6.4 Okuma / yazma ayrımı

> **Okuma amaçlı kullanılan referans ve göstericiler `const` olmalı, yazma amaçlı
> kullanılanlar olmamalıdır.**

Bu kural Kısım 8.5'te işlev parametreleri bağlamında verilmişti. Kapsamı daha geniştir:
bir nesneye dokunmayacak her bağlantı `const` olmalıdır.

Kazancı iki yönlüdür. Derleyici, yanlışlıkla yazma girişimlerini yakalar. Ve kodu okuyan
kişi, bildirime bakarak niyeti anlar.

`const` eklemek sonradan yapılabilecek bir iş değildir; bir işlevi `const` yapmadığınızda
onu çağıran bütün kod `const` olmayan nesnelerle çalışmak zorunda kalır ve zincir
büyür.
