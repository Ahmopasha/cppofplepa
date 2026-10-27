---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.1.5 C++17: PR-Value artık bir nesne belirtmiyor"
kaynak: "ders notları"
kutular: ["Standart Notu — C++17"]
son_kontrol: "2026-10 (C++23)"
---

### 1.1.5 C++17: PR-Value artık bir nesne belirtmiyor

C++17 öncesinde sınıf türünden bir PR-Value, geçici bir nesneyi temsil ediyordu. C++17 ile
tanım değişti: **PR-Value artık bir nesne değil, bir nesneye ilk değer vermek ya da bir
işlecin operandının değerini hesaplamak için kullanılan bir reçetedir.** Türü `void` olan
ifadeler de PR-Value'dur; bunlar bir nesneye ilk değer vermez.

PR-Value'nun ilk değer verdiği nesneye *result object* denir. Bu nesne PR-Value ile (cv
nitelemesi dışında) aynı türden bir değişken, işlev parametresi ya da geri dönüş değeriyse
PR-Value onu doğrudan kurar; standart arada başka bir nesne gerektirmez. Ancak bir
**geçici** nesne gerektiğinde reçete o geçici nesneye dönüştürülür. Buna *materialization*
denir ve bir PR-Value → X-Value dönüşümüdür.

Materialization başlıca şu durumlarda olur: PR-Value bir referansa bağlanırken, sınıf
türündeki bir PR-Value'nun bir üyesine erişilirken, dizi türündeki bir PR-Value
indislenirken ya da göstericiye dönüştürülürken, küme parantezli bir listeden
`std::initializer_list` kurulurken ve `void` türünden olmayan bir PR-Value'nun değeri
atılırken *(discard)*.

```cpp
class Myclass {
public:
    Myclass(int) { std::cout << "Myclass(int)\n"; }
    Myclass(const Myclass&) = delete;   // kopyalama kapalı
};

Myclass bar(int x) { return Myclass{x}; }

int main()
{
    Myclass mx = bar(31);                  // yalnızca bir kez Myclass(int)
    auto my = Myclass(Myclass(bar(31)));   // yine yalnızca bir kez
}
```

C++17 öncesinde bu kod, kopyalayan kurucu işlev `delete` edildiği için sentaks hatası
verirdi. Artık vermiyor; PR-Value'lar `mx`'i ve `my`'yi doğrudan kurar, kopyalanacak bir
ara nesne hiç oluşmaz.

> **Standart Notu — C++17**
> **C++17 öncesi:** Sınıf türünden bir PR-Value geçici bir nesneyi temsil eder. Yukarıdaki
> gibi kodlarda kopyalayan veya taşıyan kurucu işlevin *çağrılabilir olması* gerekir.
> Standart çağrının elenmesine izin verir, ama bunu garanti etmez.
> **C++17 ile:** PR-Value bir reçetedir ve ilk değer verdiği nesne aynı türdense onu
> doğrudan kurar; standart arada başka bir nesne gerektirmez. Geçici bir nesne
> gerektiğinde, materialization ile oluşur. Kopyalayan veya taşıyan kurucu işlevin
> çağrılabilir olması **gerekmez**.
> **Neden değişti:** Kopyalamanın elenmesi gerçeklemenin tercihine bırakılmış bir
> optimizasyondu. Değer kategorisinin tanımı değiştirilerek, PR-Value'nun aynı türden bir
> nesneye ilk değer verdiği durumlarda bu optimizasyon olmaktan çıkarıldı ve dilin
> garantisi haline getirildi.

Bunun doğrudan devamı zorunlu kopyalama eliminasyonu ile RVO/NRVO ayrımıdır: Kısım 3.
