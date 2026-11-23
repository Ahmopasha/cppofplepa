---
cilt: "I — Temel"
kisim: "26 — Giriş–Çıkış Akımları"
baslik: "26.1 Hiyerarşi"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 26.1 Hiyerarşi

Bu kısımda giriş ve çıkış, **akım** *(stream)* denen nesnelerle yapılır. Akım sınıfları
bir kalıtım hiyerarşisidir. Tepedeki `std::ios_base` şablon olmayan bir sınıftır; şemadaki
öteki sınıflar karakter türüyle parametrelenen sınıf şablonlarıdır. Günlük kullandığınız
tür isimleri, `char` açılımlarının tür eş isimleridir (Kısım 16.1).

```
                 ios_base
                    │
              basic_ios<>
               ╱        ╲
    basic_istream<>    basic_ostream<>
          │                   │
    basic_ifstream<>    basic_ofstream<>
    basic_istringstream<>  basic_ostringstream<>
```

`std::cout`'un türü olan `std::ostream`, `std::basic_ostream<char>` demektir. Şemanın
altında dosya akımları (Kısım 26.5) ve **yazı akımları** *(string streams)* (Kısım 26.6)
vardır.

`char` için dört standart akım nesnesi vardır: `std::cin` (giriş), `std::cout` (çıkış),
`std::cerr` (hata) ve `std::clog` (hata); `wchar_t` için de `w` önekli dört karşılığı
(`std::wcout` gibi) vardır. Çıkış önce **tampona** *(buffer)* yazılıp toplu aktarılabilir.
`std::cerr`'in tamponu varsayılan olarak her çıkış işleminden sonra boşaltılır;
`std::cout` ve `std::clog` için standart bunu istemez.

Hiyerarşinin varlığı pratik bir kazanç sağlar: `std::ostream&` parametreli bir işlev,
ekrana da dosyaya da yazı akımına da yazabilir.

<!-- kod-baglam
std::ofstream dosya_akimi;
std::ostringstream yazi_akimi;
-->
```cpp
void rapor_yaz(std::ostream& os);

rapor_yaz(std::cout);
rapor_yaz(dosya_akimi);
rapor_yaz(yazi_akimi);
```
