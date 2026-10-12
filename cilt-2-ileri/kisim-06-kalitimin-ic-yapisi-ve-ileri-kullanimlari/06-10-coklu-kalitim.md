---
cilt: "II — İleri"
kisim: "6 — Kalıtımın İç Yapısı ve İleri Kullanımları"
baslik: "6.10 Çoklu kalıtım"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 6.10 Çoklu kalıtım

Bir sınıf birden fazla taban sınıftan türetilebilir. Kalıtımların hepsi `public` ise iki
taraflı is-a ilişkisi kurulur.

```cpp
class A { public: void fA(); virtual void vfA(); };
class B { public: void fB(); virtual void vfB(); };

class AB : public A, public B {
public:
    void vfA() override;
    void vfB() override;
};
```

**Kalıtım biçimini her taban sınıf için ayrı yazın.** `class AB : public A, B` yazarsanız
`B`'den `private` kalıtım yapmış olursunuz.

**İsim arama.** Ad önce türemiş sınıf kapsamında aranır. Bulunamazsa taban sınıfların
hepsinde **aynı anda** aranır. Birden fazla tabanda bulunursa çift anlamlılık hatası
oluşur; işlev yüklemesi devreye girmez, çünkü kapsamlar farklıdır.

```cpp
class A  { public: void func(int);    };
class B  { public: void func(double); };
class AB : public A, public B { };

AB x;
x.func(87);      // çift anlamlılık hatası
x.func(1.9);     // çift anlamlılık hatası
x.A::func(87);   // nitelenerek çözülür
```

**Taban sınıfların yazılma sırası** nesne yerleşimini ve `upcasting` sonucu elde edilen
adresi etkiler. Türemiş nesnenin içinde her iki taban sınıfın da ayrı birer alt nesnesi
vardır; dolayısıyla `A*` ve `B*` dönüşümleri aynı adresi vermez.
