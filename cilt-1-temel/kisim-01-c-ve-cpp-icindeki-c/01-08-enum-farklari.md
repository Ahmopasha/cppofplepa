---
cilt: "I — Temel"
kisim: "1 — C ve C++ İçindeki C"
baslik: "1.8 `enum` farkları"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 1.8 `enum` farkları

Kısım 5'te ayrıntılandırılır. C'de **numaralandırıcıların** *(enumerator)* türü `int`'tir;
`enum` türünün temel aldığı tamsayı türü gerçeklemeye bağlıdır ve aritmetik türlerden
`enum` türlerine örtülü dönüşüm vardır. C++'ta kapsamlandırılmamış (bkz. Kısım 5.2)
`enum`'un **temel türünü** *(underlying type)* siz belirtebilirsiniz; belirtmezseniz
gerçeklemeye bağlıdır ve aritmetik türlerden `enum` türlerine örtülü dönüşüm yoktur.
