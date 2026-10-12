---
cilt: "II — İleri"
kisim: "14 — Deyimler ve Kalıplar"
baslik: "14.2 Kapsülleme deyimleri"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 14.2 Kapsülleme deyimleri

### Pimpl

Sınıfın gerçeklemesini, başlık dosyasında görünmeyen bir içsel sınıfa taşır. Başlıkta
yalnızca bir gösterici kalır.

```cpp
// myclass.h
class Myclass {
    class Impl;                          // tamamlanmamış tür
    std::unique_ptr<Impl> pimpl;
public:
    Myclass();
    ~Myclass();                          // tanımı kaynak dosyada olmak ZORUNDA
    void func();
};
```

İki kazancı vardır. **Derleme bağımlılığı kırılır**: gerçeklemede yapılan değişiklik,
başlığı dahil eden dosyaların yeniden derlenmesini gerektirmez. Ve **ikili uyumluluk**
korunur: sınıfın boyutu değişmediği için kütüphane güncellenirken kullanıcı kodu yeniden
derlenmeyebilir.

Sonlandırıcı işlevin tanımı kaynak dosyada olmalıdır; başlıkta `= default` yazarsanız
`unique_ptr` tamamlanmamış türü yok etmeye çalışır ve derlenmez. Bu, Cilt I Kısım
2.6'daki tamamlanmamış tür kısıtının en sık karşılaşılan sonucudur.

Bedeli, her erişimde bir dolaylılık ve bir dinamik bellek ayırmadır. **Fast Pimpl**,
ayırma maliyetini ortadan kaldırmak için gerçeklemeyi sınıfın içindeki hizalanmış bir
tamponda tutar; `placement new` ile oluşturulur (bkz. Kısım 17.3). Karşılığında
gerçeklemenin boyutunu başlıkta bildirmek zorunda kalırsınız.

### Attorney-Client

`friend` bildirimi, Cilt I Kısım 12.16'da belirtildiği gibi sınıfın **bütün** `private`
bölümünü açar. Attorney-Client, bu erişimi daraltır.

Araya bir vekil sınıf konur; asıl sınıf yalnızca ona `friend` verir, vekil sınıf da
yalnızca gerekli üyeleri kendi `private` bölümünden seçilmiş taraflara açar.

```cpp
class Myclass {
    void gizli_a();
    void gizli_b();
    friend class Vekil;
};

class Vekil {
    static void gizli_a(Myclass& m) { m.gizli_a(); }    // yalnızca a açılıyor
    friend class Musteri;
};
```

### Hidden Friend

Bir işlevi sınıf içinde `friend` olarak **tanımlamak**, onu yalnızca ADL yoluyla
bulunabilir hâle getirir (bkz. Cilt I Kısım 14.4).

Kazancı, işlevin isim aramaya hiç katılmamasıdır. Aday listesine girmediği için derleme
hızlanır ve istenmeyen örtülü dönüşümlerle seçilme ihtimali ortadan kalkar.

### Thread-Safe Interface

Sınıfın `public` işlevleri kilidi alır, `private` işlevleri almaz. Böylece bir `public`
işlev diğerini çağırdığında aynı kilit iki kez alınmaya çalışılmaz.

```cpp
class Guvenli {
    mutable std::mutex m;
    void ekle_impl(int);                    // kilit almaz
public:
    void ekle(int x)
    {
        std::lock_guard kilit{m};
        ekle_impl(x);                       // impl'ler birbirini çağırabilir
    }
};
```

`mutex` nesnesinin `mutable` olması gerekir; `const` üye işlevlerde de kilitlenebilmesi
için (bkz. Cilt I Kısım 12.15).
