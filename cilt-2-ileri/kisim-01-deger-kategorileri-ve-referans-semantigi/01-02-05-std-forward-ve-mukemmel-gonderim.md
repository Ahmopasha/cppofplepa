---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.2.5 `std::forward` ve mükemmel gönderim"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

### 1.2.5 `std::forward` ve mükemmel gönderim

Aktarmanın önünde bir engel var. Kısım 1.1.2'de görüldüğü gibi, `arg` bir **isimdir** ve
isimler L-Value'dur. Parametrenin türü `Myclass&&` olsa bile, gövdede `arg` yazdığınızda
elde ettiğiniz ifade L-Value'dur.

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

Artık `foo`'yu aracı olarak kullanmakla `bar`'ı doğrudan çağırmak arasında hiçbir fark
kalmaz. Buna **mükemmel gönderim** *(perfect forwarding)* denir.

Standart kütüphanedeki kanonik örneği kapların `emplace` işlevleridir. `emplace`'e
geçirdiğiniz argümanlar, kabın içinde oluşturulacak nesnenin kurucu işlevine, kategorileri
ve `const`lukları bozulmadan iletilir.

İki kullanım kuralı vardır. **Şablon argümanını her zaman açıkça yazın**; `std::forward<T>`
doğru, `std::forward` değil. Ve **her argümanı yalnızca bir kez iletin**; iki kez
iletirseniz ikinci kullanımda nesnenin kaynağı çoktan devralınmış olur.
