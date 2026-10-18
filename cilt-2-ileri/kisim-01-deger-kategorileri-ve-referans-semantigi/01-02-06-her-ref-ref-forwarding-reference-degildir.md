---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.2.6 Her `&&` forwarding reference değildir"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

### 1.2.6 Her `&&` forwarding reference değildir

Bu, konunun en çok hata yapılan yeridir. `&&` yazılışı forwarding reference için yeterli
değildir; **tür çıkarımı o parametre için, o çağrıdan yapılıyor olmalıdır.**

Aşağıdakilerin hiçbiri forwarding reference değildir, hepsi düz R-Value referanstır:

```cpp
template<typename T>
void f1(const T&& arg);          // const var: çıkarım kuralı bozuldu

template<typename T>
void f2(std::vector<T>&& arg);   // T çıkarılır, ama biçim T&& değil: vector<T>&&

template<typename T>
class Myclass {
public:
    void f3(T&& arg);            // T sınıfın parametresi, çağrıda çıkarılmıyor
};

void f4(std::string&& arg);      // f4 şablon değil: çıkarım yok
```

Üçüncüsü özellikle sinsidir: `Myclass<int>` nesnesi oluşturulduğunda `T` çoktan `int`
olmuştur, dolayısıyla `f3`'ün parametresi `int&&`'dir. Aynı sınıfın üye işlevini
forwarding reference yapmak için ona **kendi** şablon parametresi verilmelidir:

```cpp
template<typename T>
class Myclass {
public:
    template<typename U>
    void f3(U&& arg);            // artık forwarding reference
};
```
