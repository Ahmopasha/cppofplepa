---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.2 Kapsam"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 2.2 Kapsam

**Kapsam** *(scope)*, bir ismin görünür olduğu program bölgesidir.

C dilinde dört kapsam vardır: dosya, blok, işlev ve işlev prototip kapsamı. C++ sınıflar,
isim alanları ve şablonlarla birlikte bunu genişletir:

| Kapsam | Nerede |
|---|---|
| İsim alanı kapsamı | `namespace` bloğu içinde ve global isim alanında |
| Sınıf kapsamı | Sınıf bloğu içinde |
| Blok kapsamı | Süslü parantezler arasında |
| İşlev kapsamı | Yalnızca etiketler için |
| İşlev prototip kapsamı | Bildirimdeki parametre parantezi içinde |

İç kapsamda dıştakiyle aynı isim tanımlanırsa, dıştaki isim **gölgelenir**
*(shadowing)*. Gölgelenen isme `::` ile erişilebilir:

```cpp
int x = 10;          // global

int main()
{
    int x = 20;      // globali gölgeler
    std::cout << x;      // 20
    std::cout << ::x;    // 10
}
```
