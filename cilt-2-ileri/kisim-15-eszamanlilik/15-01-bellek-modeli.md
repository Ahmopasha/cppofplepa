---
cilt: "II — İleri"
kisim: "15 — Eşzamanlılık"
baslik: "15.1 Bellek modeli"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 15.1 Bellek modeli

Tek iş parçacıklı programlarda derleyicinin tek yükümlülüğü, **gözlemlenebilir
davranışın** kaynak koddaki gibi olmasıdır. Bunu sağladığı sürece komutları yeniden
sıralayabilir, değişkenleri yazmaca alabilir, işlemleri eleyebilir.

Çok iş parçacıklı programlarda bu özgürlük sorun çıkarır: bir iş parçacığının yaptığı
yeniden sıralama, başka bir iş parçacığı tarafından gözlemlenebilir.

C++11, bu belirsizliği kurallaştıran bir **bellek modeli** tanımladı. Model iki soruya
cevap verir: bir iş parçacığının yazdığı değeri diğeri ne zaman görür, ve işlemlerin
hangi sırayla gerçekleştiği konusunda ne varsayılabilir.

Varsayılan davranış **sıralı tutarlılık** *(sequential consistency)* olarak adlandırılır:
bütün atomik işlemler, sanki tek bir küresel sırada gerçekleşmiş gibi görünür ve her iş
parçacığı kendi işlemlerini kaynak kodundaki sırada yapar.

Bu en güçlü ve en anlaşılır garantidir; en pahalı olanı da odur. Gevşetilmiş
seçenekler 15.8'in konusu.
