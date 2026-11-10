---
cilt: "I — Temel"
kisim: "9 — İşlev Yüklemesi ve Yükleme Çözümlemesi"
baslik: "9.5 Dönüşüm hiyerarşisi"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 9.5 Dönüşüm hiyerarşisi

Birden fazla uygun aday varsa, argümanlardan parametrelere yapılacak dönüşümler
karşılaştırılır. Üç kategori vardır ve aralarındaki sıra kesindir:

```
standart dönüşüm  >  kullanıcı tanımlı dönüşüm  >  variadic dönüşüm
        (en iyi)                                      (en kötü)
```

**Standart dönüşüm** — dilin kendi kurallarıyla yapılan dönüşümler.

**Kullanıcı tanımlı dönüşüm** — normalde geçersiz olan bir dönüşümün, bir sınıfın
(`std::string` gibi kütüphane sınıfları dahil) dönüştüren kurucu işlevi (Kısım 12.13) veya
tür dönüştürme operatör işlevi (Cilt II, Kısım 16.1) sayesinde geçerli hâle gelmesi.

**Variadic dönüşüm** — işlev imzasındaki `...` parametresine yapılan geçiş.

Bir argüman için aynı kategoride dönüşüm gerektiren birden fazla uygun aday varsa,
kategorinin kendi içindeki sıraya bakılır (standart dönüşümler için Kısım 9.6; aynı
sıradaki dönüşümleri ayıran ek kurallar da vardır, ör. referans bağlamada değer
kategorisi: Cilt II, Kısım 1.1.6); bunlarla da ayrılamazlarsa o argüman bakımından
eşittirler ve çağrının sonucunu Kısım 9.7'deki kural belirler.
