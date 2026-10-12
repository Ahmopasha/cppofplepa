---
cilt: "II — İleri"
kisim: "18 — Derleme Zamanı Hesaplamanın Evrimi"
baslik: "18.4 `constinit`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 18.4 `constinit`

Statik ömürlü nesnelerin ilk değer almasında iki aşama vardır. **Statik ilk değer verme**
derleme zamanında olur; değer doğrudan çalıştırılabilir dosyaya yazılır. **Dinamik ilk
değer verme** ise program başlarken, `main` çağrılmadan önce çalışır.

İkincisi iki sorun doğurur. Farklı çeviri birimlerindeki nesnelerin hangi sırayla hayata
geleceği **belirtilmemiştir** (Cilt I Kısım 12.14'te değinilmişti). Ve program başlangıcına
gizli bir maliyet ekler.

`constinit`, bir nesnenin **statik ilk değer verme ile** hayata geleceğini garantiler:

```cpp
constinit int genel = 42;              // derleme zamanında ilk değer alır

int oku();
constinit int bozuk = oku();           // sentaks hatası
```

`constexpr` ile farkı şudur: `constexpr` nesne hem derleme zamanında ilk değer alır hem
de `const`'tur. `constinit` yalnızca ilk değer vermeyi garantiler; nesne sonradan
değiştirilebilir.

```cpp
constexpr int a = 10;     // a değiştirilemez
constinit int b = 10;     // b değiştirilebilir, ama başlangıcı derleme zamanında
```

Üçünün karşılaştırması:

| Anahtar sözcük | Ne garantiler | Nesne değiştirilebilir mi |
|---|---|---|
| `const` | Değişmezlik | Hayır |
| `constexpr` | Derleme zamanında değer + değişmezlik | Hayır |
| `constinit` | Derleme zamanında ilk değer | **Evet** |
