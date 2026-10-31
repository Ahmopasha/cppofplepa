---
cilt: "I — Temel"
kisim: "3 — İlk Değer Verme"
baslik: "3.2 Default-initialization"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 3.2 Default-initialization

İlk değer verme ifadesi hiç yazılmaz.

Yerleşik türlerde sonuç ömür türüne bağlıdır. **Otomatik ömürlü** değişkenler çöp değer
tutar; o değeri okumak tanımsız davranıştır. **Statik ömürlü** değişkenler ise önce
sıfırlanır.

```cpp
int g;              // global — 0

int main()
{
    int x;          // yerel — çöp değer
    std::cout << x; // tanımsız davranış
}
```

Sınıf türlerinde varsayılan kurucu işlev çağrılır. Sınıfın varsayılan kurucu işlevi yoksa
sentaks hatası alırsınız.
