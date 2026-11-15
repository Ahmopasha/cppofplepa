---
cilt: "I — Temel"
kisim: "18 — Exception Handling"
baslik: "18.9 Kurucu işlevde hata"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 18.9 Kurucu işlevde hata

Kurucu işlev hata gönderirse nesne **hayata gelmemiş sayılır** ve sonlandırıcı işlevi
çağrılmaz. Ancak o ana kadar hayata gelmiş taban sınıf kısımlarının ve veri elemanlarının
sonlandırıcı işlevleri çalıştırılır. Devreden kurucu işlevin gövdesinden hata ile
çıkılırsa durum farklıdır (Kısım 12.12).

Sonuç: veri elemanlarınız RAII uyguluyorsa, kurucu işlevde hata oluşsa bile kaynak
sızmaz. Çıplak kaynak tutuyorsanız sızar.

Bu, Rule of Zero'yu tercih etmenin bir sebebi daha.
