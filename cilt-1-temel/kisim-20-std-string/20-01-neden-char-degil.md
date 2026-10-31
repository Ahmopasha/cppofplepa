---
cilt: "I — Temel"
kisim: "20 — `std::string`"
baslik: "20.1 Neden `char*` değil"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 20.1 Neden `char*` değil

C dilinde yazılar, sonunda boş karakter bulunan karakter dizileriyle temsil edilir.
Bellek yönetimi, uzunluk takibi ve taşma denetimi programcıya aittir; hataların büyük
kısmı bu üç işten çıkar.

`std::string` yazıyı bir nesne olarak ele alır: belleğini kendi yönetir, uzunluğunu
kendi tutar, gerektiğinde kendi büyür. RAII uygular ve Rule of Zero'ya uyar
(bkz. Kısım 13.9, 18.6).
