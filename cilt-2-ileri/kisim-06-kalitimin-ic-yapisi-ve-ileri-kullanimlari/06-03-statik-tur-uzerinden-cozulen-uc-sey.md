---
cilt: "II — İleri"
kisim: "6 — Kalıtımın İç Yapısı ve İleri Kullanımları"
baslik: "6.3 Statik tür üzerinden çözülen üç şey"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 6.3 Statik tür üzerinden çözülen üç şey

Cilt I Kısım 2.3'te, isim arama / yükleme çözümlemesi / erişim kontrolü sıralaması
verilmiş ve üçünün de derleme zamanında işlediği söylenmişti. Kalıtım, o sıralamanın en
şaşırtıcı sonuçlarını doğurur.

Çok biçimlilik yalnızca **hangi gövdenin çalışacağını** çalışma zamanına bırakır. Bunun
dışındaki her şey derleme zamanında ve statik türe göre kararlaştırılır. Üç kalem
özellikle şaşırtıcıdır:

| Ne | Neye göre |
|---|---|
| İsim arama (`.`, `->`, `::` ile) | **statik** tür |
| Erişim kontrolü | **statik** tür |
| Varsayılan argümanlar | **statik** tür |
| Çağrılan gövde | **dinamik** tür |

Cilt I, Kısım 17.10'daki varsayılan argüman tuzağı bu tablonun bir sonucudur. Erişim
kontrolünün statik türe bakması ise şunu mümkün kılar: taban sınıfta `public` olan bir
sanal işlev, türemiş sınıfta `private` olarak geçersiz kılınabilir ve taban sınıf
göstericisi üzerinden yine çağrılabilir. Kısım 6.6'daki NVI deyimi bu davranışın üzerine
kurulur.
