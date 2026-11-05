---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.2 Kapsam"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 2.2 Kapsam

**Kapsam** *(scope)*, bir ismin görünür olduğu program bölgesidir.

C dilinde dört kapsam vardır: dosya, blok, işlev ve işlev prototip kapsamı. C++ sınıflar,
isim alanları, numaralandırmalar ve şablonlarla birlikte bunu genişletir. Başlıca
kapsamlar:

| Kapsam | Nerede |
|---|---|
| İsim alanı kapsamı | `namespace` bloğu içinde ve global isim alanında |
| Sınıf kapsamı | Sınıf bloğu içinde ve sınıf dışında yazılan üye tanımlarında (Kısım 12) |
| Numaralandırma kapsamı | `enum` bloğu içinde; `enum class` olmayan bir `enum`'un sabitleri dıştaki kapsamda da görünür (Kısım 5) |
| Blok kapsamı | Süslü parantezler arasında; `if`, `switch`, `while` ve `for` başlığında bildirilen isimler için deyimin sonuna kadar |
| İşlev parametre kapsamı | Parametre listesinde; işlev tanımında gövdenin sonuna kadar |
| Şablon parametre kapsamı | Şablon parametre listesinde; şablon bildiriminin ya da tanımının sonuna kadar (Kısım 22) |

Etiketler (`goto` hedefleri) ise işlevin bütün gövdesinde geçerlidir.

İç kapsamda dıştakiyle aynı isim bildirilirse, dıştaki isim **gölgelenir**
*(name hiding; shadowing da denir)*.
**Ancak bir parametreyi işlev gövdesinin en dış bloğunda yeniden bildirmek gölgeleme değil, sentaks hatasıdır.**
**`if`, `switch`, `while` ya da `for` başlığında bildirilen bir ismi denetlenen deyimin en dış bloğunda yeniden bildirmek de sentaks hatasıdır.**
Şablon parametreleri ise kendi kapsamlarındaki hiçbir iç kapsamda yeniden bildirilemez
(Kısım 22). Gölgelenen global bir isme `::x`, bir isim alanı üyesine isim alanının adıyla
(`N::x`) erişilebilir; gölgelenen yerel bir isme erişmenin yolu yoktur:

```cpp
int x = 10;          // global

int main()
{
    int x = 20;      // globali gölgeler
    std::cout << x;      // 20
    std::cout << ::x;    // 10
}
```
