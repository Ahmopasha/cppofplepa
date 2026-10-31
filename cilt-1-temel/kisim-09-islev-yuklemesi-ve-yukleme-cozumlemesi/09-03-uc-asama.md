---
cilt: "I — Temel"
kisim: "9 — İşlev Yüklemesi ve Yükleme Çözümlemesi"
baslik: "9.3 Üç aşama"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 9.3 Üç aşama

Bir işlev çağrısı görüldüğünde derleyici şu sırayı izler:

1. **İsim arama** — isim hangi kapsamdaysa, o kapsamdaki aynı isimli bütün işlevler
   listelenir. Parametrelerine ve geri dönüş türlerine bakılmaz.
2. **Yükleme çözümlemesi** — listeden uygun olan seçilir.
3. **Erişim kontrolü** — seçilen işleve erişim hakkı var mı bakılır.

Üçüncü aşamanın en sonda olması şu sonucu doğurur: `private` bir yükleme seçilirse,
derleyici "başka bir yükleme deneyeyim" demez; hata verir.
