---
cilt: "I — Temel"
kisim: "9 — İşlev Yüklemesi ve Yükleme Çözümlemesi"
baslik: "9.3 Üç aşama"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 9.3 Üç aşama

Bir işlev çağrısı şu sırayla çözülür (Kısım 2.3):

1. **İsim arama** — isim hangi kapsamda bulunursa, o kapsamda çağrı noktasında görünen
   aynı isimli bütün işlevler listelenir; argümana bağlı arama listeye ek adaylar
   getirebilir (Kısım 16.5). Parametrelerine ve geri dönüş türlerine bakılmaz.
2. **Yükleme çözümlemesi** — listeden en iyi eşleşen işlev seçilir (Kısım 9.4–9.7).
3. **Erişim kontrolü** — seçilen işleve erişim hakkı var mı bakılır.

Üçüncü aşamanın en sonda olması şu sonucu doğurur: seçilen yüklemeye çağrının yapıldığı
yerden erişilemiyorsa (ör. sınıf dışından `private` (Kısım 12.3) bir üyeye) başka bir
yükleme denenmez; çağrı sentaks hatasıdır.
