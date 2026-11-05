---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.4.5 Referans bağlama kuralları"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

### 2.4.5 Referans bağlama kuralları

Bölümün asıl işe yarar kısmı burasıdır. Üç referans türü ve bağladıkları:

| Referans | Neyi bağlar | Neyi bağlamaz |
|---|---|---|
| `T&` | const olmayan L-Value | R-Value, const L-Value |
| `const T&` | **her şeyi** | — |
| `T&&` | const olmayan R-Value | L-Value |

Başlangıçtaki dört satır artık açıklanabilir:

```cpp
int x = 10;

int& a = x;           // geçerli          — T& referansa L-Value
int& b = 10;          // sentaks hatası   — T& referansa R-Value bağlanamaz
const int& c = 10;    // geçerli          — const T& her şeyi bağlar
int&& d = x;          // sentaks hatası   — T&& referansa aynı türden L-Value bağlanamaz
```

`const T&` bir R-Value'ya şöyle bağlanır: gerekiyorsa geçici bir nesne oluşturulur ve
referans ona bağlanır. Geçici nesnenin ömrü, referansın ömrü kadar uzar. Bu mekanizma ve
istisnaları Kısım 8.3'te ayrıntılandırılıyor.

Referans, türü kendisiyle uyumlu bir nesneye bağlanır: aynı türden ya da (Kısım 17.4'te
göreceğiniz gibi) türemiş sınıftan bir nesneye. Referans, bağlandığı nesneden daha `const`
olabilir, daha az olamaz: `const int&` bir `int`'e doğrudan bağlanır, `int&` bir
`const int`'e bağlanamaz. Nesnenin türü, `const` farkı bir yana, referansın türüyle aynı
ya da ondan türemiş değilse (ör. `int` ile `double`), `T&` bağlanamaz; `const T&` ve `T&&`
ise, değer o türe dönüştürülebiliyorsa, dönüştürülmüş değeri tutan geçici bir nesneye
bağlanır (sınıf türlerinde tür dönüştürme operatör işlevleri bu kuralı değiştirebilir;
Cilt II, Kısım 16.1):

```cpp
int ival = 100;

double& dr = ival;         // sentaks hatası — tür uyuşmazlığı
const double& cdr = ival;  // geçerli        — geçici nesne oluşturulur
```

Tür aynı ya da türemişse ama referans daha az `const` ise ya da bir `T&&` bir L-Value'ya
bağlanmak isteniyorsa, geçici nesne oluşmaz ve bağlama sentaks hatasıdır. Örneğin
`const int` bir nesneyi `int&&`'ye bağlamak da, türemiş sınıftan bir L-Value'yu taban
sınıfın `T&&` referansına bağlamak da sentaks hatasıdır.
