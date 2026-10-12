---
cilt: "II — İleri"
kisim: "7 — Concepts"
baslik: "7.1 Çözdüğü problem"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 7.1 Çözdüğü problem

Kısım 4.8'de SFINAE anlatılmış, `std::enable_if` ile yazılan kısıtların okunması zor
olduğu söylenmişti. Sorun ikiye ayrılır.

**Niyet gizlenir.** "Bu şablon yalnızca tamsayı türleriyle çalışır" demenin yolu şuydu:

```cpp
template<typename T, typename = std::enable_if_t<std::is_integral_v<T>>>
void func(T t);
```

Yazılan şey bir kısıt değil, kısıt oluşturmak için kullanılan bir hile. Fazladan bir
şablon parametresi, kullanılmayan bir varsayılan argüman ve dolaylı bir tür ifadesi.

**Hata mesajları kullanılamaz.** Kısıt ihlal edildiğinde derleyici, şablon örnekleme
zincirinin tamamını döker; asıl sebep onlarca satırın içinde kaybolur.

C++20'nin **kavramları** *(concepts)*, kısıtı doğrudan yazılabilir ve derleyicinin
adlandırabileceği bir şey hâline getirdi.

```cpp
template<std::integral T>
void func(T t);
```

Kısıt ihlal edildiğinde derleyici artık "`T`, `std::integral` kısıtını sağlamıyor" diyebilir.
