---
cilt: "I — Temel"
kisim: "5 — `enum` ve `enum class`"
baslik: "5.3 `enum class`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 5.3 `enum class`

C++11 üç sorunu birden çözmek için **kapsamlandırılmış** `enum` türlerini ekledi.

```cpp
enum class Renk { Kirmizi, Yesil, Mavi };

Renk r = Renk::Yesil;        // nitelemek zorunlu
```

Anahtar sözcük `class` olmasına rağmen bu türlerin sınıflarla hiçbir ilgisi yoktur;
isim seçimi yanıltıcıdır. `enum struct` yazımı da aynı anlama gelir.

Üç sorun da çözülür:

**Sabitler kendi kapsamlarındadır.** `Renk::Kirmizi` ile `Meyve::Kirmizi` bir arada
bulunabilir.

**Tamsayı türlerine örtülü dönüşüm yoktur.** Gerçekten istiyorsanız açıkça
dönüştürürsünüz:

```cpp
int x = static_cast<int>(Renk::Yesil);
```

**Temel tür belirtilebilir** ve belirtilmezse `int`'tir:

```cpp
enum class Durum : unsigned char { Bekliyor, Calisiyor };
```

Temel tür belirtme imkânı kapsamlandırılmamış `enum` türlerine de C++11 ile geldi:

```cpp
enum Renk : unsigned char { Kirmizi, Yesil, Mavi };
```

> **Varsayılan tercihiniz `enum class` olsun.** Kapsamlandırılmamış `enum` kullanmak için
> bilinçli bir sebebiniz olmalı; tipik olarak eski kodla uyumluluk veya bit bayrakları.
