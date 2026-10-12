---
cilt: "II — İleri"
kisim: "8 — Ranges ve Views"
baslik: "8.7 Boru hattı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 8.7 Boru hattı

Uyumlandırıcılar `|` operatörüyle zincirlenir. Bir uyumlandırıcının ürettiği görünüm,
bir sonrakinin girdisi olur.

```cpp
auto sonuc = v
    | std::views::filter([](int x) { return x % 2 == 0; })
    | std::views::transform([](int x) { return x * x; })
    | std::views::take(3);

for (int x : sonuc)
    std::cout << x << ' ';
```

Okuma sırası soldan sağadır ve işlem sırasıyla aynıdır. Aynı işi eski STL ile yazmak
iki ara kap ve üç algoritma çağrısı gerektirirdi.

**Zincirin tamamı tek geçişte çalışır.** Ara kap oluşmaz; her eleman, zincirin tamamından
geçip çıkar. `take(3)` yüzünden de yalnızca üç eleman üretilecek kadar iş yapılır.

Boru hattı yazımı, işlevsel programlamadan ödünç alınmıştır.
