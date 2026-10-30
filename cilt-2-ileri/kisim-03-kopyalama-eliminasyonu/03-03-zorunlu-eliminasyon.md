---
cilt: "II — İleri"
kisim: "3 — Kopyalama Eliminasyonu"
baslik: "3.3 Zorunlu eliminasyon"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 3.3 Zorunlu eliminasyon

Kısım 1.1.5'te anlatıldığı gibi, C++17 ile PR-Value artık bir nesne değil, bir nesneye ilk
değer vermek için kullanılan bir reçetedir. Aynı türden (cv nitelemesi dışında) bir
nesneye ilk değer verdiğinde onu doğrudan kurar; standart arada başka bir nesne
gerektirmez.

Zorunlu eliminasyon bu tanımın doğrudan sonucudur: elenecek bir kopyalama yoktur,
çünkü kopyalanacak ikinci bir nesne hiç oluşmamıştır. Bu yüzden bir optimizasyon değil,
dilin kuralıdır.

Kural geneldir: aynı sınıf türünden (cv nitelemesi dışında) bir PR-Value bir nesneye ilk
değer verdiğinde nesneyi doğrudan kurar. `Myclass m = foo();` ve `Myclass m = Myclass{};`
da böyledir. `throw Myclass{};` ifadesinde de hata nesnesi PR-Value'dan doğrudan kurulur,
ama kopyalayan kurucunun silinmemiş ve erişilebilir olması yine gerekir.

Doğrudan kurma kuralının bir istisnası vardır: türün en az bir **uygun** *(eligible)*,
yani silinmemiş, varsa kısıtları sağlanan ve aynı türden daha kısıtlı bir eşi bulunmayan
kopyalayan ya da taşıyan kurucusu varsa, bunların hepsi trivial ve sonlandırıcısı trivial
ya da silinmişse, gerçekleme işlev parametresi ya da dönüş nesnesi için ek bir geçici
nesne oluşturabilir.

Kuralın en sık görüldüğü iki yer şunlardır.

### Unnamed Return Value Optimization

Geri dönüş ifadesi aynı türden bir PR-Value ise:

```cpp
Myclass foo()
{
    return Myclass{31};     // isimsiz
}

Myclass mx = foo();         // yalnızca bir nesne oluşur
```

`Myclass` sınıfının kopyalayan ve taşıyan kurucu işlevleri silinmiş olsa bile bu
kod derlenir.

### Unmaterialized Object Passing

Aynı türden bir PR-Value, `call-by-value` parametreye argüman olarak geçirilirse:

```cpp
void func(Myclass ax);

func(Myclass{});      // yalnızca parametre nesnesi hayata gelir
```

C++17 öncesindeki beklenti dört adımdı: geçici nesne oluşur, parametreye kopyalanır ya da
taşınır, parametre yıkılır, geçici nesne yıkılır. Gerçekleşen iki adımdır: parametre
nesnesi doğrudan oluşur ve yıkılır.
