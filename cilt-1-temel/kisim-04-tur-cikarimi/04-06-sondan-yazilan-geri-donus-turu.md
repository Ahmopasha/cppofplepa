---
cilt: "I — Temel"
kisim: "4 — Tür Çıkarımı"
baslik: "4.6 Sondan yazılan geri dönüş türü"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 4.6 Sondan yazılan geri dönüş türü

Geri dönüş türü, parametre listesinden **sonra** yazılabilir:

```cpp
auto func(int x, int y) -> int;
```

Buradaki `auto` bir tür çıkarımı yapmaz; yalnızca "geri dönüş türü ileride yazılacak"
işaretidir.

Faydası, geri dönüş türünün parametrelere bağlı olduğu durumlarda ortaya çıkar. Normal
yazımda parametreler henüz bildirilmemiş olduğu için isimlerine başvuramazsınız; sondan
yazımda başvurabilirsiniz. Bu, esas olarak şablon yazarken (Kısım 22) gerekir: geri dönüş
türü parametrelerden `decltype` ile hesaplanır (Cilt II, Kısım 1.1.4).

C++14'ten itibaren geri dönüş türü tamamen çıkarılabilir:

```cpp
auto kare(int x) { return x * x; }    // int çıkarılır
```

Bu kullanımda geri dönüş türü tanımdaki `return` deyiminden çıkarılır, hiç `return` deyimi
yoksa `void` olur; bu yüzden işlevi kullanan bir ifadeden (örneğin çağrıdan) önce türün
çıkarılmış olması gerekir. İşlevin dışında bu, tanımın önce gelmesi demektir. İşlev kendi
gövdesinde ise türü bir `return` deyiminden çıkarıldıktan sonra kendini çağırabilir.
Başlık ve kaynak dosyasıyla çalışırken bu kural, tanımın aynı çeviri biriminde (Kısım 0.3)
bulunması demektir. Başlık dosyasında yalnızca bildirimini verip kaynak dosyada
tanımladığınız bir işlevde bu yazım işe yaramaz: işlev başka kaynak dosyalardan
çağrılamaz. Tanımı birden çok kaynak dosyanın dahil ettiği bir başlık dosyasına
yazacaksanız işlevi `inline` tanımlayın (Kısım 11.1).
