---
cilt: "I — Temel"
kisim: "26 — Giriş–Çıkış Akımları"
baslik: "26.3 Akımın durumu"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 26.3 Akımın durumu

Her akımın durumu vardır. Durumu `std::ios_base`'in üyesi olan üç bit belirler; hiçbiri
kurulu değilse durum `goodbit`'tir (değeri sıfır).

| Değer | Anlamı |
|---|---|
| `goodbit` | Sorun yok |
| `failbit` | Okuma beklenen karakterleri alamadı ya da yazma istenenleri üretemedi |
| `eofbit` | Okuma girdinin sonuna vardı |
| `badbit` | Girdinin ya da çıktının bütünlüğü bozuldu (ör. kurtarılamaz okuma hatası) |

Akım nesnesi `bool` bağlamında kullanılabilir; `failbit` veya `badbit` kurulmuşsa yanlış
değer üretir. Okuma döngülerinin doğru yazımı budur:

```cpp
int x;
while (std::cin >> x) {
    // x başarıyla okundu
}
```

Yaygın bir hata, `eof()` ile döngü kurmaktır:

```cpp
while (!std::cin.eof()) {     // YANLIŞ
    std::cin >> x;
    // son eleman iki kez işlenir
}
```

`eofbit`, bir okuma girdinin sonuna vardığında kurulur; kurulu olmaması, bir sonraki
okumanın başarılı olacağını göstermez. Girdi, çoğu metin dosyasında olduğu gibi, son
sayıdan sonra satır sonuyla bitiyorsa son sayının okunması başarılı olur ama `eofbit`
kurulmaz. Bir sonraki okuma boşluk karakterlerini atlarken girdinin sonuna varır,
başarısız olur ve `x`'i değiştirmez; döngü bir fazla döner.

Bir hata oluştuktan sonra akım kullanılamaz hâle gelir; `clear()` ile durum sıfırlanmadan
sonraki okumalar çalışmaz.
