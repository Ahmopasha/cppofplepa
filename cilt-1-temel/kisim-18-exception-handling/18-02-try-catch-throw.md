---
cilt: "I — Temel"
kisim: "18 — Exception Handling"
baslik: "18.2 `try`, `catch`, `throw`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 18.2 `try`, `catch`, `throw`

```cpp
try {
    // hata gönderebilecek kod
    islem();
}
catch (const std::runtime_error& ex) {
    std::cerr << ex.what() << '\n';
}
catch (const std::exception& ex) {
    std::cerr << "başka bir hata: " << ex.what() << '\n';
}
```

`throw` ile bir nesne gönderilir:

```cpp
if (bolen == 0)
    throw std::runtime_error{"sıfıra bölme"};
```

`try` ve `catch` blokları da birer bloktur; blok kapsamı kurallarına tabidirler. `try`
içinde tanımlanan bir değişkene `catch` içinden erişemezsiniz.

`catch` blokları **yukarıdan aşağıya sırayla** denenir ve ilk uyan çalışır. Bu yüzden
taban sınıf türünden yakalayan blok **en sona** yazılmalıdır; başa yazarsanız türemiş
sınıflar için yazdığınız bloklara hiç sıra gelmez.

`catch (...)` yazımı, türünden bağımsız olarak her şeyi yakalar. Yalnızca en sonda
kullanılır.
