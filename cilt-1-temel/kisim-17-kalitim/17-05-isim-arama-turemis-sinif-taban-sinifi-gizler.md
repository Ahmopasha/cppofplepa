---
cilt: "I — Temel"
kisim: "17 — Kalıtım"
baslik: "17.5 İsim arama: türemiş sınıf taban sınıfı gizler"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 17.5 İsim arama: türemiş sınıf taban sınıfı gizler

Kalıtımla ilgili en sık karşılaşılan derleyici hatasının kaynağı budur.

```cpp
class Base {
public:
    void func(int);
};

class Der : public Base {
public:
    void func(double);
};

int main()
{
    Der d;
    d.func(12);     // Base::func(int) DEĞİL, Der::func(double) çağrılır
}
```

İsim arama, ismi bulduğu ilk kapsamda durur. `func` ismi `Der` içinde bulunduğu için
taban sınıfa hiç bakılmaz. **Taban sınıf ile türemiş sınıfın işlevleri birbirinin
`overload`'ı olmaz**, çünkü farklı kapsamlardadırlar.

Bunu istemiyorsanız taban sınıftaki ismi türemiş sınıf kapsamına taşıyın:

<!-- kod-baglam
class Base {
public:
    void func(int);
};
-->
```cpp
class Der : public Base {
public:
    using Base::func;      // artık Base::func da Der kapsamında görünür
    void func(double);
};

int main()
{
    Der d;
    d.func(12);     // artık Base::func(int) çağrılır
    d.func(1.5);    // Der::func(double)
}
```

İmzalar birebir aynı olursa çift anlamlılık hatası **oluşmaz**; türemiş sınıftaki işlev
seçilir.

`using` bildirimini taban sınıfın `private` bölümündeki bir işlev için yaparsanız,
bildirimin kendisi sentaks hatası olur.
