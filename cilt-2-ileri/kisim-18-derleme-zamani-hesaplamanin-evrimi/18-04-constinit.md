---
cilt: "II — İleri"
kisim: "18 — Derleme Zamanı Hesaplamanın Evrimi"
baslik: "18.4 `constinit`"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 18.4 `constinit`

Statik ömürlü nesnelerin ilk değer almasında iki aşama vardır: statik ve dinamik ilk değer
verme; ikisinin tanımı ve zamanlaması Kısım 17.5'tedir.

Dinamik ilk değer verme iki sorun doğurabilir. Farklı çeviri birimlerindeki blok dışı
nesnelerin hangi sırayla hayata geleceği genel olarak **belirtilmemiştir** (Kısım 17.5).
Ayrıca program akışına gizli bir maliyet ekleyebilir.

`constinit`, bir nesnenin **statik ilk değer verme ile** hayata geleceğini garantiler:

```cpp
constinit int genel = 42;              // statik ilk değer alır

int oku();
constinit int bozuk = oku();           // sentaks hatası
```

`constexpr` ile farkı şudur: `constexpr` nesne hem sabit ifadeyle ilk değer alır hem de
`const`'tur. `constinit` yalnızca statik ilk değer vermeyi garantiler; nesneyi
kendiliğinden `const` yapmaz.

```cpp
constexpr int a = 10;     // a değiştirilemez
constinit int b = 10;     // b değiştirilebilir, ama statik ilk değer alır
```

Üçünün karşılaştırması:

| Anahtar sözcük | Ne garantiler | Nesneyi `const` yapar mı |
|---|---|---|
| `const` | Değişmezlik (`mutable` hariç) | Evet |
| `constexpr` | Sabit ifadeyle ilk değer + değişmezlik (`mutable` hariç) | Evet |
| `constinit` | Statik ilk değer | **Hayır** |
