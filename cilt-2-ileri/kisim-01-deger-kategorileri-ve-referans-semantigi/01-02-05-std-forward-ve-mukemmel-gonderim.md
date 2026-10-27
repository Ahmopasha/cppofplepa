---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.2.5 `std::forward` ve mükemmel gönderim"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

### 1.2.5 `std::forward` ve mükemmel gönderim

Aktarmanın önünde bir engel var. `arg` bir değişken adıdır ve Kısım 1.1.2'de görüldüğü
gibi değişken adları (`return` ve `throw` istisnası dışında) L-Value'dur. Parametrenin
türü `Myclass&&` olsa bile, gövdede `arg` yazdığınızda elde ettiğiniz ifade L-Value'dur.

```cpp
template<typename T>
void foo(T&& arg)
{
    bar(arg);       // arg her zaman L-Value: bar hep kopyalar
}
```

`std::forward` bu bilgiyi geri kazandırır. `T`'ye bakarak koşullu bir dönüşüm yapar:
`T` referans türüne çıkarılmışsa ifadeyi L-Value olarak, çıkarılmamışsa R-Value olarak
geçirir.

```cpp
template<typename T>
void foo(T&& arg)
{
    bar(std::forward<T>(arg));
}
```

Artık argümanın türü, `const`luğu ve L-Value mı R-Value mi olduğu `bar`'a olduğu gibi
ulaşır. Buna **mükemmel gönderim** *(perfect forwarding)* denir. Adına rağmen her farkı
ortadan kaldırmaz; başlıcaları:

- PR-Value bir argüman parametreye bağlanırken geçici bir nesneye dönüşür ve X-Value
  olarak iletilir. Son alıcı parametreyi değerle alıyorsa ve argüman parametreyle (cv
  nitelemesi dışında) aynı sınıf türündense, doğrudan çağrıda PR-Value parametreyi
  doğrudan kurar (bkz. Kısım 1.1.5). İletilen çağrıda ise parametre bu X-Value'dan kurulur
  ve kurucuyu aşırı yük çözümlemesi seçer (çoğu durumda taşıyan kurucu; taşıyan kurucu
  `const` olmayan bir R-Value referans alıyorsa ve X-Value `const` ise kopyalayan kurucu).
  Seçilen kurucu silinmiş ya da erişilemezse çağrı sentaks hatasıdır.
- `0` sabiti iletildiğinde artık boş gösterici sabiti sayılmaz; iletilen ifade `arg`
  parametresini gösteren bir X-Value'dur, değeri sıfır olan bir tamsayı değişmezi
  değildir.
- Küme parantezli ilk değer listeleri iletilemez.

Standart kütüphanedeki kanonik örneği kapların `emplace` işlevleridir. `emplace`'e
geçirdiğiniz argümanlar, kabın içinde oluşturulacak nesnenin kurucu işlevine, L-Value mı
R-Value mi oldukları ve `const`lukları bozulmadan iletilir.

İki kullanım kuralı vardır. **Şablon argümanını her zaman açıkça yazın**;
`std::forward<T>` doğru, `std::forward` değil. Ve **her argümanı yalnızca bir kez
iletin**; iki kez iletirseniz ilk alıcı nesneyi taşımışsa, ikinci kullanımda kaynağı
devralınmış olabilir.
