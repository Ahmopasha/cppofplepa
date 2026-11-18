---
cilt: "I — Temel"
kisim: "19 — Çalışma Zamanı Tür Bilgisi"
baslik: "19.1 Ne işe yarar"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 19.1 Ne işe yarar

Çok biçimli bir hiyerarşide elinizde taban sınıf göstericisi vardır ve ardındaki gerçek
türü bilmezsiniz. Çoğu zaman bilmenize gerek de yoktur; sanal işlevler işi halleder.

Bazen gerekir. Bir göstericinin ya da referansın gösterdiği asıl nesnenin türüne
**dinamik tür** *(dynamic type)*, programın çalışması göz önüne alınmadan belirlenen türe
**statik tür** *(static type)* (Kısım 17.10'da geçmişti) denir: `Sekil* s = new Daire;`
için `*s`'nin statik türü `Sekil`, dinamik türü `Daire`'dir. **RTTI**
*(run-time type information)*, nesnenin dinamik türünü çalışma zamanında sorgulamanın
yoludur ve iki aracı vardır: `dynamic_cast` ve `typeid`.

Dinamik türü sorgulamak için taban sınıfın **çok biçimli** (Kısım 17.6) olması, yani en az
bir sanal işlev bildirmesi ya da devralması gerekir. Taban sınıf çok biçimli değilse
`typeid` statik türü verir; `dynamic_cast` ile aşağı dönüşüm ise sentaks hatasıdır (Kısım
10.5). Dinamik türün çalışma zamanında nasıl bulunduğunu standart belirtmez; yaygın
gerçekleme yolu Cilt II, Kısım 6.1'de anlatılıyor.
