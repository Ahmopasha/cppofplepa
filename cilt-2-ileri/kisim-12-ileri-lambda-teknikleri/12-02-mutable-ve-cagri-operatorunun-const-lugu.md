---
cilt: "II — İleri"
kisim: "12 — İleri Lambda Teknikleri"
baslik: "12.2 `mutable` ve çağrı operatörünün `const`luğu"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 12.2 `mutable` ve çağrı operatörünün `const`luğu

Cilt I Kısım 24.4'te verilen kuralın gerekçesi 12.1'deki anatomiden doğrudan okunur:
derleyicinin ürettiği `operator()` işlevi **`const`'tur.**

```cpp
class __Kapanis {
    int a;
public:
    int operator()() const { return ++a; }      // const üye işlevde değiştirme: hata
};
```

`mutable` yazmak, o `const`luğu kaldırır:

<!-- kod-baglam
void f()
{
    int a = 0;
@kod@
}
-->
```cpp
auto f = [a]() mutable { return ++a; };
```

```cpp
class __Kapanis {
    int a;
public:
    int operator()() { return ++a; }            // artık const değil
};
```

Üç sonuç çıkar.

**Değişiklik kapanış nesnesinde kalıcıdır.** Aynı lambda ikinci kez çağrıldığında,
birinci çağrının bıraktığı değerden devam eder. Kapanış nesnesi durum taşır.

```cpp
auto f = [n = 0]() mutable { return ++n; };
f();    // 1
f();    // 2
```

**Dışarıdaki değişken etkilenmez.** Yakalama kopyalama olduğu için, değişen şey kapanış
nesnesinin veri elemanıdır.

**Referansla yakalamada `mutable` gerekmez.** `const` üye işlev, referans türünden veri
elemanının *kendisini* değiştirmenizi engeller; gösterdiği nesneyi değiştirmenizi
engellemez (bkz. Cilt I Kısım 6.3).

```cpp
int a = 10;
auto f = [&a] { ++a; };      // mutable gerekmez, a gerçekten değişir
```

`mutable` bir lambda, `const` bir bağlamda çağrılamaz; algoritmalara yüklem olarak
geçirirken buna dikkat edin. Standart kütüphane, yüklemlerin durum taşımamasını bekler.
