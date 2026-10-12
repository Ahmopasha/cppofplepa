---
cilt: "II — İleri"
kisim: "2 — Taşıma Semantiği ve Bildirim Kuralları"
baslik: "2.7 Taşımanın sessizce devre dışı kaldığı iki senaryo"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 2.7 Taşımanın sessizce devre dışı kaldığı iki senaryo

Cilt I, Kısım 13.12'deki iki kuralın sebebi burada. İkisinde de ortak örüntü şudur:
yükleme çözümlemesi taşıyan işlevi **seçemez** ve sessizce kopyalayan işleve düşer.
Derleyici uyarı vermez.

**Geri dönüş türünün `const T` olması.**

```cpp
const Myclass foo(int x);

Myclass mx;
mx = foo(123);       // Move Assignment değil, Copy Assignment çağrılır
```

Taşıyan işlevin parametresi `T&&`'dir ve `const T` bu türe bağlanamaz. Yükleme
çözümlemesi `const T&` parametreli kopyalayan işlevi seçer. Sınıf türünden geri dönüş
değerlerini `const` yapmayın.

**`return` ifadesinde `std::move` çağırmak.**

```cpp
Myclass bar(int x)
{
    Myclass mx(x);
    return std::move(mx);     // yapmayın
}
```

İngilizcede *pessimistic move* denir. `std::move` olmasaydı derleyici kopyalamayı
tamamen eleyebilirdi; `std::move` yazdığınız için eleme yapılamaz ve taşıyan kurucu
işlev çağrılır. Taşıma kopyalamadan ucuzdur, ama **hiç işlem yapmamak** ikisinden de
ucuzdur.

Eliminasyonun neden mümkün olduğu ve hangi durumlarda garanti edildiği Kısım 3'te.
