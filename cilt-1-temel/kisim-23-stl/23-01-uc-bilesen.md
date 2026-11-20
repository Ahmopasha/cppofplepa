---
cilt: "I — Temel"
kisim: "23 — STL"
baslik: "23.1 Üç bileşen"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 23.1 Üç bileşen

STL üç parçadan oluşur ve tasarımının tamamı bu üçünün birbirinden **bağımsız**
olmasına dayanır.

**Kaplar** *(containers)* veriyi tutar. **Algoritmalar** *(algorithms)* veri üzerinde
işlem yapar. **İteratörler** *(iterators)* ikisini birbirine bağlar.

Ayrımın kazancı şudur: `N` kap ve `M` algoritma için `N × M` kod yazmak yerine `N + M` kod
yazılır. `std::sort`, `std::vector` için ayrı, `std::deque` için ayrı yazılmamıştır;
ikisiyle de çalışır çünkü ikisinin de iteratörleriyle konuşur.
