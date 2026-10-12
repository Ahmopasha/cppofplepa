---
cilt: "II — İleri"
kisim: "3 — Kopyalama Eliminasyonu"
baslik: "3.3 Zorunlu eliminasyon"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 3.3 Zorunlu eliminasyon

Kısım 1.1.5'te anlatıldığı gibi, C++17 ile PR-Value artık bir nesne değil, nesne üretmek
için kullanılacak bir reçetedir. Materialization gerçekleşmezse ortada bir nesne yoktur.

Zorunlu eliminasyon bu tanımın doğrudan sonucudur: elimine edilecek bir kopyalama yoktur,
çünkü kopyalanacak ikinci bir nesne hiç oluşmamıştır. Bu yüzden bir optimizasyon değil,
dilin kuralıdır.

İki yerde görülür.

### Unnamed Return Value Optimization

Geri dönüş ifadesi isimsiz bir geçici nesne ise:

```cpp
Myclass foo()
{
    return Myclass{31};     // isimsiz
}

Myclass mx = foo();         // yalnızca bir nesne oluşur
```

`Myclass` sınıfının kopyalayan ve taşıyan kurucu işlevleri `delete` edilmiş olsa bile bu
kod derlenir.

### Unmaterialized Object Passing

Bir geçici nesne, `call-by-value` parametreye argüman olarak geçirilirse:

```cpp
void func(Myclass ax);

func(Myclass{});      // yalnızca parametre nesnesi hayata gelir
```

C++17 öncesindeki beklenti dört adımdı: geçici nesne oluşur, parametreye kopyalanır,
geçici nesne yıkılır, parametre yıkılır. Gerçekleşen iki adımdır: parametre nesnesi
doğrudan oluşur ve yıkılır.
