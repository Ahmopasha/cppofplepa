---
cilt: "I — Temel"
kisim: "18 — Exception Handling"
baslik: "18.5 Yığının geri sarılması"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 18.5 Yığının geri sarılması

Bir hata gönderildiğinde, programın akışı uygun `catch` bloğuna sıçrar. Bu sıçrama
sırasında, terk edilen bütün bloklardaki **otomatik ömürlü nesnelerin sonlandırıcı
işlevleri çalıştırılır.** Buna *stack unwinding* denir.

```cpp
void f()
{
    std::string s{"veri"};     // sonlandırıcı işlevi çalışır
    g();                       // buradan hata gelirse
    // buraya hiç gelinmez
}
```

Bu mekanizma, hata durumunda kaynakların serbest bırakılmasını **otomatik** hâle getirir.

Ama yalnızca sonlandırıcı işlevi olan nesneler için. Çıplak `new` ile ayırdığınız bellek
serbest bırakılmaz:

```cpp
void f()
{
    Myclass* p = new Myclass;
    g();                        // hata gelirse p sızar
    delete p;                   // buraya gelinmez
}
```
