---
cilt: "I — Temel"
kisim: "4 — Tür Çıkarımı"
baslik: "4.4 `auto` ne zaman kullanılmalı"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 4.4 `auto` ne zaman kullanılmalı

`auto` kodu kısaltmak için değil, **doğru tür yazmayı garantilemek** için vardır.

Kullanılması gereken yerler:

- Tür ismi uzun ve açıkça yazmanın hiçbir bilgi katmadığı durumlar
(`std::vector<int>::iterator` yerine `auto`; iteratörler: Kısım 23.2) - Adıyla yazılamayan
türler (lambda ifadelerinin türü, Kısım 24) - Şablon kodunda (Kısım 22), türün bağlama
göre değiştiği durumlar

Kaçınılması gereken yer, türün okuyucu için önemli olduğu ve ilk değer veren ifadeden
anlaşılmadığı durumlardır. `auto x = foo();` satırında `x`'in ne olduğu okunmuyorsa,
`auto` kodu kısaltmış ama okunmaz hâle getirmiştir.

Bir de sessiz dönüşüm tuzağı vardır:

```cpp
std::vector<int> v;
auto boyut = v.size();     // std::vector<int>::size_type, int değil
int  boyut2 = v.size();    // geçerli, ama değer int'e sığmayabilir
```

`size_type` işaretsiz bir tamsayı türüdür; hangisi olduğu gerçeklemeye bağlıdır. Burada
`auto` doğru türü verir; açıkça `int` yazmak, `int`'ten geniş olabilen işaretsiz bir
türdeki değeri `int`'e daraltıcı bir dönüşümle çevirir (Kısım 3.7). Değer sığmazsa sonuç
tanımsız davranış değildir, ama değer değişir (Kısım 3.7).
