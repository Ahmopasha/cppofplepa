---
cilt: "I — Temel"
kisim: "4 — Tür Çıkarımı"
baslik: "4.6 Sondan yazılan geri dönüş türü"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 4.6 Sondan yazılan geri dönüş türü

Geri dönüş türü, parametre listesinden **sonra** yazılabilir:

```cpp
auto func(int x, int y) -> int;
```

Buradaki `auto` bir tür çıkarımı yapmaz; yalnızca "geri dönüş türü ileride yazılacak"
işaretidir.

Faydası, geri dönüş türünün parametrelere bağlı olduğu durumlarda ortaya çıkar.
Normal yazımda parametreler henüz bildirilmemiş olduğu için isimlerine başvuramazsınız;
sondan yazımda başvurabilirsiniz. Bu, esas olarak şablon yazarken gerekir.

C++14'ten itibaren geri dönüş türü tamamen çıkarılabilir:

```cpp
auto kare(int x) { return x * x; }    // int çıkarılır
```

Bu kullanımda işlevin tanımının, çağrıldığı yerde görünür olması gerekir. Bu yüzden
başlık dosyasında bildirim verip kaynak dosyada tanımlayacağınız işlevlerde
kullanılamaz.
