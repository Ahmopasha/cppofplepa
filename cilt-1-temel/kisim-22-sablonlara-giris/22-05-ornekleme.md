---
cilt: "I — Temel"
kisim: "22 — Şablonlara Giriş"
baslik: "22.5 Örnekleme"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 22.5 Örnekleme

Şablon bir kod değil, **kod üreten bir şablondur.** Derleyici, kullanıldığını gördüğü her
farklı şablon argümanı bileşimi için ayrı bir sürüm üretir. Buna **örnekleme**
*(instantiation)* denir.

İki sonucu vardır.

**Bir sınıf şablonu örtülü olarak örneklendiğinde, sanal olmayan üye işlevlerinin
tanımları yalnızca gerektiğinde üretilir.** Bu örneklemede üye işlevlerin yalnızca
bildirimleri üretilir; bir üye işlevin tanımı, işlev çağrıldığında ya da başka bir yolla
tanımına gerek duyulduğunda üretilir (sanal üye işlevler kullanılmasalar da üretilebilir).
Bu yüzden bir sınıf şablonu, sanal olmayan bazı üye işlevlerinin tanımı (gövdesi) belirli
şablon argümanları için geçersiz olsa bile, o işlevler kullanılmadıkça kullanılabilir; bir
üye işlevin parametre ya da dönüş türü o argümanlar için geçersizse sınıf şablonunun o
argümanlarla örneklenmesi sentaks hatasıdır.

**Şablon tanımları genellikle başlık dosyasına konur.** Derleyici, örnekleme yapabilmek
için şablonun tanımını görmek zorundadır; yalnızca bildirimi görmesi yetmez. İşlev
şablonunun ya da sınıf şablonu üye işlevinin tanımını yalnızca bir kaynak dosyaya koyar,
onu başka bir çeviri biriminde tanımını gerektirecek biçimde kullanırsanız (örneğin
çağırırsanız) ve kullanılan şablon argümanları için **açık örnekleme**
*(explicit instantiation)* yapılmamışsa program hatalıdır; standart bunun bildirilmesini
istemez, bağlayıcı bildirebilir (Kısım 0.3). Sınıf şablonunun kendi tanımı görünmüyorsa
tamamlanmış tür gerektiren kullanım (Kısım 2.6) sentaks hatasıdır. İşlev şablonunun ya da
sınıf şablonu üye işlevlerinin tanımlarını kaynak dosyada tutmanın yolu, kullanılacak
şablon argümanları için tanımın bulunduğu kaynak dosyada açık örnekleme yapmaktır; sınıf
şablonunun açık örneklenmesi, kendisinden önce tanımlanmış üye işlevlerin tanımlarını
kullanılmasalar da üretir: Cilt II, Kısım 4.2.

Şablonlar, Kısım 2.7'deki ODR istisnasının kapsamındadır: sınıflar ve `inline` işlevler
(Kısım 11) gibi, bütün tanımlar aynı olmak koşuluyla birden fazla çeviri biriminde
tanımlanabilirler.
