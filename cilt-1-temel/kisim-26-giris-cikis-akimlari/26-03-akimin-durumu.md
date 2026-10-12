---
cilt: "I — Temel"
kisim: "26 — Giriş–Çıkış Akımları"
baslik: "26.3 Akımın durumu"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 26.3 Akımın durumu

Her akım, dört durum bitini taşır.

| Bit | Anlamı |
|---|---|
| `goodbit` | Sorun yok |
| `failbit` | Biçimsel hata; okuma başarısız oldu |
| `eofbit` | Dosya sonuna gelindi |
| `badbit` | Kurtarılamaz hata |

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

`eofbit`, okuma **başarısız olduktan sonra** kurulur; döngü koşulu olarak kullanıldığında
bir fazla dönülür.

Bir hata oluştuktan sonra akım kullanılamaz hâle gelir; `clear()` ile durum sıfırlanmadan
sonraki okumalar çalışmaz.
