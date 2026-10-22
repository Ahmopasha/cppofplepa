---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.1.5 C++17: PR-Value artık bir nesne belirtmiyor"
kaynak: "ders notları"
kutular: ["Standart Notu — C++17"]
son_kontrol: "2026-09 (C++23)"
---

### 1.1.5 C++17: PR-Value artık bir nesne belirtmiyor

C++17 öncesinde PR-Value, bir ifadenin bir nesneye karşılık gelmesi anlamına geliyordu.
C++17 ile tanım değişti: **PR-Value artık bir nesne değil, nesne üretmek için
kullanılacak bir reçetedir.**

Reçetenin nesneye dönüşmesine *materialization* denir. Gerçekleştiğinde
PR-Value → X-Value dönüşümü olur ve ortaya bir *result object* çıkar. Materialization
olmazsa ortada bir nesneden söz edilemez.

Materialization şu durumlarda olur: ifade bir nesneye ilk değer verirken, bir
işlevin parametre değişkeni olurken, geri dönüş değerini tutarken, ifade *discard*
edilirken, ya da ifade bir `const T&` veya `T&&` referansa bağlanırken.

```cpp
class Myclass {
public:
    Myclass(int) { std::cout << "Myclass(int)\n"; }
    Myclass(const Myclass&) = delete;   // kopyalama kapalı
};

Myclass bar(int x) { return Myclass{x}; }

int main()
{
    Myclass mx{ bar(31) };                 // yalnızca bir kez Myclass(int)
    auto my{ Myclass{Myclass{bar(31)}} };  // yine yalnızca bir kez
}
```

C++17 öncesinde bu kod, kopyalayan kurucu işlev `delete` edildiği için sentaks hatası
verirdi. Artık vermiyor; ortada kopyalanacak bir nesne hiç oluşmuyor.

> **Standart Notu — C++17**
> **C++17 öncesi:** PR-Value bir nesneyi temsil eder. Yukarıdaki gibi kodlarda
> kopyalayan veya taşıyan kurucu işlevin *çağrılabilir olması* gerekir. Derleyiciler
> çağrıyı optimizasyonla eleyebilir, ama bu bir garanti değildir.
> **C++17 ile:** PR-Value bir reçetedir. Nesne yalnızca materialization anında oluşur.
> Kopyalayan veya taşıyan kurucu işlevin çağrılabilir olması **gerekmez**.
> **Neden değişti:** Kopyalamanın elenmesi derleyici insafına bırakılmış bir
> optimizasyondu. Değer kategorisinin tanımı değiştirilerek bu durum optimizasyon
> olmaktan çıkarıldı ve dilin garantisi haline getirildi.

Bunun doğrudan devamı zorunlu kopyalama eliminasyonu ile RVO/NRVO ayrımıdır: Kısım 3.
