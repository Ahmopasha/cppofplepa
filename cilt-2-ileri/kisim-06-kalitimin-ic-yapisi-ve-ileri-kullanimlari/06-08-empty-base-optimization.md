---
cilt: "II — İleri"
kisim: "6 — Kalıtımın İç Yapısı ve İleri Kullanımları"
baslik: "6.8 Empty Base Optimization"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 6.8 Empty Base Optimization

Ne veri elemanı ne de arayüzü olan bir sınıf ne işe yarar? Etiketleme, ilke sınıfı
(*policy class*) ve derleme zamanı bilgisi taşıma için kullanılır.

Böyle bir sınıfın `sizeof` değeri sıfır olamaz; standart, farklı nesnelerin farklı
adresleri olmasını gerektirir. Ancak boş sınıf bir **taban sınıf** olarak
kullanıldığında derleyicinin ona yer ayırmama izni vardır. Buna *empty base
optimization* denir.

```cpp
struct Bos { };

struct Uye   { Bos b; int x; };     // sizeof genellikle 8
struct Taban : Bos { int x; };      // sizeof genellikle 4
```

Standart kütüphanenin birçok yerinde, örneğin `allocator` ve karşılaştırıcı nesnelerinin
kap sınıflarında tutulmasında bu teknik kullanılır. `private` kalıtımın composition'a
üstün geldiği üçüncü durum budur.
