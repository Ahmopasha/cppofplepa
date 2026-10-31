---
cilt: "I — Temel"
kisim: "22 — Şablonlara Giriş"
baslik: "22.5 Örnekleme"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 22.5 Örnekleme

Şablon bir kod değil, **kod üreten bir şablondur.** Derleyici, kullanıldığını gördüğü her
tür için ayrı bir sürüm üretir. Buna *instantiation* denir.

İki sonucu vardır.

**Yalnızca çağrılan üye işlevler üretilir.** Bir sınıf şablonunun hiç çağırmadığınız üye
işlevi, o tür için hiç derlenmez. Bu yüzden bir sınıf şablonu, bazı işlevleri o tür için
geçersiz olsa bile kullanılabilir.

**Şablon tanımları başlık dosyasında olmalıdır.** Derleyici, örnekleme yapabilmek için
şablonun tam tanımını görmek zorundadır; yalnızca bildirimi görmesi yetmez. Kaynak
dosyada tanımlarsanız bağlayıcı hatası alırsınız.

Bu, Kısım 11'deki ODR istisnasıyla ilişkilidir: şablonlar, birden fazla çeviri biriminde
tanımlanabilen üç şeyden biridir (bkz. Kısım 2.7).
