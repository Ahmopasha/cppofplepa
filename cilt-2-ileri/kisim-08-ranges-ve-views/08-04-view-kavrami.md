---
cilt: "II — İleri"
kisim: "8 — Ranges ve Views"
baslik: "8.4 `view` kavramı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 8.4 `view` kavramı

**Görünüm**, kopyalanması ve taşınması ucuz olan bir aralıktır. Veriyi sahiplenmez;
üzerinde durduğu aralığa bakar.

Kısım 11.2 ve 11.3'teki `string_view` ve `span` ile aynı fikirdir; buradaki fark,
görünümün bir **dönüşüm** de uygulayabilmesidir.

```cpp
std::vector<int> v{1, 2, 3, 4, 5};

auto ciftler = v | std::views::filter([](int x) { return x % 2 == 0; });
```

`ciftler` yeni bir kap değildir. Hiçbir bellek ayrılmaz, hiçbir eleman kopyalanmaz.
Üzerinde dolaşıldığında, `v`'nin elemanları teker teker süzgeçten geçirilir.
