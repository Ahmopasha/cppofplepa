---
cilt: "I — Temel"
kisim: "18 — Exception Handling"
baslik: "18.9 Kurucu işlevde hata"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 18.9 Kurucu işlevde hata

Kurucu işlev hata gönderirse nesne **hayata gelmemiş sayılır** ve sonlandırıcı işlevi
çağrılmaz. Ancak o ana kadar hayata gelmiş veri elemanlarının sonlandırıcı işlevleri
çalıştırılır.

Sonuç: veri elemanlarınız RAII uyguluyorsa, kurucu işlevde hata oluşsa bile kaynak
sızmaz. Çıplak kaynak tutuyorsanız sızar.

Bu, Rule of Zero'yu tercih etmenin bir sebebi daha.
