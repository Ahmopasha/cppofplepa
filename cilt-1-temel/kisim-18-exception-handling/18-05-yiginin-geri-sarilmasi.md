---
cilt: "I — Temel"
kisim: "18 — Exception Handling"
baslik: "18.5 Yığının geri sarılması"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 18.5 Yığının geri sarılması

Bir hata gönderildiğinde, programın akışı uygun `catch` bloğuna sıçrar. Bu sıçrama
sırasında, o `catch` bloğunun bağlı olduğu `try` bloğuna girildikten sonra hayata gelmiş
ve henüz yok edilmemiş **otomatik ömürlü nesnelerin sonlandırıcı işlevleri çalıştırılır.**
Buna **yığının geri sarılması** *(stack unwinding)* denir. Uygun bir `catch` bloğu
bulunamazsa `std::terminate` çağrılır; o durumda yığının geri sarılıp sarılmayacağı
gerçeklemeye bağlıdır.

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
