---
cilt: "II — İleri"
kisim: "6 — Kalıtımın İç Yapısı ve İleri Kullanımları"
baslik: "6.11 Elmas formasyonu ve sanal kalıtım"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 6.11 Elmas formasyonu ve sanal kalıtım

En tepede bir taban sınıf, ondan ayrı ayrı türetilen iki sınıf, ve o ikisinden çoklu
kalıtımla türetilen bir dördüncü sınıf. Bu şekle *diamond formation* denir.

```
        Device
        /    \
     Fax      Modem
        \    /
      FaxModem
```

`FaxModem` nesnesinin içinde **iki adet** `Device` alt nesnesi bulunur: biri `Fax`
üzerinden, biri `Modem` üzerinden. Bu iki soruna yol açar.

**Birincisi derleme zamanına ilişkindir:** `Device`'ın bir öğesine erişmeye
çalıştığınızda hangisi olduğu belirsizdir, çift anlamlılık hatası alırsınız. Niteleyerek
çözülebilir ama bu, semptomu gizlemekten ibarettir.

**İkincisi mantıksaldır:** iki `Device` alt nesnesinden birinde yaptığınız değişiklik
diğerine yansımaz. Problem alanında tek bir cihaz varken bellekte iki tane vardır.

Boyut farkı doğrudan gözlenebilir:

```
sizeof Device    : 4
sizeof Fax       : 8
sizeof Modem     : 8
sizeof FaxModem  : 16      // iki adet Device
```

Çözüm **sanal kalıtımdır**. Ara sınıflar taban sınıftan `virtual` olarak türetilirse, en
alttaki sınıfta yalnızca bir adet taban sınıf alt nesnesi bulunur.

```cpp
class Device { };
class Fax      : virtual public Device { };
class Modem    : virtual public Device { };
class FaxModem : public Fax, public Modem { };
```

**Sanal kalıtımın getirdiği üçüncü problem.** Normal çoklu kalıtımda en alttaki sınıfın
kurucu işlevi, doğrudan taban sınıflarının kurucu işlevlerini çağırır; onlar da kendi
tabanlarını çağırır. Sanal kalıtımda bu zincir çalışmaz: paylaşılan taban sınıfın kurucu
işlevini çağırmak **en alttaki sınıfın sorumluluğudur.** Ara sınıfların ilk değer verme
listesindeki çağrılar yok sayılır.

Paylaşılan taban sınıfın varsayılan kurucu işlevi yoksa ve en alttaki sınıf listesinde
onu çağırmazsa, derleyici o sınıfın varsayılan kurucu işlevini `delete` eder. Alınan
hata mesajı sebebi doğrudan göstermez:

```
error: use of deleted function 'FaxModem::FaxModem()'
```

Kendiniz kurucu işlev yazarsanız mesaj daha açıklayıcı olur:

```
error: no matching function for call to 'Device::Device()'
```

Çözüm, paylaşılan taban sınıfı en alttaki sınıfın listesinde açıkça çağırmaktır:

```cpp
class FaxModem : public Fax, public Modem {
public:
    FaxModem() : Device(0), Fax(), Modem() { }
};
```
