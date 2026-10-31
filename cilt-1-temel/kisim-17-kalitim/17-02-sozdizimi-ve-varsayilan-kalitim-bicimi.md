---
cilt: "I — Temel"
kisim: "17 — Kalıtım"
baslik: "17.2 Sözdizimi ve varsayılan kalıtım biçimi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 17.2 Sözdizimi ve varsayılan kalıtım biçimi

C++'ta üç kalıtım biçimi vardır: `public`, `protected`, `private`. İlk yıl boyunca
kullanacağınız `public` kalıtımdır; is-a ilişkisini kuran tek biçim odur. Diğer ikisi
başka bir amaca hizmet eder ve Cilt II'de ele alınıyor.

```cpp
class Der : public Base { };
```

**Kalıtım biçimini yazmayı unutursanız varsayılan uygulanır ve varsayılan `class` ile
`struct` için farklıdır:**

```cpp
class  D1 : Base { };   // private kalıtım — muhtemelen istediğiniz bu değil
struct D2 : Base { };   // public kalıtım
```

Bu, yeni başlayanların düzenli olarak düştüğü bir tuzaktır. `public` anahtar sözcüğünü
her zaman yazın.
