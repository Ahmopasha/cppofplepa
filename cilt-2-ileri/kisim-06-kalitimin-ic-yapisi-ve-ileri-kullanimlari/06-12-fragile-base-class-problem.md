---
cilt: "II — İleri"
kisim: "6 — Kalıtımın İç Yapısı ve İleri Kullanımları"
baslik: "6.12 Fragile Base Class Problem"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 6.12 Fragile Base Class Problem

Taban sınıfta yapılan bir değişikliğin, sözdizimsel olarak hiçbir şeyi bozmadan türemiş
sınıfların davranışını hatalı hale getirmesidir. Kalıtımın en sinsi başarısızlık
biçimidir.

Sayaç tutan bir küme sınıfı düşünün. Taban sınıfın `add` ve `add_range` işlevleri var;
ikisi de sanal `..._impl` işlevlerine devrediyor. Türemiş sınıf bu `_impl` işlevlerini
geçersiz kılıp sayacı artırıyor.

Taban sınıfın ilk sürümünde `add_range`, doğrudan alttaki kaba ekleme yapıyorsa sayaç
doğru çalışır. Bir gün taban sınıfın bakımcısı `add_range`'i, kod tekrarını azaltmak için
döngü içinde `add` çağıracak şekilde yeniden yazarsa, artık her öğe için hem
`add_range_impl` hem `add_impl` çağrılır ve **sayaç iki katına çıkar.**

Türemiş sınıf değişmedi. Taban sınıfın arayüzü değişmedi. Yine de davranış bozuldu.

Buna karşı savunma, taban sınıfın sanal işlevlerini kendi içinden çağırıp çağırmadığını
belgelemek, ya da Kısım 6.6'daki NVI deyimini uygulayarak arayüz işlevlerini sanal olmayan
tek giriş noktalarına indirgemektir.
