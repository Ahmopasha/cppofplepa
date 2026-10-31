---
cilt: "I — Temel"
kisim: "26 — Giriş–Çıkış Akımları"
baslik: "26.1 Hiyerarşi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 26.1 Hiyerarşi

Akım sınıfları bir kalıtım hiyerarşisidir ve hepsi sınıf şablonudur. Günlük kullandığınız
isimler, `char` açılımlarının tür eş isimleridir.

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

`std::ostream`, `basic_ostream<char>`'ın eş ismidir. `std::cout` da bu türden bir
nesnedir.

Dört standart akım nesnesi vardır: `std::cin` (giriş), `std::cout` (çıkış, tamponlu),
`std::cerr` (hata, tamponsuz), `std::clog` (hata, tamponlu).

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
