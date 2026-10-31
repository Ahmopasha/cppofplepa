---
cilt: "I — Temel"
kisim: "23 — STL"
baslik: "23.1 Üç bileşen"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 23.1 Üç bileşen

STL üç parçadan oluşur ve tasarımının tamamı bu üçünün birbirinden **bağımsız**
olmasına dayanır.

**Kaplar** veriyi tutar. **Algoritmalar** veri üzerinde işlem yapar. **İteratörler**
ikisini birbirine bağlar.

Ayrımın kazancı şudur: `N` kap ve `M` algoritma için `N × M` kod yazmak yerine `N + M`
kod yazılır. `std::sort`, `vector` için ayrı, `deque` için ayrı yazılmamıştır; ikisiyle
de çalışır çünkü ikisinin de iteratörleriyle konuşur.
