---
cilt: "II — İleri"
kisim: "2 — Taşıma Semantiği ve Bildirim Kuralları"
baslik: "2.2 Bildirim baskılama tablosu"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 2.2 Bildirim baskılama tablosu

Bir özel üye işlevi bildirmek, diğerlerinin statüsünü değiştirir. Kural seti tek tablodur:

| Kullanıcı şunu bildirirse | Varsayılan ktor | Kopyalayan ktor | Kopyalayan atama | Taşıyan ktor | Taşıyan atama |
|---|---|---|---|---|---|
| Hiçbir şey | implicit | implicit | implicit | implicit | implicit |
| Varsayılan kurucu | user | implicit | implicit | implicit | implicit |
| **Sonlandırıcı** | implicit | implicit\* | implicit\* | **not declared** | **not declared** |
| **Kopyalayan kurucu** | **not declared** | user | implicit\* | **not declared** | **not declared** |
| **Kopyalayan atama** | implicit | implicit\* | user | **not declared** | **not declared** |
| **Taşıyan kurucu** | **not declared** | **deleted** | **deleted** | user | **not declared** |
| **Taşıyan atama** | implicit | **deleted** | **deleted** | **not declared** | user |
| Herhangi bir kurucu | **not declared** | — | — | — | — |

\* Bildirilir ama bu kullanım artık önerilmiyor *(deprecated)*.

Tablodan çıkan üç sonuç:

**Sonlandırıcı işlev yazmak taşımayı öldürür.** Sırf günlükleme eklemek için boş bir
sonlandırıcı işlev yazdığınızda, sınıfınız sessizce taşınamaz hâle gelir ve her yerde
kopyalanmaya başlar. Performans kaybı derleyici uyarısı vermez. Bu, Big-Five kuralının
asıl teknik gerekçesidir.

**Taşıma işlevi yazmak kopyalamayı siler.** Yalnızca taşıyan kurucu yazarsanız sınıf
kopyalanamaz hâle gelir. Bunu isteyerek yapıyorsanız sorun yok; istemeden yaptıysanız
sürpriz olur.

**Herhangi bir kurucu işlev yazmak varsayılan kurucu işlevi kaldırır.** Tek parametreli
bir dönüştüren kurucu işlev yazmak bile yeterlidir.
