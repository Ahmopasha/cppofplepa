---
cilt: "I — Temel"
kisim: "9 — İşlev Yüklemesi ve Yükleme Çözümlemesi"
baslik: "9.5 Dönüşüm hiyerarşisi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 9.5 Dönüşüm hiyerarşisi

Birden fazla uygun aday varsa, argümanlardan parametrelere yapılacak dönüşümler
karşılaştırılır. Üç kategori vardır ve aralarındaki sıra kesindir:

```
standart dönüşüm  >  kullanıcı tanımlı dönüşüm  >  variadic dönüşüm
        (en iyi)                                      (en kötü)
```

**Standart dönüşüm** — dilin kendi kurallarıyla yapılan dönüşümler.

**Kullanıcı tanımlı dönüşüm** — normalde geçersiz olan bir dönüşümün, sizin yazdığınız
bir dönüştüren kurucu işlev veya tür dönüştürme operatör işlevi sayesinde geçerli hâle
gelmesi (bkz. Kısım 12.13).

**Variadic dönüşüm** — işlev imzasındaki `...` parametresine yapılan geçiş.

Aynı kategoriden birden fazla aday varsa çift anlamlılık hatası oluşur.
