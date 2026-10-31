---
cilt: "I — Temel"
kisim: "4 — Tür Çıkarımı"
baslik: "4.4 `auto` ne zaman kullanılmalı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 4.4 `auto` ne zaman kullanılmalı

`auto` kodu kısaltmak için değil, **doğru tür yazmayı garantilemek** için vardır.

Kullanılması gereken yerler:

- Tür ismi uzun ve açıkça yazmanın hiçbir bilgi katmadığı durumlar
  (`std::vector<int>::iterator` yerine `auto`)
- Yazılması mümkün olmayan türler (lambda ifadelerinin türü)
- Şablon kodunda, türün bağlama göre değiştiği durumlar

Kaçınılması gereken yer, türün okuyucu için önemli olduğu ve ilk değer veren ifadeden
anlaşılmadığı durumlardır. `auto x = foo();` satırında `x`'in ne olduğu okunmuyorsa,
`auto` kodu kısaltmış ama okunmaz hâle getirmiştir.

Bir de sessiz dönüşüm tuzağı vardır:

```cpp
std::vector<int> v;
auto boyut = v.size();     // std::size_t, int değil
int  boyut2 = v.size();    // daraltıcı dönüşüm, uyarı verebilir
```

Burada `auto` doğru olanı yapar; açıkça `int` yazmak hatalıdır.
