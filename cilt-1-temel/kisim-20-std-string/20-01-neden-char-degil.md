---
cilt: "I — Temel"
kisim: "20 — `std::string`"
baslik: "20.1 Neden `char*` değil"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 20.1 Neden `char*` değil

C dilinde yazılar, sonunda boş karakter bulunan karakter dizileriyle temsil edilir.
Bellek yönetimi, uzunluk takibi ve taşma denetimi programcıya aittir; hataların büyük
kısmı bu üç işten çıkar.

`std::string` yazıyı bir nesne olarak ele alır: belleğini kendi yönetir, uzunluğunu kendi
tutar, gerektiğinde kendi büyür. RAII uygular (Kısım 18.6). Kısım 13.9'daki Rule of
Zero'yu mümkün kılan sınıflardandır: kaynak yönetimini `std::string` gibi veri
elemanlarına bırakan bir sınıf, kopyalama ve taşıma işlevlerini ve sonlandırıcı işlevi
yazmak zorunda kalmaz.
