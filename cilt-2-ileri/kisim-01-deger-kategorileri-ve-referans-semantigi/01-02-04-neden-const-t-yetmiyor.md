---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.2.4 Neden `const T&` yetmiyor"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

### 1.2.4 Neden `const T&` yetmiyor

`T&&` parametreli bir işleve gönderebildiğiniz ifadeleri, `const T&` parametreli bir
işleve de gönderebilirsiniz (`volatile` nitelikli R-Value'lar dışında). Öyleyse fark
nedir?

Fark, **gövdenin içinde** ortaya çıkar. `const T&` parametreli işlevin gövdesinde
argümanın değer kategorisi ve `const`luğu **kaybolmuştur**; elinizde yalnızca "bir
şeye `const` referans" vardır. `T&&` parametreli işlevin gövdesinde ise bu iki bilgi
`T`'nin içinde korunur.

Bilgiyi korumak tek başına bir amaç değildir. Amaç, o bilgiyi **bir sonraki işleve
aktarabilmektir.**
